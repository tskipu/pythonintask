#Задача 8
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

#Зябко Антон
#21.05.2016

import random
WORDS = ("альстромерия", "астры", "васильки", "гвоздика", "иберис", "гладиолусы")
word = random.choice(WORDS)
correct = word
jumble =""
help=""
balls=100
while word:
	position = random.randrange(len(word))
	jumble += word[position] 
	word = word[:position] + word[(position + 1):]
print (
"""
 Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter. не вводя своей версии.)
Если у вас нет предположений, введите "Подсказка", но учтите, что за отгаданное вами слово, вы получите меньше балов.
"""
)
print("Boт анаграмма:", jumble)
guess=" "
while guess != correct and guess != "":
	guess=input("Попытайтесь угадать изначальное слово: ")
	if guess=="Подсказка":
		help=(correct[:position+1])
		print (help)
		balls-=10
		position+=1
	elif guess==correct:
		print("Отлично, у вас получилось!\n")
		print("Поглядим сколько вы набрали: {} балов!".format(balls))
	elif guess==correct:
		print("Увы, но ответ неверный. Попробуйте еще раз")
print("Спасибо за игру!")
input("Нажмите Enter для выхода")