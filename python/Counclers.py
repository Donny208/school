'''
Donovan Wright / 21 Sept

Boolean logic towards mastering if- elif -else

Assign A counselor programer

Ask a student for name, grade, gender, and age. Then Assign A councler

12 M = Mr. Able
12 F - Ms. Baker

11 M = Mr. Charles
11 F = Ms. Davis

10 M = Mr. Ellis
10 F = Ms. Franklin

9 M = Mr. Goode
9 F = Ms. Harris

age 18 M = Mr. Isle
age 18 F = Ms. Jacobs
'''
#Imports
import time

#Variables
council = ['Mr. Able','Ms. Baker','Mr. Charles','Ms. Davis','Mr. Ellis','Ms.Franklin','Mr. Goode','Ms. Harris','Mr. Isle','Ms. Jacobs']
moreStudents = True

#Main
def main():
    global moreStudents
    while moreStudents:
        name = input('What Is Your Name> ')
        time.sleep(0.5)
        print('Hello',name)
        time.sleep(0.5)
        grade = input('What Year Of School Are You> ')
        time.sleep(0.5)
        age = input('How Old Are You> ')
        time.sleep(0.5)
        gender = input('Male Or Female> ')
        time.sleep(0.5)
        print('Ok! Your Name Is',name,', You Are In Your',grade,'Year Of School, And You Are A',age,gender)
        '''
        if int(age) == 18 and gender.lower() == 'male' and int(grade) == 12:
            print('Your Councler Is',council[8])
            
        elif int(age) == 18 and gender.lower() == 'female' and int(grade) == 12:
            print('Your Councler Is',council[8])
        '''
        if gender.lower() == 'male':
            if int(grade) == 12:
                if int(age) == 18:
                    print('Your Councler Is',council[8])
            elif int(grade) == 11:
                print('Your Councler Is',council[2])
            elif int(grade) == 10:
                print('Your Councler Is',council[4])
            elif int(grade) == 9:
                print('Your Councler Is',council[0])

        elif gender.lower() == 'female':
            if int(grade) == 12:
                if int(age) == 18:
                    print('Your Councler Is',council[9])
            elif int(grade) == 11:
                print('Your Councler Is',council[3])
            elif int(grade) == 10:
                print('Your Councler Is',council[5])
            elif int(grade) == 9:
                print('Your Councler Is',council[1])

        else:
            print("Sorry, You Don't Have A Counciler")
        morestu = input('Are There More Students? (Y Or N)')
        if morestu == "Y" or morestu == "y":
            moreStudents = True
        else:
            moreStudents = False

if __name__ == '__main__':
    main()
