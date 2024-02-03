def reverse_words(sentence):
    # Разделили предложение на слова
    words = sentence.split()

    # Измените порядок слов и выведите их на печать
    #Оператор * распаковки используется для передачи элементов перевернутого списка в качестве отдельных аргументов функции print
    print(*reversed(words))

# Принять значения с пользователя
user_input = input("Enter a sentence: ")

# Вызываем функцию
reverse_words(user_input)