# MealApp

MealApp is a web application that you can use to plan your menus for your collaborators and send them to slack. So they can review the menu, place their order and customize their order.
It also allows you to monitor menu orders from the administrator panel.

## Installation

This application uses python and celery, so you need to install a broker for celery like:

* redis
* rabbitmq 
* Amazon SQS
* Zookeeper


Download the repo and install te packages

```github
git clone https://github.com/KrlosAren/Backend-Test-Lopez 


pip install -r requierement.txt

```

## Usage

you need to configure the **.env** with your variables

```.env
# // DB CONFIG

DB_USER=
DB_PASSWORD=
DB_HOST=
DB_NAME=

# //  SLACK CONFIG

SLACK_API_TOKEN=
SLACK_CHANNEL=


# // CELERY 
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
CELERY_ACCEPT_CONTENT=
CELERY_TASK_SERIALIZER=
CELERY_RESULT_SERIALIZER=

```
### Now run
```python
py manage.py runserver
```
and now you can view the app in 
```
localhost:8000/
```


## License
[MIT](https://choosealicense.com/licenses/mit/)