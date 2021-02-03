import random
import requests
import BitVector

API_URL = 'http://cryptlygos.pythonanywhere.com'	#DON'T CHANGE THIS
my_id = 23574   									#ATTN: Change this into your id number

endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
response = requests.get(endpoint) 	
a = 0
b = 0
if response.ok:	
  res = response.json()
  print(res)
  a, b = res['a'], res['b']		#Binary polynomials a and b
else:
  print(response.json())

##SOLUTION  





#You need to calculate c and a_inv
#c = a(x)*b(x)
#a_inv is inverse of a
c = " "			
a_inv = " "		

##END OF SOLUTION
 

#check result of part a
endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
response = requests.put(endpoint) 	
print(response.json())

#check result of part b
endpoint = '{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)
response = requests.put(endpoint) 	
print(response.json())
