import json
import uvicorn
from fastapi import FastAPI
from pathlib import Path
import uuid

shopping_list = Path('db/shopping_list.json')

app = FastAPI()

@app.get('/items')
def get_items(name, quantity):
    with open('db/shopping_list.json', 'r') as file:
        items = file.read()
    return json.loads(items)


@app.post('/items')
def add_item(item : dict):
    if 'name' not in item or 'quantity' not in item:
        return {'message' : 'Error: Invalid item'}

    item['id'] = uuid.uuid4()

    if not shopping_list.exists():
        with open(shopping_list, 'w') as f:
            f.write('[]')

    with open('db/shopping_list.json', 'w+') as file:
        items = json.loads(file.read())
        items.append(item)
        file.write(items)
    return {'message' : 'success'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000)