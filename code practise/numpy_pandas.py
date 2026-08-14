import numpy as np
import random
import pandas as pd
'''a=np.array([1,2,3,4])
print(type(a))
print(a)

b=np.array([1,2,3,"10"]) # it will convert all list values into string type
print(type(b))
print(b)

#creating of 2d array
array=np.array([[1,2],[3,4]])
print(array)
print(type(array))

#creating of lists
list=[[1,2],[3,4]] #based on first type of braces it will decide the type.
print(list)
print(type(list))
tuple=([1,2],[3,4])
print(tuple)
print(type(tuple))
#method in numpy library
shape_of_array=np.array([[[1,2,3],[4,5,6]],
                         [[1,2,3],[4,5,6]],
                         [[1,2,3],[4,5,6]]]
                        )
print(shape_of_array)
print(shape_of_array.shape)
print(shape_of_array.size)
print(shape_of_array.ndim)
print(shape_of_array.dtype)
# it will prints the float values 
c=np.zeros((3,4))
print(c)
d=np.ones((4,3))
print(d)   
e=np.ones((4,6),dtype=int) # it will print only integer values 
print(e) 
e.shape=(12,2)# it will reshape the array
print(e)
f=np.arange(100)
print(f)
g=np.arange(0,100,2)
print(g)
h=np.random.normal(1,10)
print(h)
i=np.random.normal(1,10,(3,4)) # (3,4) is declared as a size of array it will represent as rows and coloums
print(i)
print()
j=np.random.normal(1,10,size=(3,5))
print(j)
print()'''

'''number_series=pd.Series([1,2,3])
print(number_series)
print()
number_series1=pd.Series([4,5,6,7],index=["a","b","c","d"],name='number')
print(number_series1)

k=number_series[0]
print(k)
l=number_series1['a']
print(l)

#creating a data frame using pandas
some_data=np.random.randint(1,5,(3,4))
print(some_data)
print()
data_set=pd.DataFrame(some_data,columns=['rupesh','rajesh','raju','umesh'])
print(data_set)
#creating a indexes
another_data_set=pd.DataFrame(some_data,columns=['rupesh','rajesh','raju','umesh'],index=["a","b","c"])
print(another_data_set)

#store the data in list_in_lists
my_list=[['rupesh',10],['rajesh',20],['raju',30]]
print(my_list)
df=pd.DataFrame(my_list,columns=['NAME','AGE'])
print(df)

#store the data in dictionary
employee={"employee_name":["rupesh","rajesh","raju","umesh"],"income":[10000,20000,30000,40000]}
df_1=pd.DataFrame(employee)
print(df_1)


series_dict={'first_series':pd.Series([10,20,30,40]),
             'second_series':pd.Series([50,60,70,80])}
df_2=pd.DataFrame(series_dict)
print(df_2)'''




numbers=np.random.randint(1,100,(10,5))
df_3=pd.DataFrame(numbers,columns=['a','b','c','d','e'])
print(df_3.index)
print(df_3)
print(type(df_3))
print()
print(df_3.head(5))
print()

print(df_3.tail(2))
print(df_3.columns)
print(df_3.info)
#renaming the columns temperoary
df_4=df_3.rename(columns={'a':'rup','b':'raj'})
print(df_4)
#renaming the columns permenantely
df_5=df_3.rename(columns={'a':'rup','b':'raj'},inplace=True)
print(df_5)
