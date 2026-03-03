# FastAPI Stripe Payment Integration

A minimal FastAPI project for Stripe Checkout payment collection with webhook persistence into a PostgreSQL database using SQLAlchemy.

## Features
- Create Stripe Checkout session (`POST /create-checkout-session`)
- Handle Stripe webhook events (`POST /webhook`)
- Persist successful payments to `payments` table
- Basic success and cancel pages

## Tech Stack
- FastAPI
- Stripe Python SDK
- SQLAlchemy
- PostgreSQL
- python-dotenv

## Project Structure
- `main.py` - API routes and Stripe logic
- `config.py` - environment variable loading
- `database.py` - SQLAlchemy engine/session setup
- `model.py` - `Payment` ORM model
- `schemas.py` - request schema (`PaymentRequest`)

## Requirements
Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file with:

```env
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/payment_db
```

## Run the App

```bash
uvicorn main:app --reload
```

App URL: `http://127.0.0.1:8000`

## API Endpoints

### `POST /create-checkout-session`
Request body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "amount": 499
}
```

Response:

```json
{
  "checkout_url": "https://checkout.stripe.com/..."
}
```

### `POST /webhook`
Used by Stripe to notify payment events. Configure this endpoint in Stripe dashboard or Stripe CLI.

## Notes
- Make sure PostgreSQL is running and the database in `DATABASE_URL` exists.
- Tables are auto-created on startup via `Base.metadata.create_all(bind=engine)`.
- For local webhook testing, use Stripe CLI:

```bash
stripe listen --forward-to localhost:8000/webhook
```
