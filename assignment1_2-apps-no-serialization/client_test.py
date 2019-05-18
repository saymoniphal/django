import requests

def test_customer():
    print(requests.get('http://localhost:8000/customers').json())

    resp = requests.post('http://localhost:8000/customers')

test_customer()
