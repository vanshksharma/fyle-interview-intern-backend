def test_invalid_header(client,invalid_header):
    response = client.get(
        '/teacher/assignments',
        headers=invalid_header
    )

    assert response.status_code == 400
    data = response.json

    assert data['error'] == 'JSONParseException'

def test_no_principal(client,no_principal):
    response = client.get(
        '/teacher/assignments',
        headers=no_principal
    )

    assert response.status_code == 401
    data = response.json

    assert data['error'] == 'FyleError'

def test_empty_teacher_id(client,empty_teacher_id):
    response = client.get(
        '/teacher/assignments',
        headers=empty_teacher_id
    )

    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'

def test_empty_student_id(client,empty_student_id):
    response = client.get(
        '/student/assignments',
        headers=empty_student_id
    )

    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'