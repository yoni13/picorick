from flask import Flask
import os
import psutil
import time
try:
    import httplib
except:
    import http.client as httplib
def ci(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
import webbrowser
import threading
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()
app = Flask(__name__)
app.debug = False
@app.errorhandler(500)
def pageNotFound(error):
    return "erorr"
@app.route('/')
def index():
    return 'ok'
@app.route('/esc')
def esc():
    keyboard.press_and_release('esc')
    return 'ok'
@app.route('/rickroll')
def rickroll():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    return 'ok'
@app.route('/anotherrickroll')
def anotherrickroll():
    webbrowser.open('https://www.youtube.com/watch?v=t9N5Msr_Ftg')
    return 'ok'
@app.route('/herewegoagain')
def herewegoagain():
    webbrowser.open('https://www.youtube.com/watch?v=-1qju6V1jLM')
    return 'ok'
@app.route('/hh')
def hello():
    messagebox.showinfo("ㄏㄏ", "ㄏㄏ")
    return 'ok'
@app.route('/4xuan')
def xuan():
    webbrowser.open('https://youtu.be/CqWZq1mJJh0?t=11')
    return 'ok'

def alive():
    if "powerpoint" in (p.name() for p in psutil.process_iter()) and ci() == False:
        os.system('TASKKILL /IM powerpoint.exe /F')
    time.sleep(3)

if __name__ == '__main__':
    t = threading.Thread(target=app.run,args=('0.0.0.0',5000,))
    t.daemon=True
    t.start()
    t2 = threading.Thread(target=alive,)
    t2.daemon=True
    t2.start()
    root.mainloop()
