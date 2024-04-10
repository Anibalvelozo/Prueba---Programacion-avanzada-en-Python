from datetime import date, datetime
from anuncio import Anuncio, Video, Display, Social
from typing import List, Union
from error import LargoExcedidoError

class Campana():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date, anuncio:dict) -> None:
        
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        
        for formato, datos in anuncio.items():
            if formato == "Video":
                self.__anuncios.append(Video(duracion=datos["duracion"], url_archivo=datos["url_archivo"], url_clic=datos["url_clic"], sub_tipo=datos["sub_tipo"]))
            elif formato == "Display":
                self.__anuncios.append(Display(ancho=datos["ancho"], alto=datos["alto"], url_archivo=datos["url_archivo"], url_clic=datos["url_clic"], sub_tipo=datos["sub_tipo"]))
            elif formato == "Social":
                self.__anuncios.append(Social(ancho=datos["ancho"], alto=datos["alto"], url_archivo=datos["url_archivo"], url_clic=datos["url_clic"], sub_tipo=datos["sub_tipo"]))

    @property
    def nombre(self) -> str:
       
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str) -> None:
       
        if len(nombre) > 250:
            raise LargoExcedidoError(nombre, 250)
        else:
            self.__nombre = nombre
    
    @property
    def fecha_inicio(self) -> date:
        
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:date) -> None:
       
        self.__fecha_inicio = fecha_inicio
    
    @property
    def fecha_termino(self) -> date:
       
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino:date) -> None:
    

        self.__fecha_termino = fecha_termino
    
    @property
    def anuncios(self) -> List[Anuncio]:
   
        return self.__anuncios

    def __str__(self) -> str:
      
        retorno = f"Nombre de la campaña: {self.nombre}\n"
        formatos = (Video, Social, Display)
        cantidad_anuncios = [[sum([1 for anuncio in self.anuncios if isinstance(anuncio, formato)]), formato] for formato in formatos]
        retorno += f"Anuncios: "
        textos_anuncios = []
        for cantidad_anuncio in cantidad_anuncios:
            textos_anuncios.append(f"{cantidad_anuncio[0]} {cantidad_anuncio[1].FORMATO}")
        retorno += ", ".join(textos_anuncios)
        return retorno
