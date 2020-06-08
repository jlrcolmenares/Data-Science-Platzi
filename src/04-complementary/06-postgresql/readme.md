![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/joseluisramon-diploma-postgresql.png)

# Curso de PostgreSQL

**Prof. Oswaldo Rodriguez Gonzales** 

# Unidad 1. Configurar Postgres

##  ¿Qué es PostgreSQL? 

Postgres es un **motor de bases de datos** que afirma ser la base de datos relacional más poderosa del mundo. Cuando hablamos de bases de datos hay varios conceptos importantes:

* Base de Datos: Es la información a la que accedes usando lenguaje SQL
* Motor: Es el que permite estructurar toda la información dentro de un servidor
* Servidor: Es el equipo que tiene una ram y un procesador, donde tu instalas la base de datos

Postgres es Base de Datos creada en 1986 en la University of California at Berkeley. Ésta base de datos es:

1. **Open Source:** una comunidad la mantiene y agregar funciones a su núcleo
2. **Usa Objeto-Relacional en las RDB:** Las bases de datos tiene una estructura como la del desarrollo orientada objetos en la que tengas herencias e interfaces. Una estructura en la cual las bases puedan relacionarse en torno a una información congruente
3. **Utilizar servicios de PostGIS o PL/PgSQL**: PostGIS es un servicios de localización con respecto a mapas, el cual te hace independiente de software de terceros (ESRI). PL/PgSQL puedes desarrollar código usando el lenguaje de postgres para no depender de backend
4. **Cumple estandar ==ACID==** de buenas prácticas para las bases de datos que se refiere a:
   1. **A**tomicity (Atomicidad): Tu puedes separa las funciones que estás desarrollando las funciones de la bases de datos en tareas más pequeñas. Cuando ejecutas las pequeñas tareas y terminan bien todas se valida, se autoriza los cambios. En caso contrario se hace rollback y se desahacen todos los cambios parciales. Esto no era posible en las bases de datos antiguas
   2. **C**onsistency (Consistencia): Todo lo que se desarrolla entorno al objeto relacional (llaves primarias, secundarias,etc) tienen una relacion entre si
   3. **I**solation (Aislamiento): Puedes tener varias tareas relaizándose en una base de datos (consultas, modificaciones, etc)
   4. **D**urabilidy (Durabilidad): La información no se va a perder en caso de una fallo catastrófico. Postgres guarda la información en una bitácora y luego la mueve a la base de datos

Existe otro estándar que puede ser interesante para las bases de datos. El estándar [CAP](https://platzi.com/blog/que-es-el-teorema-cap-y-como-elegir-la-base-de-datos-para-tu-proyecto/)

### Ventajas de Postgres

Es OpenSource. Airbnb, Uber, Netflix empezaron así, empresas así de grandes siguen apoyando el proyecto de posgres. Si queremos enumerar algunas de las ventajas de posgres serían

* Tipos de Datos
* Integridad de datos
* Concurrencia. Rendimiento
* Fiabilidad (recuperación ante desastres)
* Seguridad
* Extensibilidad
* Internazionalización. Búsqueda de texto