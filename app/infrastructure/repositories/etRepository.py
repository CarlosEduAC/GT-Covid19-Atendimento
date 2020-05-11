from infrastructure.contexts.connect import consulta,dml_single_blob, dml_single
from domain.entities.ET import ET_DTO
from domain.entities.RodadaTopico import RodadaTopico_DTO
from domain.entities.RodadaItem import RodadaItem_DTO
from flask import session
from requests import Session
import datetime
import base64
import os
import io

def salvaET(sq_et,nm_ET,sg_ET,filename,path,id_familia):
    cd_chave_id = session.get('chave')

    #pdf_File = open(os.path.abspath(path),'rb') #'ANEXO I - ESPECIFICACAO DOS SERVICOS.pdf'
    #blob = base64.b64encode(pdf_File.read())

    """
    with open(os.path.abspath(path), 'rb') as file:
        binaryData = io.BytesIO(file.read())"""
        
    pdf_File = open(os.path.abspath(path),'rb')
    mem_file = io.BytesIO(pdf_File.read())
    mem_file.seek(0, os.SEEK_END)   
    file_size = mem_file.tell() 

    
    if sq_et == "0":
        sql = []
        sql.append("insert into saet.et (sq_et, id_familia, ds_et, sg_et) values (saet.seq_sq_et.nextval, " + str(id_familia) + ", '" +str(nm_ET)+ "' , '" + str(sg_ET)+ "')")
        dml_single(sql)

        sql = "select max(sq_et) from saet.et where id_familia = " + str(id_familia) + ""
        listaBD = consulta(sql)
        sq_et = listaBD[0][0]


    mySQL = 'INSERT INTO saet.ET_Complemento (sq_et_complemento, sq_et, mm_anexo, tx_nome_documento, tx_extensao, dt_execucao, cd_chave_id ) '
    mySQL += 'values (saet.seq_sq_complemento.nextval, :sq_et, :mm_anexo, '':nomeFile'', '':formatoFile'', :dataExec, '':chave'' )'
    print("mysql", mySQL)
    data = datetime.datetime.now()

    #args = {'mm_anexo':binaryData.getvalue(), 'nomeFile':filename, 'formatoFile':filename.split(".")[1], 'dataExec':data, 'chave':cd_chave_id } 

    dml_single_blob(mySQL,sq_et,mem_file,file_size,filename,filename.split(".")[1],data,cd_chave_id)

    sql = "select max(sq_et_complemento) from saet.ET_Complemento where tx_nome_documento like '"+ str(filename) +"'"
    listaBD = consulta(sql)
    sq_et_complemento = listaBD[0][0]

    return sq_et_complemento
    
def getTopicoItens(sq_topico):
       
    sql = " select t.sq_topico,t.ds_topico,sq_item,nm_item,ds_item,tx_observacao, f.id_familia, f.ds_familia"
    sql += " from saet.topico t, saet.item i, saet.familia f"
    sql += " where  t.sq_topico = i.sq_topico"
    sql += " and i.id_familia = f.id_familia(+)"
    if sq_topico != "":
        sql += " and t.sq_topico in (" + sq_topico + ") "
    sql += " order by t.ds_topico, i.ds_item"

    listaBD = consulta(sql)    

    return listaBD

def getFamilia():  
    sql = "Select id_familia as valor, ds_familia as texto from saet.familia order by ds_familia"
    lista = consulta(sql)

    return lista

def salvaRodadaItem(sq_et,sq_et_Complemento,sq_item,in_verificacao):
    sql = "select count(*) from saet.et, saet.et_complemento etc where et.sq_et = etc.sq_et and et.sq_et = " + str(sq_et) + ""
    listaBD = consulta(sql)

    nr_rodada = listaBD[0][0] + 1

    sql = []
    sql.append("insert into saet.rodada_valida_item (sq_item,sq_et_complemento,nr_rodada,in_verificacao) values (" + str(sq_item) + ", "+ str(sq_et_Complemento) +", "+ str(nr_rodada) +", '" + str(in_verificacao)  + "')" )

    dml_single(sql)   

def salvaRodadaTopico(sq_topico,sq_et_comp,sq_et,vl_percentual):
    sql = []
    sql.append("insert into saet.rodada_valida_topico (sq_topico,sq_et_complemento,vl_percentual) values (" + str(sq_topico) + ", " + str(sq_et_comp)+ ", " + str(vl_percentual) + " )")
    dml_single(sql) 

