import cx_Oracle
import os
import io
import PyPDF2
import datetime

if os.environ.get('BD_CONNECTION') is None:
    DSN_TNS = cx_Oracle.makedsn('npaa5513.petrobras.biz','1521','aplc08d')
    DB_USERNAME = 'saet_aplicacao'
    BD_PASSWORD = 'saet_aplicacao'

else:
    DSN_TNS = cx_Oracle.makedsn(os.environ['BD_CONNECTION'], os.environ['BD_PORT'],
                            os.environ['BD_NAMEDB'])
    DB_USERNAME = os.environ['BD_USERNAME']
    BD_PASSWORD = os.environ['BD_PASSWORD']

def consulta(sql):
    connection = cx_Oracle.connect(DB_USERNAME, BD_PASSWORD, DSN_TNS, encoding="UTF-8", nencoding="UTF-8")
    #connection = cx_Oracle.connect("system","xeoracle9","XE", encoding="UTF-8", nencoding="UTF-8") #cria a conexãocont

    cursor = connection.cursor() # cria um cursor
    #print("inicio consulta ", datetime.datetime.now())
    cursor.execute(sql) # consulta sql
    result = cursor.fetchall()  # busca o resultado da consulta
    #print("fim consulta ", datetime.datetime.now())
    if result == None: 
        final_result = []
    else:
        final_result = [list(i) for i in result]

    cursor.close()
    connection.close()

    return final_result

def consulta_Blob(sql):
    connection = cx_Oracle.connect(DB_USERNAME, BD_PASSWORD, DSN_TNS, encoding="UTF-8", nencoding="UTF-8")
    #connection = cx_Oracle.connect("system","xeoracle9","XE", encoding="UTF-8", nencoding="UTF-8") #cria a conexãocont

    cursor = connection.cursor() # cria um cursor

    #sql = "select sq_et_complemento,tx_nome_documento,mm_anexo from saet.et_complemento where sq_et_complemento=21"

    cursor.execute(sql) # consulta sql
    result = cursor.fetchall()  # busca o resultado da consulta

    
    if result == None: 
        final_result = []
    else:
        final_result = [list(i) for i in result]
    
    print(final_result[0][1])
    
    #recupera o arquivo e salva local
    FileName="C:\\Users\\1275867\\Documents\\%s" % final_result[0][1]
    pdf_file = open(FileName,'wb')
    pdf_file.write(final_result[0][2].read())
    pdf_file.close()
  

    cursor.close()
    connection.close()

    return "final_result"    

def dml_single(sqlList): #DML (Data Manipulation Language)
    connection = cx_Oracle.connect(DB_USERNAME, BD_PASSWORD, DSN_TNS, encoding="UTF-8", nencoding="UTF-8")
    #connection = cx_Oracle.connect("system","xeoracle9","XE", encoding="UTF-8", nencoding="UTF-8") #cria a conexãocont

    cursor = connection.cursor() # cria um cursor
    for sql in sqlList:
        cursor.execute(sql) # executa a query
    connection.commit()
    cursor.close()
    connection.close()
    #print("Solicitação realizada com sucesso")
    return ""

 #args = {'mm_anexo':binaryData.getvalue(), 'nomeFile':filename, 'formatoFile':filename.split(".")[1], 'dataExec':data, 'chave':cd_chave_id } 

def dml_single_blob(sql,sq_et,mem_file,file_size,filename,formatoFile,data,cd_chave_id):
    connection = cx_Oracle.connect(DB_USERNAME, BD_PASSWORD, DSN_TNS, encoding="UTF-8", nencoding="UTF-8")
    #connection = cx_Oracle.connect("system","xeoracle9","XE", encoding="UTF-8", nencoding="UTF-8") #cria a conexãocont

    cursor = connection.cursor() # cria um cursor

    cursor.setinputsizes(mm_anexo = cx_Oracle.CLOB)
    my_blob = cursor.var(cx_Oracle.BLOB, file_size)
    my_blob.setvalue(0, mem_file.getvalue())

    params = {'sq_et':sq_et, 'mm_anexo':my_blob, 'nomeFile':filename, 'formatoFile':formatoFile, 'dataExec':data, 'chave':cd_chave_id } 

    result = cursor.execute(sql, params)
    
    #cursor.execute(sql) # executa a query

    connection.commit()
    cursor.close()
    connection.close()
    #print("Solicitação realizada com sucesso")
    return result
  
