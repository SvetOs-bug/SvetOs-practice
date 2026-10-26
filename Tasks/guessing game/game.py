#!/usr/bin/env python3
import random

secret_number = random.randint(1, 100)
print("Guess my number (1-100) or type 'exit' to quit:")

while True:
    user_input = input("> ").strip()
    
    # 1. Проверяем команду на выход
    if user_input == 'exit':
        print("Goodbye! 👋")
        break
        
    # 2. Проверяем, ввёл ли пользователь именно число (чтобы программа не падала)
    if not user_input.isdigit():
        print("Please enter a number or 'exit'!")
        continue
        
    # 3. Переводим в число и проверяем догадку
    user_guess = int(user_input)
    
    if user_guess == secret_number:
        print("Correct! 🎯")
        break
    else:
        print("Wrong guess :( Try again! ❌")
