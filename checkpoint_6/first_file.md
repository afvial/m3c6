## Checkpoint 6

### ¿Para qué usamos Clases en Python?

Una clase en Python es una plantilla para crear objetos, y es una de las formas en que se pueden implementar programación orientada a objetos (POO) en Python. Las clases contienen atributos (datos o estado) y métodos (funciones o comportamiento) que se aplican a objetos específicos creados a partir de la clase.

Un objeto es una instancia de una clase en programación orientada a objetos (POO). Un objeto es una entidad única que tiene atributos (datos o estado) y métodos (funciones o comportamiento) que le permiten interactuar con otros objetos y realizar tareas específicas. Los objetos se crean a partir de clases y pueden ser modificados y manipulados de acuerdo con las reglas y características definidas por su clase. En resumen, un objeto es una representación concreta de una clase.

#### ¿Que ventajas tienen las clases en Python?

Las clases en Python ofrecen varias ventajas, incluyendo:
<ul>
<li>Abstracción: las clases permiten encapsular y ocultar la complejidad detrás de una interfaz simplificada y fácil de usar.</li>
<li>Reutilización de código: los objetos pueden ser creados a partir de una misma clase, lo que permite reutilizar y compartir el código de la clase en diferentes partes de un programa.</li>
<li>Organización: las clases ayudan a organizar y estructurar el código de una manera lógica y coherente.
Mantenibilidad: las clases hacen que sea más fácil mantener y mejorar el código a medida que evoluciona un programa.</li>
<li>Programación orientada a objetos: las clases son la base de la programación orientada a objetos (POO), un paradigma de programación que se centra en la representación de los objetos y sus interacciones para resolver problemas y modelar sistemas complejos.</li>
</ul>

#### Y ¿cuales son los inconvenientes?

Pero no todo son ventajas, también te puedes encontrar algunos inconvenientes. Aunque las clases ofrecen muchas ventajas, también existen algunos inconvenientes, incluyendo:

<ul>
<li>Complejidad: las clases pueden ser más complejas y difíciles de entender para programadores principiantes o para aquellos que no están familiarizados con la programación orientada a objetos.</li>
<li>Overhead: el uso de clases puede requerir más tiempo y recursos que otras formas de programación, especialmente si se usan en exceso.</li>
<li>Dificultad para depurar: debido a la complejidad y la estructura de las clases, puede ser más difícil depurar y solucionar errores en el código.</li>
<li>Restricciones: el uso de clases puede ser más limitante que otras formas de programación y no siempre es la mejor opción para resolver todos los problemas.</li>
<li>Es importante tener en cuenta que estos inconvenientes dependen del contexto y la aplicación específicos, y que las clases siguen siendo una herramienta poderosa y ampliamente utilizada en la programación de Python y otros lenguajes de programación.</li>
</ul>

#### Un ejemplo de clase en Python

Veamos el siguiente ejemplo de una clase en Python.

````
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Guau!")

perro = Perro("Niebla", "Mastín")
print(perro.nombre)
print(perro.raza)
perro.ladrar()
````

En este ejemplo, se define una clase llamada ``Perro`` que tiene dos atributos, ``nombre`` y ``raza``, y un método, ``ladrar``. Luego se crea un objeto ``perro`` a partir de esta clase y se accede a sus atributos y métodos. 

Como se ve, una clase en Python consiste generalmente en las siguientes partes:
<ul>
    <li>Nombre de la clase: es el nombre que se le da a la clase y que se usa para crear objetos a partir de ella.</li>
    <li>Método __init__: es un método especial que se llama automáticamente cuando se crea un objeto a partir de una clase. Este método se usa para inicializar los atributos del objeto.
    Atributos: son las variables o valores que definen el estado de un objeto.
    <li>Métodos: son las funciones que definen el comportamiento de un objeto y que permiten interactuar con otros objetos y realizar tareas específicas.</li>
</ul>

Estas son las partes principales de una clase en Python, aunque también existen otras partes como los métodos especiales, las propiedades, los métodos estáticos y las clases anidadas. Sin embargo, la estructura básica de una clase es la descrita anteriormente.


### ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

El método ``__init__`` es un método especial (también llamado método dunder) en Python que se utiliza para inicializar una instancia de una clase. Cuando se crea una instancia de una clase, el método ``__init__`` es llamado automáticamente por el intérprete de Python y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

El método ``__init__`` se usa para asignar valores iniciales a los atributos de una instancia de la clase. Los atributos son las variables que pertenecen a una instancia particular de la clase. Al llamar al método ``__init__``, podemos establecer los valores de estos atributos y configurar la instancia de la clase para su uso posterior.

````
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
````

En este ejemplo, el método ``__init__`` toma dos parámetros: nombre y edad. Estos se utilizan para inicializar los atributos nombre y edad de la instancia de la clase.

Al crear una instancia de la clase Persona, se debe proporcionar un valor para cada uno de los parámetros nombre y edad, como en el siguiente ejemplo:

````
persona1 = persona('Juan', 30)
````



### ¿Cuáles son los tres verbos de API?

API es el acrónimo de interfaz de programación de aplicaciones (*application programming interface* en inglés). Es un conjunto de reglas bien definidas que se utilizan para especificar formalmente la comunicación entre dos componentes de software. 

En la actualidad existen distintas clases de API, pero en este caso nos enfocaremos un poco más en las API REST (ya que son ellas las que tienen relación con la pregunta). 

Una API REST es una interfaz de comunicación entre sistemas de información que usa el protocolo de transferencia de hipertexto (hypertext transfer protocol o HTTP, por su siglas en inglés) para obtener datos o ejecutar operaciones sobre dichos datos en diversos formatos, como pueden ser XML o JSON.

Se basa en el **modelo cliente-servidor** donde el cliente es el que solicita obtener los recursos o realizar alguna operación sobre dichos datos, mientras que el servidor es aquel ente que entrega o procesa dichos datos a solicitud del cliente.

#### Criterios de API REST
Existen diversos criterios para identificar si una API es REST o no. Algunos de ellos son que:
<ul>
    <li>Debe usar una arquitectura cliente-servidor.</li>
    <li>Las ejecuciones de la API no deben considerar el estado del cliente, el estado de peticiones anteriores o algún indicador almacenado que haga variar su comportamiento. La comunicación debe ser sin estado (stateless).</li>
    <li>Ha de estar orientada a recursos, usando las operaciones estándar de los verbos HTTP.
    Hace uso de la URL como identificador único de los recursos.</li>
    <li>Debe ser hipermedia: cuando se consulte un recurso, este debe contener links o hipervínculos de acciones o recursos que lo complementen.</li>
</ul>

#### Verbo HTTP
Son aquellos verbos propios del protocolo HTTP que fueron tomados para definir operaciones muy puntuales y específicas sobre los recursos de la API.

Los más utilizados son los tres primeros:
<ul>
<li>GET: listado de recursos. Detalle de un solo recurso.</li>
<li>POST: creación de un recurso.</li>
<li>PUT: modificación total de un recurso.</li>
<li>PATCH: modificación parcial de un recurso.</li>
<li>DELETE: eliminación de un recurso. En muchas ocasiones es un soft delete, es decir, no se elimina definitivamente un recurso sino que únicamente es marcado como eliminado o desactivado.</li>
</ul>

### ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es un sistema de base de datos NoSQL, orientado a documentos y de código abierto.

En informática, NoSQL (a veces llamado "no solo SQL") es una amplia clase de sistemas de gestión de bases de datos que difieren del modelo clásico de SGBDR (Sistema de Gestión de Bases de Datos Relacionales) en aspectos importantes, siendo el más destacado que no usan SQL como lenguaje principal de consultas. Los datos almacenados no requieren estructuras fijas como tablas, normalmente no soportan operaciones JOIN, ni garantizan completamente ACID (atomicidad, consistencia, aislamiento y durabilidad) y habitualmente escalan bien horizontalmente.

En lugar de guardar los datos en tablas, tal y como se hace en las bases de datos relacionales, MongoDB guarda estructuras de datos BSON (una especificación similar a JSON) con un esquema dinámico, haciendo que la integración de los datos en ciertas aplicaciones sea más fácil y rápida.

