FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y ffmpeg gcc libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]