# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:28:01 2018

@author: rajpa
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:10:13 2018

@author: rajpa
"""


import numpy as np
from sklearn.linear_model import LogisticRegression
import sklearn.preprocessing as sl

import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

file=open("2015_unique.csv")
f1=file.read()
station=[]
gender=[]
location=[]
day=[]
time=[]
count=[]
lines=f1.split("\n")
x=np.ndarray(shape=(len(lines)-2,4), dtype=float, order='F')
print(x.shape)
for i in range(1,len(lines)-1):
    station.append(lines[i].split(",")[0])
    location.append(lines[i].split(",")[1])
    day.append(int(lines[i].split(",")[2]))
    time.append(int(lines[i].split(",")[3]))
    count.append(int(lines[i].split(",")[4]))

enc1 = sl.LabelEncoder()
enc1.fit(station)
station = enc1.transform(station)    

enc2=sl.LabelEncoder()
enc2.fit(location)
location = enc2.transform(location)  
outer=[]
x[:,0]=station
x[:,1]=location
x[:,2]=day
x[:,3]=time
outer=np.array(count)
y = outer

def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=4, kernel_initializer='normal', activation='relu'))
    model.add(Dense(30, input_dim=20, kernel_initializer='normal', activation='relu'))
    model.add(Dense(40, input_dim=30, kernel_initializer='normal', activation='relu')) 
    model.add(Dense(40, input_dim=40, kernel_initializer='normal', activation='relu')) 
    model.add(Dense(50, input_dim=40, kernel_initializer='normal', activation='relu')) 
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

seed=7
np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, x, y, cv=kfold)
print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))
pipeline.fit(x,y)
f=open("2016.csv")
f1=f.read()
lines=f1.split("\n")
station=[]
location=[]
day=[]
time=[]
for i in range(1,len(lines)-1):
    station.append(lines[i].split(",")[0])
    location.append(lines[i].split(",")[1])
    day.append(int(lines[i].split(",")[2]))
    time.append(int(lines[i].split(",")[3]))
    #print(i)

enc1 = sl.LabelEncoder()
enc1.fit(station)
station = enc1.transform(station)    

enc2=sl.LabelEncoder()
enc2.fit(location)
location = enc2.transform(location)  
x=np.ndarray(shape=(len(lines)-2,4), dtype=float, order='F')
x[:,0]=station
x[:,1]=location
x[:,2]=day
x[:,3]=time
y=pipeline.predict(x)
f2=open("count2016.csv","w")
for i in range(len(y)):
    f2.write(str(y[i]))
    f2.write("\n")
f2.close()    


