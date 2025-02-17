#a list of squares

l = [i*i for i in range(1,5)] 
print(l) 

#covert to upper 
words = ["hello", "world", "python"]

upper = [i.upper() for i in words] 
print(upper) 

#extract even 
lsit1 = [10,1,2,4,6,79]

even = [i for i in lsit1 if i % 2==0]
print(even) 

#make pair of number and it squares 
l1 = [(i,i*2) for i in range(1,6)]
print(l1) 

#extract vowels from string 
sentence = "list comprehension is powerful" 

vowel = [{i,sentence[i]} for i in range(len(sentence)) if sentence[i] in "aeiouAEIOU"]
print(vowel) 

#multiplr if else's 
a = [("fives",i) if i%5==0 else ("three's",i) if i% 3==0 else ("even",i) if i%2==0 else "Not in condition" for i in range(1,50)]
print(a) 