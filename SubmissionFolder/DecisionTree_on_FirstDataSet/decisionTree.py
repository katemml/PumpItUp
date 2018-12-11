import pandas as pd
#df = pd.read_csv('C:/Users/Kay/Desktop/cleaned_train_values.csv',converters={"date_recorded":int})
#print(my_csv)
#df.to_csv("C:/Users/Kay/Desktop/UpdatedData.csv")

from sklearn import tree
train_set = []
label_set = []
file = open('C:/Users/Kay/Desktop/final/train.csv',"r")
label = open('C:/Users/Kay/Desktop/final/label.csv',"r")
for line in file:
    #train_set.append(map(int,(line.strip().split(','))))
    train_set.append(line.strip().split(','))
file.close()
#print(train_set)

for line in label:
    label_set.append(int(line))

label.close()
#print(label_set)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_set,label_set)

test_set = []
testfile = open('C:/Users/Kay/Desktop/final/test.csv',"r")
for line in testfile:
   # test_set.append(map(int,(line.strip().split(','))))
    test_set.append(line.strip().split(','))
testfile.close()

result = open ('C:/Users/Kay/Desktop/final/result.txt',"w")
for i in clf.predict(test_set):
    result.write(str(i))
    result.write('\n')


