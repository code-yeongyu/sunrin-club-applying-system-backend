sleep 4;
python manage.py migrate;
echo "SERVER STARTED ON 0.0.0.0:5000";
python manage.py runserver 0.0.0.0:5000