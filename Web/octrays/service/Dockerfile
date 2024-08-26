FROM python:3.12-alpine

WORKDIR /opt

COPY ./app.py /opt
COPY ./index.html /opt
COPY ./pricing.html /opt
COPY ./.DS_Store /opt
COPY ./alpha20_cf9e67 /opt/alpha20_cf9e67

RUN adduser -D octrays

USER octrays

EXPOSE 8000

CMD ["python3", "app.py"]
