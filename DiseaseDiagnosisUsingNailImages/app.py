import os
import sys

# Flask
from flask import Flask, request, render_template, jsonify


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/DenseNet121RMSProp.h5'

# Load your own trained model
model = load_model(MODEL_PATH)
model.make_predict_function()          # Necessary
# print('Model loaded. Start serving...')


dic = {0: 'Darier_s disease',
       1: 'Healthy nail',
       2: 'Muehrck-e_s lines',
       3: 'Onychogryphosis',
       4: 'Onycholycis_NailPsoriasis',
       5: 'alopecia areata',
       6: 'beau_s lines',
       7: 'bluish nail',
       8: 'clubbing',
       9: 'eczema',
       10: 'half and half nailes (Lindsay_s nails)',
       11: 'koilonychia',
       12: 'leukonychia',
       13: 'pale nail',
       14: 'red lunula',
       15: 'splinter hemmorrage_Acral Lentiginous Melanoma',
       16: 'terry_s nail_WhiteNails',
       17: 'yellow nails'}


def model_predict(img, model):
    img = img.resize((224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    #x = preprocess_input(x, mode='tf')

    preds = np.argmax(model.predict(x))

    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)
        img = img.convert('RGB')

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img, model)

        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability

        output = ['Darier_s disease','Muehrck-e_s lines','aloperia areata','beau_s lines','bluish nail',
                  'clubbing','eczema','half and half nailes (Lindsay_s nails)','koilonychia',
                  'leukonychia','onycholycis','pale nail','red lunula',
                  'splinter hemmorrage','terry_s nail','white nail','yellow nails']
        '''
        output = ['AlopeciaAreata_DariersDisease','BeausLines','BluishNail','HalfMoonRedBands'
                  ,'HealthyNail','Koilonychia','Leukonychia','Onychogryphosis',
                  'Onycholycis_NailPsoriasis_Onychomycosis',
                  'SplinterHemmorrage_AcralLentiginousMelanoma',
                  'TerrysNail_WhiteNails_LindsaysNails_PaleNails',
                  'YellowNails']
        '''
        result = output[preds]     # Convert to string
        result = result.replace('_', ' ').capitalize()
        
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)

    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)
    #app.debug = True
	app.run(debug = True)