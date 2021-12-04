a=open("people1-exercise.txt","w")
a.write("rishabh - meerut\nimtiyaz - delhi\nnilima - cochin\n")
a.write("rati - shimla\nayishah - delhi\nraghu - shimla\nnaseer - kanpur\n") 
a.write("karthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\n")
a.write("govind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\n")
a.write("rajeev - shimla\nmohinder - delhi\nrajendra - jaipur\npriyanka - shimla\n")
a.write("neela - delhi\nsashi - jaipur\nsarika - delhi\ndeepti - shimla\nharshad - delhi\n") 
a.write("trishna - raipur\npradeep - jaipur\nsekhar - delhi\nnand - delhi\nanoop - delhi\nbalwinder - tokyo)\n")

a.close()

# a=open("people1-exercise.txt")
# print(a.read())
# a.close()

a=open("people1-exercise.txt")
c=0
for i in a:
    print(i)
    c+=1
print(c)
a.close()