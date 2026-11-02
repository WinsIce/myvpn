from fastapi import FastAPI

app = FastAPI(title="MyVPN Demo API")

SERVERS = [
    {"id": "germany", "name": "Germany", "city": "Frankfurt", "status": "demo"},
    {"id": "netherlands", "name": "Netherlands", "city": "Amsterdam", "status": "demo"},
    {"id": "finland", "name": "Finland", "city": "Helsinki", "status": "demo"}
]

@app.get("/")
def home():
    return {"app": "MyVPN", "version": "0.1.0"}

@app.get("/api/servers")
def get_servers():
    return {"servers": SERVERS}

@app.get("/api/status")
def get_status():
    return {"connected": False, "mode": "demo"}