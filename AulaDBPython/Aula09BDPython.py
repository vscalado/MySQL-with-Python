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
valor = [
    ('Gleen', 'Pistola'),
    ('Daryl', 'Besta'),
    ('Carol', 'Metralhadora')
    ]

cursor.executemany(com_sql,valor)

conexao.commit()
print (cursor.rowcount,'Inserido com sucesso')