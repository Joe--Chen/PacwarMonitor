from flask import Flask, url_for, jsonify
from flask import render_template
import json
from flask import request
from jinja2 import Environment, FileSystemLoader
from werkzeug.contrib.fixers import ProxyFix
import sys
import os
import os.path
import subprocess

DIR = '/home/ec2-user/PacWar/python/log/'
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

def get_credential():
    with open('credential.txt', 'r') as f:
        for line in f:
            return line.strip()   
CREDENTIAL = get_credential()

@app.route('/')
def monitor():
    js_url = url_for('static', filename='canvasjs.min.js')
    jq_url = url_for('static', filename='jquery-3.1.1.min.js')
    entries =  get_all_prefix()
    return render_template("index.html", jsurl=js_url, jqurl=jq_url, 
            entries=entries)

@app.route('/refresh', methods = ['POST'])
def refresh():
    jsonData = request.get_json()
    parameter = jsonData['parameter']
    filename = jsonData['filename']
    print parameter
    dic = {}
    for i in range(1,9):
        if os.path.isfile(DIR + filename + '_instance_'  + str(i) + ".log"):
            dic[i] = parse_file(filename + '_instance_'  + str(i), parameter = parameter)
    return json.dumps(dic)

@app.route('/kill', methods = ['POST'])
def kill():
    jsonData = request.get_json()
    # security is important, no shell injection!
    if 'credential' not in jsonData:
        print 'no credential'
        return json.dumps({"status": "failed"})
    if jsonData['credential'] != CREDENTIAL:
        print jsonData['credential'], CREDENTIAL    
        return json.dumps({"status": "failed"})

    instance = jsonData['instance']
    if instance == 'all':
        p = subprocess.Popen('pkill  -f run_pacwar', cwd='/home/ec2-user/PacWar/python',shell=True)
        p = subprocess.Popen('./batch_run.sh', cwd='/home/ec2-user/PacWar/python',shell=True)        
    else:
        p = subprocess.Popen('', cwd='/home/ec2-user/PacWar/python',shell=True)
    return json.dumps({"status": "success"})

def get_all_prefix():
    DIR = '/home/ec2-user/PacWar/python/log/'
    res = set()
    for root, dirs, filenames in os.walk(DIR):
        for fn in filenames:
            if len(fn) > 16:
                res.add(fn[:16])
    return sorted(list(res)) 

def parse_file(filename, parameter='max'):
    cur_key = None
    result = []
    count = 0
    with open(DIR + filename + ".log", "r") as f:
        for line in f:
            if "INFO" in line:
                res = line.rstrip()[10:].split(",")
                if parameter == 'hamming':
                    result.append(float(res[2]))
                elif parameter == 'max':
                    result.append(float(res[1]))
                elif parameter == 'avg':
                    if float(res[0]) > 15:
                        print res
                    result.append(float(res[0]))
    return result

if __name__ == '__main__':
    pass
    #app.run(host='0.0.0.0', port=80)