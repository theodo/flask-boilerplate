```
# Installation
# ------------
git clone git@github.com:theodo/flask-boilerplate.git
cd flask-boilerplate
fig run --rm server pip install -r requirements.txt -t vendor --upgrade
fig up -d server

# You can access containers (Docker >= 1.3)
docker exec -it flaskboilerplate_db_1 psql -Upostgres
docker exec -it flaskboilerplate_server_1 bash

# Migration process
# -----------------
fig run --rm server python src/manage.py db init
fig run --rm server python src/manage.py db migrate
# check file + remove comment + improve file if needed
sudo vim migration/versions/<migration_id>.py
fig run --rm server python src/manage.py db upgrade

# Commands
# --------
fig run --rm server pip freeze > requirements.txt
```
