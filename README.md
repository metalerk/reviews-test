# Company Reviews

Review and rate companies.


## Setup

### Linux/Mac


```bash
# Create virtualenv
$ virtualenv -p python3 env

# Activate it
$ source env/bin/activate

# Install requirements
(env)$ pip install -r requirements.txt

# Migrations
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate

# Create superuser
(env)$ python manage.py createsuperuser

# Run
(env)$ python manage.py runserver

# Run tests
(env)$ python manage.py test
```


## Authenticate

Get the JWT token

```bash
(env)$ curl -X POST \
  http://localhost:8000/api/user/auth/ \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": <user>,
    "password": <password>
}'
```


## Create a review
Parameters:

- company => company id (uuid)
- rating => company rating (int)
- title => review title (string)
- summary => review summary (string)
- is_employee => is current employee (bool)

You can create it in `/api/review/create/`

```bash
(env)$ curl -X POST \
  http://localhost:8000/api/review/create/ \
  -H 'Authorization: JWT <token>' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
	"company": <company_id>,
	"rating": 5,
	"title": "Bairesdev rocks!",
	"summary": "Cool!",
	"is_employee": true
}'
```

## Get reviews

You can retrieve them in `/api/review/list/`

```bash
(env)$ curl -X GET \
  http://localhost:8000/api/review/list/ \
  -H 'Authorization: JWT <token>' \
  -H 'Cache-Control: no-cache'
```

## Get companies

You can retrieve them in `/api/company/list/`

```bash
(env)$ curl -X GET \
  http://localhost:8000/api/company/list/ \
  -H 'Authorization: JWT <token>' \
  -H 'Cache-Control: no-cache'
```