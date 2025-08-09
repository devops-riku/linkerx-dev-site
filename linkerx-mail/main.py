# server.py
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import resend

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can specify a list of allowed origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Set Resend API key
resend.api_key = os.getenv("RESEND_API_KEY")

# General function to send an email
def send_email_notification(to_email: str, subject: str, html: str):
    params: resend.Emails.SendParams = {
        "from": "contact@linkerx.dev",  # LinkerX sender's email address
        "to": [to_email],  # Recipient's email address
        "subject": subject,  # Subject of the email
        "html": html  # HTML content of the email
    }

    try:
        # Sending the email using Resend API
        email = resend.Emails.send(params)
        print(email)  # Log the email response
        return email  # Return the email response
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")


class EmailRequest(BaseModel):
    name: str
    email: str
    subject: str
    message: str

@app.post("/send-email")
async def send_email(email_request: EmailRequest):
    # Compose the HTML body for the email
    html_content = f"""
    <h2>Message from: {email_request.name}</h2>
    <p>Email: {email_request.email}</p>
    <p>{email_request.message}</p>
    """

    try:
        # Use the send_email_notification function to send the email
        email = send_email_notification(
            to_email="support@linkerx.dev",  # Receiver's LinkerX email address
            subject=email_request.subject,
            html=html_content  # HTML formatted message
        )
        return {"message": "Email sent successfully!", "data": email}
    
    except HTTPException as e:
        # Return error if the email couldn't be sent
        raise e
    except Exception as e:
        # Catch other exceptions and return a generic error
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")