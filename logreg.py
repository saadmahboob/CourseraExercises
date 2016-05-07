import numpy as np
import csv 

def readDataset(filename='ex2data1.txt'):

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        datlist = list(reader)

    return np.array(datlist,dtype='float32')


def cost(x,y,theta):
    m = y.shape[0]
    h = hyp(x,theta,m)
    h1 = np.multiply(y,np.log(h))
    h2 = np.multiply(1- y,np.log(1-h))
    return -np.sum(h1+h2)/(1.0*m)

def hyp(x,theta,m):
    return sigmoid(np.dot(theta,x.reshape([3,m])))

def gd(x,y,theta,alpha = 0.005,iter=1000000):
    m = y.shape[0]

    for i in range(iter):
        h = hyp(x,theta,m)
        error = h-y
        update = np.dot(x,error)
        theta = theta - ( (alpha*update)/m )

    print 'theta',theta
    print 'cost',cost(x,y,theta)

def normalize(dataset):
    return np.divide(dataset.T,np.max(dataset,axis=1))

def sigmoid(x):
    return 1/(1 + np.exp(-x))

'''
_______ MAIN ________

'''
## Prepare dataset ##
dataset = readDataset(filename='ex2data1.txt').T
x = normalize(dataset[:-1]).T
y = dataset[-1]

print x.shape
print y.shape

m = y.shape[0]

X = np.ones([3,m])
print X.shape
X[1:] = x

print X.shape
print y.shape

# init theta 
theta = np.array([0,0,0])

#print hyp(X,theta,m)
#print hyp(X,theta,m).shape
# initial cost
print 'Initial Cost',cost(X,y,theta)
print 'Initial theta',theta

# gradient descent
gd(X,y,theta)
