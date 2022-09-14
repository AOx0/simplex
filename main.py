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
    [["x1", -1],     ["x2", Compuesto(2, 2)],     ["s1", Compuesto(0, -1)],     ["s2", Compuesto(0, -1)],     ["r1", 0], ["r2", 0],["x5", 0],   ["Sol", Compuesto(0, 3)]],
    [["s1", 1],     [None, 1],      [None, -1],     [None, 0],      [None, 1],      [None, 0],      [None, 0], [None, 2]],
    [["r1", -1],     [None, 1],      [None, 0],     [None, -1],      [None, 0],      [None, 1],      [None, 0], [None, 1]],
    [["r2", 0],     [None, 1],      [None, 0],     [None, 0],      [None, 0],      [None, 0],      [None, 1], [None, 3]],
]
"""

class Compuesto:
    def __init__(self, i, m):
        self.i = Fraction(Decimal(i)) if type(i) != Fraction else i
        self.m = m

    def __int__(self):
        return self.m * 1000 + self.i

    def __add__(self, other):
        if type(other) == Compuesto:
            return Compuesto(self.i + other.i, self.m + other.m)
        else:
            return Compuesto(self.i + other, self.m)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Compuesto:
            return Compuesto(self.i - other.i, self.m - other.m)
        else:
            return Compuesto(self.i - other, self.m)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) == Compuesto:
            return Compuesto(self.i * other.i, self.m * other.m)
        else:
            return Compuesto(self.i * other, self.m * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == Compuesto:
            return Compuesto(0 if self.i == 0 or other.i == 0 else self.i/other.i, 0 if self.i == 0 or other.i == 0 else self.m/other.m)
        else:
            return Compuesto(self.i/other, self.m)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.m == 0:
            return f"{str(self.i)}"
        elif self.i == 0:
            return f"{self.m}M"
        else:
            return f"({self.m}M" + "," + f"{self.i})"

    def __ge__(self, other):
        if type(other) == Compuesto:
            return self.i + int(self.m) * 1000 >= other.i + int(other.m) * 1000
        else:
            return self.i + int(self.m) * 1000 >= other

    def __le__(self, other):
        if type(other) == Compuesto:
            return self.i + int(self.m) * 1000 <= other.i + int(other.m) * 1000
        else:
            return self.i + int(self.m) * 1000 <= other

    def __gt__(self, other):
        if type(other) == Compuesto:
            return self.i + int(self.m) * 1000 > other.i + int(other.m) * 1000
        else:
            return self.i + int(self.m) * 1000 > other

    def __lt__(self, other):
        if type(other) == Compuesto:
            return self.i + int(self.m) * 1000 < other.i + int(other.m) * 1000
        else:
            return self.i + int(self.m) * 1000 < other

    def __itruediv__(self, other):
        self = self.__truediv__(other)


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
                if type(matriz[j][i][1]) != Compuesto:
                    matriz[j][i][1] = Fraction(Decimal(matriz[j][i][1]))
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
                1 if self.matriz[0][i][1] >= 0 else
                0 for i in range(len(self.matriz[0])-1)
        ]
        #print(non_negative)
        if sum(non_negative) == len(self.matriz[0])-1:
            return True

        return False

    def stop_iter_min(self):
        non_positive = [
                1 if self.matriz[0][i][1] <= 0 else
                0 for i in range(len(self.matriz[0])-1)
        ]
        #print(non_positive)
        if sum(non_positive) == len(self.matriz[0])-1:
            return True

        return False

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
                    menor = self.matriz[0][i][1]
                    j = i
                elif self.matriz[0][i][1] < menor:
                    menor = self.matriz[0][i][1]
                    j = i
        elif not es_maximizar:
            mayor = None
            for i in range(len(self.matriz[0])-1):
                if self.matriz[0][i][1] == 0:
                    continue
                if mayor is None:
                    #print("Primer menor:", self.matriz[0][i][1])
                    mayor = self.matriz[0][i][1]
                    j = i
                elif self.matriz[0][i][1] > mayor:
                    #print("Menor:", self.matriz[0][i][1])
                    mayor = self.matriz[0][i][1]
                    j = i

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
            # print(f"Ratio de {ratio} {valor_sol}/{valor}")

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


matriz = [
    [["x1", Compuesto(-6, 3)], ["x2", Compuesto(-10, 4)], ["s1", 0], ["s2", Compuesto(0, -1)], ["r1", 0], ["r2", 0],   ["Sol", Compuesto(0, 90)]],
    [["s1", 1],     [None, 0],      [None, 1],     [None, 0],      [None, 0],      [None, 0],       [None, 12]],
    [["r1", 3],     [None, 2],      [None, 0],     [None, 1],      [None, 1],      [None, 0],      [None, 54]],
    [["r2", 0],     [None, 2],      [None, 0],     [None, 0],      [None, 0],      [None, 1],      [None, 36]],
]

simple = Simplex(matriz, es_maximizar=False)

print(simple)

while not simple.iteracion():
    print(simple)

