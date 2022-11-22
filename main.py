from fractions import Fraction, Decimal

"""
matriz = [
    # First row & column is (tag, value)
    [["x1", -3],     ["x2", -2],     ["x3", 0],     ["x4", 0],     ["x5", 0],  ["Solucion", 0]],
    [["x3", 2],     [None, 1],      [None, 1],     [None, 0],      [None, 0],      [None, 18]],
    [["x4", 2],     [None, 3],      [None, 0],     [None, 1],      [None, 0],      [None, 42]],
    [["x5", 3],     [None, 1],      [None, 0],     [None, 0],      [None, 1],      [None, 24]],
]

matriz = [
    # First row & column is (tag, value)
    [["x1", -1],     ["x2", 2],     ["x3", 0],     ["x4", 0],     ["x5", 0],  ["Solucion", 0]],
    [["x1", 1],     [None, 0],      [None, -1/2],     [None, 1/2],      [None, 0],      [None, 1/2]],
    [["x2", 0],     [None, 1],      [None, -1/2],     [None, -1/2],      [None, 0],      [None, 3/2]],
    [["x5", 0],     [None, 0],      [None, 1/2],     [None, 1/2],      [None, 1],      [None, 3/2]],
]

matriz = [
    [["x1", -2],     ["x2", -5],     ["x3", 0],     ["x4", 0],     ["x5", 0],  ["Solucion", 0]],
    [["x3", 1],     [None, 6],      [None, 1],     [None, 0],      [None, 0],      [None, 20]],
    [["x4", 1],     [None, 1],      [None, 0],     [None, 1],      [None, 0],      [None, 60]],
    [["x5", 1],     [None, 0],      [None, 0],     [None, 0],      [None, 1],      [None, 40]],
]


matriz = [
    [["x1", -3],     ["x2", 2],     ["s1", 0],     ["s2", 0],     ["s3", 0],  ["Solucion", 0]],
    [["s1", 2],     [None, 1],      [None, 1],     [None, 0],      [None, 0],      [None, 18]],
    [["s2", 2],     [None, 3],      [None, 0],     [None, 1],      [None, 0],      [None, 42]],
    [["s3", 3],     [None, -2],      [None, 0],     [None, 0],      [None, 1],      [None, 5]],
]

matriz = [
    [["x1", -1],     ["x2", M(2, 2)],     ["s1", M(0, -1)],     ["s2", M(0, -1)],     ["r1", 0], ["r2", 0],["x5", 0],   ["Sol", M(0, 3)]],
    [["s1", 1],     [None, 1],      [None, -1],     [None, 0],      [None, 1],      [None, 0],      [None, 0], [None, 2]],
    [["r1", -1],     [None, 1],      [None, 0],     [None, -1],      [None, 0],      [None, 1],      [None, 0], [None, 1]],
    [["r2", 0],     [None, 1],      [None, 0],     [None, 0],      [None, 0],      [None, 0],      [None, 1], [None, 3]],
]
"""

class M:
    def __init__(self, m, i=0):
        self.m = Fraction(m).limit_denominator() if type(m) != Fraction else m
        self.i = Fraction(i).limit_denominator() if type(i) != Fraction else i

    def __int__(self):
        return self.m * 1000 + self.i

    def __add__(self, other):
        if type(other) == M:
            return M(self.m + other.m, self.i + other.i)
        else:
            return M(self.m, self.i + Fraction(other))

    def __radd__(self, other):
        return self.__add__(Fraction(other))

    def __sub__(self, other):
        if type(other) == M:
            return M(self.m - other.m, self.i - other.i)
        else:
            return M(self.m, self.i - Fracion(other))

    def __rsub__(self, other):
        return self.__sub__(Fraction(other))

    def __mul__(self, other):
        if type(other) == M:
            return M(self.m * other.m, self.i * other.i)
        else:
            return M(self.m * Fraction(other), self.i * Fraction(other))

    def __rmul__(self, other):
        return self.__mul__(Fraction(other))

    def __truediv__(self, other):
        if type(other) == M:
            return M(
                Fraction(self.m/other.m),
                Fraction(self.i/other.i)
            )
        else:
            return M(
                self.m,
                Fraction(self.i/Fraction(other))
            )

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        return float(self.m * 1000 + self.i)

    def __str__(self):
        if self.m == 0:
            return f"{Fraction(str(self.i))}"
        elif self.i == 0:
            return f"{Fraction(self.m)}M"
        else:
            return f"({Fraction(self.m)}M" + "," + f"{Fraction(self.i)})"

    def __ge__(self, other):
        return float(self) >= float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __itruediv__(self, other):
        self = self.__truediv__(Fraction(other))


