import random
nums=['1','2','3','4','5']
special_char=['@','#','^','&','!']

wordlist = []

with open("Wikipedia-text.txt", "r") as file:
    data=file.readlines()

    for line in data:
        words = line.split()
        
        for items in words:
            if len(items)>5:
                wordlist.append(items.capitalize())


word = random.choice(wordlist)
spec_char=random.choice(special_char)
num=random.randint(10,99)

readable_pass= word+spec_char+str(num)

print(readable_pass)