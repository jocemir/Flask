import RPi.GPIO as gpio
from app import app
from flask import render_template

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

ledvermelho = 11

gpio.setup(ledvermelho, gpio.OUT)

gpio.output(ledvermelho, gpio.LOW)

def statusledvermelho():
    if gpio.input(ledvermelho) == 1:
        statusledvermelho = 'LED vermelho ON'
    else:
        statusledvermelho = 'LED vermelho OFF'
    return statusledvermelho

def ligaledvermelho():
    gpio.output(ledvermelho, gpio.HIGH)
    ligaledvermelho = 'LED vermelho ligado'
    return ligaledvermelho

def desligaledvermelho():
    gpio.output(ledvermelho, gpio.LOW)
    desligaledvermelho = 'LED vermelho desligado'
    return desligaledvermelho

@app.route("/")
def index():
    templateData = {
        'ledred' : statusledvermelho(), 
    }
    return render_template('index.html', **templateData)

@app.route("/led_vermelho/<action>")
def led_vermelho(action):
    if action == 'on':
        ligaledvermelho()
    if action == 'off':
        desligaledvermelho()

    templateData = {
    'ledred' : statusledvermelho(), 
    }
    return render_template('index.html', **templateData)
    
