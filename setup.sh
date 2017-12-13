sudo cat "deb http://ftp.de.debian.org/debian jessie main" >> /etc/apt/sources.list 
sudo apt-get update
sudo apt-get install git python python-pip vim openssl libssl-dev python-opencv 
sudo pip install pyyaml gevent flask functools
sudo pip install numpy --upgrade
