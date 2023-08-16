import random

upper_char=['A','B','C','D','E']
lower_char=['a','b','c','d','e']    
nums=['1','2','3','4','5']
special_char=['@','#','^','&','!']

pass_random =random.choice(upper_char) + random.choice(lower_char)+ random.choice(nums) + random.choice(special_char) +random.choice(upper_char) + random.choice(lower_char)+ random.choice(nums) + random.choice(special_char)

print(pass_random)