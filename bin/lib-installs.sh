#!/usr/bin/bash
# Update and Upgrade
sudo apt-get update 
sudo apt-get upgrade

# Install Dependancies
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

# Install OpenCV (Alternate)
# sudo apt-get install libopencv-dev python3-opencv



# Alternate Libs
# sudo apt-get update 
# sudo apt-get upgrade
# sudo apt-get install build-essential cmake pkg-config
# sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
# sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
# sudo apt-get install libxvidcore-dev libx264-dev
# # sudo apt-get install libgtk2.0-dev # OpenCV GUI
# sudo apt-get install libatlas-base-dev gfortran
