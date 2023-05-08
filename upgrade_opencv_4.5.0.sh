#!/bin/bash

echo ""
echo "[Note] Update opencv from 4.2.0 to 4.5.0"
echo ""

sudo apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev build-essential mlocate
sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo apt update -y
sudo apt install -y libjasper1 libjasper-dev
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.5.0 opencv
mv opencv_contrib-4.5.0 opencv_contrib
mv opencv_contrib opencv
cd ~/opencv && mkdir build && cd build
cmake ..
sudo make
sudo make install
cd ~
rm opencv.zip opencv_contrib.zip

sudo touch /etc/ld.so.conf.d/opencv.conf
sudo sh -c "echo \"/usr/local/lib\" >> /etc/ld.so.conf.d/opencv.conf"
sudo ldconfig -y
sudo sh -c "echo \"PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig\" >> /etc/bash.bashrc"
sudo sh -c "echo \"export PKG_CONFIG_PATH\" >> /etc/bash.bashrc"
source /etc/bash.bashrc
sudo updatedb -y

echo ""
echo "[Note] Update opencv complete"
echo ""

source $HOME/.bashrc
exit 0
