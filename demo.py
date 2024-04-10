from campana import Campana
from datetime import datetime
from error import SubTipoInvalidoError, LargoExcedidoError

# Inicio de un diccionario con los datos necesarios para un anuncio de tipo video
anuncio_dict = {"duracion": 50, "url_archivo": "direccion.com", "url_clic": "direccion.cl", "sub_tipo": "instream"}
# Creacion de la camapaña
super_campana = Campana(nombre="Super Campana", fecha_inicio=datetime.now(), fecha_termino=datetime.now(), anuncio=anuncio_dict)

# Prueba de funcionamiento
print(super_campana)

try:
    # Se intenta cambiar el sub tipo
    sub_tipo = input("Introduzca el nuevo sub tipo para el anuncio\n\n")
    super_campana.anuncios[0].sub_tipo = sub_tipo
except SubTipoInvalidoError as e:
    # Si falla por sub tipo se guarda el error en un log
    with open("error.log", "a+", encoding="utf-8") as log:
        log.write(f"El sub tipo {e.sub_tipo} no es un valor válido para este tipo de anuncio, solo pueden ser {e.sub_tipos}\n")
        log.close()
except Exception as e:
    with open("error.log", "a+", encoding="utf-8") as log:
        log.write(f"{e.__str__()}\n")
        log.close()

try:
    # Se intenta cambiar el nombre de la campaña
    nombre = input("Introduzca el nuevo nombre de la campaña\n\n")
    super_campana.nombre = nombre
except LargoExcedidoError as e:
    # Si falla por el máximo de caracteres se guarda el error en un log
    with open("error.log", "a+", encoding="utf-8") as log:
        log.write(f"El nombre {e.nombre} no es un valor válido para el nombre de campaña, el máximo de caracteres es {e.maximo}\n")
        log.close()
except Exception as e:
    with open("error.log", "a+", encoding="utf-8") as log:
        log.write(f"{e.__str__()}\n")
        log.close()

print(super_campana)
