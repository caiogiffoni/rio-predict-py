from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import new_vars
import re

app = FastAPI()

class Body(BaseModel):
    property_type_Bed_and_breakfast: int  | None = None
    property_type_Apartment: int  | None = None
    property_type_Condominium: int  | None = None
    property_type_Guest_suite: int  | None = None
    property_type_Guesthouse: int  | None = None
    property_type_Hostel: int  | None = None
    property_type_House: int  | None = None
    property_type_Loft: int  | None = None
    property_type_Other: int  | None = None
    property_type_Serviced_apartment: int  | None = None
    room_type_Entire_home_apt: int  | None = None
    room_type_Hotel_room: int  | None = None
    room_type_Private_room: int  | None = None
    room_type_Shared_room: int  | None = None
    cancellation_policy_flexible: int  | None = None
    cancellation_policy_moderate: int  | None = None
    cancellation_policy_strict: int  | None = None
    cancellation_policy_strict_14_with_grace_period: int  | None = None
    latitude: float  | None = None
    longitude: float  | None = None
    accommodates: int  | None = None
    bathrooms: int  | None = None
    bedrooms: int  | None = None
    beds: int  | None = None
    extra_people: int  | None = None
    minimum_nights: int  | None = None
    year: int  | None = None
    month: int  | None = None
    amenities: int  | None = None
    host_listings_count: int  | None = None
    host_is_superhost: int  | None = None
    instant_bookable: int   | None = None



@app.post("/predict")
async def predict_values(body: Body):
    # import ipdb
    # ipdb.set_trace()
    body_dict = body.dict()
    body_df = pd.DataFrame(body_dict, index=[0])
    values_x = pd.DataFrame(new_vars.ddd, index=[0])
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
    xxx = pd.DataFrame(new_vars.dddxxx, index=[0])[new_vars.index]
    values_x_new  = values_x[new_vars.index]
    model = joblib.load('model.joblib')
    price = model.predict(body_df)
    price1 = model.predict(values_x_new)
    price2 = model.predict(xxx)

    return {
        '0': price[0],
        "message": price1[0],
       "message2": price2[0]
    }