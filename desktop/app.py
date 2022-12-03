from flask import Flask
import keyboard  # using module keyboard
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
if __name__ == '__main__':
    t = threading.Thread(target=app.run,args=('0.0.0.0',5000,))
    t.setDaemon(True)
    t.start()
    root.mainloop()
