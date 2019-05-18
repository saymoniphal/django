import requests
import random
import string

def test_customer():
    # generate random name and cell
    name = ''.join(random.choices(string.ascii_letters, k=5))
    cell = ''.join(random.choices(string.digits, k=9))
    resp = requests.post('http://localhost:8000/customers/',
                        json={"name": name, "dob": "1980-01-01", "gender": "F",
                              "cell": cell, "email": name+"@email.com"})
    print(resp)
    print(requests.get('http://localhost:8000/customers').json())

    # get customer with id=1
    print(requests.get('http://localhost:8000/customers/1').json())

test_customer()
