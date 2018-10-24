from ReadExcelFile import ReadExcelFile
from FuzzyLogic import FuzzyLogic

dataSet = ReadExcelFile("childDataset.xls")
fuzzy = FuzzyLogic()
print(len(dataSet.table_data))
fuzzy.sugeno_calculate(dataSet.table_data)
