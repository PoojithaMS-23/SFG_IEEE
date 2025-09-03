from bson import ObjectId
from database import collection
from models import PersonCreate
from typing import List

def serialize_person(person) -> dict:
    person["id"] = str(person["_id"])
    del person["_id"]
    return person

async def create_person(person: PersonCreate) -> dict:
    person_dict = person.model_dump()
    result = await collection.insert_one(person_dict)
    new_person = await collection.find_one({"_id": result.inserted_id})
    return serialize_person(new_person)

async def get_all_persons() -> List[dict]:
    persons = []
    async for person in collection.find():
        persons.append(serialize_person(person))
    return persons

async def get_person_by_id(person_id: str) -> dict:
    person = await collection.find_one({"_id": ObjectId(person_id)})
    if person:
        return serialize_person(person)
    return None

async def update_person(person_id: str, person_update: PersonCreate):
    update_result = await collection.update_one(
        {"_id": ObjectId(person_id)},
        {"$set": person_update.model_dump()}  # use model_dump() if Pydantic v2
    )
    if update_result.modified_count == 1:
        updated_person = await collection.find_one({"_id": ObjectId(person_id)})
        return serialize_person(updated_person)
    return None