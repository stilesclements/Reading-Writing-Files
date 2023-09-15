def main():
    outfile=open("clients.txt","r")
    count=0
    for i in outfile:
        count+=1
        i=i.rstrip("\n")
        print(count,". ", i, sep="")
    outfile.close()

main()