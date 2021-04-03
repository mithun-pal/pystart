import xlrd
import xlwt

workbook = xlrd.open_workbook('sample_file.xlsx')
sheet = workbook.sheet_by_name('Sheet1')

for i in range(10):
    row = sheet.row_values(i)
    file1_data =[row[0],row[1]]
    file2_data = [row[2],row[3],row[4]]
    print(file1_data)
    print(file2_data)



