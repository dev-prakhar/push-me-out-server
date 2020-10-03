# manage.py commands
migrations:
	docker exec -it pmo_server python manage.py makemigrations ${ARGS}

migrate:
	docker exec -it pmo_server python manage.py migrate ${ARGS}

superuser:
	docker exec -it pmo_server python manage.py createsuperuser

console:
	docker exec -it pmo_server python manage.py shell

collectstatic:
	docker exec -it pmo_server python manage.py collectstatic

start_app:
	docker exec -it pmo_server python manage.py startapp $(APP_NAME)

# Docker commands
setup:
	make collectstatic
	make dev

dev:
	docker-compose up -d

restart_api:
	docker restart pmo_server

build_up:
	docker-compose up -d --build

logs:
	docker logs -f --tail 1000 pmo_server

pip_install:
	docker exec -it pmo_server pip install -r requirements.txt

# Misc Services Commands
db_shell:
	docker exec -it pmo_db psql -U postgres
