import requests


def test_get_api_root():
    res = requests.get('http://127.0.0.1:8080/api')

    assert res.status_code == 200
    assert 'http://127.0.0.1:8080/api/todos/' in res.text


# Define the url to the todo api for all subsequent tests to use
todo_url = 'http://127.0.0.1:8080/api/todos/'


def test_get_todos_api():
    res = requests.get(todo_url)

    assert res.status_code == 200
    assert 'eat more sauce' in res.text


def test_post_todos_api():
    task = {'title': 'shovel snow'}
    res = requests.post(todo_url, data=task)

    assert res.status_code == 201
    assert 'shovel snow' in res.text


    # with open('test.txt', 'w') as f:
    #     f.write(res)
