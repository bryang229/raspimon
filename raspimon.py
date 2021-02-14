from sense_hat import SenseHat
from flask import Flask, render_template,request
from time import sleep
import unicodedata

app = Flask (__name__,static_url_path='/static')


senseHat = SenseHat()
senseHat.clear()

global r
global g
global b
global k
global w
global y
global o

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)

global rmon1
global rmonJumping
global black

rmon1 = [k, k, k, k, k, k, k, k,
         k, w, w, w, w, w, w, k,
         k, w, r, o, o, r, w, k,
         k, w, w, w, w, w, w, k,
         k, k, k, w, w, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, w, k, k, w, k, k,
         k, k, w, k, k, w, k, k
         ]	

rmonJumping = [k, w, w, w, w, w, w, k,
         k, w, r, o, o, r, w, k,
         k, w, w, w, w, w, w, k,
         k, k, k, k, k, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, w, k, k, w, k, k,
         k, k, w, k, k, w, k, k
         ]	

black = [k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k]

@app.route('/')
def indexjhb ():
    return render_template('home.html')

@app.route('/disappear')
def disappear():
    senseHat.set_pixels(black)
    sleep(3)
    senseHat.set_pixels(rmon1)
    return render_template('backToHome.html')

@app.route('/jump')
def jump():
    senseHat.set_pixels(rmonJumping)
    sleep(2)
    senseHat.set_pixels(rmon1)
    return render_template('backToHome.html')
@app.route('/colorChange', methods = ['GET','POST'])
def colorChange():
    if request.method == "POST":
        text = request.form['text']
        text = unicodedata.normalize('NFKC',text)
        text = text.lower()
        if text.__contains__("skin"):
            changeVar(2,text)
        elif text.__contains__("background"):
            changeVar(1,text)
        elif text.__contains__("eyes"):
            changeVar(3,text)
            print("test one")
    return render_template('changeColor.html')

#Red, Green, Blue, Yellow, Orange, Purple.
def changeVar(num,choice):
    global r,k,w
    if num == 1:
        if choice.__contains__("blue"):
            k = b
        elif choice.__contains__("red"):
            k = (255,0,0)
        elif choice.__contains__("green"):
            k = g
        elif choice.__contains__("yellow"):
            k = y
        elif choice.__contains__("orange"):
            k = o
        updateColors()
        senseHat.set_pixels(rmon1)
    elif num == 2:
        if choice.__contains__("blue"):
            w = b
        elif choice.__contains__("red"):
            w = (255,0,0)
        elif choice.__contains__("green"):
            w = g
        elif choice.__contains__("yellow"):
            w = y
        elif choice.__contains__("orange"):
            w = o
        updateColors()
        senseHat.set_pixels(rmon1)
    elif num == 3:
        if choice.__contains__("blue"):
            print("test two", r)
            r = b
        elif choice.__contains__("red"):
            r = (255,0,0)
        elif choice.__contains__("green"):
            r = g
        elif choice.__contains__("yellow"):
            r = y
        elif choice.__contains__("orange"):
            r = o
        updateColors()
        senseHat.set_pixels(rmon1)
        
def updateColors():
    global rmon1, rmonJumping,black
    rmon1 = [k, k, k, k, k, k, k, k,
         k, w, w, w, w, w, w, k,
         k, w, r, o, o, r, w, k,
         k, w, w, w, w, w, w, k,
         k, k, k, w, w, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, w, k, k, w, k, k,
         k, k, w, k, k, w, k, k]	

    rmonJumping = [k, w, w, w, w, w, w, k,
         k, w, r, o, o, r, w, k,
         k, w, w, w, w, w, w, k,
         k, k, k, k, k, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, k, w, w, k, k, k,
         k, k, w, k, k, w, k, k,
         k, k, w, k, k, w, k, k]	

    black = [k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k]

	
class LilQtip:
    def __init__(self):
        senseHat.set_pixels(rmon1)
senseHat.show_message("Hey! I'm Lil Qtip")
lilQtip = LilQtip()

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')