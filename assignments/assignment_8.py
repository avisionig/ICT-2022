'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
# input1 = input()
# input2 = input()
# input3 = input()

import numpy as np
input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]
input3 = [int(i) for i in input3.split(',')]

import sklearn.linear_model as skmod
import sklearn.preprocessing as skprepro
import sklearn.model_selection as sksel

input1 = np.array(input1).reshape(-1,1)
input2 = np.array(input2).reshape(-1,1)
input3 = np.array(input3).reshape(-1,1)

arr = np.hstack([input1, input2, input3])
scaler_f = skprepro.StandardScaler()

data_x_train = scaler_f.fit_transform(arr)
sksel.train_test_split(data_x_train, shuffle=False)
data_x_train = data_x_train[0:3]





#use this printing (where "data_x" is your features scaled and standardized)
print("{}".format(np.round(data_x_train,2)))