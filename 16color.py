"""
Name: Eric Zheng
Date:12/2/2021
"""

import pandas as pd
import numpy as np
import warnings; warnings.simplefilter('ignore')
from sklearn.cluster import MiniBatchKMeans
from matplotlib import image as img
from matplotlib import pyplot as plt



def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data
    
    # choose a random subset
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T
    
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].scatter(R, G, color=colors, marker='.')
    ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

    ax[1].scatter(R, B, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title, size=20);







imagename = input()
picture =img.imread(imagename))
ax = plt.axes(xticks=[], yticks=[])
data = picture / 255.0 # use 0...1 scale
data = data.reshape(427 * 640, 3)
data.shape
kmeans = MiniBatchKMeans(16)
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]
plot_pixels(data, colors=new_colors,title="Reduced color space: 16 colors")
picture_recolored = new_colors.reshape(picture.shape)
fig, ax = plt.subplots(1, 2, figsize=(16, 6),subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(picture)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(china_recolored)
ax[1].set_title('16-color Image', size=16);









