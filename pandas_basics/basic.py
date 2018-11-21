import pandas as pd

dict = {"country": ["Brazil", "Russsia", "India","China", "South Africa"], "capital": ["Brasilia", "Moscow","New Delhi","Beijing","Pretoria"]}
brics = pd.DataFrame(dict)
print(brics)
-------------
     capital       country
0   Brasilia        Brazil
1     Moscow       Russsia
2  New Delhi         India
3    Beijing         China
4   Pretoria  South Africa

##################################
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
##########################

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars['cars_per_cap'])
print(cars[['cars_per_cap']])
print(cars[['cars_per_cap', 'country']])


#All the examples are from learnpython.org/pandas basics[https://www.learnpython.org/en/Pandas_Basics]
