# Імпортуємо необхідні модулі з бібліотеки PuLP
from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpStatus, value

# Створюємо модель
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні для виробництва "Лимонаду" та "Фруктового соку"
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')  # Кількість "Лимонаду"
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')  # Кількість "Фруктового соку"

# Цільова функція: максимізувати загальну кількість вироблених продуктів
model += lpSum([lemonade, fruit_juice]), "Total_Products"

# Обмеження на ресурси
model += (2 * lemonade + fruit_juice <= 100, "Water_Constraint")  # Вода
model += (lemonade <= 50, "Sugar_Constraint")  # Цукор
model += (lemonade <= 30, "Lemon_juice_Constraint")  # Лимонний сік
model += (2 * fruit_juice <= 40, "Fruit_puree_Constraint")  # Фруктове пюре

# Розв'язуємо модель
model.solve()

# Виводимо статус розв'язку
print(f"Status: {LpStatus[model.status]}")

# Виводимо кількість вироблених напоїв
print(f"Лимонад: {value(lemonade)}")
print(f"Фруктовий сік: {value(fruit_juice)}")
print(f"Загальна кількість продуктів: {value(model.objective)}")
