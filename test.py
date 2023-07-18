import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# pandas의 read_csv를 이용하여 train데이터와 test데이터 불러오기
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# 풍향을 예측한다는 점과 데이터를 분석한 결과 시계열 분포인 것을 확인
# 그리고 측정 시간대가 
print(train_data['측정 시간대'].unique())