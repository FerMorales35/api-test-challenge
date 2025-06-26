import pyodbc # para sql server como ejemplo

def obtener_personId_db(person_id):
    #Dejo los campos vacios para completar con los datos necesarios para la conexion con la DB
    conn = pyodbc.connect(
        host="",
        database="",
        user="",
        password=""
    )
    cursor = conn.cursor()
    query = f"SELECT * FROM Worldsys WHERE personId = {person_id}"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result