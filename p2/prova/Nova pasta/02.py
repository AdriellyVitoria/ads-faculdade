#recebe como entrada dois inteiros positivos (largura e altura) 
largura, altura = map (int, input ().split ())

giros = base = 0 #contadores para parar os dois while
while giros < largura: #enquando giros for menor q largura
  giros += 1 #aumento no contador
  while base < altura: #só quero q saia até o tamanho da altura 
    print ('#' * largura) #saida
    base += 1 #aumento no contador 

#Adrielly Vitoria
