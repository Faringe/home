#Задание №2

my_list = [3, 20, 9, 5, 11, 8, 51, 6, 16]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)