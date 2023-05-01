from flask import Flask, request, jsonify
from fnet_api import extract_faces
from flask_cors import CORS
# import base64

app = Flask(__name__)
CORS(app)

@app.route('/api/identify', methods=['POST'])
def process_image():
    image = request.files['image'].read()
    # encoded_image = base64.b64encode(image).decode('utf-8')
    faces = extract_faces(image)
    result = {'faces': faces}
    return jsonify(result)

# hello world route
@app.route('/')
def hello_world():
    return 'Hello Amber is stupid!'

if __name__ == '__main__':
    # run on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=8000, debug=True)