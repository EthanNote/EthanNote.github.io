import keras
import numpy as np
import cv2
keras.datasets.mnist.get_file('MNIST', 'http://yann.lecun.com/exdb/mnist/')
(x_train, y_train), (x_test, y_test)=keras.datasets.mnist.load_data('MNIST')

model=keras.models.Sequential()

model.add(keras.layers.Dense(units=100, activation='relu', input_dim=784))
model.add(keras.layers.Dense(units=100, activation='relu'))
model.add(keras.layers.Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

x=x_train.reshape([60000, 784])
xt=x_test.reshape([10000, 784])

y=np.array([[0]*10]*60000)
for i in range(60000):
	y[i][y_train[i]]=1

yt=np.array([[0]*10]*10000)
for i in range(10000):
	yt[i][y_test[i]]=1


model.fit(x, y, batch_size=16, epochs=20)
out=model.predict(xt)

match=0
for i in range(out.shape[0]):
	if np.argmax(out[i])==np.argmax(yt[i]):
		match+=1
print("ACC: %d/%d"%(match, out.shape[0]))

i=0
while(True):	
	m=cv2.resize(x_test[i], (560, 560))
	cv2.putText(m, str(np.round(out[i],2)),(0,20),0,0.5,(255,0,0),2)
	cv2.putText(m, str(np.argmax(out[i])),(0,60),0,1,(255,0,0),2)
	cv2.imshow('Test image', m)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('n'):
		i+=1
	if k==ord('q'):
		break
