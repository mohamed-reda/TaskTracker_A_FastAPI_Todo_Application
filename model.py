from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel


class TodoBase(BaseModel):
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)


class TodoCreate(TodoBase):
    item: str = Form(...)


class TodoInDB(TodoBase):
    id: int


class Todo(TodoInDB):
    pass

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


class TodoItem(TodoBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
