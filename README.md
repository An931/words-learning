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


shell
exec(open('scripts/add_levels.py').read())

pip3 freeze > requirements.txt - todo
todo flake8, isort