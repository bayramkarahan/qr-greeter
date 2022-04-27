#!/usr/bin/python3
import sys, os
import time
import threading

logfile = open("{}/qr-greeter.log".format(os.environ["HOME"]),"a")
logfile.write("------------------------\n")
logfile.flush()

def asynchronous(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper

def log(msg,type="log"):
    if len(msg.strip()) == 0:
        return
    ltime = int(time.time())
    if logfile:
        logfile.write("[{}] => {}\n".format(ltime,msg.strip()))
        logfile.flush()

def readfile(path):
    path = "{}/{}".format(os.environ["HOME"],path)
    path = path.replace("..","./")
    if not os.path.isfile(path):
        return ""
    f = open(path,"r")
    data = f.read()
    f.close()
    return data

def writefile(path,data):
    path = "{}/{}".format(os.environ["HOME"],path)
    path = path.replace("..","./")
    with open(path,"w") as f:
        f.write(data)
