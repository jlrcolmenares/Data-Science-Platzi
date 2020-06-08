![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/joseluisramon-diploma-bd.png)

# Fundamentos de Bases de Datos

**Prof. Israel Vázquez**

## Bases de Datos Relacionales

**SQL** significa **S**tructured **Q**uery **L**anguage y tiene una estructura clara y fija. Su objetivo es hacer un solo lenguaje para consultar cualquier manejador de bases de datos volviéndose un gran estándar.

Ahora existe el **NOSQL** o **N**ot **O**nly **S**tructured **Q**uery **L**anguage que significa que no sólo se utiliza SQLen las bases de datos no relacionales. Algunos ejemplos son Cassandra (Base de Datos tipo Columnas) o BigQuery (Para data warehouse)

### DDL: Data Definition Language

MySQL tiene dos grandes sublenguajes que nos ayudan a crear y modificar la estructura de la base de datos. Estos lenguajes nos permiten trabajar tanto con BD locales, como con bases de datos en línea.

**DDL** o Data Definition Language que nos ayuda a crear la estructura de una base de datos. Existen 3 grandes comandos:

- **Create**: Nos ayuda a crear bases de datos, tablas, vistas, índices, etc.
- **Alter**: Ayuda a alterar o modificar entidades.
- **Drop**: Nos ayuda a borrar. Hay que tener cuidado al utilizarlo.

**3 objetos que manipularemos con el lenguaje DDL:**

- Database o bases de datos (llamado Schemas)
- Table o tablas. Son la traducción a SQL de las entidades
- View o vistas: Se ofrece la proyección de los datos de la base de datos de forma entendible.

### DML: Data Manipulation Language

**DML** trata del contenido de la base de datos. Son las siglas de Data Manipulation Language y sus comandos son:

#### **Insert**

Inserta o agrega nuevos registros a la tabla.

```mysql
-- Insert. Inserta una serie de datos después del ultimo que existe
INSERT INTO `people` (last_name, first_name, address, city)
VALUES (`Hernández`, `Laura`, `Calle 21`, `Monterrey`);
```

#### **Update**

Actualiza o modifica los datos que ya existen.

``` mysql
-- Update. Modifica datos segun ciertas condiciones
UPDATE `people` -- UPDATE [indicar tabla a modificar]
SET last_name = 'Chávez', city= 'Mérida' -- SET [nuevos valores]
WHERE person_id = 1; --  WHERE [condicion para elegir que se sustituye]

UPDATE people -- tabla
SET first_name = `Juan` -- nuevo dato
WHERE city = `Mérida`; -- condicion

UPDATE people
SET first_name = `Juan`; -- si no se indica donde, lo cambiará en todos los registros de la columna first_name
```

#### **Delete**

Esta sentencia es riesgosa porque puede borrar el contenido de una tabla.

```mysql
-- Delete. Elimina datos dentro de una o tabla.
DELETE FROM people 
WHERE person_id = 1; -- elimina un registro
    
DELETE FROM people; -- este comando elimina TODA la tabla

```

#### **Select**

Trae información de la base de datos.

```mysql
-- Select. Selecciona o trae datos a una vista.
SELECT * FROM platziblog.posts;

SELECT fist_name, last_name 
FROM people;

SELECT first_name
WHERE last_name: `Cordero`;
```

## Bases de Datos NO Relacionales

## ¿Qué son?

Hay varios tipos de NRDB, suelen ser utilizadas para aplicaciones específicas, pero eso las hace más versátiles. Usualmente se clasifican de la siguiente forma.

### Jerarquía

| FireStore                                                    | MySQL                                             |
| ------------------------------------------------------------ | ------------------------------------------------- |
| 1. Base de Datos                                             | 1.1. Esquemas                                     |
| 1.1. Colecciones                                             | 1.1.1. Tablas / Entidades                         |
| 1.1.1. Documentos                                            | 1.1.1.1. Tuplas / Rows                            |
| Son los objetos que agrupan la información que queremos guardar en formato JSON | Cada row debe tener un dato atómico y consistente |

Los documentos dentro de ellos tienen datos y estos tipos de datos varían según la base de datos.