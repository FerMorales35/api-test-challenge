def test_sad_path(api):
    response = api.post_person("")
    assert response.status_code == 401
    print("Error: falta personId - status 401 OK")