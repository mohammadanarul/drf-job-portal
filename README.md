# Django Restframework Job Portal

`Dependencies`

```commandline
Python >= 3.10.7
Django >= 4.1.3
Postgres >= 13.0
```

### setup

```bash
git clone https://github.com/mohammadanarul/drf-job-portal.git
cd drf-job-portal
```

#### ``.env_example`` replace `.env` and update some data
-------------------------------------------
```bash
|--> .env-example
|--> .env
```

### Applocation Local server `environment` setup

```base
pip install virtualenv 
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### `celery` use for send mail

```base
celery -A core worker --loglevel=INFO --pool=solo
```


