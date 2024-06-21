immutable_var = 1, 2, True, "String" #Присвоение переменной immutable_var кортежа
print(immutable_var) #Вывод в консоль кортеж immutable_var
#immutable_var[1] = 3 #Изменение элемента кортежа по индексу
#print(immutable_var) #Объект кортежа не поддерживает изменение элементов


mutable_list = ["apple", 4, 3.56, True]#Присвоение переменной mutable_list списка 
print(mutable_list)#Вывод в консоль списка mutable_list
mutable_list[2] = 5#Изменение элемента в списке по индексу
mutable_list[3] = False#Изменение элемента в списке по индексу
print(mutable_list)#Вывод в консоль измененный список
