from pydantic import BaseModel, Field
from typing import Optional, List

class UserRegister(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    password: str
    role: str # 'OFFICER' or 'FARMER'
    # Officer optional initial fields
    designation: Optional[str] = "Agricultural Officer"
    department: Optional[str] = "Department of Agriculture"
    assigned_area: Optional[str] = ""
    # Farmer optional initial fields
    village: Optional[str] = ""
    area: Optional[str] = ""
    district: Optional[str] = ""
    state: Optional[str] = ""
    land_area: Optional[float] = 1.0
    land_unit: Optional[str] = "Acres"
    farming_type: Optional[str] = "Conventional"

class UserLogin(BaseModel):
    identifier: str # Email, mobile, officer_id, or login_id
    password: str
    role: Optional[str] = None # Role filter if supplied

class OfficerVerifyRequest(BaseModel):
    officer_id: str

class OfficerVerifyOtpRequest(BaseModel):
    officer_id: str
    otp: str

class OfficerResendOtpRequest(BaseModel):
    officer_id: str

class OfficerCreateAccountRequest(BaseModel):
    officer_id: str
    verification_token: str
    login_id: str
    password: str
    confirm_password: str


class OfficerProfileUpdate(BaseModel):
    name: str
    designation: str
    department: str
    assigned_area: str
    district: str
    state: str
    contact: str
    email: Optional[str] = None
    photo_url: Optional[str] = None

class FarmerProfileUpdate(BaseModel):
    name: str
    village: str
    area: str
    district: str
    state: str
    land_area: float
    land_unit: str = "Acres"
    farming_type: str = "Conventional"
    contact: Optional[str] = None
    email: Optional[str] = None
    photo_url: Optional[str] = None

class ProduceCreate(BaseModel):
    crop_name: str
    quantity: float
    unit: str = "Tons"
    price: Optional[float] = None
    area: str
    village: Optional[str] = ""
    district: str
    state: str
    produce_type: Optional[str] = "Field Crop"
    quality: Optional[str] = "Grade A"
    availability_date: str
    expected_harvest_date: Optional[str] = None
    notes: Optional[str] = None

class ProduceUpdate(BaseModel):
    quantity: Optional[float] = None
    unit: Optional[str] = None
    price: Optional[float] = None
    quality: Optional[str] = None
    availability_date: Optional[str] = None
    expected_harvest_date: Optional[str] = None
    verification_status: Optional[str] = None
    notes: Optional[str] = None

class FarmerCropSubmission(BaseModel):
    crop_name: str
    cultivated_area: float
    cultivated_area_unit: str = "Acres"
    expected_quantity: float
    quantity_unit: str = "Tons"
    expected_harvest_date: str
    crop_stage: Optional[str] = "Vegetative"
    quality: Optional[str] = "Grade A"
    village: Optional[str] = ""
    area: str
    district: str
    state: str
    notes: Optional[str] = None

class VerificationAction(BaseModel):
    action: str # 'VERIFY' or 'REJECT'
    comment: Optional[str] = None

class PurchaseRequestCreate(BaseModel):
    produce_id: int
    buyer_name: str
    buyer_contact: str
    requested_quantity: float
    quantity_unit: str = "Tons"
    message: Optional[str] = ""

class PurchaseRequestStatusUpdate(BaseModel):
    status: str # 'accepted' or 'rejected'
