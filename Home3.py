#Задание №3

number = range(20, 241)
new_list = [el for el in number if el % 20 == 0 or el % 21 == 0]
print(new_list)