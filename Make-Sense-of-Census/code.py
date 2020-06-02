# --------------
#####################  Data Reading ##############################
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
# Append 'new_record' (given) to 'data'
census = np.concatenate((new_record,data))
print(census)


# --------------
################### Young Country? Old Country? ##############

#Code starts here
age = census[:,0]
print(age)

# max age
max_age = age.max()
print(max_age)

# min age
min_age = age.min()
print(min_age)

# mean of age
age_mean = age.mean()
print(age_mean)

# Standard diviation of age 
age_std = age.std()
print(age_std)


# --------------
######################### Minority Report ####################

#Code starts here
race_0 = census[census[:,2]==0]
len_0 = len(race_0)   # length of array
print("length of race_0 : ",len_0)

race_1 = census[census[:,2]==1]
len_1 = len(race_1)   # length of array
print("length of race_1 : ",len_1)

race_2 = census[census[:,2]==2]
len_2 = len(race_2)     # length of array
print("length of race_2 : ",len_2)

race_3 = census[census[:,2]==3]
len_3 = len(race_3)     # length of array
print("length of race_3 : ",len_3)

race_4 = census[census[:,2]==4]
len_4 = len(race_4)     # length of array
print("length of race_4 : ",len_4)

minn = min(len_0,len_1,len_2,len_3,len_4)
print(minn)

minority_race = 3


# --------------
########################## Senior Welfare ##########################
#Code starts here

# new subset array with index 0 based on the age 
senior_citizens = census[census[:,0]>60]

#Calculating the sum of all the values of array with index 6
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

# length of senior_citizens
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

# average working hours of the senior citizens
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

# two new subset arrays based on 'education' column
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

#Finding the average pay
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()

print(avg_pay_high)
print(avg_pay_low)

# comparing arrays 
compare = np.array_equal(avg_pay_high,avg_pay_low)
print(compare)


