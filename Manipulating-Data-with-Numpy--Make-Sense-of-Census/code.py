# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

data_file= path # path for the file
data= np.genfromtxt(data_file, delimiter=",", skip_header=1)


print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

census= np.concatenate((data,new_record),axis=0)
print(census)

#Code starts here



# --------------
#Code starts here

age=census[:,:1]
print(age)

# max age 
max_age= np.max(age)
print(max_age)

# min age
min_age= np.min(age)
print(min_age)

# mean of age
age_mean= np.mean(age)
print(age_mean)

# Standard deviation
age_std= np.std(age)
print(age_std)





# --------------
#Code starts here

# Slicing to get the array of only age column from census to race
race= census[:,2]

# array to store only race values with 0 
race_0= census[race==0]
#print(race_0)

# array to store only race values with 1
race_1= census[race==1]
#print(race_1)

# array to store only race values with 2
race_2= census[race==2]
#print(race_2)

# array to store only race values with 3 
race_3= census[race==3]
#print(race_3)

# array to store only race values with 4
race_4= census[race==4]
#print(race_4)

len_0= len(race_0) 
# print(len_0)
len_1= len(race_1) 
len_2= len(race_2)  
len_3= len(race_3) 
len_4= len(race_4)  

# race with minimum citizens

citizens=np.array([len_0,len_1,len_2,len_3,len_4])
print(citizens)

minimum_citizens=np.min(citizens)


# print(minority_race)
minority_race= 0
if minimum_citizens==len_0:
    minority_race=0
elif minimum_citizens==len_1:
    minority_race=1
elif minimum_citizens==len_2:
    minority_race=2
elif minimum_citizens== len_3:
    minority_race=3
elif minimum_citizens==len_4:
    minority_race-=4

print(minority_race)




# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]

#print(senior_citizens)

# total working hours of senior citizens

working_hours_sum=  sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

# avwrgae 

avg_working_hours= working_hours_sum/senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
high= census[census[:,1]>10]

low= census[census[:,1]<=10]
avg_pay_high= np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low= np.mean(low[:,7])
print(avg_pay_low)