### ¿Qué es una API?

Las API o interfaz de programación de aplicaciones son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.

#### ¿Cómo funcionan las API?

La arquitectura de las API suele explicarse en términos de cliente y servidor. La aplicación que envía la solicitud se llama cliente, y la que envía la respuesta se llama servidor. En el ejemplo del tiempo, la base de datos meteorológicos del instituto es el servidor y la aplicación móvil es el cliente.

Las API permiten que sus productos y servicios se comuniquen con otros, sin necesidad de saber cómo están implementados. Esto simplifica el desarrollo de las aplicaciones y permite ahorrar tiempo y dinero. Las API le otorgan flexibilidad; simplifican el diseño, la administración y el uso de las aplicaciones; y ofrecen oportunidades de innovación, lo cual es ideal al momento de diseñar herramientas y productos nuevos (o de gestionar los actuales).

#### Las API remotas
Las API remotas están diseñadas para interactuar en una red de comunicaciones. La palabra remota indica que los recursos que administra la API se encuentran fuera de la computadora que envía la solicitud. Dado que la red de comunicaciones más usada es Internet, la mayoría de las API están diseñadas de acuerdo con los estándares web. No todas las API remotas son API web, pero se puede suponer que las API web son remotas.

Por lo general, las API web usan HTTP para los mensajes de solicitud y proporcionan una definición de la estructura de los mensajes de respuesta. Estos mensajes suelen tomar la forma de un archivo XML o JSON, que son los formatos preferidos porque presentan los datos en una manera que otras aplicaciones pueden manejar con facilidad.

#### Diferencias entre SOAP y REST
A medida que se ha difundido el uso de las API, se desarrolló una especificación de protocolo para permitir la estandarización del intercambio de información; se llama Protocolo de Acceso a Objetos Simples, más conocido como SOAP. Las API diseñadas con SOAP usan XML para el formato de sus mensajes y reciben solicitudes a través de HTTP o SMTP. Con SOAP, es más fácil que las aplicaciones que funcionan en entornos distintos o están escritas en diferentes lenguajes compartan información.

Otra especificación es la Transferencia de Estado Representacional (REST). Las API web que funcionan con las limitaciones de arquitectura REST se llaman API de RESTful. La diferencia entre REST y SOAP es básica: SOAP es un protocolo, mientras que REST es un estilo de arquitectura. Las API son RESTful siempre que cumplan con las 6 limitaciones principales de un sistema RESTful:

<ul>
    <li> Arquitectura cliente-servidor: la arquitectura REST está compuesta por clientes, servidores y recursos; y administra las solicitudes con HTTP.</li>
    <li>Sistema sin estado: el contenido de los clientes no se almacena en el servidor entre las solicitudes. En su lugar, la información sobre el estado de la sesión está en posesión del cliente.</li>
    <li>Capacidad de almacenamiento en caché: el almacenamiento en caché elimina la necesidad de algunas interacciones cliente-servidor.</li>
    <li>Sistema en capas: las interacciones cliente-servidor pueden estar mediadas por capas adicionales. Estas capas pueden ofrecer funcionalidades adicionales, como equilibrio de carga, cachés compartidos o seguridad.</li>
    <li>Disponibilidad del código según se solicite (opcional): los servidores pueden ampliar las funciones de un cliente transfiriendo código ejecutable.</li>
    <li>Interfaz uniforme: esta limitación es fundamental para el diseño de las API de RESTful e incluye cuatro aspectos:
    <ul>
        <li>Identificación de los recursos en las solicitudes: se identifican los recursos en las solicitudes y se separan de las representaciones que se envían al cliente.</li>
        <li>Administración de los recursos mediante representaciones: los clientes reciben archivos que representan los recursos. Estas representaciones deben tener la información suficiente como para poder ser modificadas o eliminadas.</li>
        <li>Mensajes autodescriptivos: cada mensaje que se envía al cliente contiene una descripción clara sobre la manera en que debe procesar la información.</li>
        <li>Hipermedios como el motor del estado de la aplicación: es necesario que después de que el cliente REST acceda a un recurso, pueda descubrir todas las otras acciones que están disponibles actualmente mediante hipervínculos.</li>
    </ul>
    </li>    
