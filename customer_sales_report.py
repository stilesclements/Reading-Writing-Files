import csv



def main():
    Sales=open("sales.csv","r")
    Sales_csv=csv.reader(Sales)
    next(Sales_csv)

    Sales_report=open("salesreport.csv","w")
    Sales_report.write("Customer ID,Total\n")
    CustomerId="250"
    Total_cost=0
    for rec in Sales_csv:
        if rec[0]==CustomerId:
            Total_cost+=float(rec[3])+float(rec[4])+float(rec[5])
        else:
            Sales_report.write(f"{CustomerId},{Total_cost:.2F}\n")
            CustomerId=rec[0]
            Total_cost=float(rec[3])+float(rec[4])+float(rec[5])
    Sales_report.write(f"{CustomerId},{Total_cost:.2F}")


main()