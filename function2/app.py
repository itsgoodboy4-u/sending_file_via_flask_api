from flask import Flask, send_file, request, abort, render_template, jsonify
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_file_or_directory():
    file_name = request.form.get('fileName')
    target_directory = request.form.get('targetDirectory')
    
    if not file_name:
        abort(400, 'File name is required')
    
    base_path = '/home/divyansh/Downloads/test/'
    full_path = os.path.join(base_path, file_name)
    
    if not os.path.exists(full_path):
        return jsonify({'error': 'File not found'}), 404

    if not os.path.exists(target_directory):
        try:
            os.makedirs(target_directory)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    try:
        if os.path.isfile(full_path):
            target_file_path = os.path.join(target_directory, file_name)
            with open(full_path, 'rb') as f:
                data = f.read()
            with open(target_file_path, 'wb') as f:
                f.write(data)
            return send_file(target_file_path, as_attachment=True)
        elif os.path.isdir(full_path):
            memory_file = zip_directory(full_path)
            return send_file(memory_file, download_name='archive.zip', as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
