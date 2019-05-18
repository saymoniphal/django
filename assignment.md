1. Design webservices for the below requirements.
	create a project CLOUDdatacenter, and virtualmachine app

- req:  http://127.0.0.1:8000/get_temp/  
response: your processor temperature
- req:  http://127.0.0.1:8000/get_ram/  
response: Total: 8GB, using:3GB available:5GB
- req:  http://127.0.0.1:8000/get_numberofCPUS/  
response: 4CORES
- req:  http://127.0.0.1:8000/get_hdd/
response: Total: 1TB, Used: 300GB, available: 700GB 


2. Create sales app which contains Customer model(name, age, address, cell, email).
  do makemigrations and migrate to default DB (sqlite).
The app should be able to handle CRUD (Create/Retrive/Update/Delete) with below endpoints:
- GET: http://127.0.0.1:8000/customers or http://localhost:8000/customers
- POST:  http://localhost:8000/customers/<id>
- PUT:  http://localhost:8000/customers/<id>
- DELETE:  http://localhost:8000/customers/<id>
