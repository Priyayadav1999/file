a=open("question3.txt","w")
a.write("rishabh - meerut\nimtiyaz - delhi \nnilima - cochin\nrati - shimla\nayishah - delhi\nraghu - shimla\n") 
a.write("naseer - kanpur\nkarthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\n") 
a.write("govind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\nrajeev - shimla\n")
a.write("mohinder - delhi\nrajendra - jaipur\npriyanka - shimla\nneela - delhi\nsashi - jaipur\n") 
a.write("sarika - delhi\ndeepti - shimla\nharshad - delhi\ntrishna - raipur\npradeep - jaipur\n")
a.write("sekhar - delhi\nnand - delhi\nanoop - delhi\nbalwinder - tokyo\n" )

a.close()

a=open("question3.txt")
k=open("delhi.txt","w")
p=open("shimla.txt","w")
q=open("others.txt","w")

for i in a:
    if "delhi" in i:
        # k=open("delhi.txt","w")
        k.write(i)
        k.write("\n")
    elif "shimla" in i:
        # p=open("shimla.txt","w")
        p.write(i)
        p.write("\n")
    else:
        # q=open("others.txt","w")
        q.write(i)
        q.write("\n")

a.close()
p.close()
q.close()
k.close()