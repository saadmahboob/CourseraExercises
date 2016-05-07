import numpy as np
import csv 

def readDataset(filename='ex1data1.txt'):

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        datlist = list(reader)

    return np.array(datlist,dtype='float32')


def cost(x,y,theta):
    m = y.shape[0]
    h = np.dot(theta,x.reshape([3,m]))
    #print h.shape,x.shape,y.shape,theta.shape
    return np.sum(np.square(y-h))/(2.0*m)

def hyp(x,theta,m):
    return np.dot(theta,x.reshape([3,m]))

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

'''
_______ MAIN ________

'''
## Prepare dataset ##
dataset = readDataset(filename='ex1data2.txt').T
# normalize
nr_dataset = normalize(dataset).T
x = nr_dataset[:-1]
y = nr_dataset[-1]

m = y.shape[0]

X = np.ones([3,m])
X[1:] = x

print X.shape
print y.shape

# init theta 
theta = np.array([0,0,0])

# initial cost
print 'Initial Cost',cost(X,y,theta)
print 'Initial theta',theta

# gradient descent
gd(X,y,theta)
