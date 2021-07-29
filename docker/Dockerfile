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

RUN set -eux; \
        useradd --create-home --system --shell=/bin/false builder; \
        usermod --lock builder
USER builder

RUN pip3 install --user --no-warn-script-location \
        geopy \
        getorg \
        pybtex \
        ;

COPY Gemfile /tmp
RUN cd /tmp && bundle install
