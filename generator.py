from __future__ import print_function, division
from keras.datasets import mnist
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from keras.models import load_model
import os
import cv2

model_dir = ""
output_dir = ""


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print("Finished loading tensorflow backend.")
print("Loading model ")
generator = load_model(f'{model_dir}/g_[2000].h5')
print("Finished loading model.")
def get_noise():
	latent_dim = 100
	r, c = 5, 5
	return np.random.normal(0, 1, (r * c, latent_dim))


def generate():
	noise = get_noise()
	gen_imgs = generator.predict(noise)
	gen_imgs = 0.5 * gen_imgs + 0.5
	print("Generating images")
	for i in tqdm(range(len(gen_imgs))):
		plt.axis('off')
		plt.imshow(cv2.cvtColor(gen_imgs[i], cv2.COLOR_BGR2RGB))
		plt.savefig(f"{output_dir}/{i}.png", bbox_inches='tight')
		plt.close()
generate()