def getRodadaTopicoItem(sq_et,sq_et_Complemento):
    sql = "select et.sq_et, et.ds_et, etc.tx_nome_documento,etc.tx_extensao, etc.sq_et_complemento,rvi.sq_item,item.nm_item,rvi.nr_rodada, rvi.in_verificacao,  "
    sql += " rvt.sq_topico,topico.ds_topico,rvt.vl_percentual,etc.dt_execucao, etc.cd_chave_id "
    sql += " from saet.et, saet.et_complemento etc, saet.rodada_valida_item rvi, saet.rodada_valida_topico rvt, saet.item, saet.topico "
    sql += " where et.sq_et = etc.sq_et  "
    sql += " and etc.sq_et_complemento = rvi.sq_et_complemento "
    sql += " and etc.sq_et_complemento = rvt.sq_et_complemento "
    sql += " and rvi.sq_item = item.sq_item "
    sql += " and rvt.sq_topico = topico.sq_topico "
    sql += " and item.sq_topico = topico.sq_topico "
    if sq_et_Complemento != 0:
        sql += " and etc.sq_et_complemento = " + str(sq_et_Complemento)
    else:
        sql += " and etc.sq_et_complemento =  (select max(a.sq_et_complemento) from et_complemento a, rodada_valida_topico b where a.sq_et_complemento = b.sq_et_complemento and sq_et = " + str(sq_et) + ")"    
    sql += " order by topico.sq_topico, item.sq_item "
    listaBD = consulta(sql)

    etList = []

    if len(listaBD) > 0:
        index = 0
        objET_DTO = ET_DTO()
        objET_DTO.sq_ET = listaBD[index][0]
        objET_DTO.sg_ET = listaBD[index][1]
        objET_DTO.dsc_ET = listaBD[index][1]
        objET_DTO.nm_arquivo = listaBD[index][2]
        objET_DTO.ext_arquivo = listaBD[index][3]
        objET_DTO.data_execucao = listaBD[index][12]
        objET_DTO.chave_usuario = listaBD[index][13]
        objET_DTO.in_tipoLista = "ET_Complemento"
        sq_topico = 0
        nrTopico = 0
        vl_Percentual = 0
        rodadaTopicList = []
        while index < len(listaBD):
            
            if sq_topico != listaBD[index][9]:
                if index > 0:
                    #adiciona a lista de objItem ao objTopico
                    objRodadaTopico_DTO.list_RodadaItem = rodadaItemList
                    #adiciona o objTopico a lista de tópicos
                    rodadaTopicList.append(objRodadaTopico_DTO)   

                nrTopico += 1
                objRodadaTopico_DTO = RodadaTopico_DTO()
                objRodadaTopico_DTO.sq_RodadaTopico = listaBD[index][9]
                objRodadaTopico_DTO.dsc_RodadaTopico = listaBD[index][10]
                objRodadaTopico_DTO.vl_Percentual = listaBD[index][11]
                vl_Percentual += listaBD[index][11]

                rodadaItemList = []
                objRodadaItem_DTO = RodadaItem_DTO()
                objRodadaItem_DTO.sq_RodadaItem = listaBD[index][5]
                objRodadaItem_DTO.nm_RodadaItem = listaBD[index][6]
                objRodadaItem_DTO.nr_RodadaTItem = listaBD[index][7]
                objRodadaItem_DTO.in_verificacao = ""
                objRodadaItem_DTO.dsc_RodadaItem = "Não identificado na análise"
                if listaBD[index][8] == "S":
                    objRodadaItem_DTO.in_verificacao = "complete"
                    objRodadaItem_DTO.dsc_RodadaItem = "Validado" 
                
                #adiciona o objItem na lista
                rodadaItemList.append(objRodadaItem_DTO)

            if sq_topico == listaBD[index][9]:
                objRodadaItem_DTO = RodadaItem_DTO()
                objRodadaItem_DTO.sq_RodadaItem = listaBD[index][5]
                objRodadaItem_DTO.nm_RodadaItem = listaBD[index][6]
                objRodadaItem_DTO.nr_RodadaTItem = listaBD[index][7]
                objRodadaItem_DTO.in_verificacao = ""
                objRodadaItem_DTO.dsc_RodadaItem = "Não identificado na análise"
                if listaBD[index][8] == "S":
                    objRodadaItem_DTO.in_verificacao = "complete"
                    objRodadaItem_DTO.dsc_RodadaItem = "Validado"

                #adiciona o objItem na lista
                rodadaItemList.append(objRodadaItem_DTO)
        
            sq_topico = listaBD[index][9]
            index += 1

        #finalizou o loop adiciona a lista de topico e itens a ET
        #adiciona a lista de objItem ao objTopico
        objRodadaTopico_DTO.list_RodadaItem = rodadaItemList
        #adiciona o objTopico a lista de tópicos
        rodadaTopicList.append(objRodadaTopico_DTO) 

        objET_DTO.list_RodadaTopico = rodadaTopicList 
        objET_DTO.vl_porcentagem = vl_Percentual/nrTopico

        etList.append(objET_DTO)

    return etList

