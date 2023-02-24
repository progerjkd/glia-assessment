FROM python:3.9-alpine

WORKDIR /code
RUN apk update && apk add gcc musl-dev mariadb-connector-c-dev
COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
