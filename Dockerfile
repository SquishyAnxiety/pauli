FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    WEB_CONCURRENCY=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody
EXPOSE 8000

# listens on 0.0.0.0:$PORT and starts $WEB_CONCURRENCY workers
CMD ["gunicorn", "app:app"]
