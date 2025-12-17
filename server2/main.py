import json
import uvicorn
from fastapi import FastAPI
from pathlib import Path
import uuid

shopping_list = Path('db/shopping_list.json')

backup = Path('data/backup_shopping_list.json')

app = FastAPI()



def read_file(file):
    try:
        with open(file, 'r') as f:
            return json.loads(f.read())
    except Exception as e:
        return {'Error' : e}


def write_file(file, content, mode=None):
    try:
        with open(file, 'w+') as f:
            items = f.read()
            if mode:
                if items:
                    items += content
                    return True
            f.write(content)
            return True

    except Exception as e:
        return {'Error' : e}



@app.get('/items')
def get_items():
    items = read_file(shopping_list)
    return items


@app.post('/items')
def add_item(item : dict):
    if 'name' not in item or 'quantity' not in item:
        return {'message' : 'Error: Invalid item'}

    item['id'] = uuid.uuid4()

    if not shopping_list.exists():
        write_file(shopping_list, '[]')

    items = read_file(shopping_list)
    if 'Error' in items:
        return items
    items.append(item)
    write_file(shopping_list, items)
    return {'message' : 'item saved successfully'}


@app.get('/backup')
def get_items_from_mount():
    items = read_file(backup)
    return items


@app.post('/backup/save')
def save_items_in_backup():
    items = read_file(shopping_list)
    if 'Error' in items:
        return items
    write_file(backup, items)
    return {'message' : 'saved successfully'}



if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8001)