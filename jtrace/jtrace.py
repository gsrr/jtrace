import signal
import os
import sys
import traceback
import threading
import datetime

DEBUG_MODE = False

def log_trace(msgs):
    msg = "::".join(msgs)
    with open("./trace.log", 'a') as fw:
        fw.write("[%s]%s\n"%(datetime.datetime.now(), msg))

def tracefunc(frame, event, arg, indent=[0]):
    try:
        if event == "call":
            msgs = [event, frame.f_code.co_name, str(frame.f_locals)]
            log_trace(msgs)
        elif event == "return":
            msgs = [event, frame.f_code.co_name, str(arg)]
            log_trace(msgs)
    except:
        log_trace([traceback.format_exc()])
    finally:
        return tracefunc

def handle_trace(sig, frame):
    global DEBUG_MODE
    if DEBUG_MODE == False:
        sys.settrace(tracefunc)
        DEBUG_MODE = True
    else:
        sys.settrace(None)
        DEBUG_MODE = False

def jtrace_listen():
    signal.signal(signal.SIGUSR1, handle_trace)
    
def hello():
    print "Hello World!!"
