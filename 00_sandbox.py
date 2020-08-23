from os import listdir
from PIL import Image as PImage


def loadimages(pth):
    # return array of images

    imageslist = listdir(pth)
    loadedimages = []
    for IMAGE in imageslist:
        imag = PImage.open(pth + IMAGE)
        loadedimages.append(imag)

    return loadedimages


pth = "F:\COM301\Programming\JA_Flags_Quiz\Flags_Dataset"

# your images in an array
imgs = loadimages(pth)

for img in imgs:
    # you can show every image
    img.show()
