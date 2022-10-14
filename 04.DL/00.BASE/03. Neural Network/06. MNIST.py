import sys, os
sys.path.append('dataset')
from mnist import load_mnist
from PIL import Image

# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# print(x_train.shape)
def img_show(img):
    pil_img = Image.fromarray(np.uint8)
