# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
asteroid_diameter = 40
asteroid_speed = 20
# Para probar el código, prueba con varias velocidades y tamaños
if ((asteroid_diameter > 25 or asteroid_diameter < 1000) and (asteroid_speed > 25)):
    print('Warning. The asteroid is approaching at high speed');
elif asteroid_speed >= 20:
    print('Look up! see the asteroid ') 
else:
    print('Nothing to see here :)')