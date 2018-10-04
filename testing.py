
#exercise
def who_do_know():
    people = input('Enter the name of peopl you know separated by comma: ')
    peope_list = people.split(",")
    people_without_space =[]
    for person in peope_list:
        people_without_space.append(person.strip())
    return people_without_space

def ask_user():
    person = input("Enter the name of someone you know: ")
    if person in who_do_know():
        print("you know {}".format(person))


ask_user()
