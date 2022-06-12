from typing import Union
from fastapi import FastAPI
# import tensorflow
import json

app = FastAPI()

# model = tensorflow.keras.models.load_model('model.h5')

@app.get("/")
def read_root():
    return {"message": "Welcome to restabot API"}

@app.get("/api/v1/restabot/data")
def get_message(message: Union[str, None] = None):
    # Opening JSON file
    f = open('data.json')
    
    # returns JSON object as 
    # a dictionary
    json_file = json.load(f)
    data = json_file["intents"]

    lowerCaseMessage = message.lower()
    for obj in data:
        inputs = obj["inputs"]
        response = obj["responses"][0]
        print(inputs)
        if lowerCaseMessage in inputs:
            return { "cnt": response }