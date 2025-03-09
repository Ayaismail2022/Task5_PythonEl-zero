"""
Task 5
"""
Name = "Aya",
print(Name)
print(type(Name))

friends = ("Osama", "Ahmed", "Sayed")
List_friends = list(friends)
List_friends[0]="El-Zero"
friends = tuple(List_friends)
print(friends)
print(type(friends))
print(f"{len(friends)} Elements")


nums = (1, 2, 3)
letters = ("A", "B", "C")
sum = nums + letters
print(sum)
print(f"{len(sum)} Elements")

my_tuple = (1, 2, 3, 4)
a,b,_,c = my_tuple
print(a)
print(b)
print(c)
