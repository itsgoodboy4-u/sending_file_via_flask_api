#!/bin/bash

python3 app.py &

sleep 5

curl -X POST http://127.0.0.1:5000/send-directory \
-H "Content-Type: application/json" \
-d '{
    "directory_path": "/home/divyansh/Documents/toDownload",
    "remote_host": "192.168.1.106",
    "remote_user": "narayan",
    "remote_path": "/home/narayan/testing",
    "remote_password": "lovelove"
}'

# Deactivate the virtual environment (optional)
# deactivate


