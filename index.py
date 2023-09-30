"""
Программа для расчета налога с продаж
Версия: 1.0
Автор: Сергей
"""

# Исходные данные
RENAME = 69.8
AMOUNT = 4
TAX = 0.20

# Выполнение расчетов
total_price = round(RENAME * AMOUNT, 2)
tax_from_sale = round(total_price * TAX, 2)
price_without_tax = round(total_price - tax_from_sale, 2)

# Вывод информации
print("Цена покупки", total_price)
print("Включая налог", tax_from_sale)
