def solucion(asesino):
    asesino = asesino.lower()
    if asesino == "jeremy bowers":
        return print("¡Felicidades, encontraste al asesino! Pero espera, hay más...\n Si crees que estas preparado para un desafío, segui investigando \n la transcripcion del asesino para encontrar al verdadero villano detrás de este crimen")
    elif asesino == "miranda priestly":
        return print("¡Muy bien hecho! Encontraste a la mente detras del asesinato\n Todos en Pandas City te aclaman como el mejor detective de PANDAS de todos los tiempos. ¡Ya es hora de sacar el champagne!")
    else:
        return print("Esa no es la persona correcta. ¡Segui intentando!")