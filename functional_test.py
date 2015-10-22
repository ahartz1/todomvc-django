import json
import requests


def test_get_api_root():
    res = requests.get('http://127.0.0.1:8080/api')

    assert res.status_code == 200
    assert 'http://127.0.0.1:8080/api/todos/' in res.text


# Define the url to the todo api for all subsequent tests to use
todos_url = 'http://127.0.0.1:8080/api/todos/'


def test_delete_all_todos_api():
    starting_tasks = requests.get(todos_url).json()
    for task in starting_tasks:
        requests.delete(task['url'])

    ending_tasks = requests.get(todos_url).json()
    print(ending_tasks)
    assert len(ending_tasks) == 0


def test_post_todos_api():
    task = {'title': 'shovel snow'}
    res = requests.post(todos_url, data=task)

    assert res.status_code == 201
    assert 'shovel snow' in res.text



def test_get_todos_api():
    res = requests.get(todos_url)

    assert res.status_code == 200
    assert 'shovel snow' in res.text


def test_delete_todos_api():
    res = requests.get(todos_url).json()
    task_url = res[-1]['url']
    res_del = requests.delete(task_url)

    assert res_del.status_code == 204


    # with open('test.txt', 'w') as f:
    #     f.write(res)
