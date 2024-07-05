from flask import Flask, request, jsonify
import os
import shutil
import paramiko

app = Flask(__name__)

def compress_directory(directory_path):
    base_name = os.path.basename(directory_path)
    archive_name = shutil.make_archive(base_name, 'zip', directory_path)
    return archive_name

def transfer_file(file_path, remote_host, remote_user, remote_path, remote_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host, username=remote_user, password=remote_password)
    
    sftp = ssh.open_sftp()
    sftp.put(file_path, os.path.join(remote_path, os.path.basename(file_path)))
    sftp.close()
    ssh.close()

@app.route('/send-directory', methods=['POST'])
def send_directory():
    data = request.json
    directory_path = data.get('directory_path')
    remote_host = data.get('remote_host')
    remote_user = data.get('remote_user')
    remote_path = data.get('remote_path')
    remote_password = data.get('remote_password')

    if not all([directory_path, remote_host, remote_user, remote_path, remote_password]):
        return jsonify({"error": "Missing required parameters"}), 400

    if not os.path.isdir(directory_path):
        return jsonify({"error": "Invalid directory path"}), 400

    archive_path = compress_directory(directory_path)
    transfer_file(archive_path, remote_host, remote_user, remote_path, remote_password)
    
    return jsonify({"message": "Directory sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
