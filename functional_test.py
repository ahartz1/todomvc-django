import requests


def test_get_api_root():
    res = requests.get('http://127.0.0.1:8080/api')

    assert res.status_code == 200
    assert 'http://127.0.0.1:8080/api/todos/' in res.text


def test_get_todos_api():
    res = requests.get('http://127.0.0.1:8080/api/todos')

    assert res.status_code == 200
    assert 'eat more sauce' in res.text

    # with open('test.txt', 'w') as f:
    #     f.write(res)

if __name__ == '__main__':
    test_creation_of_todo()
