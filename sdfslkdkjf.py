import random

# Программа для открытия сейфа с заданиями

# Список вопросов и ответов
questions = [
    ("Сколько будет 7 + 5?", "12"),
    ("Как называется столица России?", "Москва"),
    ("Какое животное говорит 'мяу'?", "Кошка"),
    ("Как зовут главного персонажа сказки о Буратино?", "Буратино"),
    ("Сколько дней в неделе?", "7")
]

# Генерация кода
correct_code = "2808"  # Правильный код сейфа

# Перемешиваем вопросы
random.shuffle(questions)

# Функция проведения викторины
def run_quiz():
    print("Чтобы открыть сейф, ответьте на вопросы!")
    code = ""
    for i, (question, answer) in enumerate(questions[:4]):
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Верно!")
            code += correct_code[i]
        else:
            print("Неправильно! Попробуй еще раз.")
            return run_quiz()
    return code

# Основная программа
user_code = run_quiz()

if user_code == correct_code:
    print("Сейф открыт! Подарки внутри!")
else:
    print("Неправильный код! Попробуй еще раз.")
