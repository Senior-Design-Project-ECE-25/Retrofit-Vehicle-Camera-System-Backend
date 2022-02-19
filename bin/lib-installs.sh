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
