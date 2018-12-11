from sklearn.ensemble import RandomForestClassifier
import random

train_set = []
label_set = []
file = open('C:/Users/Kay/Desktop/final/train_new.csv',"r")
label = open('C:/Users/Kay/Desktop/final/label.csv',"r")
for line in file:
    #train_set.append(map(int,(line.strip().split(','))))
    train_set.append(line.strip().split(','))
file.close()
#print(train_set)

for line in label:
    label_set.append(int(line))
label.close()

clf = RandomForestClassifier(n_estimators=200)
clf = clf.fit(train_set,label_set)


test_set = []
testfile = open('C:/Users/Kay/Desktop/final/test_new.csv',"r")
for line in testfile:
   # test_set.append(map(int,(line.strip().split(','))))
    test_set.append(line.strip().split(','))
testfile.close()

result = open ('C:/Users/Kay/Desktop/final/result_rf.txt',"w")
for i in clf.predict(test_set):
    result.write(str(i))
    result.write('\n')
