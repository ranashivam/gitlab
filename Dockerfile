FROM python:3.10.0-alpine3.15
EXPOSE 80
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src
ENTRYPOINT ["python", "./src/app.py"]
