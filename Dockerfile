FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ARG APPLICATION_ENVIRONMENT
ENV APPLICATION_ENVIRONMENT=${APPLICATION_ENVIRONMENT}
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

CMD ["python", "__main__.py"]
