import os
from flask import Flask, request, redirect, url_for
from config.jconfig import render
from werkzeug import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/' 
ALLOWED_EXTENSIONS = ['txt'] #for testing, only allow txt files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    # make sure the file being uploaded has the allowed extention
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload():
    """
    GET: show the upload file page
    * POST: upload the file to be drawn, then show them the draw page
    * uploading files gets pretty scary, this will really need to be locked 
      down before deploying
    """
    if request.method == 'GET':
        return render('upload.html')

    elif request.method == 'POST':
        file = request.files['upload']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render('draw.html', {
                'filename': file.filename
            })


@app.route('/gallery', methods=['GET'])
def gallery():
    """
    Render the galler on a GET request
    """
    return render('base.html')


if __name__ == '__main__':
    app.debug = True
    app.run()


