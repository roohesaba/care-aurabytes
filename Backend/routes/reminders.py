from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from storage import reminders

router = APIRouter()

class Reminder(BaseModel):
    medicine_name: str
    time: str

# CREATE
@router.post("/reminders")
def create_reminder(reminder: Reminder):
    new_rem = reminder.dict()
    new_rem["id"] = len(reminders) + 1
    reminders.append(new_rem)
    return {"message": "Reminder created", "reminder": new_rem}

# READ - all reminders
@router.get("/reminders")
def get_reminders():
    return {"reminders": reminders}

# READ - single reminder
@router.get("/reminders/{reminder_id}")
def get_reminder(reminder_id: int):
    for r in reminders:
        if r["id"] == reminder_id:
            return r
    raise HTTPException(status_code=404, detail="Reminder not found")

# UPDATE
@router.put("/reminders/{reminder_id}")
def update_reminder(reminder_id: int, reminder: Reminder):
    for r in reminders:
        if r["id"] == reminder_id:
            r.update(reminder.dict())
            return {"message": "Reminder updated", "reminder": r}
    raise HTTPException(status_code=404, detail="Reminder not found")

# DELETE
@router.delete("/reminders/{reminder_id}")
def delete_reminder(reminder_id: int):
    for i, r in enumerate(reminders):
        if r["id"] == reminder_id:
            reminders.pop(i)
            return {"message": "Reminder deleted"}
    raise HTTPException(status_code=404, detail="Reminder not found")
