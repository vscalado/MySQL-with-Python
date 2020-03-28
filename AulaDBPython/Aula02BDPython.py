# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd=''
)

# Verificando quais bancos de dados estão criados.
cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)
