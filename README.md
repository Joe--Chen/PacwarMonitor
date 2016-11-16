
export FLASK_APP=monitor.py
Debug mode
flask run --debugger -h 0.0.0.0
Backend mode
nohup gunicorn -w 4 -b 0.0.0.0:5000 monitor:app &

