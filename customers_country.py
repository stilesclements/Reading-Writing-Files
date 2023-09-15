import csv

customers =open("customers.csv","r")
csv_file=csv.reader(customers)
next(csv_file) #Skips a row

outfile=open("customer_country.csv","w")
outfile.write("Full name, Country\n")
count=0
for rec in csv_file:
    #Full_name=rec[1]+" "+rec[2]
    #Country=rec[4]
    #outfile.write(Full_name+","+Country+"\n")
    outfile.write(rec[1]+" "+rec[2]+","+rec[4]+"\n")
    count+=1
print("Read", count, "customers")
outfile.close()
