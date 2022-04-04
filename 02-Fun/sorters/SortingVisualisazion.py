"""
Marc EDLINGER
1bHIF | 04/04/2022
"""
import glfw
from p5 import *
from random import randint
from BubbleSort import bubble_sort
from QuickSort import quick_sort

data_size = 100
data = [0] * data_size
width = 1000


def setup():
    background(0)
    size(width, width)

    # fill data array with random numbers
    for i in range(data_size):
        data[i] = randint(0, width)

    size_per_bar: int = width / data_size
    background(255)
    for i in range(data_size):
        start: int = i * size_per_bar
        end: int = start + size_per_bar
        rect(start, 0, end, data[i])


def draw():

    pass


run()

