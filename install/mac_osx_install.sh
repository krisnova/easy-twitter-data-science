#!/usr/bin/env bash

cd install

# Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Jupyter
brew install -y wget
brew install -y make
EXISTS=`which jupyter`
if [ -z "$EXISTS" ]; then
    wget -nc https://repo.continuum.io/archive/Anaconda2-4.1.1-MacOSX-x86_64.pkg -O anaconda.pkg
    open anaconda.pkg
fi

# Tweepy
sudo easy_install six
sudo -H pip install tweepy

# Numpy
sudo -H pip install numpy

# Matplotlib
sudo -H pip install matplotlib
