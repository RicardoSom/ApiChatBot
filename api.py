import flask
from flask import request
import aiml
import pyttsx3
import os
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# Create the kernel and learn AIML files

kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
   kernel.bootstrap(brainFile = "bot_brain.brn")
else:
   kernel.bootstrap(learnFiles = "zoe-startup.xml", commands = "load aiml b")
   kernel.saveBrain("bot_brain.brn")

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for a chatbot using python and AIML</p></br><p>Created by Ricardo Orellana RSOM </p>"

@app.route('/bot', methods=['GET'])
def API():
    
    data = request.args.get('input')

    zoes_response = kernel.respond(data)
    
    return zoes_response 

app.run()