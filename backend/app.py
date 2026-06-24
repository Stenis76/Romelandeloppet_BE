from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

# Ladda .env så vi får in URL + KEY
load_dotenv()

# Hämta miljövariabler
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Skapa Supabase-klienten
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Starta FastAPI-appen
app = FastAPI()

# Modell för anmälan (så FastAPI vet vilka fält som ska tas emot)
class Anmalan(BaseModel):
    fornamn: str
    efternamn: str
    email: str
    fodelsear: int
    klass: str
    kategori: str
    mobil: str

# Endpoint för att ta emot anmälningar
@app.post("/api/anmalan")
def anmalan(data: Anmalan):
    print("MOTTAGET:", data.dict())  # logg

    response = supabase.table("anmalningar").insert(data.dict()).execute()

    print("SUPABASE RESPONSE:", response)  # logg

    return {"status": "ok", "saved": response.data}
