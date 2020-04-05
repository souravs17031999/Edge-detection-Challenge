from flask import Flask, render_template, request
from inference import edge_detection
from PIL import Image
import io
import numpy as np
import os

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'images/')

full_path = target + 'result.png'

# defining default route
@app.route('/',methods = ['GET','POST'])
def hello_world():
    '''
    methods :
        GET : is used to request data from a specified resource.
        POST : is used to send data to a server to create/update a resource.
    '''
	# if we are just opening the webpage
    if request.method == 'GET':
        return render_template('index.html',name = "sourav")
	# if we are creating POST requests when filling the form for uploading the image
    if request.method == 'POST':
		# checking for file upload errors
        if 'file' not in request.files:
            return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
        file = request.files['file']
		# checking for file upload errors  , if empty means nothing selected
        if file.filename == '':
            return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
        image = file.read()
        npimg = np.fromstring(image, np.uint8)

        X = request.form['xname']
        Y = request.form['yname']
		# check if nothing is provided in text box
        if not X or not Y:
            return render_template('error.html', message='EMPTY_STRING_ERROR : Either of coordinate is empty, please enter something !')
		# deleting older images to save space
        for file in os.listdir(target):
            os.remove(target + file)

        coordinates = [int(X), int(Y)]
        m = edge_detection()
        result_paths = m.main(npimg, coordinates)

        return render_template('result.html', image_name1=result_paths[0], image_name2=result_paths[1], image_name3=result_paths[2], distance=result_paths[3])
