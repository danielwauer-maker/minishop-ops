from fastapi import FastAPI

app = FastAPI(title="MiniShop Ops")

@app.get("/health")
def health():
    return {"status": "ok"}
