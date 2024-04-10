class Error(Exception):

    pass

class LargoExcedidoError(Error):
    def __init__(self, nombre: str, maximo: int, *args: object) -> None:
   
        super().__init__(*args)
        self.nombre = nombre
        self.maximo = maximo

class SubTipoInvalidoError(Error):
    def __init__(self, sub_tipos: tuple, sub_tipo: str, *args: object) -> None:
      
        super().__init__(*args)
        self.sub_tipos = sub_tipos
        self.sub_tipo = sub_tipo
