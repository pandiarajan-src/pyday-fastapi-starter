import random

import fastapi

app = fastapi.FastAPI()


@app.get("/generate_name", responses={404: {}})
async def generate_name(max_length: int = None, starts_with: str = None):
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if max_length:
        names = [name for name in names if len(name) <= max_length]
    if starts_with:
        names = [name for name in names if name.startswith(starts_with)]
    if len(names) == 0 or max_length == 0:
        raise fastapi.HTTPException(404, detail="No names with the length of zero.")
    random_name = random.choice(names)
    return {"name": random_name}
