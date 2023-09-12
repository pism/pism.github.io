FROM ruby:3.0-buster
ENV DEBIAN_FRONTEND=noninteractive
RUN set -eux; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
        fonts-humor-sans \
        python3-matplotlib \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        ; \
        rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    pip3 install \
      folium \
      pybtex \
    ;

COPY Gemfile /tmp
RUN cd /tmp && bundle install
