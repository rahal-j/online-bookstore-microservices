FROM python:3.10-slim

WORKDIR /app

COPY app.py .

# Combine all installs into one to avoid layer issues
RUN pip install flask flask-cors prometheus_flask_exporter

EXPOSE 5000

CMD ["python", "app.py"]
