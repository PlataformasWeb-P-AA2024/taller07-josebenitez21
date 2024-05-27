from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club 
clubs = {}
with open('../ejemplo02/data/datos_clubs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nombre, deporte, fundacion = line.strip().split(';')
        fundacion = int(fundacion)
        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        session.add(club)
        clubs[nombre] = club


# Leer datos de jugadores desde el archivo
with open('../ejemplo02/data/datos_jugadores.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nombre_club, posicion, dorsal, nombre = line.strip().split(';')
        dorsal = int(dorsal)
        club = clubs.get(nombre_club)
        if club:
            # Crear el jugador y asignar el club utilizando la relación
            jugador = Jugador(nombre=nombre, dorsal=dorsal, posicion=posicion, club=club)
            session.add(jugador)




session.commit()
