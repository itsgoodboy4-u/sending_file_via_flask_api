import requests
import zipfile
import os

def download_file_or_directory(server_url, path, save_path):
    params = {'path': path}
    response = requests.get(f'{server_url}/download', params=params)
    
    if response.status_code == 200:
        if 'application/zip' in response.headers.get('Content-Type'):
            with open(save_path, 'wb') as file:
                file.write(response.content)
            with zipfile.ZipFile(save_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(save_path))
            print(f'Directory downloaded and extracted to {os.path.dirname(save_path)}')
            
            os.remove(save_path)
            print(f'Archive file {save_path} deleted')
        else:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f'File downloaded successfully and saved to {save_path}')
    else:
        print(f'Failed to download. Status code: {response.status_code}')

if __name__ == '__main__':
    server_url = 'http://xxx.xxx.x.xxx:5000'
    path = '/home/divyansh/Downloads/test'            # <---- Where the file is
    save_path = '/home/divyansh/Downloads/save_here'  # <---- Where to save the folder or file
    
    if os.path.isfile(path):
        save_path = save_path + "/" + os.path.basename(path)

    elif os.path.isdir(path):
        save_path = save_path + "/recieved_archive.zip"
        
    download_file_or_directory(server_url, path, save_path)
