
# PacwarMonitor
Web application to monitor genetic algorithm

## Installation
1. pip install flask
2. pip install gunicorn (optional)

## Format of log files
1. All log files must be under log directory defined in `config.txt`
2. file names should be `YYYY-MM-DD-hh-mm_instance_n.log` (year, month, day, hour, minute, number of instance)
3. Each line in each file should be `INFO:root:%f,%f,%f` (replace `%f` with actual numbers, float or integer)
4. If you don't like this format, change `def refresh()`, `def parse_file()` in `monitor.py`

## Usage
1. Modify `config.txt` to change the password, your own python directory and log directory
2. `export FLASK_APP=monitor.py`
3. `python monitor.py` (run foreground)
4. `flask run --debugger -h 0.0.0.0` (optional)
5. `nohup gunicorn -w 4 -b 0.0.0.0:5000 monitor:app &` (4 threads, run background, optional)


