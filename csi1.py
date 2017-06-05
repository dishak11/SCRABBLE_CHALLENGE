import time
import string

start_time = time.clock()

rack =''.join(sorted((raw_input("Enter Rack:")).upper()))             #recieve user input for rack

if (rack.isalpha()) != True:                     #check whether rack is only alphabets
	print "Enter Only Alphabets "
	exit(1)

rack  = rack.upper()

r = rack
l = len(rack)
score = 0
answer = {}                                     #dict of valid words made from rack

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}
         
try:
    fp=open("sowpods.txt","r")		            #opening and reading the file
except EnvironmentError:                        #handle error when sowpods.txt is missing
    print "Cannot find sowpods.txt"
    exit(1)
    
for line in fp.readlines():
	word=line.strip()				            #taking each word
	for i in word:					            #checking each letter in word
		for a in r:				  	            #each letter in rack
			if i==a:
				r= string.replace(r,a,"", 1)	#deleting the element once occured
				break
		else:
			break
	
	else:
		for s in word:					        #to calculate the score
			score += scores[s]
		answer.update({score:word})		       	#updating the answer dictionary
		score=0						
	
	r=rack
	
fp.close()
							                    #closing the file
print "\nAND YOU GO\n"
for key in sorted(answer):					    #your final answer
	print key, answer[key] 
	
print time.clock() - start_time, "seconds"
