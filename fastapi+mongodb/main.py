from fastapi import FastAPI, HTTPException
from models import PersonCreate, PersonOut
import crud

app = FastAPI()

@app.post("/persons", response_model=PersonOut)
async def create_person(person: PersonCreate):
    return await crud.create_person(person)

@app.get("/persons", response_model=list[PersonOut])
async def get_persons():
    return await crud.get_all_persons()

@app.get("/persons/{person_id}", response_model=PersonOut)
async def get_person(person_id: str):
    person = await crud.get_person_by_id(person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.put("/persons/{person_id}", response_model=PersonOut)
async def update_person(person_id: str, person_update: PersonCreate):
    updated_person = await crud.update_person(person_id, person_update)
    if not updated_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return updated_person