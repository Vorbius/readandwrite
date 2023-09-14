import csv
total=0
infile=open('sales.csv','r')
outfile=open('salesreport.csv','w')
outfile.write(f'Customer ID,Total \n')
read_file=csv.reader(infile)
next(read_file)
for record in read_file:
    Emp_Id=record[0]
    total+=float(record[3])
    total+=float(record[4])
    total+=float(record[5])
    break 

for record in read_file:
    if Emp_Id==record[0]:
        total+=float(record[3])+float(record[4])+float(record[5])
        total=round(total,2)
   
    else:
        outfile.write(Emp_Id)
        Emp_Id=record[0]
        outfile.write(',')
        outfile.write((str(total)))
        outfile.write(f'\n')
        total=float(record[3])+float(record[4])+float(record[5])

        
    Emp_Id=record[0]

outfile.write(Emp_Id)
outfile.write(',')
outfile.write(str(total))
infile.close()
outfile.close()