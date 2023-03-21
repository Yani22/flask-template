# aimhi-server

## Prerequisites
* [Python 3](https://www.python.org/downloads/)
* [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)
    * [Installation Guide](https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/)

## Clone repo
``` bash
# clone through https...
git clone https://ashleyvillos@bitbucket.org/ashleyvillos/aimhi.git

# ...or clone through ssh
git clone git@bitbucket.org:ashleyvillos/aimhi.git

# go into main directory
cd aimhi

# go into server directory
cd aimhi-server
```

## Install and activate Virtual Environment
``` bash
# install virtual environment
pip install virtualenv

# create a virtual environment
virtualenv venv

# activate virtual environment (windows os)
source venv/Scripts/activate

# activate virtual environent (mac os)
source venv/bin/activate
```

## Install Python library prerequisites
``` bash
pip install -r requirements.txt
```

## List of Libraries that will be downloaded
Check out requirements.txt in aimhi-server/ directory
```
certifi==2021.5.30
chardet==4.0.0
click==8.0.1
colorama==0.4.4
cycler==0.10.0
decorator==4.4.2
easyocr==1.3.2
Flask==2.0.1
Flask-Cors==3.0.10
idna==2.10
imageio==2.9.0
itsdangerous==2.0.1
Jinja2==3.0.1
joblib==1.0.1
kiwisolver==1.3.1
MarkupSafe==2.0.1
matplotlib==3.4.2
networkx==2.5.1
numpy==1.20.3
opencv-python==4.5.2.52
pandas==1.2.4
pdf2image==1.15.1
Pillow==8.2.0
pip-autoremove==0.9.1
pyparsing==2.4.7
python-bidi==0.4.2
python-dateutil==2.8.1
pytz==2021.1
PyWavelets==1.1.1
PyYAML==5.4.1
requests==2.25.1
scikit-image==0.18.1
scikit-learn==0.24.2
scipy==1.6.3
six==1.16.0
sklearn==0.0
threadpoolctl==2.1.0
tifffile==2021.4.8
torch==1.8.1
torchvision==0.9.1
typing-extensions==3.10.0.0
urllib3==1.26.5
Werkzeug==2.0.1
```

## Run Server
``` bash
python server.py
``` 