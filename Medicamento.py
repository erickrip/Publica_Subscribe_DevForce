#!/usr/bin/env python

class Medicamento:
    nombre = None
    hora = None
    tomado = None

    def __init__(self, nombre, hora):
        self.nombre = nombre
        self.hora = hora
        self.tomado = False
	

    def get_hora(self):
        return self.hora

    def get_name(self):
        return self.nombre

    def set_tomado(self, cambio):
        self.tomado = cambio

    def get_tomado(self):
        return self.tomado
