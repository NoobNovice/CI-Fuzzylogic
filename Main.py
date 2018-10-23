from ReadExcelFile import ReadExcelFile
from FuzzyLogic import FuzzyLogic

# dataSet = ReadExcelFile("TestDataset.xls")
# fuzzy = FuzzyLogic()
# fuzzy.trapezoidal(0, 0, 45, 50, "F")
# fuzzy.triangular(45, 50, 55, "D")
# fuzzy.triangular(50, 55, 60, "D+")
# fuzzy.triangular(55, 60, 65, "C")
# fuzzy.triangular(60, 65, 70, "C+")
# fuzzy.triangular(65, 70, 75, "B")
# fuzzy.triangular(70, 75, 80, "B+")
# fuzzy.trapezoidal(75, 80, 100, 100, "A")
#
# result = fuzzy.calculate_member(dataSet.get_table_sum())
# for i in result:
#     print(i)

dataSet = ReadExcelFile("childDataset.xls")
fuzzy = FuzzyLogic()
fuzzy.trapezoidal(50, 70, 100, 100, "p")
fuzzy.trapezoidal(100, 100, 130, 150, "q")
fuzzy.triangular(23, 33, 43, "r")
fuzzy.trapezoidal(17, 18.5, 24, 25, "s")
fuzzy.trapezoidal(1.5, 1.5, 12, 30, "t")

result = fuzzy.logical_calculate(dataSet.table_data)
for i in result:
    print(i)
