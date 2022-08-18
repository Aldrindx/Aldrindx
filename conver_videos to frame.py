# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 19:02:41 2022

@author: adars
"""

import cv2
vidcap = cv2.VideoCapture('Epoi Ali _ tutorial haircut.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1