numbers =[1,2,3,4,5,6,7,8,9]
choice = "a"
def even_number():
    even =[]
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return

def user_menu(choice):
    if choice == 'a':
        return "Add"
    elif choice == 'q':
        return "Quit"

even_number()
user_menu(choice)
