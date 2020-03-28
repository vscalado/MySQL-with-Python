# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='twdbd'
)
#Criando Tabelas- Tabela criada comalexandria com as colunas nome e arma
cursor = conexao.cursor()
cursor.execute('CREATE TABLE comalexandria(nome VARCHAR(255), arma VARCHAR(255))')