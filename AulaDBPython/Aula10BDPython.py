# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',   #Servidor
    user='root',        #Usuario
    passwd='',          #Senha
    database='twdbd'    #Nome do Banco de dados
)

'''cursor = conexao.cursor()
cursor.execute('SELECT arma, nome FROM comalexandria')

resultado = cursor.fetchall()
for x in resultado:
    print(x)'''

cursor = conexao.cursor()
cursor.execute("SELECT * FROM comalexandria where arma = 'Besta'")

resultado = cursor.fetchall()
for x in resultado:
    print(x)