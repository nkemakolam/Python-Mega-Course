grade = [77,45,89,34,67,908,]
tupple_grade = (45,67,90,45,23,)
Set_grade ={77,89,54,67,89,23,89}

grade.append(109)
tupple_grade = tupple_grade +(111,)

print(grade)
print(tupple_grade)
print(Set_grade)

user_want_number =True
while user_want_number == True:
    print(10)
    user_input = input("Should we print again (y/n)")
    if user_input == 'n':
        user_want_number = False

#new code on if
should_continue = True
if should_continue:
    print("helo")
known_people = ['nkem','dare','Mary']
person = input("Enter the name of the user you know")
if person in known_people:
     print("you know {}".format(person))
else:
    # person not in known_people:
    print("you dont know {}".format(person))

    #exercise for returing Even user_want_number
