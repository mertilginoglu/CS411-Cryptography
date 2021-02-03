import requests

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 11111

endpoint = '{}/{}/{}'.format(API_URL, "q2", my_id )
response = requests.get(endpoint) 	
if response.ok:	
  r = response.json()
  p, q, e, c = r['p'], r['q'], r['e'], r['cipher']    #Use these variables to calculate m
  print(c)
else:  print(response.json())

##SOLUTION
#
#
#
## END OF SOLUTION


m = 0 	#ATTN: change this into the number you calculated and DECODE it into a string m_
m_ = "Change this to the message you found from m by decoding. Yes, it is a meaningful text."


#query result
endpoint = '{}/{}/{}/{}'.format(API_URL, "q2c", my_id, m_ )    #send your answer as a string
response = requests.put(endpoint) 	
print(response.json())
