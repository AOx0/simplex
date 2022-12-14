from fractions import Fraction, Decimal

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
            return f"{Fraction(self.m)}M | {Fraction(self.i)}"

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
    def __init__(self, matriz, es_maximizar: bool = True, ints_only: bool = False):
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
        self.int = ints_only
        return

    def check_consistencia(self):
        pass

    def stop_iter_max(self):
        non_negative = [
                1 if self.matriz[0][i][1] >= M(0) else
                0 for i in range(len(self.matriz[0])-1)
        ]
        return sum(non_negative) == len(self.matriz[0])-1

    def stop_iter_min(self):
        non_positive = [
                1 if self.matriz[0][i][1] <= M(0) else
                0 for i in range(len(self.matriz[0])-1)
        ]
        return sum(non_positive) == len(self.matriz[0])-1

    def __str__(self):
        from prettytable import PrettyTable
        x = PrettyTable()

        names = [" "]
        for i in range(len(self.matriz[0])):
            if self.iterador == i:
                names += [C.BOLD + C.RED + "{0}".format(str(self.matriz[0][i][0])) + C.END]
            else:
                names += ["{0}".format(str(self.matriz[0][i][0]))]
        # print(names)
        x.field_names = names

        for j in range(len(self.matriz)):
            row = []
            # Row name
            if j == 0:
                row += ["{0}".format("z")]
            else:
                if self.iterador == i or self.iterador_fila == j:
                    row += [C.BOLD + C.RED + "{0}".format(str(self.matriz[j][0][0])) + C.END]
                else:
                    row += ["{0}".format(str(self.matriz[j][0][0]))]
            # Row values
            for i in range(len(self.matriz[j])):
                if self.iterador == i or self.iterador_fila == j:
                    row += [C.BOLD + C.RED + "{0}".format(str(self.matriz[j][i][1])) + C.END]
                else:
                    row += ["{0}".format(str(self.matriz[j][i][1]))]
            x.add_row(row)

        return x.__str__()

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
                    mayor = self.matriz[0][i][1]
                    j = i
                elif self.matriz[0][i][1] > mayor:
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
                self.matriz[j][i][1] = para_uno * self.matriz[self.iterador_fila][i][1] + self.matriz[j][i][1] 


matriz = [
    [["x1", -50], ["x2", -20], ["x3", -25], ["s1", 0], ["s2", 0], ["s3", 0], ["s4", 0], ["sol", 0]],
    [["s1", 9], 3, 5, 1, 0, 0, 0, 500],
    [["s2", 5], 4, 0, 0, 1, 0, 0, 350],
    [["s3", 3], 0, 3, 0, 0, 1, 0, 150],
    [["s4", 0], 0, 1, 0, 0, 0, 1, 20]
]
simple = Simplex(matriz, es_maximizar=True)

print(simple)

while not simple.iteracion():
    print(simple)

