# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:43:20 2018

@author: rajpa
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
import sklearn.preprocessing as sl
file=open("2015_unique.csv")
f1=file.read()
station=[]
gender=[]
location=[]
day=[]
time=[]
count=[]
lines=f1.split("\n")
z=np.ndarray(shape=(len(lines)-2,4), dtype=float, order='F')
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
z[:,0]=station
z[:,1]=location
z[:,2]=day
z[:,3]=time
outer=np.array(count)
outer=outer
assert outer.shape == (316,)
import tensorflow as tf

n_nodes_hl1=4
n_nodes_hl2=4
n_nodes_hl3=4

n_classes=55
batch_size=317

x=tf.placeholder('float',[None,4])
y=tf.placeholder('float')
def neural_network_model(data):
    hidden_1_layer={'weights':tf.Variable(tf.random_normal([4,n_nodes_hl1])),'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}
    hidden_2_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}
    hidden_3_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_nodes_hl3])),'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}
    output_layer={'weights':tf.Variable(tf.random_normal([n_nodes_hl3,n_classes])),'biases':tf.Variable(tf.random_normal([n_classes]))}
    
    l1=tf.add(tf.matmul(data,hidden_1_layer['weights']),hidden_1_layer['biases'])
    l1=tf.nn.relu(l1)
    l2=tf.add(tf.matmul(l1,hidden_2_layer['weights']),hidden_2_layer['biases'])
    l2=tf.nn.relu(l2)
    l3=tf.add(tf.matmul(l2,hidden_3_layer['weights']),hidden_3_layer['biases'])
    l3=tf.nn.relu(l3) 
    output=tf.add(tf.matmul(l3,output_layer['weights']),output_layer['biases'])
    return output
def train_neural_network(x):
    prediction=neural_network_model(x)
    cost =tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=tf.reshape(y,[316,55]),logits=prediction))
    optimizer= tf.train.AdamOptimizer(0.01).minimize(loss=cost)
    hm_epochs=10
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        
        for epoch in range(hm_epochs):
            epoch_loss=0
            
            epoch_x,epoch_y=z,outer
            tf.reshape(epoch_y,[316,1])
            _ , c = sess.run([optimizer,cost], feed_dict = {x:epoch_x,y:epoch_y})
            epoch_loss += c
            print('Epoch:',epoch,'Loss:',epoch_loss)
        print(y)        
        #correct=tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        #accuracy=tf.reduce_mean(tf.cast(correct,'float'))
        #print('Accuracy',accuracy.eval({x:mnist.test.images,y:mnist.test.labels}))

train_neural_network(x)


