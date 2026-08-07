from hashlib import blake2s
from pathlib import Path

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

from app.engine import calculate_chart
from app.models import ChartRequest
from app.glossary import as_dict as glossary_dict

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
STATIC_DIR = Path("app/static")


def static_url(request: Request, path: str) -> str:
    """Return a content-fingerprinted static URL for safe long-lived caching."""
    digest = blake2s((STATIC_DIR / path).read_bytes(), digest_size=8).hexdigest()
    return f"{request.url_for('static', path=path)}?v={digest}"


templates.env.globals["static_url"] = static_url


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/glossary", response_class=HTMLResponse)
async def glossary(request: Request):
    """Dedicated glossary page — data injected server-side."""
    return templates.TemplateResponse(
        "glossary.html",
        {"request": request, "glossary": glossary_dict()},
    )


@app.get("/api/glossary", response_class=JSONResponse)
async def glossary_json():
    """Raw glossary data as JSON for programmatic access."""
    return JSONResponse(content=glossary_dict())


@app.post("/calculate", response_class=JSONResponse)
async def calculate(req: ChartRequest):
    """Single entry point — dispatches on req.method."""
    try:
        result = calculate_chart(
            req.date, req.time, req.city,
            name=req.name, method=req.method,
        )
    except (ValueError, LookupError) as exc:
        return JSONResponse(status_code=422, content={"error": str(exc)})
    except ConnectionError as exc:
        return JSONResponse(status_code=503, content={"error": str(exc)})
    return JSONResponse(content=result)
