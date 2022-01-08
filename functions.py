text = input()
dict = {}

letter_list = []
text=text.lower()
for x in text:
   if x not in letter_list:
    letter_list.append(x) 

count=0
counts=[]
for x in text: 
    for y in text:
        if x == y:
           count+=1
    text=text.replace(x,"")
    counts.append(count)
    count=0

for x in counts:
   if x ==0:
      counts.remove(x)  

for i in range(len(letter_list)):
     if letter_list[i] not in  [" ","-","'","!","?"]:
           dict[letter_list[i]]=counts[i] 
   
print(dict)
