from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Allows React frontend to call the FastAPI backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample API endpoint that returns data
@app.get("/api/message")
async def get_message(name, age):
    return {"message": f"Hello I am {name} and have age {age}"}  # Auto-converts to JSON



# Run with: uvicorn main:app --reload
