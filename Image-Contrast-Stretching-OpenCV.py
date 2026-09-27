# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 12:29:10 2024

@author: jose ochoa
"""

import cv2
import numpy as np 

img = cv2.imread("img3_E13.jpg")  

i_min = 10 
i_max = 80

img = img.clip(10, 80) 

img = (img-i_min)/(i_max-i_min) 

img = (img*255).astype(int)

cv2.imwrite("img3_corregida_E13.jpg", img)

#ejrcicio 13