def getETs(id_chave):
    
    sql  = "select et.sq_et, et.sg_et, ds_et, et.id_familia, etc.sq_et_complemento, etc.tx_nome_documento, etc.cd_chave_id, etc.dt_execucao, rvt.vl_percentual "
    sql += " from saet.et, "
    sql += "  saet.et_complemento etc, "
    sql += "  (select et.sq_et, max(etc.sq_et_complemento) as sq_et_complemento from saet.et, saet.et_complemento etc,  saet.rodada_valida_topico rvt where et.sq_et = etc.sq_et and rvt.sq_et_complemento = etc.sq_et_complemento group by et.sq_et) etsComp, "
    sql += "  (select sq_et_complemento, sum(vl_percentual)/count(sq_topico) as vl_percentual from saet.rodada_valida_topico group by sq_et_complemento) rvt "
    sql += " where et.sq_et = etc.sq_et "
    sql += " and et.sq_et = etsComp.sq_et "
    sql += " and etc.sq_et_complemento =  etsComp.sq_et_complemento "
    sql += " and etc.sq_et_complemento = rvt.sq_et_complemento "
    sql += " and LOWER(etc.cd_chave_id) = LOWER('" + str(id_chave) + "') "
    sql += " order by  etc.dt_execucao desc "

    listaBD = consulta(sql)
   
    etList = []
    index = 0
    sq_et = 0
    while index < len(listaBD):
        objET_DTO = ET_DTO()
        objET_DTO.sq_ET = listaBD[index][0]
        objET_DTO.sg_ET = listaBD[index][1]
        objET_DTO.dsc_ET = listaBD[index][1]
        objET_DTO.nm_arquivo = listaBD[index][5]
        objET_DTO.data_execucao = listaBD[index][7]
        objET_DTO.chave_usuario = listaBD[index][6]
        objET_DTO.vl_porcentagem = listaBD[index][8]
        objET_DTO.sq_et_Complemento = listaBD[index][4]
        objET_DTO.id_familia = listaBD[index][3]
        objET_DTO.in_tipoLista = "ETs_Analisadas"
        objET_DTO.list_RodadaTopico = ""
        etList.append(objET_DTO)

        index += 1
    return etList

def getEtComplementos(sq_ET):
    sql  = "select et.sq_et, et.sg_et, ds_et, et.id_familia, etc.sq_et_complemento, etc.tx_nome_documento, "
    sql += " etc.cd_chave_id, etc.dt_execucao, rvt.vl_percentual "
    sql += " from saet.et, saet.et_complemento etc, "
    sql += " (select sq_et_complemento, sum(vl_percentual)/count(sq_topico) as vl_percentual from saet.rodada_valida_topico group by sq_et_complemento) rvt "
    sql += " where et.sq_et = etc.sq_et "
    sql += " and etc.sq_et_complemento = rvt.sq_et_complemento "
    sql += " and et.sq_et = " + str(sq_ET) + " "
    sql += " order by  etc.dt_execucao desc "

    listaBD = consulta(sql)
   
    etList = []
    rodadaTopicList = []
    index = 0
    while index < len(listaBD):
        objET_DTO = ET_DTO()
        objET_DTO.sq_ET = listaBD[index][0]
        objET_DTO.sg_ET = listaBD[index][1]
        objET_DTO.dsc_ET = listaBD[index][1]
        objET_DTO.nm_arquivo = listaBD[index][5]
        objET_DTO.data_execucao = listaBD[index][7]
        objET_DTO.chave_usuario = listaBD[index][6]
        objET_DTO.vl_porcentagem = listaBD[index][8]
        objET_DTO.sq_et_Complemento = listaBD[index][4]
        objET_DTO.in_tipoLista = "ET_Complemento"
        objET_DTO.list_RodadaTopico = ""
        etList.append(objET_DTO)
        index += 1


    return etList

def deleteEtRodadaTopicoItem(sq_et_Complemento): 
    sql = []
    sql.append("delete from saet.rodada_valida_item where sq_et_complemento = " + str(sq_et_Complemento) + "")
    sql.append("delete from saet.rodada_valida_topico where sq_et_complemento = " + str(sq_et_Complemento) + "")
    dml_single(sql)    

def getIdET(sq_et_Complemento):
    sql = "select sq_et from saet.et_complemento where sq_et_complemento = " + str(sq_et_Complemento) + ""
    listaBD = consulta(sql)
    sq_et = listaBD[0][0]  

    return sq_et  




