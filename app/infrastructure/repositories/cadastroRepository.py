from infrastructure.contexts.connect import consulta,dml_single_blob, dml_single
import os
import io

def manterItem(sq_topico,sq_item,nm_item,ds_item,tx_observacao,id_familia):
    try:
        sql = []
        if sq_item == "0":
            if id_familia == "0":
                sql.append("insert into saet.item (sq_item, sq_topico, nm_item,ds_item,tx_observacao) values (saet.seq_sq_item.nextval, " + str(sq_topico) + ", '"+ str(nm_item) +"', '"+ str(ds_item) +"', '" + str(tx_observacao)  + "')" )
            else:    
                sql.append("insert into saet.item (sq_item, sq_topico, nm_item,ds_item,tx_observacao,id_familia) values (saet.seq_sq_item.nextval, " + str(sq_topico) + ", '"+ str(nm_item) +"', '"+ str(ds_item) +"', '" + str(tx_observacao)  + "', " + str(id_familia) + ")" )
        else:
            if id_familia != "0":
                sql.append("update saet.item set nm_item = '" + str(nm_item) + "', ds_item= '" + str(ds_item) + "', tx_observacao='" + str(tx_observacao) + "', id_familia=" + str(id_familia) + " where sq_item =" + sq_item + " ")    
            else:
                sql.append("update saet.item set nm_item = '" + str(nm_item) + "', ds_item= '" + str(ds_item) + "', tx_observacao='" + str(tx_observacao) + "' where sq_item =" + sq_item + " ")

        dml_single(sql) 

        return "success"
    except Exception as e:
        return "Atenção: Ocorreu um erro ao realizar a operação: " + str(e)


def excluiItem(sq_item): 
    #try:
        sql = "Select * from saet.Rodada_valida_item where sq_item =" + str(sq_item) + ""
        listaBD = consulta(sql)  

        print(len(listaBD))
        
        if len(listaBD) == 0:
            sql = []   
            sql.append("delete from saet.item where sq_item =" + sq_item + "")
            dml_single(sql) 

            return "success"     
        else:   
            return "Atenção: Não é possível excluir o item, existe análise de ET associada." 
        
    #except Exception as e:
        #return "Atenção: Ocorreu um erro ao realizar a operação: " + str(e)