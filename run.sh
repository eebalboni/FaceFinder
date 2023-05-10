pip3 install tensorflow mtcnn flask flask_cors Pillow
cd backend && python3 web_fnet_api.py
cd ../front-end && python3 -m http.server 9000