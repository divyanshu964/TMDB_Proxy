from fastapi import FastAPI, Request
import requests, os

app = FastAPI()

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

@app.get("/")
def root():
    return {"message": "TMDb Proxy is running!"}

@app.get("/movies")
def get_movies():
    url = "https://api.themoviedb.org/3/discover/movie?language=hi-IN&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    r = requests.get(url, headers=headers, timeout=20)
    return r.json()

@app.get("/tv")
def get_tv():
    url = "https://api.themoviedb.org/3/discover/tv?language=hi-IN&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    r = requests.get(url, headers=headers, timeout=20)
    return r.json()

# Optional: forward all query params to TMDB
@app.get("/proxy/{path:path}")
def proxy(path: str, request: Request):
    url = f"https://api.themoviedb.org/3/{path}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    r = requests.get(url, headers=headers, params=dict(request.query_params), timeout=20)
    return r.json()
