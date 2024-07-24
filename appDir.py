from flask import Flask, send_file, request, abort
import os
import zipfile
from io import BytesIO

app = Flask(__name__)

def zip_directory(directory_path):
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                zf.write(os.path.join(root, file),
                         os.path.relpath(os.path.join(root, file),
                                         os.path.join(directory_path, '..')))
    memory_file.seek(0)
    return memory_file

@app.route('/download', methods=['GET'])
def download_file_or_directory():
    path = request.args.get('path')
    if not path:
        abort(400, 'Path is required')
    
    if not os.path.exists(path):
        abort(404, 'Path not found')

    if os.path.isfile(path):
        return send_file(path, as_attachment=True)
    elif os.path.isdir(path):
        memory_file = zip_directory(path)
        return send_file(memory_file, download_name='archive.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
