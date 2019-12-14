'''
Jasbir Kaur
Assignment#1
'''
#variable to count total number of palindromes in English.txt
count=0

# Opening English.txt available in the same directory of this python code
with open('English.txt') as f:

    for line in f:

        #remove the newline charachter \n from each line
        line = line.rstrip()

        #invert the line and compare with the original line
        if(line==line[::-1]):

            count+=1
            print line
f.close()
print 'Total number of palindromes in English.txt:',count            
