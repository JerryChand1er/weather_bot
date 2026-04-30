FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN RUN apt-get update && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Chicago

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "send_weather_update.py"]