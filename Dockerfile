FROM python:3.9-slim-buster

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y gcc libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]