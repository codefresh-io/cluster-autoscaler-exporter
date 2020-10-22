FROM python:3.8-alpine
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

ADD app.py .
USER nobody
ENTRYPOINT ["python", "-u", "app.py"]
