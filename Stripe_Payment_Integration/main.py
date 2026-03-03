from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import stripe
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from model import Payment, Base
from schemas import PaymentRequest
from config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


stripe.api_key = settings.STRIPE_SECRET_KEY

@app.post("/create-checkout-session")
def create_checkout_session(data: PaymentRequest):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "inr",
                "product_data": {"name": data.name},
                "unit_amount": data.amount * 100,
            },
            "quantity": 1,
        }],
        mode="payment",
        customer_email=data.email,
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )

    return {"checkout_url": session.url}

@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Webhook error")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        db = SessionLocal()

        payment = Payment(
            name=session["customer_details"]["name"],
            email=session["customer_email"],
            amount=session["amount_total"] // 100,
            currency=session["currency"],
            stripe_session_id=session["id"],
            stripe_payment_intent=session["payment_intent"],
            status="paid"
        )

        db.add(payment)
        db.commit()
        db.close()

    return {"status": "success"}

@app.get("/success", response_class=HTMLResponse)
def payment_success():
    return """
    <html>
        <head>
            <title>Payment Success</title>
        </head>
        <body style="text-align:center; margin-top:100px;">
            <h1 style="color:green;">✅ Payment Successful!</h1>
            <p>Thank you for your payment.</p>
        </body>
    </html>
    """


@app.get("/cancel", response_class=HTMLResponse)
def payment_cancel():
    return """
    <html>
        <head>
            <title>Payment Cancelled</title>
        </head>
        <body style="text-align:center; margin-top:100px;">
            <h1 style="color:red;">❌ Payment Cancelled</h1>
            <p>Your payment was not completed.</p>
        </body>
    </html>
    """