FROM ubuntu:18.04

WORKDIR /workspace/

RUN apt update && apt install -y python3 python3-pip wget zip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
	apt install -y ./google-chrome-stable_current_amd64.deb && \
	wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip && \
	unzip chromedriver_linux64.zip -d /root/
ADD requirements.txt /
RUN pip3 install -r /requirements.txt

ADD . /workspace/
