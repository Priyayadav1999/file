a=open("count_file.txt","w")

a.write("my name is priya\n")
a.write("I am doing programming language in navkgurukul")

a.close()
k=open("count_file.txt","r")
data=k.read()
word=data.split()
i=0
max=" "
while i<len(word):
    c=0
    j=0
    while j<len(word[i]):
        c+=1
        j+=1
    if c>len(max):
        max=word[i]
    i+=1
print("biggest word=", max)




# a="my name is priya"
# a=a.split()
# i=0
# while i<len(a):
#     print(a[i])
#     j=0
#     c=0
#     while j<len(a[i]):
#         c+=1
#         j+=1
#     print(c)
#     i+=1