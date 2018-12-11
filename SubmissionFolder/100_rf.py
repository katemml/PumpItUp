
# coding: utf-8

# In[103]:


from sklearn.ensemble import AdaBoostClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import random


# In[104]:


train_set = []
label_set = []
test_set = []
my_result = []
cleaned_id = []
label = open('/Users/trevor/Desktop/final_project/kate/label_classify.csv', "r")
file = open('/Users/trevor/Desktop/final_project/new_Set/train2.csv', "r")
test = open('/Users/trevor/Desktop/final_project/new_Set/test2.csv',"r")
id = open('/Users/trevor/Desktop/final_project/cleaned/cleaned_test_values.csv',"r")
for line in file:
    line = line[0:len(line)-2]
    train_set.append(line.split(','))
file.close()
for line in label:
    label_set.append(int(line))
label.close()
for line in test:
    line = line[0:len(line)-2]
    test_set.append(line.split(','))
test.close()
for line in id:
    cleaned_id.append(line.split(','))
id.close()


# In[105]:


train_set_b = train_set
label_set_b = label_set
ad_all = []
dt_all = []
rf_all = []
x_v = []


# In[106]:


def get_dt(train_set,label_set,test_set,test_label):
    global dt_all
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_set,label_set)
    result_dt = clf.predict(test_set)
    correct = 0
    total = 0
    for i in range(0,len(result_dt)):
        total = total + 1
        if result_dt[i]==test_label[i]:
            correct = correct + 1
    dt = float(correct)/total
    dt_all.append(dt)
    #print dt


# In[107]:


def get_ad(train_set,label_set,test_set,test_label):
    global ad_all
    clf = AdaBoostClassifier(n_estimators=100,learning_rate=1)
    clf.fit(train_set,label_set)
    result_ad = clf.predict(test_set)
    correct = 0
    total = 0
    for i in range(0,len(result_ad)):
        total = total + 1
        if result_ad[i]==test_label[i]:
            correct = correct + 1
    ad = float(correct)/total
    ad_all.append(ad)
    #print ad


# In[108]:


def get_rf(train_set,label_set,test_set,test_label):
    global rf_all
    clf = RandomForestClassifier(n_estimators=200)
    clf = clf.fit(train_set,label_set)
    result_rf = clf.predict(test_set)
    correct = 0
    total = 0
    for i in range(0,len(result_rf)):
        total = total + 1
        if result_rf[i]==test_label[i]:
            correct = correct + 1
    rf = float(correct)/total
    rf_all.append(rf)
    #print rf


# In[125]:


for k in range(1,6):
    x_v.append(k*1000)
    for n in range(0,5):
        train_set = []
        label_set = []
        test_set = []
        test_label = []
        chosen = random.sample(range(0, len(train_set_b)), k*1000)
        for i in range(0,len(train_set_b)):
            if i in chosen:
                test_label.append(label_set_b[i])
                test_set.append(train_set_b[i])
            else:
                train_set.append(train_set_b[i])
                label_set.append(label_set_b[i])
        get_rf(train_set,label_set,test_set,test_label)
        get_ad(train_set,label_set,test_set,test_label)
        get_dt(train_set,label_set,test_set,test_label)


# In[126]:


rf_f = sum(rf_all)/len(rf_all)
ad_f = sum(ad_all)/len(ad_all)
dt_f = sum(dt_all)/len(dt_all)
print 'rf_f = ',rf_f
print 'ad_f = ',ad_f
print 'dt_f = ',dt_f


# In[127]:


print rf_all
print ad_all
print dt_all


# In[112]:


clf_dt = tree.DecisionTreeClassifier()
clf_dt = clf_dt.fit(train_set_b,label_set_b)

clf_ad = AdaBoostClassifier(n_estimators=100,learning_rate=1.5)
clf_ad = clf_ad.fit(train_set_b,label_set_b)

clf_rf = RandomForestClassifier(n_estimators=100)
clf_rf = clf_rf.fit(train_set_b,label_set_b)


# In[113]:


test_set = []
test = open('/Users/trevor/Desktop/final_project/new_Set/test2.csv',"r")
for line in test:
    line = line[0:len(line)-2]
    test_set.append(line.split(','))
test.close()


# In[114]:


