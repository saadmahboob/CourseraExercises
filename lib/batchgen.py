import numpy as np

def batch_gen(X,y,N):
    while True:
        idx = np.random.choice(len(y),N)
        yield X[idx].astype('float32'),y[idx].astype('int32')
