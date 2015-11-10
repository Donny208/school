'''
embedding values inside of strings
myscore = 1000
message = 'I scored $s points'
print(mssage % score)
I scored 1000 points
'''
myscore = 1000
message = "I scored %s points"
print(message % myscore)
print("%s I am embedding a value of %s into my string for %s" %(myscore, 100,'3b'))
for x in range(100):
    print('x = %s'%x)
'''
joke_text = '%s: a device for findnig furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
'''
joke_text = '%s: a device for findnig furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
