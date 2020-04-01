import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()

def create_table(): #Cria uma nova tabela no banco de Dados tutorial1.db
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
#A nova tabela tem o nome stuffToPlot com as colunas unix(REAL), datestamp(TEXT), keyword(TEXT) e value(REAL)

def data_entry(): #Fução para inserir valores dentro da tabela stuffToPlot
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    # Sintax- INSERT INTO *nomedatabela* VALUES(Parametros conforme as colunas da tabela)

    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = int(time.time())
    print(unix)
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    print(date)
    keyword = 'Python'
    value = random.randrange(0, 10)

    c.execute('INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)',
              (unix, date, keyword, value))

    conn.commit()

#create_table()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

c.close()
conn.close()



#data_entry()