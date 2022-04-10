import numpy as np
from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import image

emotion_classes = { 0:"Angry", 1:"Disgust", 2:"Fear", 3:"Happy", 4:"Sad", 5:"Surprised", 6:"Neutral" }
gender_classes = { 0:'Female', 1:'Male' }

def load_models():
    ''' load emotion model (jsn format) and gender model(h5 format) '''
    json_file = open("/home/abdelghafour/Desktop/PFE/models/model_v2.json", 'r')
    model = json_file.read()
    json_file.close()
    emotion_model = model_from_json(model)
    emotion_model.load_weights("/home/abdelghafour/Desktop/PFE/models/model_v2_weights.h5")
    
    gender_model = load_model("/home/abdelghafour/Desktop/PFE/models/gender_model.h5")

    return emotion_model, gender_model


def make_predictions(model, gray_image):
    ''' make predictions from model and return his % '''
    pixels = image.img_to_array(gray_image)
    pixels = np.expand_dims(pixels, axis=0)
    predictions = model.predict(pixels)
    index = np.argmax(predictions)
    percent = predictions.max()*100
    percent = "({:.2f})".format(percent)
    
    return predictions, index, percent
    