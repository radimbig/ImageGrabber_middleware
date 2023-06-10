# ImageGrabber_middleware
This is a program that you can use as middleware to download photos from sites that have strict CORS rules.
## Installation
```pip install flask flask_cors```
## How to run?
```cd ImageGrabber_middleware```\
```py main.py```
## Usage
To download image from other website you have to make post requests to 
```http://127.0.0.1:5000/api/download-image```
with json body that have "link" as key ad image link as value
