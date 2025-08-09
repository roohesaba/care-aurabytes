* Important Endpoints

  1)Medications
  
1.1)Create Medication (Quick Setup)
       Feature: Create medication & schedule in one step

       Method: POST

       Path: /api/v1/medications/quick-setup

       Request Body:

       json
       {
         "name": "Metformin",
         "type": "tablet",
         "strength": "500 mg",
         "dosage": { "label": "1 tablet" },
         "frequency": { "type": "twice_daily", "times": ["08:00","20:00"] },
         "start_date": "2025-08-10"
       }
       Success: { "data": { "medication": { }, "schedule": { } } }

1.2)List Medications
       Method: GET

       Path: /api/v1/medications

       Success: { "data": [ ], "meta": { "total": 2 } }

1.3)Delete Medication
       Method: DELETE

       Path: /api/v1/medications/:medId

       Success: { "data": { "deleted": true } }


2)Reminder Schedules

2.1)Create Schedule
       Method: POST

       Path: /api/v1/medications/:medId/schedules

       Request Body:

       json
       {
         "dosage": { "label": "1 tablet" },
         "frequency": { "type": "every_n_hours", "every_n_hours": 8 },
         "start_date": "2025-08-10"
       }
       Success: { "data": { } }

2.2)List Upcoming Doses
       Method: GET

       Path: /api/v1/doses/upcoming

       Success: { "data": [ ] }


3)Health Checkups

3.1)Create Checkup
       Method: POST

       Path: /api/v1/checkups

       Request Body:

       json
       {
         "type": "blood_test",
         "title": "Quarterly Blood Test",
         "scheduled_for": "2025-09-01T04:00:00Z"
       }
       Success: { "data": { } }

3.2)List Checkups
       Method: GET

       Path: /api/v1/checkups

       Success: { "data": [ ] }


4)Prescription Scanning

4.1)Upload Prescription
       Method: POST

       Path: /api/v1/prescriptions

       Headers: Content-Type: multipart/form-data

       Form Data: file (image/pdf)

       Success: { "data": { "id": "p1", "status": "processing" } }

4.2)Get Parsed Prescription
       Method: GET

       Path: /api/v1/prescriptions/:prescriptionId

       Success: { "data": { "items": [ ] } }

4.3)Confirm Prescription
       Method: POST

       Path: /api/v1/prescriptions/:prescriptionId/confirm

       Request Body:
       json
        {
         "selections": [
           {
             "name": "Amoxicillin",
             "type": "capsule",
             "strength": "500 mg",
             "frequency": { "type": "thrice_daily", "times": ["08:00","14:00","20:00"] }
           }
         ]
      }

Success: { "data": { "created": [ ] } }


5)Notifications

5.1)List Notifications
       Method: GET

      Path: /api/v1/notifications

       Success: { "data": [ ] }














