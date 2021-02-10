#Written by Michael S. Smith 12/17/20
# import required libraries
def convertFile(file1,file2,path):
    import openpyxl 
    import csv 
    
    importfile = file1
    exportfile = file2
    directory = path

    # open given workbook  
    excel = openpyxl.load_workbook(directory + importfile, data_only=True, read_only=True) 
  
    # select the active sheet
    sheet = excel.active 
  
    # writer object is created 
    col = csv.writer(open(directory + exportfile, 'w', newline="")) 
  
    # writing the data in csv file 
    for r in sheet.rows: 
        # row by row write  
        # operation is perform 
        col.writerow([cell.value for cell in r])

    excel.close()
    
    return('ok')