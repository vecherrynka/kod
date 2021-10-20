print('Как тебя зовут?')
name = input()
print('Привет,', name,'\n Сколько тебе лет?')
age = input()
print ('Неплохо! Ответь еще на пару вопросов!')

overlap = 0 # Переменная, считающая совпадения

print ('Какой твой любимый цвет?(1 – красный, 2 – зеленый, 3 – синий)')
color = int(input())
print('Следующий вопрос! Какой музыкальный жанр ты предпочетаешь?(1 – классика, 2 – поп-музыка, 3 – рок)')
music = int(input())
print('Последний вопрос. Какое твоё любимое время года (1 – осень, 2 – зима, 3 – весна, 4 – лето)')
season = int(input())
print('Последний вопрос. Какой твой любимый фрукт (1 – груша, 2 – яблоко, 3 – банан)')
fruits = int(input())
print('Последний вопрос. Какое твое любимое животное (1 – кошка, 2 – собака, 3 – хомяк')
animals = int(input())
print('Последний вопрос. Какой твой любимый жанр фильмов (1 – романтика, 2 – ужасы, 3 – фантастика)')
films = int(input())
print('Последний вопрос. Какой твой любимый напиток (1 – кола, 2 – фанта, 3 – спрайт)')
drinks = int(input())
print('Последний вопрос. Какой твой любимый спорт (1 – волейбол, 2 – футбол, 3 – баскетбол)')
sport = int(input())

if (color == 1 or color == 2):
    overlap += 1
if (music == 2):
    overlap += 1
if (season == 4 or season == 3):
    overlap += 1
if (fruits == 3):
    overlap += 1
if (animals == 2):
    overlap += 1
if (films == 1 or films == 3):
    overlap += 1
if (drinks == 1 or drinks == 2):
    overlap += 1
if (sport == 1):
    overlap += 1   

if overlap == 7 or overlap == 8:
       print('А мы 100% подружимся!')
elif overlap == 6 or overlap == 5 or overlap == 4:
       print('Возможно мы подружимся')
else:
       print('Подружиться будет трудновато...')
