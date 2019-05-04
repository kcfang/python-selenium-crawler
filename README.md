## Install requirements
### Run through ubuntu:18.04 image
You can use this image as a crawler environment.
```
docker build -t python-selenium-crawler .
```

### Install manually
```
// Install python3 and selenium
apt update && apt install -y python3 python3-pip wget zip
pip install -r requirements.txt

// Install chrome and chromedriver
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d /root/
```


## Run test script
```
docker run -ti python-selenium-crawler python3 /workspace/yahoo.py
```

Or just...
```
python yahoo.py
```
