left = -10 ** 9
right = 10 ** 9

print("Загадай число от -1000000000 до 1000000000")
input("Нажмите Enter, когда будете готовы...")

while left <= right:
    guess = (left + right) // 2
    print("Моё число:", guess)
    answer = input("Больше, меньше или угадал? (б/м/у): ")

    if answer == "у":
        print("Ура, угадал число:", guess)
        break
    elif answer == "б":
        # загаданное число больше, чем guess
        left = guess + 1
    elif answer == "м":
        # загаданное число меньше, чем guess
        right = guess - 1
    else:
        print("Не понял ответ, введи б, м или у")
