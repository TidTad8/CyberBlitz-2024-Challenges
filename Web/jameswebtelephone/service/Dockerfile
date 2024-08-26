FROM python:3.12-alpine

ENV FLAG="CyberBlitz{YOU_THOUGHT_IT_WAS_A_WEB_CHALLENGE_BUT_IT_WAS_I_CRYPTO}"

WORKDIR /opt

COPY ./requirements.txt /opt
COPY ./app.py /opt
COPY ./public/ /opt/public/

RUN adduser -D james && \
    python -m pip install -r requirements.txt

USER james

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
