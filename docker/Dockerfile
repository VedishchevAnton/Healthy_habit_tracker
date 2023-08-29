FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN sed -i 's/\r$//g' /app/entrypoint

RUN chmod u+x /app/entrypoint

ENTRYPOINT ["/app/entrypoint"]