class C:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Simplex:
    def __init__(self, matriz, es_maximizar: bool = True):
        for j in range(len(matriz)):
            for i in range(len(matriz[0])):
                if type(matriz[j][i]) == list:
                    if type(matriz[j][i][1]) != M:
                        matriz[j][i][1] = Fraction(matriz[j][i][1]).limit_denominator()
                else:
                    matriz[j][i] = [None, Fraction(matriz[j][i]).limit_denominator()]
        self.es_maximizar = es_maximizar
        self.es_minimizar = not es_maximizar
        self.matriz = matriz
        self.iterador = None
        self.iterador_fila = None
        return

    def check_consistencia(self):
        pass

    def stop_iter_max(self):
        non_negative = [
                1 if self.matriz[0][i][1] >= M(0) else
                0 for i in range(len(self.matriz[0])-1)
        ]
        # print(non_negative)
        return sum(non_negative) == len(self.matriz[0])-1

    def stop_iter_min(self):
        non_positive = [
                1 if self.matriz[0][i][1] <= M(0) else
                0 for i in range(len(self.matriz[0])-1)
        ]
        # print(non_positive)
        return sum(non_positive) == len(self.matriz[0])-1

    def __str__(self):
        result = ""
        """
        if self.iterador_fila is not None:
            result += "Iterador fila: {0: <10}\n".format(self.iterador_fila)

        if self.iterador is not None:
            result += "Iterador: {0: <10}\n".format(self.iterador)
        """

        result += "\n{0: >10}".format("")
        for i in range(len(self.matriz[0])):
            if self.iterador == i:
                result += C.BOLD + C.RED + "{0: >10} ".format(str(self.matriz[0][i][0])) + C.END
            else:
                result += "{0: >10} ".format(str(self.matriz[0][i][0]))

        result += "\n"

        for j in range(len(self.matriz)):
            if j == 0:
                result += "{0: >10} ".format("z")
            else:
                if self.iterador == i or self.iterador_fila == j:
                    result += C.BOLD + C.RED + "{0: >10} ".format(str(self.matriz[j][0][0])) + C.END
                else:
                    result += "{0: >10} ".format(str(self.matriz[j][0][0]))
            for i in range(len(self.matriz[j])):
                if self.iterador == i or self.iterador_fila == j:
                    result += C.BOLD + C.RED + "{0: >10} ".format(str(self.matriz[j][i][1])) + C.END
                else:
                    result += "{0: >10} ".format(str(self.matriz[j][i][1]))
            result += "\n"

        return result

    def __repr__(self):
        return self.__str__()

    def iteracion(self):
        es_maximizar = self.es_maximizar

        if es_maximizar and self.stop_iter_max():
            return True
        elif not es_maximizar and self.stop_iter_min():
            return True

        # Obtenemos la fila para iterar
        j = 0
        if es_maximizar:
            menor = None
            for i in range(len(self.matriz[0])-1):
                if self.matriz[0][i][1] == 0:
                    continue
                if menor is None:
                    # print("Primer menor:", self.matriz[0][i][1])
                    menor = self.matriz[0][i][1]
                    j = i
                elif self.matriz[0][i][1] < menor:
                    # print("Menor:", self.matriz[0][i][1])
                    menor = self.matriz[0][i][1]
                    j = i
        elif not es_maximizar:
            mayor = None
            for i in range(len(self.matriz[0])-1):
                if self.matriz[0][i][1] == 0:
                    continue
                if mayor is None:
                    # print("Primer menor:", self.matriz[0][i][1])
                    mayor = self.matriz[0][i][1]
                    j = i
                elif self.matriz[0][i][1] > mayor:
                    # print("Menor:", self.matriz[0][i][1])
                    mayor = self.matriz[0][i][1]
                    j = i

        # print(j)
        self.iterador = j

        # Obtenemos la columna para iterar
        j = 0
        menos = None
        for i in range(1, len(self.matriz)):
            valor = self.matriz[i][self.iterador][1]
            valor_sol = self.matriz[i][-1][1]

            try:
                ratio = valor_sol / valor
            except:
                continue
            print(f"Ratio de {ratio} {valor_sol}/{valor}")

            if ratio < 0:
                continue
            elif menos is None:
                menos = ratio
                j = i
            elif menos is not None and ratio < menos:
                menos = ratio
                j = i

        self.iterador_fila = j

        self.matriz[self.iterador_fila][0][0] = self.matriz[0][self.iterador][0]

        remaining = set(range(len(self.matriz))) - {self.iterador_fila}

        para_uno = self.matriz[self.iterador_fila][self.iterador][1]
        for i in range(len(self.matriz[self.iterador_fila])):
            self.matriz[self.iterador_fila][i][1] = self.matriz[self.iterador_fila][i][1]/para_uno
 
        for j in remaining:
            num = self.matriz[j][self.iterador][1]
            for i in range(len(self.matriz[j])):
                a = self.matriz[self.iterador_fila][i][1]
                para_uno = -1 * num
                # print("A: ", a, " * ", para_uno, " + ", self.matriz[j][i][1])
                self.matriz[j][i][1] = para_uno * self.matriz[self.iterador_fila][i][1] + self.matriz[j][i][1] 


# matriz = [
#     [["x1", M(-6, 3)], ["x2", M(-10, 4)], ["s1", 0], ["s2", M(0, -1)], ["r1", 0], ["r2", 0],   ["Sol", M(0, 90)]],
#     [["s1", 1],     [None, 0],      [None, 1],     [None, 0],      [None, 0],      [None, 0],       [None, 12]],
#     [["r1", 3],     [None, 2],      [None, 0],     [None, 1],      [None, 1],      [None, 0],      [None, 54]],
#     [["r2", 0],     [None, 2],      [None, 0],     [None, 0],      [None, 0],      [None, 1],      [None, 36]],
# ]

matriz = [
    [["x1", M(1.1,-0.4)], ["x2", M(0.9,-0.5)], ["s1", 0], ["s2", M(-1)], ["r1", 0], ["r2", 0],   ["Sol", M(12,0)]],
    [["s1", 0.3],   0.1,    1,     0,     0,     0,      2.7],
    [["r1", 0.5],   0.5,    0,     0,     1,     0,      6],
    [["r2", 0.6],   0.4,    0,    -1,     0,     1,      6],
]
simple = Simplex(matriz, es_maximizar=False)

print(simple)

while not simple.iteracion():
    print(simple)

