# banda, dança e dinheiro.
banda = input()
dança = input()
dinheiro = int (input())

# Minha reposta é sim, quando:
Responda = "não"

#if "banda" == "Boa" and "dança" == "boa" and "dinheiro" == 200:
if banda == "boa":
    Responda = "sim"
    print("entrei")
    if dança == "boa":
        Responda = "sim"
        if dinheiro >= 200:
            Responda = "sim"
else:
    Responda = "não"

print("vc vai para a festa: ") 
print(Responda)
