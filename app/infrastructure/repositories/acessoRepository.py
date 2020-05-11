from infrastructure.contexts.connect import consulta,dml_single_blob, dml_single
import os
import io


def getAcessoPerfil(CD_CHAVE_ID):
    sql  = " SELECT UP.SQ_USUARIO_PERFIL, UP.CD_CHAVE_ID, P.SQ_PERFIL, P.DS_PERFIL " 
    sql += " FROM SAET.USUARIO_PERFIL UP, SAET.PERFIL P "
    sql += " WHERE LOWER(UP.CD_CHAVE_ID) =  LOWER('" + CD_CHAVE_ID + "') "
    sql += " AND UP.SQ_PERFIL = P.SQ_PERFIL "
    
    index = 0
    listaPerfil = []
    acesso = consulta(sql)
    while index < len(acesso):
        listaPerfil.append(acesso[index][3])
        index +=1

    return listaPerfil

     
