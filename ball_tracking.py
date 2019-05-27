import numpy as np
import cv2
import timeit
import time
from imutils.video import FPS
from threading import Thread
import math


class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False
