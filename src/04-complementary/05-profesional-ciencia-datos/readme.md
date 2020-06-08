![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/joseluisramon-diploma-data.png)

# Curso Profesional de Data Science

**Prof. Ines Puerta**

# Unidad 1. Introducción

En los 60 existía gente que estaba empleada de como Data Miners, pero cuando los datos se volvieron más grandes el resultado era penoso. Es la evolución del hardware la que permitió que surgiera la Data Sciense 

**¿Qué hace un Data Scientist**

* *Obtención:* Puede ser descargarse una base de datos pero si necesitas hacer relaciones entre grande bases de datos, puede complicarse y necesitas lenguaje nuevo
* *Enriquecimiento:* Puedes enriquecer un set de datos con datos por redes sociales pero tienes que tener una intención, por ejemplo, conseguir un cliente
* *Adecuación e interpretación de datos:* No para todo el mundo los datos tienen el mismo sentido, explicar eso es importante
* *Aplicación del modelo:* A partir de los datos se contruye un modelo y habrá que probarlo.
* *Interpretación de los resultados:* Pues, lo dicho
* *Puesta en producción del modelo:* Al crear una algoritmo, te debería permitir predecir eventos o patrones, para eso está el data scientist

## Introducción a R

R es un lenguaje de programación que permite utilizar técnicas estadísticas a un grupo de datos

 https://cran.r-project.org/ ahí está la página y las librerías

```R
install.packages("spatial"); 	#instalar paquetes
library(spatial)				#activar paquetes
```

### **Funcionalidades Básicas de Calculadora con R**

crear un script calculadora.R y para ejecutarlo, `Ctrl + R`

```R
## Calculadora
# R como calculadora basicas
3-2
# Operadores basicos +-*/^. ()
(1+2)*7
# Para comparaciones == <> <= > = TRUE FALSE
2*2 == 4

## Variables, asignacion mediante <-
valor<-55
valor=56
valor
valor*2
```

### Operaciones de datos

Tipos de datos que se pueden utilizar en R. 

* Vectores: *Arreglo de elementos de un mismo tipo* 

```R
##Vectores
#Un vector es una coleccion de elementos, utilizamos c(elem1, elem2,..., elemN)
c(10,11,15) #declarar vector
mivec<-c(10,11,15) #asignar vector a variable
mivec/2
nuevovec<-mivec+mivec #operar vectores
nuevovec
c(60, nuevovec) #concatenar
#Tipos de vectores
a<-c("hola", "adios") #vector de caracteres
a
b<-c(TRUE, FALSE) #vector de booleanos
b 
#Indexing vector mediante  []
a[1] #seleccionar posicion 1
a[1]<-"caracola"
a
#Creando una serie
c<-c(2:12) #vector con numeros entre 2 a 12
c[1:2]
#Eliminando elementos de un vector "-"
c
c[-4] 		#eliminar numero en posicion 4
c[4]=c[4]-2	#operar sobre una posicion 
```



* Listas: *Arreglo con elementos de tipos diferentes* 

```R
##LISTAS, colecciones de elementos que puede ser diferentes tipos
# Las listas se crean con list() separando campos por comas con clave/valor
# Se indexan con $ o con []
milista<-list(num=42, saludo="Hola Rmundo")
milista$saludo #imprime ese posicion 2.
milista[[1] #imprime 42 posicion 1
```

* Matrices: *Se contruyen a partir de vectores*

```R
##Matrix filas y columnas de datos como tabla todos del mismo tipo
# Las columnas tienen nombre  colnames y las filas rownames
mat<-matrix(c(1,2,2,2,3,2),nrow=2, ncol=3)
mat		#visualizar
rownames(mat)<-c("primera", "ultima")
mat
colnames(mat)<-c("a","b", "c")
mat
#Indexado en matrices [fila, columna]
mat[1,2]	#seleccionar un elemento
```

* Dataframes: *Son tablas de datos que se forman a partir de vectores y permiten visualizar datos en conjunto, permite almacenar diferentes tipos de datos y es la estructura que más se utiliza en R*

```R
##Dataframes son matrices que pueden albergar diferentes tipos de datos en sus columnas
edad <- c(22, 34, 29, 25, 30, 33, 31, 27, 25, 25)
tiempo <- c(14.21, 10.36, 11.89, 13.81, 12.03, 10.99, 12.48, 13.37, 12.29, 11.92)
sexo <- c("M","H","H","M","M","H","M","M","H","H")
#crear data frames
misDatos <- data.frame(edad,tiempo,sexo)
misDatos
dim(misDatos)	#tamano del data frame
str(misDatos)

#Indexando dataframes con [fila, columna] o $columna[fila]
misDatos[,1]	#primera columna
misDatos[5,]	#fila nro 5
misDatos[2,3]	#elementos
colnames(misDatos)
rownames(misDatos)
misDatos[2,3]
misDatos$sexo[2] #columna 'sexo' fila 2
```

Otra de las cosas que es filtrar los datos y presentarlos en un vector. En este caso lo llamaremos 'val'. Este es el proceso:

```R
#filtramos los datos según un criterio y lo guaramos en un vector
dat<-misDatos$tiempo>=12 
# los presentamos
dat
# which nos dice la posicion de los datos que cumplen el criterio indicado
val<-which(dat)
#presentamos el data frame solo con los datos que cumplen
misDatos[val,]

#se puede hacer más compacto, sin necesidad de dat
val<-which(misDatos$edad<=29)
```

* Datos Externos (CSV)

Desde R puedes leer datos en formato comma separated value, para ellos cuentas con ciertas funciones

```R
##Leer/escribir ficheros

#escribe el dataframe de misDatos en una disco
write.csv(misDatos, "/tmp/datos.csv")
#leer y guardar un dato en una variable
mifile<-read.csv("/tmp/datos.csv")
#lanza una ventana de visualización
View(mifile) 

#aqui hay un problema, la fila de sexo no se muestra porque los datos no pueden ser interpretados en un CSV. Para ello, hay que cambiar como están los datos guardados, para que sean caracteres:
misDatos$sexo<-as.character(misDatos$sexo)
#luego escribirlos siguiendo el procedimiento anterior

#tambien se puede leer así
file<-read.csv("/tmp/datos.csv")
head(file) #muestra los primeros

#hay un set de datos para hacer pruebas que puedes utilizar, se llama iris
iris #son datos de flores y petalos
str(iris)
write.csv(iris, "/home/tmp/iris.csv") #asi lo guardo
```

Por ultimo, hay forma de chequear/analizar que tipo de dato es el que hemos creado. 

```R
##Funciones basicas de analisis
class(milista)		#desplega la clase
typeof(milista)		#desplega la clase
str(mivec)	#muestra la estructura de la variable
```

Si en algún momento quieres obtener ayuda en el uso de la funciones de RStudio lo que debes hacer es pulsar *F1*