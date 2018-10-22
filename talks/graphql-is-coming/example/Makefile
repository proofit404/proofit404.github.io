default:
	rm -f db.sqlite3
	django-admin migrate
	django-admin loaddata dump.json
	django-admin runserver
