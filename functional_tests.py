import requests


def test_creation_of_todo():
    res = requests.get('http://127.0.0.1:8080/api')

    print(res.text)

    # with open('test.txt', 'w') as f:
    #     f.write(res)

if __name__ == '__main__':
    test_creation_of_todo()
