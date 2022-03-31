persona1=input ("Jugador1: ¿Piedra, papel o tijera?: ")
persona2=input ("Jugador2: ¿Piedra, papel o tijera?: ")

if persona1=="piedra" and persona2=="piedra":
    print("Empate")
elif persona1== "piedra" and persona2== "papel":
    print("Gana el papel")
elif persona1=="piedra" and persona2=="tijera":
    print("Gana jugador1")     
 
elif persona1=="papel" and persona2=="piedra":
    print("Gana jugador2")    
elif persona1=="papel" and persona2=="papel":
    print("Empate")
elif persona1=="papel" and persona2=="tijera":
    print("Gana jugador2")       
     
elif persona1=="tijera" and persona2=="piedra":
    print("Gana jugador2")  
elif persona1=="tijera" and persona2=="papel":
        print("Empate")          
elif persona1=="tijera" and persona2=="tijera":
        print("Empate")              
  
    
       
    
    
                   