</ul>

Estas limitaciones pueden parecer demasiadas, pero son mucho más sencillas que un protocolo definido previamente. Por eso, las API de RESTful son cada vez más frecuentes que las de SOAP.

### ¿Qué es Postman?

Postman es una aplicación especialmente útil en el desarrollo web y de apps móviles que se comunican con servicios web a través de APIs.

#### Postman qué es y para qué sirve
Postman es una **herramienta de colaboración y desarrollo que permite a los desarrolladores interactuar y probar el funcionamiento de servicios web y aplicaciones**, proporcionando una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuestas correspondientes.

Con esta plataforma se puede gestionar diferentes entornos de desarrollo, organizar las solicitudes en colecciones y realizar pruebas automatizadas para verificar el comportamiento de los sistemas.

Postman es utilizado por los desarrolladores para **testear colecciones y catálogos APIs** (tanto a nivel *front-end* como *back-end*), para gestionar el ciclo de vida de las APIs, mejorar el trabajo colaborativo y mejorar la organización del proceso de diseño y desarrollo.

#### Cómo funciona Postman
Este entorno ofrece una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y a gestionar las respuestas recibidas.

Las principales características y funcionalidades de Postman son:

<ul>
    <li>Envío de solicitudes. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.</li>
    <li>Gestión de entornos. Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).</li>
    <li>Colecciones de solicitudes. Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.</li>
    <li>Pruebas automatizadas. Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).</li>
    <li>Documentación de API. Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.</li>
</ul>

#### Cuáles son sus ventajas respecto a otras herramientas

Cada vez son más los desarrolladores y programadores que apuestan por un entorno como Postman para automatizar pruebas y mejorar sus procesos de trabajo. Los principales beneficios que se obtienen con esta herramienta son:

<ul>
    <li>Facilidad a la hora de trabajar al disponer de una interfaz gráfica de usuario intuitiva, sencilla y personalizable.</li>
    <li>Amplia compatibilidad con numerosas tecnologías y protocolos web, como por ejemplo; HTTP, HTTPS, REST, SOAP, GraphQL… (lo que permite interaccionar con diversos tipos de API sin complicaciones o problemas).</li>
    <li>Ofrece una amplia gama de funcionalidades para diseñar, probar y documentar APIs, siendo probablemente la solución más completa del mercado para gestionar el ciclo de vida completo de desarrollo de APIs.</li>
    <li>Fomenta y facilita la colaboración entre los miembros del equipo de desarrollo (con opciones interesantes como compartir colecciones de solicitudes con otros desarrolladores).</li>
    <li>Cuenta con una comunidad amplia de usuarios que está en constante crecimiento y que aporta una gran cantidad de recursos, como tutoriales, documentación, foros y grupos de discusión.</li>
    <li>Se integra perfectamente con varias herramientas populares utilizadas en el desarrollo de software. Por ejemplo, se puede conectar con sistemas de control de versiones como GitHub, servicios de generación de documentación como Swagger o herramientas de automatización de pruebas como Jenkins, entre muchas otras.</li>
    <li>Permite a los usuarios agregar scripts personalizados utilizando JavaScript (para automatizar tareas repetitivas, configurar pruebas avanzadas o agregar validaciones personalizadas a las respuestas de la API).</li>
    <li>Las colecciones son una característica central de Postman que permite organizar y agrupar solicitudes relacionadas. Esto simplifica la administración de API complejas y facilita la reutilización de solicitudes y flujos de trabajo en diferentes proyectos.</li>
</ul>

### ¿Qué es el polimorfismo?

La palabra "polimorfismo" significa "muchas formas" y en programación se refiere a métodos/funciones/operadores con el mismo nombre que se pueden ejecutar en muchos objetos o clases.

#### Polimorfismo de función

Un ejemplo de una función de Python que se puede utilizar en diferentes objetos es la función ``len()``.

##### String / Cadena
Para cadenas ``len()`` devuelve el número de caracteres:

````
x = "Hello World!"

