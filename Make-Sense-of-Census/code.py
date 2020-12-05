# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate([data,new_record], axis= 0)

print(census.shape)

age = census[:,0]

max_age = age.max()
print("Max age:",max_age)
min_age = age.min()
print("Min age:",min_age)

age_mean = age.mean()
print("Mean age:",age_mean)

age_std = age.std()

print("Age SD: ", age_std)

race_0 = census[:,2][census[:,2].astype(int)==0]
len_0 = len(race_0)
print(len_0)


race_1 = census[:,2][census[:,2].astype(int)==1]
len_1 = len(race_1)
print(len_1)

race_2 = census[:,2][census[:,2].astype(int)==2]
len_2 = len(race_2)
print(len_2)

race_3 = census[:,2][census[:,2].astype(int)==3]
len_3 = len(race_3)
print(len_3)

race_4 = census[:,2][census[:,2].astype(int)==4]
len_4 = len(race_4)
print(len_4)

minority_race = 3

senior_citizens = census[:,:][census[:,0].astype(int) > 60]
print(senior_citizens.shape)

working_hours_sum = senior_citizens[:,6].sum()
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

high = census[:,:][census[:,1].astype(int) > 10]
print(high.shape)


low = census[:,:][census[:,1].astype(int) <= 10]
print(low.shape)

avg_pay_high = high[:,7].mean()
print(avg_pay_high)

avg_pay_low = low[:,7].mean()
print(avg_pay_low)



