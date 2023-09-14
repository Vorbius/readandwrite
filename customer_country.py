import csv

customers = open('customers.csv','r')
outfile = open('customer_country.csv','w')
csv_file=csv.reader(customers)

next(csv_file)
outfile.write(f'Full Name,Country \n')
for record in csv_file:
    outfile.write(f'{record[1]} {record[2]},')
    outfile.write(f' {record[4]} \n')

customers.close()
outfile.close()

