from db.db_utils import obtener_personId_db

def test_happy_path(api, person_id):
    response = api.post_person(person_id)
    assert response.status_code == 200
    print(f"Codigo de respuesta de la peticcion es 200 para personId {person_id}")


    db_result = obtener_personId_db(person_id)

    if db_result:
        print(f"El personId {person_id} fue insertado exitosamente en la DB.")
    else:
        print(f"Error: El personId {person_id} no fue encontrado en la DB.")
    
    assert len(db_result) > 0