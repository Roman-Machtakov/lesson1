grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #Присвоение в переменную списков
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #Присвоение в переменную множества
students = sorted(students) #Сортировка множества по алфовитному порядку
grades = sum(grades[0]) / len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]) #Вычисление средних чисел в списках
zippend = zip(students, grades) #Объединение элементов
grades_students = dict(zippend) #Переобразование элементов в словарь
print(grades_students) #Вывод на экран словаря в алфавитном порядке со средними числами.
