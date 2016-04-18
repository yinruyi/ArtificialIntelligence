import os
import time
import cPickle
import datetime
import logging
import flask
import werkzeug
import optparse
import tornado.wsgi
import tornado.httpserver
import urllib
import sys
import json
import image_classification_predict
import random
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

REPO_DIRNAME = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../..')
UPLOAD_FOLDER = abspath+'\\uploads'
ALLOWED_IMAGE_EXTENSIONS = set(['png', 'bmp', 'jpg', 'jpe', 'jpeg', 'gif'])

# Obtain the flask app object
app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', has_result=False)


@app.route('/classify_url', methods=['GET'])
def classify_url():
    imageurl = flask.request.args.get('imageurl', '')
    try:
        '''string_buffer = StringIO.StringIO(
            urllib.urlopen(imageurl).read())
        print string_buffer,type(string_buffer)'''
        if not allowed_file(imageurl):
            return "100"        
        imgData = urllib.urlopen(imageurl).read()
        time_ = str(datetime.datetime.now()).replace(' ', '_')
        time_ = time_.replace(':','_')
        img_tag = imageurl.rsplit('.', 1)[1]
        new_img_name = time_ + str(random.randint(10000, 1000000)) + '.' + img_tag
        f = file(UPLOAD_FOLDER+new_img_name,'wb')
        f.write(data)
        f.close()


    except Exception as err:
        # For any exception we encounter in reading the image, we will just
        # not continue.
        logging.info('URL Image open error: %s', err)
        return flask.render_template(
            'index.html', has_result=True,
            result=(False, 'Cannot open image from URL.')
        )

    logging.info('Image: %s', imageurl)
    result = app.clf.classify_image(image)
    return flask.render_template(
        'index.html', has_result=True, result=result, imagesrc=imageurl)


@app.route('/classify_upload', methods=['POST'])
def classify_upload():
    try:
        # We will save the file to disk for possible data collection.
        imagefile = flask.request.files['imagefile']
        time_ = str(datetime.datetime.now()).replace(' ', '_')
        time_ = time_.replace(':','_')
        filename_ = time_ + werkzeug.secure_filename(imagefile.filename)
        filename = os.path.join(UPLOAD_FOLDER, filename_)
        if not allowed_file(filename):
            return "100"
        imagefile.save(filename)
        logging.info('Saving to %s.', filename)

    except Exception as err:
        logging.info('Uploaded image open error: %s', err)
        return "101"
    result = image_classification_predict.Main(filename)
    return json.dumps({"result":result,"image":filename})


def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1] in ALLOWED_IMAGE_EXTENSIONS
    )


def start_tornado(app, port=5000):
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app))
    http_server.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()


def start_from_terminal(app):
    """
    Parse command line options and start the server.
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-d', '--debug',
        help="enable debug mode",
        action="store_true", default=False)
    parser.add_option(
        '-p', '--port',
        help="which port to serve content on",
        type='int', default=5000)
    parser.add_option(
        '-g', '--gpu',
        help="use gpu mode",
        action='store_true', default=False)

    opts, args = parser.parse_args()
    if opts.debug:
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        start_tornado(app, 5000)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    start_from_terminal(app)
