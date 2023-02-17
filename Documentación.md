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



### IMPORTACIÓN DE DADES BÀSIQUES
use mydb;  
ALTER TABLE eleccions  
	MODIFY COLUMN data INT;  
ALTER TABLE eleccions   
	DROP COLUMN any;   
ALTER TABLE eleccions  
	ADD any INT;  
INSERT INTO eleccions (eleccio_id, nom, data, any, mes)   
VALUES  (1, 'Eleccions 2019',28,2019,04);  
  
### IMPORTACIÓN COMUNIDADES AUTONOMAS, PROVINCIAS Y MUNICIPIOS
  
import mysql.connector   
import datetime   
cnx = mysql.connector.connect(host='192.168.56.103',user='perepi',password='pastanaga', database='mydb')   
cursor = cnx.cursor()   
   
with open("D:/Escritorio/INSTITUTO/TREBALL BASE DE DADES/02201911_MESA/07021911.DAT") as f:   
    content = f.readlines()  
    for line in content:  
        if line[9:11] != "99" and line[11:13] == "99":  
            nom=(line[14:64])  
            codine=(line[9:11])  
  
            insert = 'INSERT INTO comunitats_autonomes (nom, codi_ine) VALUES (%s,%s)'  
            valores = (nom,codine)  
            cursor.execute(insert, valores)  
    cnx.commit()  
       
    with open("D:/Escritorio/INSTITUTO/TREBALL BASE DE DADES/02201911_MESA/07021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        if line[9:11] != "99" and line[11:13] != "99":  
            comunitatautid=(line[9:11])  
            nom=(line[14:64])  
            codine=(line[11:13])  
            numescons=(line[149:155]) 
              
            insert = 'INSERT INTO provincies (comunitat_aut_id, nom, codi_ine, num_escons) VALUES (%s,%s,%s,%s)'  
            valores = (comunitatautid,nom,codine,numescons)  
            cursor.execute(insert, valores)    
    cnx.commit()  
      
    with open("D:/Escritorio/INSTITUTO/TREBALL BASE DE DADES/02201911_MESA/05021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        if line[16:18] == "99":  
            nom=(line[18:118])  
            codine=(line[13:16]) 
            provinciaid=(line[11:13])  
            districte=(line[16:18])  
  
            insert = 'INSERT INTO municipis (nom, codi_ine, provincia_id, districte) VALUES (%s,%s,%s,%s)'  
            valores = (nom,codine,provinciaid,districte)  
            cursor.execute(insert, valores)  
    cnx.commit()  
cursor.close()  
cnx.close()  
  
  
### IMPORTACIÓN DE PARTIDOS POLITICOS/CANDIDATURAS
  
**Las 4 primeras lineas sirven para conectar al servidor, despues ponemos la ruta donde está ubicado el fichero que queremos extraer los datos, con el FOR LINE
ponemos el nombre de los campos seleccionado las posiciones en la que están sus datos y por ultimo hacemos un insert para añadir los valores a la tabla de la base de datos.**

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

**Las 4 primeras lineas sirven para conectar al servidor, despues ponemos la ruta donde está ubicado el fichero que queremos extraer los datos, con el FOR LINE
ponemos el nombre de los campos seleccionado las posiciones en la que están sus datos y por ultimo hacemos un insert para añadir los valores a la tabla de la base de datos.**
  
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
      
    with open("c:/Users/santi/Desktop/02201911_MESA/04021911.DAT") as f:
    content = f.readlines()
    cursor.execute("ALTER TABLE persones MODIFY persona_id INT AUTO_INCREMENT")
      
    for line in content:
        nom = line[25:50]
        cog1 = line[50:75]
        cog2 = line[75:100]
        sexe = line[100:101]
        #datanaixement = line[101:109]
        dni = line[109:119]
        
        insert = 'INSERT INTO persones (nom, cog1, cog2, sexe, dni) VALUES (%s, %s, %s, %s, %s)'
        valores = (nom, cog1, cog2, sexe, dni)
        cursor.execute(insert, valores)
    cnx.commit()
cursor.close()  
cnx.close()  
  
  
### IMPORTACIÓN VOTOS A NIVEL MUNICIPAL
import mysql.connector  
import datetime  
cnx = mysql.connector.connect(host='10.94.254.35',user='perepi',password='pastanaga', database='mydb')  
cursor = cnx.cursor()  
  
with open("c:/Users/santi/Desktop/02201911_MESA/06021911.DAT") as f:  
    content = f.readlines()  
      
    for line in content:  
        eleccioid=(line[0:2])  
        municipiid=(line[11:14])  
        candidaturaid=(line[16:22])  
        vots=(line[22:30])  
        select = 'SELECT * FROM vots_candidatures_mun WHERE eleccio_id = %s AND municipi_id = %s AND candidatura_id = %s'  
        valores_select = (eleccioid, municipiid, candidaturaid)  
        cursor.execute(select, valores_select)  
        result = cursor.fetchall()  
        print(result)  
          
        if not result:  
            insert = 'INSERT INTO vots_candidatures_mun (eleccio_id,municipi_id,candidatura_id,vots) VALUES (%s,%s,%s,%s)'  
            valores = (eleccioid,municipiid,candidaturaid,vots)  
            cursor.execute(insert, valores)  
            print("Registre afeigit")  
        cnx.commit()  
cursor.close()  
cnx.close()  
  
  
### IMPORTACIÓN VOTOS A NIVEL PROVINCIAL  
  
**Las 4 primeras lineas sirven para conectar al servidor, despues ponemos la ruta donde está ubicado el fichero que queremos extraer los datos, con el FOR LINE  
ponemos el nombre de los campos seleccionado las posiciones en la que están sus datos y por ultimo hacemos un insert para añadir los valores a la tabla de la base de datos.**  

**Aquí nos aparecía un error de duplicar y lo solucionamos haciendo un SELECT seleccionando los campos específicos para ver si se repiten los valores, si se repiten no los añade y si no se repite lo añade a la base de datos.**


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
import mysql.connector  
import datetime  
cnx = mysql.connector.connect(host='192.168.56.103',user='perepi',password='pastanaga', database='mydb')  
cursor = cnx.cursor()  
with open("D:/Escritorio/INSTITUTO/TREBALL BASE DE DADES/02201911_MESA/08021911.DAT") as f:  
    content = f.readlines()  
    for line in content:  
        if line[9:11] != "99" and line[11:13] != "99":  
            comunitatautid=(line[9:11])  
            candidaturaid=(line[14:20])  
            vots=(line[20:28])  
              
            dropkeys= 'ALTER TABLE vots_candidatures_ca DROP PRIMARY KEY; ALTER TABLE vots_candidatures_ca DROP PRIMARY KEY'  
            insert = 'INSERT INTO vots_candidatures_ca (comunitat_autonoma_id, candidatura_id, vots) VALUES (%s,%s,%s)'  
            valores = (comunitatautid,candidaturaid,vots)  
            cursor.execute(dropkeys,insert, valores)  
        print (comunitatautid)  
    cnx.commit()  
cursor.close()  
cnx.close()  
  

## CONSULTAS
### *SIMPLES*
**1- Muestra cuántos hombres han introducido en la base de datos.**
         
SELECT COUNT(nom)  
  	FROM persones  
  	WHERE sexe = M;  


**2- Muestra todas las votaciones en blanco:**

SELECT SUM(vots_blanc)  
	FROM eleccions_municipals;  
  
**3- Muestra el nombre, apellido 1 y el dni de cada persona:**  
  
SELECT 	nom,  
	cognom1,  
	dni  
	FROM persones  
	WHERE dni IS NOT NULL;  
  
**4- Muestra el numero de escaños de cada provincia. Ordena por num_escons ASC:**  
  
SELECT nom,  
       num_escons  
FROM provincia  
WHERE num_escons ASC;  
   
  
**5- Muestra el apellido de los candidatos en mayúsculas y la longitud del apellido de los candidatos donde su apellido comience por J, A o M. Ordena los resultados por apellido de los candidatos.**  
  
SELECT UPPER(cognom1), length(cognom1)  
    FROM empleats  
WHERE LEFT(cognom1, 1) IN ("J","A","M");  
   
### *COMBINACIONES*  
**1- Muestra los códigos de los candidatos con sus votos provinciales**  
  
SELECT c.codi_candiatura,  
  	    pr.vots  
	FROM candidatures c  
  	INNER JOIN vots_candiatures_prov pr ON pr.candiatura_id = c.candiatura_id  
  	INNER JOIN vots_candiatures_mun m ON m.candiatura_id = c.candiatura_id;  
	
  
**2- Muestra todos los tipos de votos que se obtuvo en las elecciones del año 2019.**   
  
SELECT em.vots_amesos,  
  	    em.vots_valids,  
            em.vots_candiatures,  
      	    em.vots_blanc,  
  	    em.vots_ruls  
  	FROM eleccions_municipis em  
  	INNER JOIN eleccions e ON e.eleccio_id = em.eleccio_id  
  	WHERE e.any = 2019;  
  
  
**3- Nombre de los candidatos que participaron en la Elección “1”:**  
  
SELECT p.nom  
  FROM persones p  
  INNER JOIN candidats c ON c.candidatura_id = c.candiatura_id  
  INNER JOIN candidatures cs ON cs.candidatura_id = c.candiatura_id  
  INNER JOIN eleccions e ON e.eleccio_id = cs.eleccio_id  
  WHERE e.nom = 'Elección 1';  
    
    
 **4- Muestra el nombre de municipio, nombre de provincia y la cantidad de votos válidos totales que han obtenido. Ordena por nombre de municipio.**  
  
SELECT m.nom,  
	    p.nom,  
	    SUM(em.vots_valids)  
	FROM eleccions_municipis em  
	INNER JOIN municipis m ON m.municipi_id =  em.municipi_id  
	INNER JOIN provincies p ON p.provincia_id =  m.provincia_id  
ORDER BY m.nom;  
  
**5-  Muestra el número de provincias que hay por comunidad autónoma.**  
  
SELECT c.nom AS comunitat_autònoma,  
	    COUNT(p.nom) AS províncies,  
	    COUNT(m.nom) AS municipis  
	   FROM comunitats_autonomes c  
	INNER JOIN provincies p ON p.comunitat_aut_id =  c.comunitat_aut_id  
INNER JOIN municipis m ON m.provincia_id =  p.provincia_id;  
   
   
### *SUCONSULTAS*
  
**1- selecciona el nombre y el número de votos municipales de la candidatura que ha recibido el número máximo de votos en la elección = 1:**
  
SELECT c.nom_curt,  
    m.vots  
FROM candidatures c  
INNER JOIN  vots_candidatures_mu m ON m.candidatura_id = c.candidatura_id  
WHERE m.vots = (SELECT MAX(m.vots)  
                        FROM vots_candidatures_mu  
		INNER JOIN  eleccions e ON e.eleccio_id = mu.eleccio_id  
                        WHERE e.eleccio_id = 1);  
			
			
**2- Busca el máximo número de votos obtenidos por una candidatura.**  
  
SELECT e.nom, cs.nom, vc.vots  
	FROM eleccions e  
INNER JOIN candidatures cs ON cs.eleccio_id = e.eleccio_id  
INNER JOIN candidats c ON c.candidatura_id =cs.candidatura_id  
INNER JOIN vots_candidatures_ca vc ON vc.candidatura_id =cs.candidatura_id  
WHERE vc.vots = (SELECT MAX(vc.vots)  
                            FROM  vots_candidatures_ca  
                            WHERE cs.eleccio_id = e.eleccio_id);  
  
  
**3-  Les candidaturas que han obtingut mes de 5000 vots en comunitat autònoma.**  
  
SELECT nom_curt,  
	   nom_llarg  
FROM candidatures  
WHERE comunidad_autonoma IN (SELECT comunidad_autonoma   
FROM WHERE vots > 5000);  
  
  
**4-  Queremos obtener el número total de votos obtenidos por cada candidatura en una determinada elección.**  
  
SELECT candidatura_id,  
     	    SUM(vots) AS total_vots  
FROM vots_candidatures_com  
WHERE candidatura_id IN (SELECT candidatura_id   
   				FROM candidatures   
   				WHERE eleccio_id = ‘1’ )  
GROUP BY id_candidatura;  
  
  
**5- Queremos saber la provincia_id candiatura_id y los votos que pertenecen a una determinada provincia.**  
  
SELECT provincia_id,  
  	    candiatura_id,  
	    vots  
FROM vots_candidatures_prov  
WHERE provincia_id IN   
  (SELECT provincia_id   
   FROM provincies   
   WHERE nom = 'Barcelona');  
			 			
  			
### *WINDOW FUNCTION*
**Calcula la posición de cada candidatura basado en su número de votos por provincia**  
  - Utilizamos la función de ventana RANK() para asignar una posición a cada candidatura dentro de cada provincia.  
  - La cláusula OVER especifica que la función de ventana se aplica dentro de cada partición definida por la columna "id_provincia" de la tabla "votos_provincias".  
   
SELECT p.nom,  
   c.nom_curt,  
   vp.vots,  
   RANK() OVER (PARTITION BY vp.provincia_id ORDER BY vp.vots DESC) AS posicio    
FROM vots_candidatures_prov vp   
INNER JOIN candidatures c ON c.id_candidatura = vp.candidatura_id   
INNER JOIN provincies p ON p.provincia_id = vp.id_provincia   
ORDER BY p.nom, posicio   
   






