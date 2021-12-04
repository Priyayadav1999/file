banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
k=open("file-question3.txt","w")
for a in banks_list:
    k.write(a)
    k.write("\n")

k.close()