# Reading an excel file using Python
import xlrd
from sys import argv
# Give the location of the file
script, loc = argv

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

# Extracting number of rows
print "Number of rows: ", sheet.nrows

# Extracting number of columns
print "Number of Columns: ", sheet.ncols

print "Names of Columns: ",
# Extracting all columns
for i in range(sheet.ncols):
    print sheet.cell_value(0, i),
print "\n"

# Extracting first column
print "First Column :"
for i in range(sheet.nrows):
    print sheet.cell_value(i, 0)

# Extract a particular row value
print sheet.row_values(1)
