from pydantic import BaseModel

class PaymentRequest(BaseModel):
    name: str
    email: str
    amount: int
    
    
    