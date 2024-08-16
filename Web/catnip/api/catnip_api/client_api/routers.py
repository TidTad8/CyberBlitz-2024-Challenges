import os
import re
import json
import secrets
import string
import traceback

from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils.md5_hash import md5_hash
from .models import Account
from .utils.generate_pdf import generate_pdf
from .utils.is_exploting_cve import is_exploiting_cve

from django.db import connection

def _create_default_accounts():
    """
    Helper function to create default accounts.

    Deletes all account, then create 2 default accounts;
    To simulate database immutability.
    """
    def create_account(username, password, email):
        Account.objects.create(username=username, password=md5_hash(password), email=email)

    Account.objects.all().delete()
    current_username = "thepointycatt"
    current_password = "qwertyuiop"
    current_email = "pointy@sit.cyberblitz.ctf"
    create_account(current_username, current_password, current_email)

    current_username = "bluecappo"
    current_password = "1qaz2wsx"
    current_email = "cappo@sit.cyberblitz.ctf"
    create_account(current_username, current_password, current_email)

def _verify_token(token):
    _create_default_accounts()
    cache_value = cache.get(token)
    if cache_value == "thepointycatt" or cache_value == "bluecappo":
        return cache_value
    return None

@csrf_exempt
def token_check(request):
    if request.method == "GET":
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        token = token.strip()
        username = _verify_token(token)
        if username is None:
            return HttpResponse(status=401)

        return JsonResponse({
            "username": username,
            "flag": "CyberBlitz{0L4OwXpLaiwONlbpOnVoTNvhtAT0771zOe}"
        }, status=200)

    return HttpResponse(status=404)

@csrf_exempt
def login(request):
    def generate_random_string(length=64):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        username = body.get("username", "")
        password = body.get("password", "")

        _create_default_accounts()
        if username == "thepointycatt" and password == "qwertyuiop":
            token = generate_random_string()
            cache.set(token, username, 4500)
        elif username == "bluecappo" and password == "1qaz2wsx":
            token = generate_random_string()
            cache.set(token, username, 4500)
        else:
            token = None

        status = 200 if token is not None else 401
        response = JsonResponse({"token": token}, status=status)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    return HttpResponse(status=404)

@csrf_exempt
def forgot_password(request):
    if request.method == "POST":
        _create_default_accounts()
        body = json.loads(request.body.decode('utf-8'))
        email = body.get("email", "")
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT username FROM client_api_account WHERE email = '{email}';")
            rows = cursor.fetchall()

        data = {'results': [row for row in rows]}
        return JsonResponse(data, safe=False)
    return HttpResponse(status=404)

@csrf_exempt
def logout(request):
    if request.method == "POST":
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        token = token.strip()
        cache.delete(token)
        return HttpResponse(status=200)
    return HttpResponse(status=404)

@csrf_exempt
def request_cat(request):
    if request.method == "POST":
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        token = token.strip()
        username = _verify_token(token)

        if username is None:
            return HttpResponse(status=401)

        body = json.loads(request.body.decode('utf-8'))
        cat_count = body.get("cat_count")
        body_content = body.get("body_content")
        shelter_name = body.get("shelter_name")

        try:
            cat_count = int(cat_count)
            if cat_count <= 0:
                raise ValueError("Invalid value for cat_count")
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid value for cat_count"}, status=400)

        if not body_content:
            return JsonResponse({"error": "Invalid or missing body_content"}, status=400)

        if not shelter_name:
            return JsonResponse({"error": "Invalid or missing shelter_name"}, status=400)

        exploiting = is_exploiting_cve(body_content) or is_exploiting_cve(shelter_name) 

        if exploiting:
            data = {
                "result": "exploited",
                "flag": "CyberBlitz{lzbJhNIfmkShNqkIgoccr468JSyWsr3Zju}"
            }
            return JsonResponse(data, safe=False)

        if username:
            safe_body = re.fullmatch(r'[a-zA-Z0-9_\-]+', body_content)
            safe_shelter_name = re.fullmatch(r'[a-zA-Z0-9_\-]+', shelter_name)
            if not safe_input or not safe_shelter_name:
                return HttpResponse(status=500)

            try:
                pdf_data = generate_pdf(body_content, shelter_name, cat_count)
                response = HttpResponse(pdf_data, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="cat_adoption_request.pdf"'
                return response
            except Exception:
                return HttpResponse(status=500)
        return HttpResponse(status=401)
    return HttpResponse(status=404)
