# Funktionen aus der Mathematik
# 1BHIF | Marc Edlinger | 06.01.2022
import matplotlib.pyplot as pyp
import numpy as np


class MathFunction():
    def __init__(self, term: str, symbole: str = "f", var_name: str = "x", color="r"):
        self.symbole = symbole
        self.var_name = var_name
        self.term = term
        self.color = color

    def parse(self: list, symbole: str = "f", var_name: str = "x", color='r'):
        term_string = self[0]
        for part in self[1:]:
            term_string += " " + part
        return MathFunction(term_string, symbole, var_name, color)

    def __str__(self):
        return f"{self.symbole}({self.var_name}) = {self.term}"

    def __int__(self):
        return self.evaluate(0)

    def evaluate(self, x: int):
        prepared_term = self.term
        prepared_term = prepared_term.replace(self.var_name, "(" + str(x) + ")")
        prepared_term = prepared_term.replace("^", "**")
        return eval(prepared_term)

    def get_result_string(self, x: int):
        value: int = self.evaluate(x)
        return f"{self.symbole}({x}) = {value}"

    def derivative(self):
        parts = self.term.split(" ")

        derivative_parts = parts.copy()
        for i in range(0, len(parts), 2):
            part = parts[i]
            exp = 0
            var_name = self.var_name
            if part.__contains__("^"):
                exp = int(part.split("^")[1])
            elif part.__contains__(var_name):
                exp = 1

            coefficient = int(part.split("*")[0]) if part.__contains__("*") else 1
            coefficient *= exp
            exp -= 1

            if coefficient == 0:
                derivative_parts[i] = "0"
                continue

            part_string = f"{coefficient}*{var_name}"
            if exp == 0:
                part_string = part_string.replace("*" + var_name, "")
            elif exp != 1:
                part_string += "^" + str(exp)
            derivative_parts[i] = part_string
        return MathFunction.parse(derivative_parts, symbole=self.symbole + "'")

    def integrate(self):
        parts = self.term.split(" ")

        integration_parts = parts.copy()
        for i in range(0, len(parts), 2):
            part = parts[i]
            exp = 0
            var_name = self.var_name
            if part.__contains__("^"):
                exp = int(part.split("^")[1])
            elif part.__contains__(var_name):
                exp = 1

            if (part.__contains__("*")):
                coefficient = int(part.split("*")[0])
            elif (part.__contains__(var_name)):
                coefficient = 1
            else:
                coefficient = int(part)
            exp += 1
            coefficient /= exp

            part_string = f"{coefficient:,.2f}*{var_name}"

            if (exp != 1):
                part_string += "^" + str(exp)
            integration_parts[i] = part_string
        return MathFunction.parse(integration_parts, symbole=self.symbole.upper())

    def nth_derivative(self, n: int):
        f: MathFunction = self
        for i in range(n):
            f = f.derivative()
        return f

    def plot(self, neg_limit: int, pos_limit: int, only_posititve: bool = False, other_functions=None):
        numbers = np.linspace(neg_limit, pos_limit, 100)

        fig = pyp.figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.spines['left'].set_position('center')
        axis.spines['bottom'].set_position('zero')
        axis.spines['right'].set_color('none')
        axis.spines['top'].set_color('none')
        axis.xaxis.set_ticks_position('bottom')
        axis.yaxis.set_ticks_position('left')

        pyp.plot(numbers, self.get_values(numbers, only_posititve), self.color)
        if not other_functions is None:
            for function in other_functions:
                pyp.plot(numbers, function.get_values(numbers, only_posititve), function.color)
        pyp.draw()
        pyp.show()

    def get_values(self, numbers, only_positive: bool):
        y = list()
        for i in numbers:
            value = self.evaluate(i)
            y.append(value if not only_positive else (value if value >= 0 else 0))

        return y


f = MathFunction("2*x^2 + x - 3")
F = f.integrate()
f.plot(-10, 10, False, [F])
print(F.evaluate(5) - F.evaluate(1))
