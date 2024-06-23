#Словари
my_dict = {"apple":30, "tomato":20, "banana":40} #Присвоение переменной словаря
print(my_dict) #Вывод на экран словаря
print(my_dict["apple"]) #Вывод значение пары по ключу
print(my_dict.get("watermelon")) #Возвращение значения по кузанному ключу
my_dict.update({"orange":60, "plum":70}) #Добавление нескольких пар в словарь
vegetable = my_dict.pop("tomato") #Удаление пары из словаря
print(vegetable) #Вывод на экран значения удаленной пары
print(my_dict) #Вывод нового словаря

#Множества
my_set = {1, 2, 1, "Hello", 1.5, 1.5, "Hello"} #Присвоение переменной множества
print(my_set) #Вывод на экран множества
print(my_set.add(6), my_set.add(5)) #Добавление элементов во множество
print(my_set.discard(1)) #Удаление элемента из множества
print(my_set) #Вывод на экран измененное множество