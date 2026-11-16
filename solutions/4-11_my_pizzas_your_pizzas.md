# 4-11 — Моя пицца, твоя пицца

## Условие
Создать копию списка пицц под именем `friend_pizzas`, добавить разные пиццы в исходный список и копию, затем вывести оба списка отдельными циклами `for`.

## Исходный код
```python
pizza = ["margarite", "peperoni", "chiken burger"]
for pizzas in pizza:
    print("i like "  + pizzas)
print("i really like pizza")

friend_pizza = pizza [:]

pizza.append("chikibamboni")
friend_pizza.append("zalupizza")

print("\nMy favorite pizzas are:")
for papiz in pizza:
    print(papiz) 

print("\nfavorite pizzas friend:")
for rose in friend_pizza:
    print(rose)
```

## Объяснение
- `pizza` — исходный список.
- `friend_pizza = pizza[:]` создаёт отдельную копию списка, а не вторую ссылку на тот же список.
- `pizza.append(...)` добавляет новую пиццу только в исходный список.
- `friend_pizza.append(...)` добавляет другую пиццу только в копию.
- Первый цикл `for` выводит элементы исходного списка.
- Второй цикл `for` выводит элементы списка друга.

## Проверка
**Логика задания выполнена правильно.** Два списка независимы, в каждом есть своя добавленная пицца, и оба списка выводятся циклами `for`.

Небольшие отличия от текста упражнения: список назван `friend_pizza`, а не `friend_pizzas`; сообщение перед вторым циклом отличается от требуемой формулировки. На работу программы это не влияет.
