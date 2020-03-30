# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',   #Servidor
    user='root',        #Usuario
    passwd='',          #Senha
    database='twdbd'    #Nome do Banco de dados
)

cursor = conexao.cursor()
con_sql = "UPDATE comalexandria SET arma = 'Pistola' WHERE nome = 'Gleen'"
cursor.execute(con_sql)
conexao.commit()
print(cursor.rowcount,"Tabela Modificada e Gravada")
