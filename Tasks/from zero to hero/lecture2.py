import string

# Создаем функцию для новых попыток
def run_program():
    # Запрашиваем ввод
    user_input = input("Введите число от 0 до 99: ")

    # Проверяем на пустой ввод
    if len(user_input) == 0:
        print("Вы должны ввести число")
        run_program() # запускаем заново

    # 1. Если введен всего один символ
    elif len(user_input) == 1:
        if user_input in string.digits:
            number = int(user_input)
            if number == 0: print("ноль")
            elif number == 1: print("один")
            elif number == 2: print("два")
            elif number == 3: print("три")
            elif number == 4: print("четыре")
            elif number == 5: print("пять")
            elif number == 6: print("шесть")
            elif number == 7: print("семь")
            elif number == 8: print("восемь")
            elif number == 9: print("девять")
        else:
            print("Дружок, ты знаешь как выглядят числа ? Давай еще раз ;)")
            run_program() # запускаем заново

    # 2. Если введено ровно два символа
    elif len(user_input) == 2:
        first_char = user_input[0]
        second_char = user_input[1]
        
        if first_char not in string.digits:
            print("Дружок, ты знаешь как выглядят числа ? Давай еще раз ;)")
            run_program() # запускаем заново
            
        elif first_char in string.digits and second_char not in string.digits:
            print("Зайка, повнимательнее ! Сделаем вид, что этого не было и начнем заново")
            run_program() # Даем шанс исправиться
            
        else:
            number = int(user_input)
            
            if number == 10: print("десять")
            elif number == 11: print("одиннадцать")
            elif number == 12: print("двенадцать")
            elif number == 13: print("тринадцать")
            elif number == 14: print("четырнадцать")
            elif number == 15: print("пятнадцать")
            elif number == 16: print("шестнадцать")
            elif number == 17: print("семнадцать")
            elif number == 18: print("восемнадцать") 
            elif number == 19: print("девятнадцать")
            else:
                tens_digit = number // 10
                units_digit = number % 10
                
                tens_word = ""
                if tens_digit == 2: tens_word = "двадцать"
                elif tens_digit == 3: tens_word = "тридцать"
                elif tens_digit == 4: tens_word = "сорок"
                elif tens_digit == 5: tens_word = "пятьдесят"
                elif tens_digit == 6: tens_word = "шестьдесят"
                elif tens_digit == 7: tens_word = "семьдесят"
                elif tens_digit == 8: tens_word = "восемьдесят"
                elif tens_digit == 9: tens_word = "девяносто"
                
                units_word = ""
                if units_digit == 1: units_word = "один"
                elif units_digit == 2: units_word = "два"
                elif units_digit == 3: units_word = "три"
                elif units_digit == 4: units_word = "четыре"
                elif units_digit == 5: units_word = "пять"
                elif units_digit == 6: units_word = "шесть"
                elif units_digit == 7: units_word = "семь"
                elif units_digit == 8: units_word = "восемь"
                elif units_digit == 9: units_word = "девять"
                
                if units_digit == 0:
                    print(tens_word)
                else:
                    print(f"{tens_word} {units_word}")

    # 3. Если введено больше 2 символов
    else:
        # Проверяем
        all_digits = True
        if user_input[0] not in string.digits or user_input[1] not in string.digits or user_input[2] not in string.digits:
            all_digits = False
            
        if all_digits:
            print("Что непонятного в формулировке ВВЕСТИ ЧИСЛО ОТ 0 ДО 99? Еще раз вводи")
        else:
            print("Дружок, ты знаешь как выглядят числа ? Давай еще раз ;)")
        
        run_program() # запускаем заново

# Первый запуск программы
run_program()

