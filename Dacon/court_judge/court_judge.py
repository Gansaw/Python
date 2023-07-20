import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from matplotlib import font_manager
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# matplotlib 한글깨짐 방지
## 맑은 고딕 폰트 경로 설정 (PC 환경에 따라 다를 수 있음)
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# train data 정보 확인
train_data.info()
## 결측치 없음
## data type가 object이기 때문에 categorical 필요

# 데이터 전처리
vectorizer = TfidfVectorizer()
def get_vector(vectorizer, df, train_mode):
    if train_mode:
        x_facts = vectorizer.fit_transform(df['facts'])
    else:
        x_facts = vectorizer.transform(df['facts'])
    x_party1 = vectorizer.transform(df['first_party'])
    x_party2 = vectorizer.transform(df['second_party'])
    
    x = np.concatenate([x_party1.todense(), x_party2.todense(), x_facts.todense()], axis=1)
    return x

X_train = get_vector(vectorizer, train_data, True)
Y_train = train_data["first_party_winner"]
X_test = get_vector(vectorizer, test_data, False)

# model 제작
model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(units = ))