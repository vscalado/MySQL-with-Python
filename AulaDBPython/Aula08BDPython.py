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

com_sql = 'INSERT INTO comalexandria(nome,arma) VAlUES (%s,%s)'
valor = ('Ronie', 'Espada')
print(com_sql, valor)
cursor.execute(com_sql,valor)

conexao.commit()
print (cursor.rowcount,'inserido com sucesso')
