# Python Based Docker
FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /alltypmovie_bot
WORKDIR /alltypmovie_bot
COPY start.sh /start.sh

# Running alltypmovie_bot
CMD ["/bin/bash", "/start.sh"]
