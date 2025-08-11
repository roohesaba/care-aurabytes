
# API_CONTRACT.md – Care App

This document defines the "contract" between the frontend and backend for the Care App. It is the single source of truth for all API communication.

---

## Features & Endpoints

---

### Authentication

#### 1. User Registration
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/auth/register`
- **Description:** Registers a new user.
- **Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```
- **Success Response (200 OK):**
```json
{
  "message": "User registered successfully",
  "userId": "abc123"
}
```
- **Error Responses:**
```json
{
  "error": "Email already exists"
}
```

#### 2. User Login
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/auth/login`
- **Description:** Authenticates user and returns token.
- **Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword"
}
```
- **Success Response:**
```json
{
  "token": "jwt.token.string",
  "userId": "abc123"
}
```

#### 3. User Logout
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/auth/logout`
- **Description:** Invalidates user session/token.
- **Success Response:**
```json
{ "message": "Logged out successfully" }
```

---

### Dashboard

#### 4. Fetch Dashboard Overview
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/dashboard`
- **Description:** Retrieves latest documents, upcoming reminders, and health timeline preview.
- **Success Response:**
```json
{
  "recentDocuments": [...],
  "upcomingReminders": [...],
  "timelinePreview": [...]
}
```

---

### Documents

#### 5. Upload Document (with OCR)
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/documents/upload`
- **Description:** Uploads a document to storage and processes OCR for metadata extraction.
- **Request Body (Multipart):**
```
file: PDF/Image
```
- **Success Response:**
```json
{
  "documentId": "doc123",
  "category": "Prescription",
  "metadata": {
    "doctorName": "Dr. Smith",
    "date": "2025-08-10",
    "diagnosis": "Flu",
    "prescription": ["Medicine A", "Medicine B"]
  }
}
```

#### 6. Get Document Details
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/documents/:id`
- **Description:** Retrieves metadata and file URL for a specific document.

#### 7. Search & Filter Documents
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/documents/search?query=flu&category=Prescription`
- **Description:** Searches documents by keywords, doctor, category, or tags.

---

### Reminders

#### 8. Create Reminder
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/reminders`
- **Request Body:**
```json
{
  "documentId": "doc123",
  "medicine": "Paracetamol",
  "time": "2025-08-10T09:00:00Z",
  "repeat": "daily"
}
```

#### 9. Get All Reminders
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/reminders`

#### 10. Delete Reminder
- **HTTP Method:** `DELETE`
- **Endpoint Path:** `/api/reminders/:id`

---

### QR Code

#### 11. Generate QR Code for Document
- **HTTP Method:** `POST`
- **Endpoint Path:** `/api/documents/:id/qr`
- **Description:** Generates a QR code for a document’s secure view-only link.
- **Success Response:**
```json
{
  "qrCodeUrl": "https://storage.careapp.com/qrcodes/doc123.png"
}
```

---

### Profile & Settings

#### 12. Get Profile
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/profile`

#### 13. Update Profile
- **HTTP Method:** `PUT`
- **Endpoint Path:** `/api/profile`
- **Request Body:**
```json
{
  "name": "John Doe",
  "notificationsEnabled": true,
  "privacy": "private"
}
```

---

### Export Data

#### 14. Download Full Medical History
- **HTTP Method:** `GET`
- **Endpoint Path:** `/api/documents/export`
- **Description:** Returns a ZIP/PDF of all documents and metadata.
```

