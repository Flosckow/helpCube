THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help run stop restart build destroy log-app shell-app

help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null |	awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

build:
	docker-compose -f docker-compose.yaml build $(c)
run:
	docker-compose -f docker-compose.yaml up -d $(c)
stop:
	docker-compose -f docker-compose.yaml stop $(c)
restart:
	docker-compose -f docker-compose.yaml stop $(c)
	docker-compose -f docker-compose.yaml up -d $(c)
destroy:
	docker-compose -f docker-compose.yaml down -v $(c)
log-app:
	docker-compose -f docker-compose.yaml logs --tail=100 -f school-app
shell-app:
	docker-compose -f docker-compose.yaml exec school-app /bin/bash