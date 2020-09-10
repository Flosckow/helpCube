# Проект для начинающих

##Использование Makefile в проекте
#### Сборка и первый запуск
`docker network create school-network`

`make build`

`make run`

#### Простой запуск

`make run`

#### Логи

`make log-app`

#### Shell

`make shell-app` 

## Без Makefile 

#### Сборка проекта
`docker network create school-network`

`docker-compose up --build`

#### Запуск проекта
`docker-compose up`

## Сборка статики и стилей

Вся сборка статики и стилей производится с использованием **_webpack_**

Для запуска необходимо зайти в папку **assets** и запустить сборку

`yarn start`

Если не утановлен Node.js необходимо его установить (Windows, MacOS):
https://nodejs.org/en/download/current/

Если Linux, то милости прошу:
https://github.com/nodesource/distributions/blob/master/README.md