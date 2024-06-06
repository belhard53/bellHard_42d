from pydantic import BaseModel, ValidationError

class Tag(BaseModel):
    id: int
    tag: str



class City(BaseModel):
    city_id: int
    name: str
    population: int
    tags: list[Tag]

input_json = """
{
    "city_id": 12,
    "name": "Minsk",
    "population": 2000000,
    "tags": [
        {"id":1, "tag":"Capital"},
        {"id":2, "tag":"river"}
    ]
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print(e.json())
else:
    print(city)
    print(city.tags[1].tag)