# words-learning

## [Admin page](https://evening-gorge-85945.herokuapp.com/admin)

## API
[levels](https://evening-gorge-85945.herokuapp.com/api/levels)
[categories](https://evening-gorge-85945.herokuapp.com/api/categories)
[themes](https://evening-gorge-85945.herokuapp.com/api/themes)
[words](https://evening-gorge-85945.herokuapp.com/api/words)


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