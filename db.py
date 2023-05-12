# Google Sheet
import os
import pygsheets
gc = pygsheets.authorize(service_account_env_var="SERVICE_FILE")
db_d = gc.open_by_url(os.getenv("DB_URL"))[0]
db_t = gc.open_by_url(os.getenv("DB_URL"))[1]
bl = gc.open_by_url(os.getenv("DB_URL"))[2]
price_m = gc.open_by_url(os.getenv("DB_URL")).worksheet_by_title("price_mini")
price_l = gc.open_by_url(os.getenv("DB_URL")).worksheet_by_title("price_large")
deliver_fee = gc.open_by_url(os.getenv("DB_URL")).worksheet_by_title("price_deliver")

def is_in_d(id) -> bool:
    df = db_d.get_as_df()
    return id in df['id'].values

def where_d(id) -> int:
    df = db_d.get_as_df()
    return df[df['id'] == id].index[0]

def append(id, tmp: dict) -> bool:
    print(tmp)
    try:
        if tmp[id]['type'] == "deliver":
            db_d.append_table(values=[
                id, tmp[id]['total'], tmp[id]['amount_m'], tmp[id]['amount_l'], tmp[id]['sauce'], 
                tmp[id]['grade'], tmp[id]['class'], tmp[id]['number'], 
                tmp[id]['name'], tmp[id]['pos'], tmp[id]['note']
                ])
            tmp.pop(id, -1)
        else:
            return False
        return True
    except:
        return False
    
def is_ok(id) -> bool:
    '''
    if havn't reached 4 times or in blacklist
    '''

    return (list(db_d.get_as_df()['id']).count(id) < 4) and (list(db_t.get_as_df()['id']).count(id) < 4) and (id not in list(bl.get_as_df()))

def how_much_m(amount: int) -> dict:
    '''
    {
        "name": {amount: int, price: int},
    }
    '''
    df = price_m.get_as_df()

    l = {}
    i=0
    for price in df['price']:
        if amount // df.values[i][1]:
            l[df.values[i][0]] = {"amount": amount // df.values[i][1], "price": price * (amount // df.values[i][1])}
            amount = amount % df.values[i][1]
        i += 1

    print(l)
    #TODO
    
    return l
        
def how_much_l(amount: int) -> dict:
    '''
    {
        "name": {amount: int, price: int},
    }
    '''
    df = price_l.get_as_df()

    l = {}
    i=0
    for price in df['price']:
        if amount // df.values[i][1]:
            l[df.values[i][0]] = {"amount": amount // df.values[i][1], "price": price * (amount // df.values[i][1])}
            amount = amount % df.values[i][1]
        i += 1
    
    return l

def delete(i) -> bool:
    try:
        db_d.delete_rows(i)
        return True
    except:
        return False

def find_data(i: int):
    try:
        df = db_d.get_as_df()
        return df.values[i]
    except:
        return []
    
def get_deliver_fee() -> int:
    try:
        return int(deliver_fee.get_value('A1'))
    except:
        return -1