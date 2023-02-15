# WebSocket_chat

Проект собран на FastAPI с Веб-сокетами, cделан в качестве тестового задания на FastAPI в 2023
index.html подтягивает bootstrap для стилей из интернета. 
server.py, если "строго по ТЗ" имеет счетчик сообщений, который обнуляется при обновлении страницы. 
Но я его доработал до нормального чата, и убрал оттуда счетчик. Приложил обе версии. (server.py и server_chat.py)
По большому счету, сделано по примеру из официальной документации FastAPI с небольшими переделками. 

## Исходное ТЗ

Запускается на uvicorn:
`uvicorn server:app --reload`

Задача следующая. С использованием fastapi необходимо сделать веб-страницу сочетающую из:
1. Формы с текстовым полем
2. Списком сообщений пронумерованных с 1

Страница подключается к серверу по WebSocket.
С помощью формы вы можете отправить сообщение на сервер, где оно будет принято и добавлен порядковый номер этого сообщения.
Далее сообщение с порядковым номером отправляется на страницу и отображается в списке.

При перезагрузке страницы данные о номерации теряются и начинается с 1.

Страница должна быть динамической, обрабатывать все действия без перезагрузки. Имеется ввиду что при отправке сообщения на сервер через вебсокет страница не должна перезагружаться.  
Взаимодействие с сервером по вебсокет нужно реализовать с использованием JSON. Формат и именование полей не важно. можно использовать любые.

## Требования:
 - FastAPI
 - uvicorn
 - и их зависимости
 
 ## Установка:
 - клонировать репозиторий на машину, с которой будет будет запускаться сервис (либо по SSH-ссылке, либо скопировать и распаковать zip-архив)
```
git clone https://github.com/andmerk93/WebSocket_chat.git
```

- На машине должен быть установлен Python актуальной версии (тестировалось на 3.8, 3.10)
- развернуть виртуальное окружение python в папке с проектом (WebSocket_chat)
```
python3 -m venv venv
```
- активировать виртуальное окружение
(для linux/unix)
 ```
 source ./venv/bin/activate 
 ``` 
(для Windows, должно быть разрешено выполнение скриптов Powershell)
 ```
 venv\Scripts\activate
 ``` 

- с запущенным виртуальным окружением нужно выполнить установку требуемых компонентов
```
pip install fastapi uvicorn[standart]
```
- запустить uvicorn:
```
uvicorn server:app --reload
```

## ToDo:
 - Переписать стили в index.html без Bootstrap
 - Позже убрать старый server.py и исходное ТЗ