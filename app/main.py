import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from . import new_vars

app = FastAPI()

class Body(BaseModel):
    property_type_Bed_and_breakfast: int
    property_type_Apartment: int
    property_type_Condominium: int
    property_type_Guest_suite: int
    property_type_Guesthouse: int
    property_type_Hostel: int
    property_type_House: int
    property_type_Loft: int
    property_type_Other: int
    property_type_Serviced_apartment: int
    room_type_Entire_home_apt: int
    room_type_Hotel_room: int
    room_type_Private_room: int
    room_type_Shared_room: int
    cancellation_policy_flexible: int
    cancellation_policy_moderate: int
    cancellation_policy_strict: int
    cancellation_policy_strict_14_with_grace_period: int
    latitude: float
    longitude: float
    accommodates: int
    bathrooms: int
    bedrooms: int
    beds: int
    extra_people: int
    minimum_nights: int
    year: int
    month: int
    amenities: int
    host_listings_count: int
    host_is_superhost: int
    instant_bookable: int 



@app.post("/predict")
async def predict_values(body: Body):
    body_dict = body.dict()
    body_df = pd.DataFrame(body_dict, index=[0])
    body_df = body_df.rename(columns={
        "property_type_Bed_and_breakfast": "property_type_Bed and breakfast", 
        "property_type_Guest_suite": "property_type_Guest suite", 
        "property_type_Serviced_apartment": "property_type_Serviced apartment",
        "room_type_Entire_home_apt" :"room_type_Entire home/apt", 
        "room_type_Hotel_room":"room_type_Hotel room", 
        "room_type_Private_room":"room_type_Private room", 
        "room_type_Shared_room":"room_type_Shared room"
    })
    body_df = body_df[new_vars.index]
    model = joblib.load('app/model.joblib')
    price = model.predict(body_df)

    return {
        'price': price[0],
    }