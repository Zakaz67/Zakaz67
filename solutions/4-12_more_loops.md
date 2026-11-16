# 4-12 — Больше циклов

## Условие
Выбрать версию программы `foods.py` и написать два цикла `for`, чтобы вывести каждый список.

## Исходный код
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for pizza in my_foods:
    print(pizza)

print("\nMy friend's favorite foods are:")
for pizza in friend_foods:
    print(pizza)
```

## Объяснение
- `my_foods` — исходный список любимой еды.
- `friend_foods = my_foods[:]` создаёт независимую копию исходного списка.
- Первый цикл `for` последовательно перебирает элементы `my_foods` и выводит каждый из них.
- Второй цикл `for` делает то же самое со списком `friend_foods`.
- Переменная `pizza` получает очередной элемент списка на каждой итерации. Её имя не влияет на работу цикла.

## Проверка
**Задание выполнено правильно.** Оба списка выводятся отдельными циклами `for`, как и требуется.
