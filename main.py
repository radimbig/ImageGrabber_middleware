from flask import Flask, request, send_file
from flask_cors import CORS
import requests
import tempfile

app = Flask(__name__)
cors = CORS(app, resources={r"/api/download-image": {"origins": "*"}})
@app.route('/api/download-image', methods=['POST'])
def download_image():
    data = request.get_json()
    link = data.get("link")
    
    print(link)
    if link:
        try:
            response = requests.get(link)
            print(response.status_code)
            if response.status_code == 200:
                # Save the image temporarily
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                temp_file.write(response.content)
                temp_file.close()
                
                # Return the image file
                return send_file(temp_file.name, mimetype='image/jpeg')
            else:
                
                return "Failed to fetch the image from the provided link."
        except requests.exceptions.RequestException as e:
            return str(e)
    else:
        return "Please provide a valid 'link' query parameter."

if __name__ == '__main__':
    app.run()
