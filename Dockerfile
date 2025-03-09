FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./logging.conf /app/logging.conf
COPY ./static /app/static
COPY ./src /app/src

CMD ["fastapi", "run", "src/app.py", "--port", "5001", "--workers", "4"]