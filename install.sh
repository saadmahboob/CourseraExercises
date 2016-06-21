#################################
# installation for Ubuntu 16.04 
#		shoule work with Ubuntu 14.04
#################################

sudo apt-get --assume-yes install build-essential
sudo apt-get update
# BLAS → LAPACK → ATLAS → numpy → scipy → Theano
# remove numpy and scipy
sudo apt-get remove python-numpy
sudo apt-get remove python-scipy
# Instalation commands
sudo apt-get --assume-yes install gfortran
sudo apt-get --assume-yes install libopenblas-dev
sudo apt-get --assume-yes install liblapack-dev
sudo apt-get --assume-yes install libatlas-base-dev

# Theano dep
sudo apt-get --assume-yes install python-dev
sudo apt-get --assume-yes install python-pip
sudo apt-get --assume-yes install python-nose
sudo apt-get --assume-yes install g++
sudo apt-get --assume-yes install git 

sudo -H pip install pip -U

# Numpy
sudo -H pip install numpy -U
# Scipy
sudo -H pip install scipy -U
# Thano
sudo -H pip install theano -U
# Lasagne
sudo -H pip install lasagne -U
# Keras
sudo -H pip install keras -U


###
# Install Jupyter Notebook
###
sudo apt-get -y install ipython ipython-notebook
sudo -H pip install jupyter
