from gpiozero import LED
from random import randint

BIT_LEN = 4

x = randint(0, 2**BIT_LEN - 1)
y = x

for i in range(BIT_LEN):
    if (x & 1 == 1):
        led = LED(i)
        led.on()
    x = x >> 1

guess = -1
while guess != y:
    try:
        guess = int(input("Welche Zahl wird dargestellt? "))
    except ValueError:
        print("Du musst eine gültige Zahl angeben!")

print("Du hast es geschafft! Die gesuchte Zahl war", y)
print("Binär:", bin(y))