result_dt_i = clf_dt.predict(test_set)
result_ad_i = clf_ad.predict(test_set)
result_rf_i = clf_rf.predict(test_set)

result_dt = []
result_ad = []
result_rf = []

for i in range(0,len(result_dt_i)):
    result_dt.append([result_dt_i[i]])
    result_ad.append([result_ad_i[i]])
    result_rf.append([result_rf_i[i]])

for n in range(0,100):
    clf_dt = tree.DecisionTreeClassifier()
    clf_dt = clf_dt.fit(train_set_b,label_set_b)

    clf_ad = AdaBoostClassifier(n_estimators=100,learning_rate=1.5)
    clf_ad = clf_ad.fit(train_set_b,label_set_b)

    clf_rf = RandomForestClassifier(n_estimators=100)
    clf_rf = clf_rf.fit(train_set_b,label_set_b)
    for i in range(0,len(result_dt)):
        result_dt[i].append(clf_dt.predict([test_set[i]])[0])
        result_ad[i].append(clf_ad.predict([test_set[i]])[0])
        result_rf[i].append(clf_rf.predict([test_set[i]])[0])


# In[115]:


#from statistics import mode
#def find_mode(f_list):
#    all_n = []
#    count_n = []
#    for i in range(0,len(f_list)):
#        if f_list[i] not in all_n:
#            all_n.append(f_list[i])
#            count_n.append(0)
#        count_n[all_n.index(f_list[i])] = count_n[all_n.index(f_list[i])] + 1
#    return all_n[count_n.index(max(count_n))]


# In[116]:


from statistics import mode
def find_mode_f(f_list):
    all_n = []
    count_n = []
    for i in range(0,len(f_list)):
        if f_list[i] not in all_n:
            all_n.append(f_list[i])
            count_n.append(0)
        count_n[all_n.index(f_list[i])] = count_n[all_n.index(f_list[i])] + 1
    mode_n = all_n[count_n.index(max(count_n))]
    if float(max(count_n))/len(f_list) > float(6)/10:
        flag = 1
    else:
        flag = 0
    return flag,mode_n


# In[117]:


#print result_rf[110],flag_rf[110],result_rf_f[110]


# In[118]:


#print result_ad[110],flag_ad[110],result_ad_f[110]
#print result_dt[110],flag_dt[110],result_dt_f[110]


# In[119]:


from statistics import mode

flag_dt = [0]*len(result_dt)
flag_ad = [0]*len(result_ad)
flag_rf = [0]*len(result_rf)

result_dt_f = [0]*len(result_dt)
result_ad_f = [0]*len(result_dt)
result_rf_f = [0]*len(result_dt)
for i in range(0,len(result_dt)):
    #mode_rf_f,mode_rf = find_mode(result_rf[i])
    #if mode_
    flag_dt[i],result_dt_f[i] = find_mode_f(result_dt[i])
    flag_ad[i],result_ad_f[i] = find_mode_f(result_ad[i])
    flag_rf[i],result_rf_f[i] = find_mode_f(result_rf[i])


# In[120]:


result_dt = result_dt_f
result_ad = result_ad_f
result_rf = result_rf_f


# In[121]:


result = []
for i in range(0,len(result_dt)):
    
    if flag_rf[i] == 1:
        result.append(result_rf[i])
    else:
        score = [0]*4
        score[result_dt[i]] = score[result_dt[i]] + dt_f
        score[result_ad[i]] = score[result_ad[i]] + ad_f
        score[result_rf[i]] = score[result_rf[i]] + rf_f
        max_i = 0
        max_n = 0
        for j in range(1,4):
            if score[j] > max_n:
                max_n = score[j]
                max_i = j
        result.append(max_i)


# In[122]:


#result = result_rf


# In[123]:


print len(result)


# In[124]:


id = open('/Users/trevor/Desktop/final_project/cleaned/cleaned_test_values.csv',"r")
for line in id:
    cleaned_id.append(line.split(','))
id.close()
file = open('/Users/trevor/Desktop/final_project/new_Set/my_result_onlyvote.csv',"w")
file.write('id,status_group\n')
for i in range(0,len(result)):
    file.write(str(cleaned_id[i+1][0]))
    file.write(',')
    if result[i]==2:
        file.write('functional')
    elif result[i]==1:
        file.write('non functional')
    else:
        file.write('functional needs repair')
    file.write('\n')
file.close()

