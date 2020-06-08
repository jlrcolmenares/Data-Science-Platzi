![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/diploma-expresiones-regulares.png)

# Curso de Expresiones Regulares

**Prof. Alberto Alcocer**

# Unidad 1. Introducción

## ¿Qué son la RegEx?

Las expresiones regulares son patrones de caracteres que te permiten ir seleccionando o descartando datos en un archivo de texto como por ejemplo csv, o en una línea o un input, según coincidan o nó con este patrón.

# Unidad 3. Ejemplos prácticos

Todos los ejemplos que se muestra en esta sección se pueden probar en el archivo liners.txt que está en este repo

### LOGS

Dentro de un LOG pueden ocurrir un montón de eventos asociados a distintos usuarios, para diferenciar entre ellos, se puedes utilizar expresiones como las siguientes:

* `^\[LOG.*\[LOG\].*user:@beco\] .*$` - Empieza en log, es un log y está hecho por un usuario específico

* `^\[LOG.*\[WARN\].*$`  - 

### Teléfonos

Lo teléfonos en Mexico tienen un formato bien particular, por pausas y otras cosas. A continuación algunos ejemplo:

* `^\+?\d+[#pe]\d*$ ` - toma las lineas que comiencen con el símbolo +, luego toma todos los digitos, si están interrumpidos entre [#pe]. Por ultimo toma los digitos restantes
* `^\+?\d{2,3}[^\da-z]?d{2,3}[^\da-z]?\d{2,3}$` - Tomar todas las expresiones que contengan o no +, seguido por 2o 3 digitos, seguidos luego por todas las cosas que NO sean digitos ni a-z.... luego repites la expresión tantasa veces sea necesario

### URLs

Es uno de los uso más comunes cuando quieras buscar algo dentro de un documentos HTML

* `https?:\/\/[\w\-.]+` - Esto nos permite seleccionar hasta el primer / dentro de las direcciones web
* `https?:\/\/[\w\-.]+\.\w{2,5}\/?\S*` - Esto nos permitiría seleccionar lo mismo que antes pero dejando del TRD por separado y luego seleccionando hasta el final de la línea

### Emails

Filtra el tipo de email tambien se utiliza frecuentemente en frontend. Para estar seguro que dentro de un Form el correo que estás ingresando sea correcto

* `^[\w\._]{2,30}[\+\-\.]?[\w]{0,20}@\w{2,30}\.[\w]{2,10}$` - Esto nos permite direcciones que estén interrumpidas por símbolos raros y que luego tengan el @ y finalicen con la dirección. 