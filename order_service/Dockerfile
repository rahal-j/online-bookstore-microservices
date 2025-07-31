FROM python:3.10-slim

WORKDIR /app

COPY . .

# Combine install steps for cache efficiency
RUN pip install --no-cache-dir flask flask-cors requests prometheus_flask_exporter

EXPOSE 5000

CMD ["python", "app.py"]
