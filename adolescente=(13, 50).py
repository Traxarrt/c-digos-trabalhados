adulto=(19, 49)
idoso=(50, 100)
adolescente=(13, 18)
criança=(0, 12)
paulo=int(input("idade de paulo"))
if paulo >= criança[0] and paulo <= criança[1]:
    print("paulo será uma criança")
elif paulo >= adolescente[0] and paulo <= adolescente [1]:
    print("Paulo será um adolescente")
elif paulo >= adulto[0] and paulo <= adulto[1]:
    print("Paulo será um adulto")
elif paulo >= idoso[0] and paulo <= idoso[1]:
    print("Paulo será um idoso")