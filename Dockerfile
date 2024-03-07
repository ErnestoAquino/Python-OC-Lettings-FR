FROM ubuntu:latest
LABEL authors="ernesto"

ENTRYPOINT ["top", "-b"]