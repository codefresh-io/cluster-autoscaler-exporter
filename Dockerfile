FROM python:3.7-alpine
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

ADD app.py .
USER nobody
ENTRYPOINT ["python", "app.py"]
