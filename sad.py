# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         # Обработка заглавных букв кириллицы (включая 'Ё')
#         if 'А' <= char <= 'Я' or char == 'Ё':
#             shift_start = ord('А') if char != 'Ё' else ord('Ё')
#             result += chr((ord(char) - shift_start + shift) % 32 + shift_start)
#         # Обработка строчных букв кириллицы (включая 'ё')
#         elif 'а' <= char <= 'я' or char == 'ё':
#             shift_start = ord('а') if char != 'ё' else ord('ё')
#             result += chr((ord(char) - shift_start + shift) % 32 + shift_start)
#         else:
#             result += char # Не изменяем символы, не относящиеся к буквам
#     return result

# # Заданный текст
# text_to_encode = "Гнгзиплв ЫГЖ тскзугеових хидв ф ргфхцтгбьлп рсеюп жсзсп!"
# # Попробуй поменять цифры ниже, чтобы получилось слово
# shift_value = -5

# encoded_message = caesar_cipher(text_to_encode, shift_value)
# print(f"Закодированное сообщение: {encoded_message}")


# data = [10, ["a", 5], [20, ["b", 5, ["c", 2]]], 8, [[[[3]]]], "x", [7, ["y", 2]]]
# print(data[0] + data[1][1] + data[2][0] + data[2][1][1] + data[2][1][2][1] + data[3] + data[4][0][0][0][0] + data[6][0] + data[6][1][1])
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(2)
pen.circle(50, 200)
pen.forward(133)
# # Heart shape function
# def draw_heart():
#     pen.begin_fill()
#     pen.left(50)
#     pen.forward(133)
#     pen.circle(50, 200)
#     pen.right(140)
#     pen.circle(50, 200)
#     pen.forward(133)
#     pen.end_fill()

# # Draw the heart
# draw_heart()

# # Hide the turtle after drawing
# pen.hideturtle()

# Keep the window open
turtle.done()