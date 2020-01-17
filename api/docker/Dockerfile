FROM python:3.7.0

ENV APP_PATH /usr/src/app
WORKDIR $APP_PATH

RUN mkdir -p ${APP_PATH} \
    && apt-get update && apt-get install -y \
    build-essential python3-setuptools python-dev \
    libldap2-dev libsasl2-dev ldap-utils python-tox lcov valgrind \
    locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && apt-get autoremove -y

ENV LANG en_US.UTF-8

    

COPY requirements.txt ${APP_PATH}/

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && mkdir -p assets/static 


