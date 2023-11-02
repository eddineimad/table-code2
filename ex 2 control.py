def communication_du_mois(minute):
    t = []
    t.append(minute*2)
    a1 = minute - 30
    if a1 >= 0 :
        b1 = 20 + a1 * 1.5
        t.append(b1)
    else :
        t.append(20)
    a2 = minute - 60
    if a2 >= 0 :
        b2 = 50 + a2 * 1.5
        t.append(b2)
    else :
        t.append(50)
    a3 = minute - 120
    if a3 >= 0 :
        b3 = 100 + a3 * 1.5
        t.append(b3)
    else :
        t.append(100)
    return t
minute = int(input("enter the number of hours :"))
m = int(input("enter the number of minutes :"))
minute = minute * 60 + m
print("Given the time you enter, we have four plans for you :")
tab = communication_du_mois(minute)
tab2 = [0,20,50,100]
for i in range (4):
    print("Plan ",i+1," has an amount of ",tab[i],"MAD","if you subscribe by :",tab2[i],"MAD")
for i in range(4):
    for j in range(i+1,4):
        if tab[j] < tab[i]:
            min = tab[j]
print("the best for you is the plan when you well pay :",min,"MAD")
print("the last plan that we think is the best for everyone you will pay 200 MAD and you'll get infinity time to speak")