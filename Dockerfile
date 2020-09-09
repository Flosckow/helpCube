FROM        python:3.7 as devstage
ENV         LANG C.UTF-8
ENV         USER school
ENV         PROJECTPATH=/home/school/app

RUN         set -x && apt-get -qq update \
            && apt-get install -y --no-install-recommends libpq-dev python3-dev git \
            && apt-get purge -y --auto-remove\
            && rm -rf /var/lib/apt/lists/*

RUN         useradd -m -d /home/${USER} ${USER}\
            && chown -R ${USER} /home/${USER}

RUN         mkdir -p ${PROJECTPATH}

COPY        ./requirements.txt ${PROJECTPATH}
COPY        . ${PROJECTPATH}

RUN          pip install --upgrade pip\
             && pip install --no-cache-dir -r ${PROJECTPATH}/requirements.txt

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait ${PROJECTPATH}/wait
RUN         chmod +x ${PROJECTPATH}/wait

WORKDIR     ${PROJECTPATH}
USER        ${USER}


FROM        python:3.7 as production
ENV         LANG C.UTF-8
