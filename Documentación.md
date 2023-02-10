## GITHUB
Primero cree un repositorio en github dandole a NEW FILE y despues metí toda la información dentro de la carpeta creada, 
luego compartí este repositorio com mis panas del grupo y ellos se unieron con un correo que les llegó.

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

**Las 4 primeras lineas sirven para conectar al servidor:

import mysql.connector  
import datetime  
cnx = mysql.connector.connect(host='10.94.255.159',user='perepi',password='pastanaga', database='eleccions')   
cursor = cnx.cursor()  
  
with open("c:/Users/santi/Desktop/02201911_MESA/03021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        eleccioid=(line[0:2])  
        codicandidatura=(line[8:14])  
        nomcurt=(line[14:64])  
        nomllarg=(line[64:214])  
        codiacumulacioprovincia=(line[214:220])  
        codiacumulacioca=(line[220:226])  
        codiacumulacionacional=(line[226:232])  
	  
        insert = 'INSERT INTO candidatures (eleccio_id,codi_candidatura,nom_curt,nom_llarg, codi_acumulacio_provincia, codi_acumulacio_ca, codi_acumulario_nacional)   VALUES (%s,%s,%s,%s,%s,%s,%s)'  
        valores = (eleccioid,codicandidatura,nomcurt,nomllarg,codiacumulacioprovincia,codiacumulacioca,codiacumulacionacional)  
        cursor.execute(insert, valores)  
    cnx.commit()  
cursor.close()  
cnx.close()  

  
### IMPORTACIÓN CANDIDATOS Y PERSONAS

**Las 4 primeras lineas sirven para conectar al servidor:  
  
import mysql.connector  
import datetime  
cnx = mysql.connector.connect(host='10.94.255.159',user='perepi',password='pastanaga', database='eleccions')  
cursor = cnx.cursor()  
  
with open("c:/Users/santi/Desktop/02201911_MESA/04021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        candidaturaid=(line[15:21])  
        personaid=(line[109:119])  
        provinciaid=(line[9:11])  
        numordre=(line[21:24])  
        tipus=(line[24:25])  
        insert = 'INSERT INTO candidats (candidatura_id,persona_id,provincia_id,num_ordre,tipus) VALUES (%s,%s,%s,%s,%s)'  
        valores = (candidaturaid,personaid,provinciaid,numordre,tipus)  
        cursor.execute(insert, valores)  
    cnx.commit()  
cursor.close()  
cnx.close()  
  
### IMPORTACIÓN VOTOS A NIVEL MUNICIPAL

### IMPORTACIÓN VOTOS A NIVEL MUNICIPAL

### IMPORTACIÓN VOTOS A NIVEL PROVINCIAL  
  
**Las 4 primeras lineas sirven para conectar al servidor:  


import mysql.connector  
import datetime  
cnx = mysql.connector.connect(host='10.94.255.159',user='perepi',password='pastanaga', database='eleccions')  
cursor = cnx.cursor()  
  
with open("C:/Users/David UBE/OneDrive - Sa Palomera/Escritorio/cole/ASIX/Base de dades/TREBALL EN GRUP A/GRUP A/08021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        provinciaid=(line[11:13])  
        candidaturaid=(line[14:20])  
        vots=(line[20:28])  
        candidatsobtinguts=(line[28:33])  
        select = 'SELECT * FROM vots_candidatures_prov WHERE provincia_id = %s AND candidatura_id = %s'  
        valores_select = (provinciaid, candidaturaid)  
        cursor.execute(select, valores_select)  
        result = cursor.fetchall()  
        if not result:  
            insert = 'INSERT INTO vots_candidatures_prov (provincia_id,candidatura_id,vots,candidats_obtinguts) VALUES (%s,%s,%s,%s)'  
            valores_insert = (provinciaid,candidaturaid,vots,candidatsobtinguts)  
            cursor.execute(insert, valores_insert)  
    cnx.commit()  
cursor.close()  
cnx.close()  

  

### IMPORTACIÓN VOTOS A NIVEL AUTONOMICA



## CONSULTAS
### *SIMPLES*
1- Mostra quants homes n’hi han introduïts a la base de dades.
         
SELECT COUNT(nom)
	FROM persones
	WHERE sexe = M;

\
2- Muestra todas las votaciones en blanco:

SELECT SUM(vots_blanc)\
	FROM eleccions_municipals;

\
3- Muestra el nombre, apellido 1 y el dni de cada persona:

SELECT 	nom,\
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



### *WINDOW FUNCTION*







