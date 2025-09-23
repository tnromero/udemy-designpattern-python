import sqlite3

def _executar(query: str):
    db_path = './geek.university'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    resultado = None

    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        connection.commit()
    except Exception as excp:
        print(f'Erro na execução da query: {excp}')
    finally:
        connection.close()
    
    return resultado

"""
resultado = [(1, 'PlayStation 5', 1244), (2, 'Xbox 360', 1445) ]
"""
