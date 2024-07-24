# Flask File and Directory Downloader

This repository contains a Flask application that allows you to download files or directories from a server. It also includes a Python script to interact with the Flask server to download the requested files or directories.

## Features

- Download individual files from the server.
- Download entire directories from the server, which will be compressed into a ZIP archive before download.
- Extract the downloaded ZIP archive automatically on the client-side.

## Prerequisites

- Python 3.6 or above
- Flask
- Requests library

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/itsgoodboy4-u/sending_file_via_flask_api.git
    cd sending_file_via_flask_api
    ```

2. **Install the required dependencies**:
    ```bash
    pip install flask requests
    ```

3. **Run the Flask server**:
    ```bash
    python app.py
    ```
    The server will start running at `http://0.0.0.0:5000`.

## Usage

### Server Side

The Flask server provides an endpoint `/download` which accepts a `GET` request with a `path` parameter. The `path` parameter should specify the file or directory you want to download.

Example:
- To download a file or directory from the server, make a request to:
  ```
  http://<server_ip>:5000/download?path=<path_to_file_or_directory>
  ```

### Client Side

The client script `download.py` can be used to interact with the Flask server to download files or directories. 

1. **Update the script with server URL and paths**:
    - Set the `server_url` to your Flask server URL.
    - Set the `path` to the file or directory you want to download.
    - Set the `save_path` to the location where you want to save the downloaded file or directory.

2. **Run the client script**:
    ```bash
    python download.py
    ```

### Example

Suppose you want to download a file located at `/home/divyansh/Downloads/test.txt` on the server and save it to `/home/divyansh/Downloads/save_here` on the client side:

- Update the `download.py` script as follows:
  ```python
  server_url = 'http://xxx.xxx.x.xxx:5000'
  path = '/home/divyansh/Downloads/test.txt'
  save_path = '/home/divyansh/Downloads/save_here/test.txt'
  ```

- Run the script:
  ```bash
  python download.py
  ```

If you want to download a directory located at `/home/divyansh/Downloads/test` on the server and save it to `/home/divyansh/Downloads/save_here` on the client side:

- Update the `download.py` script as follows:
  ```python
  server_url = 'http://xxx.xxx.x.xxx:5000'
  path = '/home/divyansh/Downloads/test'
  save_path = '/home/divyansh/Downloads/save_here/recieved_archive.zip'
  ```

- Run the script:
  ```bash
  python download.py
  ```

The script will download the directory, extract the contents, and save them to the specified location.

## Notes

- Ensure that the `path` specified in the request exists on the server.
- The server compresses directories into ZIP archives for download.
- The client script automatically extracts the ZIP archive upon download.

