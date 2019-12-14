'''
Jasbir Kaur
Assignment#1
'''


import datetime

#check datetime to get total time taken value
x = datetime.datetime.now()
total_words=0
total_anagrams=0
d = dict()
temp_d = dict()
with open("English.txt") as f:
    x = datetime.datetime.now()
    print(x)
    for line in f:
        total_words+=1
        #anagram are similar if sorted
        #using join to convert list to string for key 
	key = ''.join(sorted(line))
	if key in d:
            #using temp dictionary to get the first anagram value
	    if (temp_d[key]==0):
                print(d[key])
		temp_d[key] = 1
		total_anagrams+=1
            print(line)
	    total_anagrams+=1
   	else:
            d[key] = line
            temp_d[key] = 0

f.close()
x = datetime.datetime.now() - x
print 'Total time taken to find',total_anagrams,'anagrams from',total_words,'in time',x 


