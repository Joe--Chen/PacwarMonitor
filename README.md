
# PacwarMonitor
Simple web application to monitor genetic algorithm

## Installation
1. pip install flask
2. pip install gunicorn

## Usage
1. Change `DIR` on line 12 of `monitor.py` to point to your log/ directory
2. Each line in log file must have three comma seperated values (max score, avg score, avg hamming distance)
3. Create `credential.txt` to store your password to enable remote shell execution
3. `export FLASK_APP=monitor.py`
4. `flask run --debugger -h 0.0.0.0` (frontend)
5. `nohup gunicorn -w 4 -b 0.0.0.0:5000 monitor:app &` (backend)

## Demo
http://35.161.96.186:5000/#


