import turtle


# Малює одну криву Коха
def koch_curve(t, order, size):
    # param t: об'єкт turtle (черепашка)
    # param order: поточний рівень рекурсії (глибина)
    # param size: довжина лінії
    
    if order == 0:
        # Базовий випадок: малюємо пряму лінію
        t.forward(size)
    
    else:
        # Розбиваємо лінію на 4 частини довжиною 1/3 від загальної
        
        # Перший сегмент
        koch_curve(t, order - 1, size / 3)
        
        # Поворот ліворуч на 60 градусів
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        
        # Поворот праворуч на 120 градусів (зворотний кут)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        
        # Поворот ліворуч на 60 градусів
        t.left(60)
        koch_curve(t, order - 1, size / 3)


# Налаштування, малювання сніжинки (3 криві Коха)
def draw_snowflake(order, size=300):
    
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Фрактал: Сніжинка Коха")
    
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.pensize(2)
    t.color("blue")

    # Центрування сніжинки: піднімаємо перо і зміщуємось
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Сніжинка складається з 3-х кривих Коха, з'єднаних під кутом 120 градусів
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Завершення роботи при кліку
    print(f"Сніжинку рівня {order} намальовано!")
    window.exitonclick()


if __name__ == "__main__":

    try:
        user_input = input("Введіть рівень рекурсії (рекомендовано 0-5): ")
        order = int(user_input)
        
        if order < 0:
            print("Рівень рекурсії не може бути від'ємним.")
        else:
            print("Починаю малювання... Перевірте вікно Turtle Graphics.")
            draw_snowflake(order)
            
    except ValueError:
        print("Будь ласка, введіть ціле число.")
