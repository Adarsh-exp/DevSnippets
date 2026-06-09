from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from typing import Annotated, List, Optional
import json


app = FastAPI()

class Snippet(BaseModel):
    title: Annotated[str, Field(..., description="Title of the snippet")]
    code: Annotated[str, Field(..., description="The code of the snippet")]
    language: Annotated[str, Field(..., description="Programming language")]
    tags: List[str] = []
    details: Annotated[Optional[str], Field(default=None, description="Extra details")]

class SnippetUpdate(BaseModel):
    title: Annotated[Optional[str], Field(default=None, description="Title of the snippet")]
    code: Annotated[Optional[str], Field(default=None, description="The code of the snippet")]
    language: Annotated[Optional[str], Field(default=None, description="Programming language")]
    tags: Optional[List[str]] = None
    details: Annotated[Optional[str], Field(default=None, description="Extra details")]

def load_data():
    with open('Snippets.json', 'r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open("Snippets.json", 'w') as f:
        json.dump(data, f)


@app.get('/')
def root():
    return "This is Dev Snippets Api"

@app.get('/all_snippets')
def view():
    return load_data()

@app.post('/create_post')
def create(snippet: Snippet):
    data = load_data()
    newData = snippet.model_dump()

    if any(s['title'] == snippet.title for s in data.values()):
        raise HTTPException(status_code=400, detail=f"{snippet.title} Already Exists")

    if data:
        new_id = str(max(int(k) for k in data.keys()) + 1)
    else:
        new_id = "1"

    data[new_id] = newData
    save_data(data)
    return {new_id: newData}

@app.put('/update/{id}')
def update(id: str, snippet_update: SnippetUpdate):
    data = load_data()

    if id not in data:
        raise HTTPException(status_code=404, detail=f"Snippet id {id} not found")

    updated = data[id]
    update_fields = snippet_update.model_dump(exclude_none=True)
    updated.update(update_fields)

    data[id] = updated
    save_data(data)
    return updated


@app.get('/view')
def view(tags: str = Query(..., description="Search all the codes with this tag")):
    data = load_data()

    result = {id: snippet for id, snippet in data.items() if tags in snippet['tags']}

    if not result:
        raise HTTPException(status_code=404, detail=f"No snippets found with tag '{tags}'")

    return result

@app.delete('/delete/{id}')
def delete(id: str):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        return JSONResponse(status_code=200, content = {'message': 'deleted successfully'}) 
    else:
        raise HTTPException(status_code= 404, detail=f"No snippet of {id} found")