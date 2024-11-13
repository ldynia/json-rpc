FROM python:3.12-slim

ARG PORT=4000 \
    HOST=0.0.0.0 \
    WORKDIR=/usr/src/jrpc

ENV PORT=$PORT \
    HOST=$HOST \
    WORKDIR=$WORKDIR

WORKDIR $WORKDIR

COPY . $WORKDIR

RUN pip install --upgrade pip \
  Flask \
  json-rpc \
  requests

EXPOSE $PORT

CMD ["sh", "-c", "python server.py"]