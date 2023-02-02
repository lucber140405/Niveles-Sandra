a= int(input("dime un numero (del uno al doce)"))
import random
numero = random.randint(1, 12)
if numero == 1:
  answer = 'enero'
elif numero == 2:
    answer="febrero"
elif numero== 3:
  answer = 'marzo'
elif numero == 4:
  answer = 'abril'
elif numero == 5:
  answer = 'mayo'
elif numero == 6:
  answer = 'junio'
elif numero == 7:
  answer = 'julio'
elif numero == 8:
  answer = 'agosto'
elif numero == 9:
  answer = 'septiembre'
elif numero == 10:
  answer = 'octubre'
elif numero == 11:
  answer = 'noviembre'
elif numero ==12:
    answer= 'diciembre'
print(answer)