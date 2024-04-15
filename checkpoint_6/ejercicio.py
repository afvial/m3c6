# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:
    def __init__(self, nombre, contraseña):
            self.nombre = nombre
            self.contraseña = contraseña

    def conditional(self):
        if self.nombre == 'André' and self.contraseña == 345:
            return f'¡Bienvenido {self.nombre} a su cuenta de mail!'
        else:
            return f'Nombre de usuario y/o contraseña incorrecta'  

use1 = Usuario('André', 345)
usuario_1 = use1.conditional()


print(usuario_1)
