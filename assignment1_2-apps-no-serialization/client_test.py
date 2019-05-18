import requests
import random
import string

def test_customer():
    # generate random name and cell number
    print("Sending request to create customer")
    name = ''.join(random.choices(string.ascii_letters, k=5))
    cell = ''.join(random.choices(string.digits, k=9))
    resp = requests.post('http://localhost:8000/customers/',
                        json={"name": name, "dob": "1980-01-01",
                              "gender": random.choice(["F", "M"]),
                              "cell": cell, "email": name+"@email.com"})
    print(resp)

    # get all customers
    print("\nGetting all customers: http://localhost:8000/customers")
    customers = requests.get('http://localhost:8000/customers')
    print(customers.text)

    # get customer with a random id within customers list
    cust_id = random.choice([c['id'] for c in customers.json()])
    print("\nGetting customer with id {}".format(cust_id))
    res = requests.get('http://localhost:8000/customers/{}'.format(cust_id))
    print(res)


    # update customer
    cust_id = random.choice([c['id'] for c in customers.json()])
    print("\nSending request to update customer id {}".format(cust_id))
    resp = requests.put('http://localhost:8000/customers/{}'.format(cust_id),
                 json={"name": "Customer{}".format(cust_id),
                       "email": "customer{}@email.com".format(cust_id)})
    print(resp)

    # delete a customer
    cust_id = random.choice([c['id'] for c in customers.json()])
    print("\nSending request to delete customer id {}".format(cust_id))
    resp = requests.delete('http://localhost:8000/customers/{}'.format(cust_id))
    print(resp)

if __name__ == "__main__":
    test_customer()
