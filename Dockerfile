FROM docker.io/python:3.10

WORKDIR /

# --- [Install python and pip] ---
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
COPY . /

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn

ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8080"

EXPOSE 8080

CMD [ "gunicorn", "main:app" ]
