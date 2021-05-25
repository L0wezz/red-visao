import cv2
import numpy as np
from reddragons.visao import estruturas
from copy import deepcopy

class ConverteHSV:
    def processa (self, imagem, dest: estruturas.Imagem = None):
        img_proc = cv2.cvtColor(
            np.uint8(imagem), cv2.COLOR_RGB2HSV
        )
        if dest:
            dest.imagem_hsv = deepcopy(img_proc)
        return img_proc
