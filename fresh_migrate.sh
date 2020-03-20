export $(egrep -v '^#' birpen/.env | xargs)

PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME \
-f fresh_migrate/drop_all_table.sql

python3 manage.py migrate
