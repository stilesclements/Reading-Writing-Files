def main():
    infile=open("philosophers.txt","r")
    #file_contents=infile.read()
    line1=infile.readline().rstrip("\n")
    line2=infile.readline().rstrip("\n")
    line3=infile.readline().rstrip("\n")
    print(line1)
    print(line2)
    print(line3)
    #print(file_contents)
    infile.close()

main()