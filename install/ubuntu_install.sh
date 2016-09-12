#!/usr/bin/env bash

cd install
echo "Please enter your password.."
sudo echo ""

# Jupyter
brew install -y wget
wget -nc https://repo.continuum.io/archive/Anaconda2-4.1.1-MacOSX-x86_64.sh -O jupyter.sh
sh jupyter.sh

# Tweepy
sudo -H pip install tweepy

# Numpy
sudo -H pip install numpy

# Matplotlib
sudo -H pip install matplotlib