from sklearn.ensemble import RandomForestClassifier
import random

train_set = []
label_set = []
file = open('C:/Users/Kay/Desktop/train5.csv',"r")
label = open('C:/Users/Kay/Desktop/label.csv',"r")
for line in file:
    #train_set.append(map(int,(line.strip().split(','))))
    train_set.append(line.strip().split(','))
file.close()


for line in label:
    label_set.append(int(line))
label.close()


for k in range(0,10):
    clf = RandomForestClassifier(n_estimators=200)
    clf = clf.fit(train_set,label_set)


    test_set = []
    testfile = open('C:/Users/Kay/Desktop/final/test4.csv',"r")
    for line in testfile:
   # test_set.append(map(int,(line.strip().split(','))))
        test_set.append(line.strip().split(','))
    testfile.close()

    result = open ('C:/Users/Kay/Desktop/rf'+str(k)+'.txt',"w")
    for i in clf.predict(test_set):
        result.write(str(i))
        result.write('\n')

    k=k+1
