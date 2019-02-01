import requests
import mp_db

url_server = 'http://10.80.178.184/UT_dev5_'


def get_catalog_request_data():
    return {
           "Filter":    {
              "CategoryName": [],
              "CategoryCode": [],
              "ProductName": [],
              "ProductCode": []
           },
           "GetPrice": True,
           "GetStock": False,
           "Modified": False,
           "Fields": [
               "InStock",
               "Available",
               "Reserve"
           ]
        }


def get_category_request_data():
    return {
            "Modified": False,
            "FilterID": [],
            "FilterName": []
            }


def get_order_status_data():
    return {
            "OrderNum": "1",
            "GetTable": False
            }


def get_catalog(_catalog_request_data):
    url = url_server + '/hs/LM_B2B_Portal/v1/GetProduct'
    headers = {'Content-type': 'application/json'}

    rsp = requests.post(url, auth=('WS', ''), json=_catalog_request_data, headers=headers)
    if rsp.status_code == 200:
        print("GetProduct: success")
    else:
        print("GetProduct: Error (status_code = %r)" % rsp.status_code)
    return rsp.json()


def get_category(_category_request_data):
    url = url_server + '/hs/LM_B2B_Portal/v1/GetCategories'
    headers = {'Content-type': 'application/json'}

    rsp = requests.post(url, auth=('WS', ''), json=_category_request_data, headers=headers)
    if rsp.status_code == 200:
        print("GetCategories: success")
    else:
        print("GetCategories: Error (status_code = %r)" % rsp.status_code)
    return rsp.json()


def get_order_status(_order_status_request_data):
    url = url_server + '//hs/LM_B2B_Portal/v1/GetOrderStatus'
    headers = {'Content-type': 'application/json'}

    rsp = requests.post(url, auth=('WS', ''), json=_order_status_request_data, headers=headers)
    if rsp.status_code == 200:
        print("GetOrder: success")
    else:
        print("GetOrder: Error (status_code = %r)" % rsp.status_code)
    print(rsp.json())
    return rsp.json()


def add_categories(count):
    request_data = get_category_request_data()
    response = get_category(request_data)
    session1 = mp_db.Session()
    for rw in response.get("Data"):
        count -= 1
        print(rw)
        catalog = mp_db.Category(rw["Category"], rw["Level"])
        session1.add(catalog)
        if count == 1:
            break
    session1.commit()


def add_catalog(count):
    request_data = get_catalog_request_data()
    response = get_catalog(request_data)
    session1 = mp_db.Session()
    for rw in response.get("Data"):
        count -= 1
        print(rw)
        catalog = mp_db.Catalog(rw["Code"], rw["Name"], rw["Category"])
        session1.add(catalog)
        if count == 1:
            break
    session1.commit()
