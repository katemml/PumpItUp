#fills missing values with 'unknown'



import pandas as pd
import numpy as np



##SUPPRESSES AN ERROR BETWEEN NUMPY AND PYTHON. NON-OPTIMAL SOLUTION
#SEE:
#https://stackoverflow.com/questions/40659212/futurewarning-elementwise-comparison-failed-returning-scalar-but-in-the-futur
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
print('x' in np.arange(5))   #returns False, without Warning



train_value = pd.read_csv("TrainingSetValues.csv")
test_value = pd.read_csv("TestSetValues.csv")


column_labels = list(train_value.columns.values)


#removed for the list, not the data, because they arent caterorical and this list is for replacing categorical with ordinal
column_labels.remove("id")
column_labels.remove("date_recorded")
column_labels.remove("gps_height")
column_labels.remove("longitude")
column_labels.remove("latitude")
column_labels.remove("district_code")
column_labels.remove("population")
column_labels.remove("construction_year")




#attributes with a large number of possible values
column_labels.remove("wpt_name")
column_labels.remove("subvillage")

#should be removed completly
# 70% missing
column_labels.remove("amount_tsh")
# only one possible value
column_labels.remove("recorded_by")
#we effectively remap region to be identical to region_code
column_labels.remove("region_code") 
#num_private almost purely 0
column_labels.remove("num_private")


#dodging an error
column_labels.remove("funder")




#also: subvillage , also funder
attributes_using_nan = [ "installer" , "scheme_management" , "scheme_name" , "public_meeting" , "permit"]
for col_name in attributes_using_nan:
	train_value[col_name] = train_value[col_name].fillna('unknown') 
	#train_value[col_name] = train_value[col_name].replace(['0'] , train_value[col_name].mode()[0])

	test_value[col_name] = test_value[col_name].fillna('unknown') 
	#test_value[col_name] = test_value[col_name].replace(['0'] , test_value[col_name].mode()[0])

attributes_using_zero = ["gps_height" , "longitude" , "latitude" , "construction_year" , "population"]
for col_name in attributes_using_zero:
	#train_value[col_name] = train_value[col_name].replace([0] , train_value[col_name].median())

	#test_value[col_name] = test_value[col_name].replace([0] , test_value[col_name].median())
	train_value[col_name] = train_value[col_name].fillna('unknown') 
	test_value[col_name] = test_value[col_name].fillna('unknown')

#also wpt_name
attributes_using_unknown = ["management" , "management_group" , "payment" , "payment_type" , "source" , "source_type" , "source_class" , "quantity" , "quantity_group", "water_quality" , "quality_group"]
for col_name in attributes_using_unknown:
	#train_value[col_name] = train_value[col_name].replace(['unknown'] , train_value[col_name].mode()[0])

	#test_value[col_name] = test_value[col_name].replace(['unknown'] , test_value[col_name].mode()[0])

	train_value[col_name] = train_value[col_name].fillna('unknown') 
	test_value[col_name] = test_value[col_name].fillna('unknown')


for i in column_labels:
	print("i is " + i)
	unique_value = list(set(np.concatenate((train_value[i].unique() , test_value[i].unique()))))
	#unique_value = list(set(train_value[i].unique()))
	#unique_value = list(set(test_value[i].unique()))
	size = len(unique_value)
	print(size)
	for j in range(size):
		# if type(train_value[i] != unique_value[j] ):
		# 	print("train_value[i] is " + train_value[i])
		# 	print("type of train_value[i] is " , type(train_value[i]))
		# 	print("unique_value[j] is " + unique_value[j])
		# 	print("type of unique_value[j] is "  type(unique_value[j]))

		if unique_value[j] != "nan":
			train_value.loc[train_value[i] == unique_value[j] , i] = j

			test_value.loc[test_value[i] == unique_value[j] , i] = j



#The reasons for dropping these are given above
train_value = train_value.drop(["wpt_name" , "subvillage" , "amount_tsh" , "recorded_by" , "region_code" , "num_private" , "funder"] , axis = 1)

test_value = test_value.drop(["wpt_name" , "subvillage" , "amount_tsh" , "recorded_by" , "region_code" , "num_private" , "funder"] , axis = 1)



train_value.to_csv("cleaned_train_values_2.csv" , index = False)

test_value.to_csv("cleaned_test_values_2.csv" , index = False)


#matplotlib
