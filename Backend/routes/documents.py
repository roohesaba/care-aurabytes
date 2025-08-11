from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from storage import documents

router = APIRouter()

class Document(BaseModel):
    title: str
    content: str

# CREATE
@router.post("/documents")
def upload_document(doc: Document):
    new_doc = doc.dict()
    new_doc["id"] = len(documents) + 1
    documents.append(new_doc)
    return {"message": "Document uploaded", "document": new_doc}

# READ - all documents
@router.get("/documents")
def get_documents():
    return {"documents": documents}

# READ - single document
@router.get("/documents/{doc_id}")
def get_document(doc_id: int):
    for d in documents:
        if d["id"] == doc_id:
            return d
    raise HTTPException(status_code=404, detail="Document not found")

# UPDATE
@router.put("/documents/{doc_id}")
def update_document(doc_id: int, doc: Document):
    for d in documents:
        if d["id"] == doc_id:
            d.update(doc.dict())
            return {"message": "Document updated", "document": d}
    raise HTTPException(status_code=404, detail="Document not found")

# DELETE
@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int):
    for i, d in enumerate(documents):
        if d["id"] == doc_id:
            documents.pop(i)
            return {"message": "Document deleted"}
    raise HTTPException(status_code=404, detail="Document not found")

# EXTRA FEATURE - Search
@router.get("/documents/search")
def search_documents(query: str):
    result = [d for d in documents if query.lower() in d["title"].lower() or query.lower() in d["content"].lower()]
    return {"results": result}

# EXTRA FEATURE - QR Code Placeholder
@router.post("/documents/{doc_id}/qrcode")
def generate_qrcode(doc_id: int):
    return {"message": f"QR code generated for document {doc_id}"}

# EXTRA FEATURE - Share Link Placeholder
@router.get("/documents/{doc_id}/share")
def share_document(doc_id: int):
    return {"message": f"Share link generated for document {doc_id}"}
