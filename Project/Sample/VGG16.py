# 1. 필수 import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.applications import vgg16
import tensorboard as tb

# 2. VGG16 모델 만들기
def createVgg16():
    model = vgg16.VGG16()
    return model

# 3. 데이터 전처리
def imageDataGenerator():
    pass

# 메인 함수
def main():
    # VGG16 모델 생성 및 출력
    vgg16_model = createVgg16()
    vgg16_model.summary()        
    data_generator = imageDataGenerator()    


if __name__ == "__main__":
    main()
