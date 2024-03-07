FROM python:3.10-slim
LABEL author={{cookiecutter.author}}
LABEL author_email={{cookiecutter.author_email}}

RUN apt-get update && apt-get install -yq libgdal-dev g++ && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash"]