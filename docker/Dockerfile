FROM ruby:3
ENV DEBIAN_FRONTEND=noninteractive
RUN set -eux; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        python3-matplotlib \
        fonts-humor-sans \
        ; \
        rm -rf /var/lib/apt/lists/*

COPY Gemfile /tmp
RUN cd /tmp && bundle install

RUN pip3 install \
        geopy \
        getorg \
        pybtex \
        ;
