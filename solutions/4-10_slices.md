# 4-10 — Срезы

## Условие
Добавить к одной из программ главы фрагмент, который выводит первые три элемента списка, три элемента из середины и последние три элемента, используя срезы.

## Исходный код
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

friend_foods.append("sasa")
friend_foods.append("sd")

my_foods.append("dizzel")
my_foods.append("finger")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nThe first three items in the list are:")
print(my_foods[0:3])

print("\nThe first three items in the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are:")
print(my_foods[-3:])
```

## Объяснение
- `my_foods[0:3]` берёт элементы с индексами 0, 1 и 2 — первые три элемента.
- `my_foods[1:4]` берёт элементы с индексами 1, 2 и 3. В списке из пяти элементов это три элемента из середины.
- `my_foods[-3:]` начинает с третьего элемента с конца и берёт всё до конца списка — последние три элемента.
- `friend_foods = my_foods[:]` создаёт копию списка.
- `append()` добавляет новые элементы в конец соответствующих списков.

## Проверка
**Основная логика срезов выполнена правильно.** Все три среза дают требуемые группы элементов для текущего списка. Небольшое расхождение с условием: перед срезом середины повторено сообщение `The first three items in the list are:`, хотя должно быть `Three items from the middle of the list are:`. Это ошибка текста, а не логики среза.
