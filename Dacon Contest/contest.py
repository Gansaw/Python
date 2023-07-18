import random
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib import font_manager
from sklearn.preprocessing import MinMaxScaler


# 고정된 seed값 설정
def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
seed_everything(42)

# matplotlib 한글깨짐 방지
## 맑은 고딕 폰트 경로 설정 (PC 환경에 따라 다를 수 있음)
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()


# pandas의 read_csv를 이용하여 train데이터와 test데이터 불러오기
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# 데이터 프레임 정보 추출
train_data.info()


# 풍향을 예측한다는 점과 데이터를 분석한 결과 시계열 분포인 것을 확인
# 그리고 측정 시간대가 문자열로 이루어져 있기 때문에 categorical을 이용해야 한다는 것을 확인

# train 데이터
## 특성과 타겟 분리
features = train_data.drop(['ID', '풍속 (m/s)'], axis=1)
target = train_data['풍속 (m/s)']


## 측정 시간대 데이터의 분포를 확인 => (저녁, 오전, 오후, 새벽)로 확인
time_labels = train_data['측정 시간대'].unique()


## one-hot encoding을 수행하기 위해 측정 시간대 특성을 integer로 변환
time_label_mapping = {label: idx for idx, label in enumerate(time_labels)}
features['측정 시간대'] = features['측정 시간대'].map(time_label_mapping)


## tf.keras.utils.to_categorical 함수를 사용해서 one-hot encoding 진행
categorical_feature = features['측정 시간대']
categorical_feature = tf.keras.utils.to_categorical(categorical_feature)


## MinMaxScaler을 이용하여 전처리 진행
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(features)
x_train = np.reshape(scaled_features, (scaled_features.shape[0], 1, scaled_features.shape[1]))


## LSTM 모델 생성
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.LSTM(64, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(tf.keras.layers.Dense(1)) 


## 모델 컴파일 - optimizer은 adam을 이용하였고 풍향을 예측하는 것이기 때문에(수치 의미 有) loss를 MSE를 사용
model.compile(optimizer='adam', loss='MSE')


## 모델 학습
model_train = model.fit(x_train, target, epochs=5, batch_size=16)

## matplotlib를 이용하여 시각화 진행
plt.plot(model_train.history['loss'])
plt.title('Train Loss')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.show()


# test 데이터 (train 데이터에 수행했던 것처럼 test 데이터에도 수행)
test_features = test_data.drop(['ID'], axis=1)
test_time_labels = test_data['측정 시간대'].unique()
test_time_label_mapping = {label: idx for idx, label in enumerate(test_time_labels)}
test_features['측정 시간대'] = test_features['측정 시간대'].map(test_time_label_mapping)
# 테스트 데이터에 대해 훈련 데이터에서 사용한 scaler를 그대로 사용
test_scaled_features = scaler.transform(test_features)
x_test = np.reshape(test_scaled_features, (test_scaled_features.shape[0], 1, test_scaled_features.shape[1]))

## test 데이터로 모델 예측
predictions = model.predict(x_test)

## 예측 결과 시각화
plt.figure(figsize=(12, 6))
plt.plot(target.values, label='실제값', color='red')
plt.plot(predictions, label='예측값', color='blue')
x_ticks = test_data['측정 시간대'].index
plt.title("test 데이터 예측값과 실제값")
plt.xlabel('측정 시간대')
plt.ylabel('풍속 (m/s)')
plt.legend()
plt.show()

# submission DataFrame을 CSV 파일로 저장
submission = pd.DataFrame()
submission['ID'] = test_data['ID']
submission['풍속 (m/s)'] = predictions
submission.to_csv('submission.csv', index=False)