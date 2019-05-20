# django_softcontruct
### Descriprion:
Application consist of three parts: 
1)  Websocket-server, which continuously send number(and its sequence number) sampling from a normal distribution with parameters (0, 1) 
2)  Websocket-client that reads a stream from websocket server. For each value that over 2 standard deviation range create an log message that
includes a current timestamp, number and and its sequence number  
3) Django-channels shows messages on HTML-page from websocket-client in real-time

### How to run project:
* Create folder for project
* Create virtual environment for python: virtualenv nameofvenv
* cd nameofvenv
* Clone repo in created folder: git clone https://github.com/Bonskeeper/django_softcontruct.git
* Install requrements: pip install -r requirements.txt
In three different terminal'ss tabs you should launch these files:
* Start django server: python manage.py runserver
* Start websocket-server: python ws_server.py
* Start websocket-client: python ws_client.py
Open web-page and watch :)
