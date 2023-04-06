import pytest
import json
from tests import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers

@pytest.fixture
def invalid_teacher():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': "1 2",
            'user_id': 3
        })
    }

    return headers

@pytest.fixture
def no_teacher():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 12,
            'user_id': 15
        })
    }

    return headers

@pytest.fixture
def no_principal():
    headers = {}

    return headers

@pytest.fixture
def empty_teacher_id():
    headers = {
        'X-Principal': json.dumps({
            'user_id': 15
        })
    }

    return headers

@pytest.fixture
def empty_student_id():
    headers = {
        'X-Principal': json.dumps({
            'user_id': 15
        })
    }

    return headers

@pytest.fixture
def invalid_header():
    headers = {
        'X-Principal': "{'user_id': 15, teacher_id:}"
    }

    return headers
