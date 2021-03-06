from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


years=list(map(getvalue,sheet['A'][1:]))
relations=list(map(getvalue,sheet['B'][1:]))
sunactivity=list(map(getvalue,sheet['C'][1:]))

pyplot.plot(years,relations,label='Отношения')
pyplot.plot(years,sunactivity,label='gfdg')
pyplot.show()
