# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='twdbd'
)
#Mostrar todas as tabelas criadad no BD twdbd
cursor = conexao.cursor()
cursor.execute('SHOW TABLES')

for x in cursor:
    print(x)