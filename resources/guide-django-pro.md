


### Environment Setup
- `Poetry` : https://python-poetry.org/docs/#installation
```sh
poetry --version

poetry init

poetry install

poetry add gunicorn


# option new environment
python3.10 -m venv _venv

source _venv/bin/activate

poetry install
```


```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser