import matplotlib.pyplot as plt

def plot(image):
    plt.axis('off')
    plt.imshow(image.reshape([28,28]),cmap='gray')

def plot_multiple(images):
    ni = images.shape[0]
    plt.figure(figsize=(50,3))
    plt.axis('off')
    for i in range(ni):
        plt.axis('off')
        plt.subplot(1,ni,i+1)
        plt.imshow(images[i].reshape([28,28]),cmap='gray')
        plt.axis('off')
