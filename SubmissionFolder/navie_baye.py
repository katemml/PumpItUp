train_set = []
label_set = []
file = open('C:/Users/Kay/Desktop/final/0417classify/train_classify.csv',"r")
label = open('C:/Users/Kay/Desktop/final/label.csv',"r")
for line in file:
    #train_set.append(map(int,(line.strip().split(','))))
    train_set.append(line.strip().split(','))
file.close()
#print(train_set)

for line in label:
    label_set.append(int(line))

label.close()

import numpy as np

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
X = np.array(train_set).astype(np.float)
Y = np.array(label_set).astype(np.float)
clf.fit(X,Y)
GaussianNB(priors=None)

test_set = []
testfile = open('C:/Users/Kay/Desktop/final/0417classify/test_classify.csv',"r")
for line in testfile:
   # test_set.append(map(int,(line.strip().split(','))))
    test_set.append(line.strip().split(','))
testfile.close()

T = np.array(test_set).astype(np.float)
result = open ('C:/Users/Kay/Desktop/final/nbresult2.txt',"w")
for i in clf.predict(T):
    result.write(str(i))
    result.write('\n')

