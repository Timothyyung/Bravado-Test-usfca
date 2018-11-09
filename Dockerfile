FROM ubuntu:latest
MAINTAINER fnndsc "dev@babymri.org"

RUN apt-get update \
  && apt-get install -y git \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . /
WORKDIR /

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["/run_benchmark.sh"]
CMD []
