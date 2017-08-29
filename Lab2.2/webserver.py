from flask import Flask
from flask import jsonify
import sys
import glob
import re

hosts = {}
flist = []
app = Flask('__name__')

@app.route('/')
@app.route('/index')
def index():
    return "Справка"

@app.route('/page1')
def page1():
    return jsonify(str(sys.__dict__))


@app.route('/configs')
def configs():
  return jsonify(list(hosts.keys()))


@app.route('/config/<hostname>')
def ips(hostname):
  return jsonify(list(hosts[hostname]["ip"]))


if __name__ == '__main__':
    flist = glob.glob("c:\\Users\\Anatoly\\PycharmProjects\\p4ne\\Lab1.5\\config_files\\*.txt")


def cl(s):
    s = re.match(' ip address ([0-9.]+) ([0-9.]+)', m)
    if s:
        return ('IP', s.group(1), s.group(2))
    s = re.match('^hostname (.+)', m)
    if s:
        return ("HOST", s.group(1))
    else:
        return ("UNCLASSIFIED",)

current_host = ""

for i in flist:
    with open(i) as f:
        strlist=list(f)
       # print (strlist)
        for m in strlist:
            a = cl(m)
            if a[0] != "UNCLASSIFIED":
                if a[0] == 'HOST':
                    current_host = a[1]
                    hosts[a[1]] = {"host": a[1]}
                if a[0] == 'IP' and current_host:
                    hosts[current_host]["ip"] = a

app.run(debug=True)


