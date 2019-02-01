import mp_db
import mp_requests
import mp_flask
from mp_db import Session


if __name__ == '__main__':
    mp_flask.app.run()

def add_catalog(_response):

    session1 = Session()
    for rw in _response:
        catalog = mp_db.Catalog(rw["Code"], rw["Name"], rw["Category"])
        session1.add(catalog)
    session1.commit()
    print("commit")


request_data = mp_requests.get_catalog_request_data()
request_data["GetStock"] = False
response = mp_requests.get_catalog(request_data)
for pr in response.get("Data"):
    print(pr)

result = mp_db.engine.execute("select * from Catalog")
cat = result.fetchall()
print("Товары", len(cat), "шт.")

add_catalog(response.get("Data"))

result = mp_db.engine.execute("select * from Catalog")
cat = result.fetchall()
print("Товары", len(cat), "шт.")


