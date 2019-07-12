# Writing to an excel sheet using Python
# sheet using Python

import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet1')

sheet1.write(0, 1, 'First Name')
sheet1.write(0, 2, 'Last Name')
sheet1.write(0, 3, 'Last Name')
sheet1.write(0, 4, 'Address')
sheet1.write(1, 0, 'First Name')
sheet1.write(2, 0, 'Last Name')
sheet1.write(3, 0, 'Last Name')
sheet1.write(4, 0, 'Address')

wb.save('Sec.xls')
