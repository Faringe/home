#Задание №1

from sys import argv

worked_hour, rate, benefit = argv

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f'Заработная плата сотрудника {calculation}')