print(len(x))
````

##### Tuple / Tupla
Para tuplas, ``len()`` devuelve el número de elementos de la tupla:

````
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
````

##### Dictionary / Diccionario
Para diccionarios, ``len()`` devuelve el número de pares clave/valor en el diccionario:

````
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
````

#### Polimorfismo de clase
El polimorfismo se usa a menudo en métodos de clase, donde podemos tener varias clases con el mismo nombre de método.

Por ejemplo, digamos que tenemos tres clases: ``Car``, ``Boat`` y ``Plane``, y todos tienen un método llamado ``move()``:

````
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Crear una clase de Car
boat1 = Boat("Ibiza", "Touring 20") #Crear una clase de Boat
plane1 = Plane("Boeing", "747")     #Crear una clase de Plane

for x in (car1, boat1, plane1):
  x.move()
````

### ¿Qué es un método dunder?

Los métodos **mágicos** o **dunder** son métodos de Python que definen cómo se comportan los objetos de Python cuando se realizan operaciones comunes sobre ellos. Estos métodos se definen claramente con guiones bajos dobles antes y después del nombre del método. Un método común de dunder es el ``__init__()``; el que se utiliza para definir constructores de clases.

#### ¿Por qué son útiles los métodos mágicos?

Los métodos mágicos son un concepto *útil* en la Programación Orientada a Objetos (OOP) en Python. Usándolos, usted especifica el comportamiento de sus tipos de datos personalizados cuando se usan con operaciones integradas comunes. Estas operaciones incluyen: 

<ul>
    <li>Operaciones aritméticas</li>
    <li>Operaciones de comparación</li>
    <li>Operaciones de ciclo de vida</li>
    <li>Operaciones de representación</li>
</ul>

#### Cómo definir métodos mágicos

Como se mencionó anteriormente, los métodos dunder o mágicos especifican el comportamiento de los objetos. Como tales, se definen como parte de la clase del objeto. Como son parte de la clase de objeto, toman como primer argumento ``self``.

Pueden tomar argumentos adicionales dependiendo de cómo los llamará el intérprete. También se definen claramente con dos guiones bajos antes y después de sus nombres.

#### Implementación

Gran parte de lo que hemos discutido hasta ahora parece teórico y abstracto. A continuación, a modo de aplicación de los conceptos vistos, crearemos una clase llamada ``Rectangle``.

Esta clase tendrá distintas propiedades y métodos. Usando el método ``__init__``, podemos especificar estas propiedades al crear instancias. Además, compararemos diferentes rectángulos para ver si son iguales, menores o mayores, usando los operadores ``==``, ``<`` y ``>``. Por último, el rectángulo debe ser capaz de proporcionar una representación de cadena significativa.

##### Crear la clase ``Rectangle``

Primero, comecemos definiendo la clase Rectangle.

```
class Rectangle:
    pass
```

##### Creando el Método Constructor

A continuación, creamos nuestro primer método mágico, el método constructor de clases. Este método tomará el alto y el ancho, y los almacenará como atributos en la instancia de clase.

````
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
````

##### Creación de un método mágico para la representación de cadenas

A continuación, queremos crear un método que permita a nuestra clase generar una cadena legible por humanos para representar el objeto. Este método será llamado siempre que llamemos la función ``str()`` al pasar una instancia de la clase ``Rectangle`` como argumento. Dicho método se llamará también cuando se llame a funciones que esperan un argumento de cadena, como en el caso de la finmción ``print''.

````
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle({self.height}, {self.width})'
````

### ¿Qué es un decorador de python?

Los *decoradores* son una funcionalidad relativamente importante en Python. Se podría decir que son funciones que modifican la funcionalidad de otras funciones, y ayudan a hacer nuestro código más corto y Pythonic. A continuación veremos lo que son, cómo se crean y cómo podemos usarlos.

#### Todo es un objeto en Python

Antes de entrar en materia con los decoradores, vamos a entender bien las funciones.

````
def hola(nombre="Covadonga"):
    return "Hola " + nombre

print(hola())
# Salida: 'Hola Covadonga'
````
Podemos ahora asignar una variable a nustra función:

