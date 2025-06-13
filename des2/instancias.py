from te import Te


te1=Te()
te2=Te()


tipo1=type(te1)
tipo2=type(te2)



print(tipo1)
print(tipo2)

if tipo1==tipo2:
    print("ambos objetos son del mismo tipo")

else:
    print("los objetos no son del mismo tipo")
