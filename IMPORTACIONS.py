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
        
with open("D:/Escritorio/INSTITUTO/TREBALL BASE DE DADES/02201911_MESA/05021911.DAT") as f:
    content = f.readlines()
    for line in content:
            municipid=(line[13:16])
            nummeses=(line[136:141])
            cens=(line[141:149])
            votsemesos=((line[216:224])+(line[224:232]))
            votsvalids=(line[216:224])
            votscandidatures=(line[205:213])
            votsblanc=(line[189:197])
            votsnuls=(line[197:205])

            insert = 'INSERT INTO eleccions_municipis (municipi_id, num_meses, cens, vots_emesos, vots_valids, vots_candidatures, vots_blanc, vots_nuls) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            valores = (municipid,nummeses,cens,votsemesos,votsvalids,votscandidatures,votsblanc,votsnuls)
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
        dni = line[109:119]
        
        insert = 'INSERT INTO persones (nom, cog1, cog2, sexe, dni) VALUES (%s, %s, %s, %s, %s)'
        valores = (nom, cog1, cog2, sexe, dni)
        cursor.execute(insert, valores)
    cnx.commit()     
    
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