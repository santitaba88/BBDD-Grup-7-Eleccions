## GITHUB

## PASOS PREVIOS IMPORTACIÓN DATOS

Primero tubimos que preparar para poder importar, ejecutamos la comanda $>pip install mysql-connector-python en nuestro powershell para conectar el python con el sistema.

Cuando terminó la instalación reiniciamos nuestro PC y en el VIsual Studio instalamos la extensión de MySQL.

Después creamos un fichero python para conectarlo a nuestro servidor donde tenemos la base de datos.

En el documento python para leer la base de datos que queremos importar creamos una variable y pusimos la ruta donde está situado el fichero que queremos.
 
Luego cada miembro entró a mysql workbench y miró las claves que había que añadir en su python, una vez que las supimos cada miembro fue a mirar en el word de ficheros.doc las líneas en las que estaban estos datos.

Una vez supimos todos los datos y su ubicación añadimos en nuestros python un bucle for con el nombre de la clave que queremos añadir y al lado en las líneas en las que están ubicadas en el fichero.


### IMPORTACIÓN DE BASE DE DADES

### IMPORTACIÓN COMUNIDADES AUTONOMAS, PROVINCIAS Y MUNICIPIOS

### IMPORTACIÓN DE PARTIDOS POLITICOS/CANDIDATURAS

### IMPORTACIÓN CANDIDATOS Y PERSONAS

### IMPORTACIÓN VOTOS A NIVEL MUNICIPAL

### IMPORTACIÓN VOTOS A NIVEL MUNICIPAL

### IMPORTACIÓN VOTOS A NIVEL PROVINCIAL

### IMPORTACIÓN VOTOS A NIVEL AUTONOMICA



## CONSULTAS
### *SIMPLES*

\
2- Muestra todas las votaciones en blanco:

SELECT SUM(vots_blanc)\
	FROM eleccions_municipals;

\
3- Muestra el nombre, apellido 1 y el dni de cada persona:

SELECT nom,\
        cognom1,\
	    dni\
	FROM persones\
	WHERE dni IS NOT NULL;

\
4- Muestra el numero de escaños de cada provincia. Ordena por provincia ASC:

 SELECT nom, \
	    num_escons \
	FROM persones\
	WHERE provincia ASC; 

\
5- Muestra el apellido de los candidatos en mayúsculas y la longitud del apellido de los candidatos donde su apellido comience por J, A o M. Ordena los resultados por apellido de los candidatos.

SELECT UPPER(cognom1), length(cognom1)\
    FROM empleats\
WHERE LEFT(cognom1, 1) IN ("J","A","M");

  

\ 
### *COMBINACIONES*



### *SUCONSULTAS*









