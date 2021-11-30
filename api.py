from flask import Flask
from threading import Thread
import random

app = Flask('Luiz Eduardo')

@app.route('/')
def home():
	return '''
	{
	"IP":"103.250.156.24",
	"PORT":"6666",
	"ANON":"Elite",
	"COUNTRY":"India",
	"ISO":"IN",
	"PING":387
	}'''
	
def run():
	app.run(host='0.0.0.0', port='8081')

def luffyprogrammer():

	servidor = Thread(target=run)
	servidor.start()