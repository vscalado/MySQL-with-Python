# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd=''
)

# Criando o Banco de Dados THE WALKING DEAD (twdbd)
cursor = conexao.cursor()
cursor.execute('CREATE DATABASE twdbd')
