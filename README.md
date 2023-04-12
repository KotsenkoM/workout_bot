## Телеграм бот workout_bot
Бот, который создает опрос в чате, так как я устал каждый раз опрашивать коллег по работе сам) 

### Запуск проекта локально
* Создайте бота в телеграм через BotFather
* Склонируйте репозиторий с github на локальную машину
* Создайте файл .env с указанием:
> TOKEN=<Токен вашего бота>\
> CHAT_ID=<Id чата куда нужно слать опрос>\
> QUESTION=<Вопрос для голосования>\
> OPTIONS=<Варианты ответа (через запятую и пробел, например: 'да, нет')>
* Создайте и активируйте виртуальное окружение
* Установите необходимые библиотеки из requirements.txt
* Не забудьте добавить бота в групповой чат и раздать ему права на создание голосований
* Запустите main.py

### Запуск проекта в docker контейнере
* Выполните первые три пункта из локального запуска проекта
* Установите docker на локальную машину если его еще у Вас нет
* Соберите образ docker:
> docker build -t <имя образа> . 
* Запустите docker контейнер:
> docker run --name <имя контейнера> -it -p 8001:8001 <имя образа>
* Порты меняются по желанию в зависимости от локальной/виртуальной машины
