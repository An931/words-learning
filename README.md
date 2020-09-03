# words-learning

## Install packages
```bash
pip install -r requirements.txt
```

## Run postgres db
```bash
docker-compose up -d postgres
```

## Migrate db
```bash
python3 manage.py migrate
```

## Run server
```bash
python3 manage.py runserver 127.0.0.1:8000
```

## Create superuser
```bash
python3 manage.py createsuperuser
```

## Add necessary levels
```bash
python3 manage.py runscript add_levels
```

## Add some other data example
```bash
python3 manage.py runscript fill_data
```

##[Admin page](http://127.0.0.1:8000/admin)

##API
[levels](http://127.0.0.1:8000/api/levels)
[categories](http://127.0.0.1:8000/api/categories)
[themes](http://127.0.0.1:8000/api/themes)
[words](http://127.0.0.1:8000/api/words)
