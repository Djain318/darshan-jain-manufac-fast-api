from fastapi import FastAPI, Response  
import uuid                            
import httpx                           
import asyncio                         

app = FastAPI(
    title="DockFastID API",
    description="A Dockerized FastAPI server for generating UUIDs and serving random cat images.",
    version="0.1.0"
)

@app.get(
    "/uuid",
    summary="Generate UUID",
    description="Returns a new UUID version 4 as a string each time it's requested."
)
def get_uuid():
    return str(uuid.uuid4())

@app.get(
    "/async-uuid",
    summary="Generate UUID (Async)",
    description="Returns a new UUID version 4 after a non-blocking 3-second delay."
)
async def get_async_uuid():
    await asyncio.sleep(3)
    return str(uuid.uuid4())

@app.get(
    "/cat",
    summary="Get Random Cat Image",
    description="Fetches a random cat image from the external API https://cataas.com/cat and returns it as a JPEG image."
)
async def get_cat():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://cataas.com/cat")
            response.raise_for_status()
        return Response(content=response.content, media_type="image/jpeg")
    except:
        return Response(status_code=204)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
