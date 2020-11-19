from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Hospital

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase3.db') 

Session = sessionmaker(bind=engine)
session = Session()

h1 = Hospital(nombre="Isidro Ayora", numero_camas=100, \
        numero_pisos=10, ciudad="Loja", provincia="Loja")

h2 = Hospital(nombre="Andrade Marín", numero_camas=200, \
        numero_pisos=20, ciudad="Quito", provincia="Pichincha")

h3 = Hospital(nombre="Machala", numero_camas=80, \
        numero_pisos=8, ciudad="Machala", provincia="El Oro")

h4 = Hospital(nombre="Luis Vernaza", numero_camas=80, \
        numero_pisos=10, ciudad="Guayaquil", provincia="Guayas")
# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos
session.add(h1)
session.add(h2)
session.add(h3)
session.add(h4)

