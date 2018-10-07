# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    n1 = int(number * (10**(ndigits + 1)))
    n2 = n1 % 10;
    if n2 >= 5 and n2 <=9:
        n1 = n1 // 10 + 1
    elif n2 >= 0 and n2 < 5:
        n1 = n1 // 10
    else:
        print("Error!")
    return float(n1 / (10**ndigits))



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if 6 != (len(str(ticket_number))):
        return False
    else:
        def count_3digits(num):
            n1 = num % 10
            n2 = num // 10 % 10
            n3 = num // 100
            return n1 + n2 + n3

        n1 = ticket_number % 1000
        n2 = ticket_number // 1000

        if count_3digits(n1) == count_3digits(n2):
            return True
        else:
            return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
