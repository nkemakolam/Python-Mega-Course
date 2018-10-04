my_list = [20,40,60,80,100]
maximun = my_list[0]
for num in my_list:
    if num > maximun:
        maximun = num
print(num)

an_equal_list = [x for x in range(5)]
multipl_list = [x * 8 for x in range(5)]
print([n for n in range(10) if n % 2 > 0])
print([n for n in range(10) if n % 2 == 0])
print([n for n in range(10) if n % 2 != 0])
print([n for n in range(10) if n % 2 < 0])
print(multipl_list)
odd_nums = []
even_nums = []
xs = {'a':1,'b':3}
ys = {'c':5,'d': 4}
print({**xs,**ys})
#num_list = list(range(1, 10))

def even_numbe_in_ten ():
    for x in range (10):
        if x % 2 == 0:
            even_nums.append(x)
        else:
            odd_nums.append(x)

x = int(input("enter value: "))
even_numbe_in_ten()

print(even_nums)
print(odd_nums)
 people_you_know = ["Rolf"," John","anna","GREG"]
 normalised_people = [person.strip().lower() for person in people_you_know]
 print(normalised_people)
