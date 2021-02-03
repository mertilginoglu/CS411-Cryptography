import random
import requests

API_URL = 'http://cryptlygos.pythonanywhere.com' #DON'T Change this
my_id = 11111   # CHANGE this into your ID number

#server communication. Try to get p and t
endpoint = '{}/{}/{}'.format(API_URL, "q1", my_id )
response = requests.get(endpoint) 	
p = 0
t = 0
if response.ok:	
  res = response.json()
  print(res)
  p, t = res['p'], res['t']		#p is your prime number. t is the order of a subgroup. USE THESE TO SOLVE THE QUESTION
else:
  print(response.json())

##SOLUTION   
#
#
#
##END OF SOLUTION

g = 0 		#ATTN: change this into generator you found
gH = 0		#ATTN: change this into generator of the subgroup you found


#You can CHECK result of PART A here
endpoint = '{}/{}/{}/{}'.format(API_URL, "q1ac", my_id, g)
response = requests.put(endpoint) 	
print(response.json())


#You can CHECK result of PART B here
endpoint = '{}/{}/{}/{}'.format(API_URL, "q1bc", my_id, gH )	#gH is generator of your subgroup
response = requests.put(endpoint) 	#check result
print(response.json())
