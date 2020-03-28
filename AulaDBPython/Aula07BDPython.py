# Importando a biblioteca PyMySQL
import pymysql

# Criando a conexao com o servidor

conexao = pymysql.connect(
    host='localhost',   #Servidor
    user='root',        #Usuario
    passwd='',          #Senha
    database='twdbd'    #Nome do Banco de dados
)

#Execução de comandos

cursor = conexao.cursor()
cursor.execute('ALTER TABLE comsalvadores ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
