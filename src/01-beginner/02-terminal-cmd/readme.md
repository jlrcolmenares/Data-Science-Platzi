# 02-Terminal-Línea-de-Comandos

**Prof. Mauro Chojrin**



![](https://joseluisramoncolmenares.files.wordpress.com/2020/05/joseluiramon-diploma-terminal.png)

## Unidad 2. Manipular Archivos

### Sistema de Archivos

La manera en que el terminal organiza su archivo es a través del esquema `directorio/subdirectorio/archivo.ext`

```bash
ls 			//ver archivos de directorio
ls -a 		//ver archivos ocultos
.config 	//los archivo ocultos comienzan con .
pwd			//print working directory
cd			//change directory
cd ~		//ir a directorio home
cd - 		//ir a directorio anterior
cd .. 		//ir a directorio padre
```

### Copiar y Eliminar

```bash
mkdir as		//crear directorio
drwxrwxrwx as 	//si comienza con d es un directorio

cp [archivo] [directorio]
cd test.py test/

rm [archivo]

mv [archivo] [nuevo-dir]
mv 

rmdir test/
```

### Comandos para mover, copiar o borrar

**`cp`**: copiar un archivo hacia un directorio.

```bash
cp [archivo que se va a copiar] [directorio hacia el que se va a mover]
```

**`rm`**: eliminar un archivo.

```bash
rm archivo.txt
```

**`mv`**: mover un archivo, cambiar su ubicación. La sintaxis es así:

```bash
mv [ruta del archivo] [directorio hacia el que se va a mover]
```

**`rmdir`**: eliminar un directorio. En este caso es importante resaltar que, para que el directorio pueda ser eliminado, no puede contener archivos u otros directorios en su interior.

```bash
> rmdir [ruta / nombre del directorio a eliminar]
```

## Unidad 3. Comunicación entre procesos

### Flujos Estándar

La terminal conoce de 3 flujos estándar: Entrada (estándar), Salida (estándar),Error (estándar).

Por defecto, si no hacemos nada, los flujos están conectados a los periféricos del equipo. La entrada vendrá del teclado, y la salida y el error, van a la pantalla, parece natural para la mayoría de los casos pero *hay ocasiones en las que no queremos que esto sea así*.

1. Cuando queremos que la entrada de un proceso no venga del teclado sino de un archivo se usa  `<`.
2. Cuando queremos que la salida no se muestre en pantalla sino en un archivo se usa `>`.
3. Cuando queremos agregar textp a un archivo que ya estaba (append) se usa `>>`.

### Modos

Cuando escribes un comando, se crea un proceso y se ejecuta inmediatamente

Hay otros casos en los cuales le das a ejecutar un proceso y la terminal se queda parpadeando hasta que nos entrega el resultado, esto se conoce como *ejecución en primer plano* **(foreground)**. 

Claro, si el proceso es muy largo quizás quieras dejarlo ejecutando y seguir con tu vida hasta que esté listo. Si quieres dejar ejecutando un proceso en modo **background** y que el control regrese a ti luego del ENTER, basta con poner el símbol `&` al final del comando.

Hay otra situación en la que queremos que un proceso se esté ejecutando constantemente (caso servidores), este tipo de sitaciónes se conocen como demonios / daemons.  Cualquier proceso que queramos dejar ejecutando en el background podemos mandarlo para allá con `Ctrl+Z`. Si queremos traerlo de regreso usamos el comando `fg`.

### Detener proceso

Para detener, se usa `Ctrl+C`.

Otra forma de deter proceso es por medio de `kill` y `killall`. Son dos comando equivales. A partir de la salida del comando `ps` se ubica el número de código de proceso y se detiene

### Permisos sobre archivos.

UNIX fue diseñado como un sistema multiusuario. 

Todos los archivos tiene un intereción con los siguientes usuarios **DUEÑO** (quien lo creó) **GRUPO** (quien está autorizado) **OTROS** (los no especificados).

Los usuarios pueden hacer la siguientes cosas con cualquier archivo: LECTURA, ESCRITURA y EJECUCIÓN. 

Esto configura un matrix de posibilidades. Vamos a ver como ser los 

`ls -l` vemos los archivos con los permisos asociados: `-rw` = `[permiso negado][lectura][escritura]`

Existen 3 comando para editar los accesos a los archivos

* `chmod`: cambia los acceso
* `chow`: cambia al dueño
* `chgrp`: cambia el grupo de usuarios

Los acceso se pueden cambiar con *notación textual* o con *notación binaria*

## Unidad 4. Herramientas Avanzadas

### Búsqueda de archivos

**whereis**

Se utiliza para buscar comandos, por ejemplo `whereis echo` nos muestra la ubicación del comando y del manual

**find**

Es la herramienta más completa, lo que hace es buscar dentro de un arbol de directorios utilizando una serie de argumentos

### Interactuar con HTTP

HTTP se trata de pedir texto y obtener texto, luego el ordenador se encarga de transformar eso y que se vea bonito. 

**curl**

Este comando pide data cruda por http.  Recibe todo lo que el servidor de una página envía al navegador

```bash
curl https://platzi.com
curl -v https://platzi.com
curl -v https://platzi.com > /dev/null `esto se usa mucho ?? segun el profesor. Descarga encabezados` 
```

**wget**

Este comando descarga archivos e imágenes directamente desde una página web

### Variables de Entorno

Una variable de entorno una definición global a la que todos los procesos tienen acceso. La variable `$PATH` contiene la ubicación de todos los comandos ejecutables. El peso `$` es una forma de pedirle a la terminal que expanda la información

El sistema ejecuta unos archivos de configuración cada vez que inicia, podemos ver la definición de $PATH por medio del comando `nano /etc/enviroment`

El archivo .bashrc se ejecuta cada vez que se inicia la terminal, para agregar tu directorio de trabajo al $PATH crear un archivo `nano .bashrc` y agregar el código

```sh
export PATH=$PATH:/home/[usr]/[dir]
```

Luego el comando `source .bashrc`. Como este archivo se llama .bashrc el archivo se va a ejecutar cada vez que inicies la sesió

## Unidad 5. Automatización de Tareas

### Scripts en Bash

Se pueden hacer cierto script utilizando la instancias de Bash y podrás crear tus propios comandos. Los comandos se pueden crear con VIM o con nano

```sh
#!/bin/bash
NEW_DIR=platzi `nueva variables`

if [ ! -d "~/$NEW_DIR" ]; then `si no existe el directorio platzi `
   mkdir ~/$NEW_DIR `crear el directorio`
fi `finalizar el if`

cp backup_code.sh ~/$NEW_DIR/ `copiar archivo al directorio`
echo "Todo listo jefe!" `imprimir mensaje`
```

### 