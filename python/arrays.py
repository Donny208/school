'''
Intro To Python Lists
Lists are like arrays in other lang
except lists are more powerful and more capable than arrays in those other lang

Donovan Wright

12/13/15

'''

wizard_list = ['Spider Legs', 'Toe of Frog', 'Eye of Newt', 'Bat Wings', 'Slug Butter', 'Snake Dandruff']
nas = ['Why','was',6,'afraid','of','because',7,8,9]
#print(wizard_list[0])

for x in range(0,len(wizard_list)):
    print(wizard_list[x])
print()
#Remember: Inclusive:Exclusive
#print(wizard_list[2:5],'\n')

#print()

#print(nas)

def changeArray(i,n):
    wizard_list[i] = n
    print(wizard_list)

def addToArray(n):
    wizard_list.append(n)
    print(wizard_list)

def removeFromArray(i):
    del wizard_list[i]
    print(wizard_list)
    
