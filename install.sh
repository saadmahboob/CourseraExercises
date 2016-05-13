#################################
# installation for Ubuntu 16.04 
#		shoule work with Ubuntu 14.04
#################################

sudo apt-get install build-essential
sudo apt-get update
# BLAS → LAPACK → ATLAS → numpy → scipy → Theano
# remove numpy and scipy
sudo apt-get remove python-numpy
sudo apt-get remove python-scipy
# Instalation commands
sudo apt-get install gfortran
sudo apt-get install libopenblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install libatlas-base-dev

# Theano dep
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install python-nose
sudo apt-get install g++
sudo apt-get install git 


# Numpy
sudo pip install numpy -U
# Scipy
sudo pip install scipy -U
# Thano
sudo pip install theano -U
# Lasagne
sudo pip install lasagne -U
# Keras
sudo pip install keras -U
