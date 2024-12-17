import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Отгадайте число от 1 до 100: "))
        attempts += 1

        if user_guess < number:
            print("Загаданное число больше.")
        elif user_guess > number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток.")
            break
print("Отгадайка")
guess_the_number()
def group_characters(input_string):
    characters = input_string.split()
    grouped = []

    for char in set(characters):
        grouped.append([char] * characters.count(char))

    return grouped

input_string = input("Введите строку символов, разделенных пробелами: ")
result = group_characters(input_string)
print(result)



import random

def blackjack():
    cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}

    random.shuffle(cards)
    player_score = 0

    while player_score < 21:
        print(f"Ваши очки: {player_score}")
        decision = input("Хотите взять карту? (y/n): ").lower()

        if decision == 'n':
            print(f"Вы набрали {player_score} очков. Теперь ходит дилер.")
            break
        elif decision == 'y':
            card = cards.pop()
            player_score += card_values[card]
            print(f"Вы взяли карту: {card}. Ваши очки: {player_score}")

            if player_score > 21:
                print(f"Вы набрали {player_score} очков. Перебор! Вы проиграли.")
                return
            elif player_score == 21:
                print(f"Вы набрали {player_score} очков. Поздравляем! Вы выиграли.")
                return
        else:
            print("Неверный ввод. Пожалуйста, ответьте 'y' или 'n'.")

    dealer_score = 0
    print("\nХодит дилер...")

    while dealer_score < 17:
        card = cards.pop()
        dealer_score += card_values[card]
        print(f"Дилер взял карту: {card}. Очки дилера: {dealer_score}")

        if dealer_score > 21:
            print(f"Дилер набрал {dealer_score} очков. Перебор! Вы выиграли.")
            return
        elif dealer_score == 21:
            print(f"Дилер набрал {dealer_score} очков. Дилер выиграл!")
            return

    # Сравнение очков игрока и дилера
    print(f"\nОчки игрока: {player_score}")
    print(f"Очки дилера: {dealer_score}")

    if player_score > dealer_score:
        print("Поздравляем! Вы выиграли!")
    elif player_score < dealer_score:
        print("Дилер выиграл!")
    else:
        print("Ничья!")

blackjack()
