from pydantic import BaseModel, Field
from typing import Optional, List


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=10, max_length=40)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
        "example": {
        "id": 1,
        "title": "Mi Pelicula",
        "overview": "excelente pelicula",
        "year": 2023,
        "rating": 9.3,
        "category": "Accion"
        }
    }

movies = [{

    "id": 1,
    "title": "Mi Peli",
    "overview": "excelente esta pelicula",
    "year": "2021",
    "rating": "8.0",
    "Category": "Accion"
},
{
        "id": 2,
        "title": "Mi Pelicula",
        "overview": "excelente esta pelicula",
        "year": "2021",
        "rating": "7.0",
        "Category": "Accion"
    }
]

