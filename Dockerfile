# syntax=docker/dockerfile:1

FROM python:3.10-slim

RUN ["useradd", "-m", "-s", "/usr/bin/nologin", "guest"]
USER guest

WORKDIR /asciiArt
COPY ./asciiArt ./data.py ./

RUN ["pip", "--no-cache-dir", "install", "pillow", "numpy", "argparse"]

ENTRYPOINT ["./asciiArt"]
