FROM ruby:3
ENV DEBIAN_FRONTEND=noninteractive
RUN set -eux; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
        fonts-humor-sans \
        python3-folium \
        python3-matplotlib \
        python3-pip \
        python3-pybtex \
        python3-setuptools \
        python3-wheel \
        ; \
        rm -rf /var/lib/apt/lists/*

COPY Gemfile /tmp
RUN cd /tmp && bundle install
