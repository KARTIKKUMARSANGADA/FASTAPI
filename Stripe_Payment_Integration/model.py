from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    stripe_session_id = Column(String)
    stripe_payment_intent = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)