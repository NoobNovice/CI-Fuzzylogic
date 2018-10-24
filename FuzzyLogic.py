import matplotlib.pyplot as plt
import numpy

class FuzzyLogic:
    __boundary_a__ = []
    __boundary_b__ = []
    __boundary_c__ = []
    __boundary_d__ = []
    __member_function__ = []
    __fuzzySet__ = []
    __rule__ = []

    def __init__(self):
        self.trapezoidal(50, 80, 100, 100, "p")
        self.trapezoidal(79, 100, 130, 150, "q")
        self.trapezoidal(16, 20, 22.4, 25, "r")
        self.trapezoidal(2, 4, 12, 30, "s")

        # self.print_member_function("p", 0, 0, 100)
        # self.print_member_function("q", 1, 70, 200)
        # self.print_member_function("r", 2, 15, 40)
        # self.print_member_function("s", 3, 1, 100)
        return

    # set function and boundary each fuzzy set
    def triangular(self, a, b, c, f):
        self.__member_function__.append("tri")
        self.__boundary_a__.append(a)
        self.__boundary_b__.append(b)
        self.__boundary_c__.append(c)
        self.__boundary_d__.append(0)
        self.__fuzzySet__.append(f)
        return

    def trapezoidal(self, a, b, c, d, f):
        self.__member_function__.append("trap")
        self.__boundary_a__.append(a)
        self.__boundary_b__.append(b)
        self.__boundary_c__.append(c)
        self.__boundary_d__.append(d)
        self.__fuzzySet__.append(f)
        return

    # member calculator
    def __member_tri__(self, x, index):
        if x < self.__boundary_a__[index]:
            return 0
        elif self.__boundary_a__[index] <= x < self.__boundary_b__[index]:
            return (x - self.__boundary_a__[index]) / (self.__boundary_b__[index] - self.__boundary_a__[index])
        elif self.__boundary_b__[index] <= x < self.__boundary_c__[index]:
            return (self.__boundary_c__[index] - x) / (self.__boundary_c__[index] - self.__boundary_b__[index])
        else:
            return 0

    def __member_trap__(self, x, index):
        if x < self.__boundary_a__[index]:
            return 0
        elif self.__boundary_a__[index] <= x < self.__boundary_b__[index]:
            return (x - self.__boundary_a__[index]) / (self.__boundary_b__[index] - self.__boundary_a__[index])
        elif self.__boundary_b__[index] <= x < self.__boundary_c__[index]:
            return 1
        elif self.__boundary_c__[index] <= x < self.__boundary_d__[index]:
            return (self.__boundary_d__[index] - x) / (self.__boundary_d__[index] - self.__boundary_c__[index])
        else:
            return 0

    def calculate_member(self, data_arr):
        # write text report
        report = []

        head = []
        for i in range(len(self.__fuzzySet__)):
            head.append(self.__fuzzySet__[i])
        head.append("result")

        report.append(head)
        for data in data_arr:
            row = []
            mem_max = 0
            fuzzy_index = 0
            for function_index in range(len(self.__member_function__)):
                if self.__member_function__[function_index] == "tri":
                    row.append(self.__member_tri__(data, function_index))
                if self.__member_function__[function_index] == "trap":
                    row.append(self.__member_trap__(data, function_index))
                # find max membership function
                if mem_max < row[function_index]:
                    mem_max = row[function_index]
                    fuzzy_index = function_index
            row.append(self.__fuzzySet__[fuzzy_index])
            report.append(row)
        return report

    def logical_calculate(self, data_table):
        # (p ^ q ^ r ^ s) v t
        report = []
        head = ["p", "q", "r", "s", "t", "member", "conclusion"]
        report.append(head)
        for data in data_table:
            row = []
            # find p
            p = self.__member_trap__(data[0], 0)
            row.append(p)
            # find q
            q = self.__member_trap__(data[1], 1)
            row.append(q)
            # find r
            r = self.__member_trap__(data[3], 3)
            row.append(r)
            # find s
            s = self.__member_trap__(data[4], 4)
            row.append(s)

            temp = min(q, r)
            member = max(temp, s, p)
            row.append(member)

            if member > 0.5:
                row.append("loli")
            else:
                row.append("non")

            report.append(row)
        return report

    def sugeno_calculate(self, data_arr):
        for data in data_arr:
            print(data)
            row = []
            p = self.__member_trap__(data[0], 0)
            q = self.__member_trap__(data[1], 1)
            r = self.__member_trap__(data[2], 2)
            s = self.__member_trap__(data[3], 3)
            np = 1 - p
            nq = 1 - q
            nr = 1 - r
            ns = 1 - s

            # rule 1: p ^ ( q ^ r ) => L
            row.append(min(p, q, r))
            # rule 2: p ^ s => L
            row.append(min(p, s))
            # rule 3: s => L
            row.append(s)
            # rule 4: p ^ ~( q ^ r ) => NL
            row.append(min(p, max(nq, nr)))
            # rule 5: ~p ^ ~s => NL
            row.append(min(np, ns))
            # rule 6: ~s ^ ~( q ^ r )=> NL
            row.append(min(ns, max(nq, nr)))

            l = max(row[0], row[1], row[2])
            nl = max(row[3], row[4], row[5])
            result = ((100 * l) + (0 * nl)) / (l + nl)
            row.append(result)
            print(row)
            print("")
        return

    def print_member_function(self, title, index, sx, ex):
        plt.title('member function ' + title)
        plt.grid(False)

        x1 = numpy.arange(sx, ex, 1)
        y1 = []
        if self.__member_function__[index] == "tri":
            for i in x1:
                y1.append(self.__member_tri__(i, index))
        else:
            for i in x1:
                y1.append(self.__member_trap__(i, index))

        plt.plot(x1, y1)
        plt.savefig(title + " member function")
        plt.show()
        print("\n")
        return
