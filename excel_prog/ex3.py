# Code #2 : Adding style sheet in excel
# importing xlwt module
import xlwt
workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Sheet Name")

# Specifying style
style = xlwt.easyxf('font: bold 1')

# Specifying column
sheet.write(0, 0, 'SAMPLE', style)
workbook.save("sample.xls")

# Applying multiple styles
style2 = xlwt.easyxf('font: bold 1, color red;')

# Specifying column
sheet.write(0, 1, 'Arnav', style)
workbook.save("sample1.xls")
