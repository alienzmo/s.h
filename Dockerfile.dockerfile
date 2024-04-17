FROM python:3.11-slim
WORKDIR /app
COPY . /app
ENV FLASK-APP=app.py
CMD [ "FLASK", "run","--host=0.0.0.0", "--port=5000" ]
