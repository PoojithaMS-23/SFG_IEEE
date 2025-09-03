from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: Optional[int] = None
    bio: Optional[str] = None


class PersonCreate(PersonBase):
    pass


class PersonOut(PersonBase):
    id: str = Field(..., alias="id")  # Use 'id', not '_id'

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "id": "64f7e3b214d2a79e6d37b9a2",
                "first_name": "Alice",
                "last_name": "Smith",
                "email": "alice@example.com",
                "age": 30,
                "bio": "Software developer and tech enthusiast."
            }
        }
    }