````
saluda = hola
````

Aquello implica lo siguiente:

````
print(saluda())
Salida: 'Hola Covadonga'
````

Es decir, obtenermos el mismo resultado en ambos casos.

#### Definir funciones dentro de funciones
En Python podemos definir funciones dentro de otras funciones. Veamos un ejemplo:

````
def hola(nombre="Covadonga"):
    print("Estás dentro de la función hola()")

    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    print(saluda())
    print(bienvenida())
    print("De vuelta a la función hola()")

hola()

Salida: Estas dentro de la función hola()
        Estás dentro de la función saluda()
        Estás dentro de la función bienvenida()
        De vuelta a la función hola()

````

Este ejemplo demuestra que cada vez que llamamos a la función ``hola()``, llamamos también a las funciones ``saluda()`` y ``bienvenida()``.

Ahora bien, es importante recalcar que las funciones *subyacentes*, para llamarlas de algun modo, no son accesibles fuera de la función principal (en este caso ``hola()``). Si intentamos llamar a una, obtendremos un error.

````
saluda()
Salida: NameError: name 'saluda' is not defined
````

Dichas funciones se conocen como funciones anidadas. Pero para entender bien los decoradores, necesitamos ir un paso más allá. Las funciones también pueden devolver otras funciones.

#### Devolviendo funciones desde funciones

En el siguiente ejemplo, vemos que *no* es necesario ejecutar la función que se encuentra dentro de la otra; podemos simplemente devolverla como salida.

````
def hola(nombre="Covadonga"):
    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    if nombre == "Covadonga":
        return saluda
    else:
        return bienvenida

a = hola()
print(a)

#Salida: <function hola.<locals>.saluda at 0x000001D2F529A020>
````
Ahora bien, en el caso que queramos ejecutar la función subyacente es necesario que que coloquemos paréntesis al final de la función.

````
print(a())

#Salida: Estás dentro de la función saluda()
````

#### Usando funciones como argumento de otras

Por último, podemos hacer que una función tenga a otra como entrada y que además la ejecute dentro de sí misma. En el siguiente ejemplo podemos ver como ``hazEstoAntesDeHola()`` es una función que de alguna forma encapsula a la función que se le pase como parámetro, añadiendo una determinada funcionalidad. En este ejemplo simplemente imprimimos algo por pantalla antes de llamar a la función.

````
def hola():
    return "¡Hola!"

def hazEstoAntesDeHola(func):
    print("Hacer algo antes de llamar a func")
    print(func())

hazEstoAntesDeHola(hola)

Salida: Hacer algo antes de llamar a func
        ¡Hola!
````

Los decoradores son funciones que decoran a otras funciones, pudiendo ejecutar código antes y después de la función que está siendo decorada.

#### Primer decorador
En el ejemplo anterior ya vimos cómo crear un decorador. Ahora vamos a modificarlo y hacerlo un poco realista.

````
def nuevo_decorador(a_func):

    def envuelveLaFuncion():
        print("Haciendo algo antes de llamar a a_func()")

        a_func()

        print("Haciendo algo después de llamar a a_func()")

    return envuelveLaFuncion

def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

funcion_a_decorar()
Salida: "Soy la función que necesita ser decorada"

funcion_a_decorar = nuevo_decorador(funcion_a_decorar)

funcion_a_decorar()
Salida: Haciendo algo antes de llamar a a_func()
        Soy la función que necesita ser decorada
        Haciendo algo después de llamar a a_func()
````

Así es exactamente como funcionan los decoradores en Python; envuelven una función para modificar su comportamiento de una manera determinada.

Ahora bien, a menudo se usa el signo ``@`` en el código. Esto es debido a que ``@`` es simplemente una forma de hacerlo más corto, pero ambas opciones son perfectamente válidas.

````
@nuevo_decorador
def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

funcion_a_decorar()
Salida: Haciendo algo antes de llamar a a_func()
        Soy la función que necesita ser decorada
        Haciendo algo después de llamar a a_func()
````

El uso de @nuevo_decorador es simplemente una forma acortada de hacer lo siguiente:

````
funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
````