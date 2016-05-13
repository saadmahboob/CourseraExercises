

# In[64]:


import numpy as np
from theano import function,tensor as T
import lasagne
import hickle as hkl


# In[ ]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[65]:

from lib.batchgen import batch_gen


# In[153]:

def plot_onehidden(image):
    plt.axis('off')
    plt.imshow(image.reshape([20,20]),cmap='gray')





tx = hkl.load('x.hkl')
ty = hkl.load('y.hkl')
print ty.shape
tobechanged = np.where(ty == 10)
ty[:500]=0





gen = batch_gen(tx,ty,64)


# In[140]:

#model 

lin = lasagne.layers.InputLayer([None,20*20])

lout = lasagne.layers.DenseLayer(lin,num_units=10,nonlinearity=lasagne.nonlinearities.softmax)


X = T.matrix()
Y = T.ivector()


output = lasagne.layers.get_output(lout,X)




loss = T.mean(lasagne.objectives.categorical_crossentropy(output,Y))
acc = T.mean(T.eq(Y,output.argmax(-1)))



params = lasagne.layers.get_all_params(lout)




grad = T.grad(loss,params)
updates = lasagne.updates.sgd(grad,params,learning_rate=0.01)
pred = output.argmax(-1) 



train = function([X,Y],[loss,acc],updates=updates)
predict = function([X],pred)

num_batches = tx.shape[0]//64



for i in range(1000):
    gloss = 0
    gacc = 0
    for _ in range(num_batches):
        batx , baty = gen.next()
        baty = baty.reshape(64)
        tloss,tacc= train(batx,baty)
        gloss+=tloss
        gacc += tacc
    print i,gloss/num_batches,gacc/num_batches



images = params[0].get_value().T
print images[9].shape
plot_onehidden(images[4])




