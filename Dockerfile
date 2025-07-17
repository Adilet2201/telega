FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ ./api
COPY public/ ./public

ENV PYTHONUNBUFFERED=1

CMD ["python", "api/telegabot.py"]
