from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader

app = FastAPI()

# Allow CORS for local Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    # Read PDF
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # Avoid None
    return {"filename": file.filename, "content": text.strip()}

@app.get("/")
def root():
    return {"message": "PyPDF RAG API is running"}
