from fastapi import FastAPI, Request
from pydantic import BaseModel
app = FastAPI()

#minimal app 
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return{"API":"Working"}


#get --> read todo
@app.get("/todo",tags=["todos"])
async def get_todo() -> dict:
    return{"data": todos}

# @app.get("/todo/{id}",tags=["todos"])
# async def get_todo_id(id:int) ->:
#     for todo in todos:
#         if int(todo['id']) == id:
#             return{

#             }

#post --> create todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data": "A todo has been added!"
    }


async def get_car(car_name: dict):
    name = car_name.get("name")
    if name not in cars:
        return {"error": "Car not found"}
    return cars[name]






#put --> update todo
@app.put("/todo/{id}",tags=["todos"])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return{
                "data":f"Todo with id {id} has been updated"
            }
    return{
        "data":f"Todo with id {id} was not found"
    }

#delete --> delete todo
@app.delete("/todo/{id}",tags=["todos"])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return{
                "data":f"Todo with {id} has been deleted"
            }




todos = [
    {
        "id":"1",
        "Activity":"Create a demo for oberoi"
    },
    {
        "id":"2",
        "Activity":"Debug the pop up and save to pdf js"
    }
]


@app.post("/cars/astor",tags=["cars_demo"])
async def car_astor() -> dict:
    return cars


class CarRequest(BaseModel):
    car_name: str

@app.post("/car_details", tags=["chat"])
async def car_details(car_request: CarRequest):
    car_name = car_request.car_name
    if car_name in my_cars:
        return my_cars[car_name]
    else:
        return {"error": "Car not found."}

cars={
    "model": "Astor",
    "colors": "Spiced Orange, Aurora Silver, Glaze Red, Candy White, Starry Black",
    "price": "₹10.52 Lakh onwards",
    "engine": "1349 to 1498 cc",
    "Fuel Type": "Petrol",
    "Seating Capacity": "5 Seater"
}

my_cars = {

    # astor complete
    "Astor":{
        "model": "Astor",
        "colors": "Spiced Orange, Aurora Silver, Glaze Red, Candy White, Starry Black",
        "price": "₹10.52 Lakh onwards",
        "engine": "1349 to 1498 cc",
        "fuel_type": "Petrol",
        "seating_Capacity": "5 Seater",
        "boot_space":"448L",
        "ground_clearance":"180mm",
        "fuel_tank":"48L",
        "transmission":"6-speed automatic, 5-speed manual and Continuous Variable Transmission",
        "infotainment":"Android Auto and Apple Car Play "
    },
    
    # astor ex complete
    "Astor EX":{
        "model": "Astor EX",
        "colors": "Spiced Orange, Aurora Silver, Glaze Red, Candy White, Starry Black",
        "price": "₹10.52 Lakh onwards",
        "engine": "1349 to 1498 cc",
        "fuel_type": "Petrol",
        "seating_capacity": "5 Seater",
        "boot_space":"448L",
        "ground_clearance":"180mm",
        "fuel_tank":"48L",
        "transmission":"Manual transmission",
        "infotainment":"Android Auto (Wired) and Apple Car Play (Wired)"
    },
    
    # hector completed
    "MG Hector":{
        "model": "Hector",
        "colors": "Dune Brown, Havana Grey, Candy White with Starry Black, Candy White, Glaze Red, Aurora Silver, Starry Black",
        "price": "₹15 Lakh onwards",
        "engine": "1956 cc",
        "fuel_type": "Diesel",
        "seating_capacity": "5 Seater",
        "boot_space":"587L",
        "ground_clearance":"192mm",
        "fuel_tank":"60L",
        "transmission":"6-speed manual and Continuous variable transmission",
        "infotainment":"Android Auto and Apple Car Play"
    },
    
    # hector plus 6 seater completed
    "MG Hector Plus 6 Seater":{
        "model": "Hector Plus 6 seater",
        "colors": "Dune Brown, Havana Grey, Candy White with Starry Black, Candy White, Glaze Red, Aurora Silver, Starry Black",
        "price": "₹18 Lakh onwards",
        "engine": "1956 cc",
        "fuel_type": "Diesel",
        "seating_capacity": "6 Seater",
        "boot_space":"155L",
        "ground_clearance":"192mm",
        "fuel_tank":"60L",
        "transmission":"6-speed manual and Continuous variable transmission",
        "infotainment":"Android Auto and Apple Car Play"
    },
    
    # hector plus 7 seater completed
    "MG Hector Plus 7 Seater":{
        "model": "Hector Plus 7 seater",
        "colors": "Dune Brown, Havana Grey, Candy White with Starry Black, Candy White, Glaze Red, Aurora Silver, Starry Black",
        "price": "₹18 Lakh onwards",
        "engine": "1956 cc",
        "fuel_type": "Diesel",
        "seating_capacity": "7 Seater",
        "boot_space":"155L",
        "ground_clearance":"192mm",
        "fuel_tank":"60L",
        "transmission":"6-speed manual and Continuous variable transmission",
        "infotainment":"Apple CarPlay and Android Auto"
    },
    
    # MG ZS EV completed
    "MG ZS EV":{
        "model": "MG ZS EV",
        "colors": "Glaze Red, Aurora Silver, Starry Black, Candy White",
        "price": "₹23.38 Lakh onwards",
        "engine": "Electric",
        "charging_time": "8.5 to 9 hours",
        "seating_capacity": "5 Seater",
        "boot_space":"448L",
        "ground_clearance":"177mm",
        "battery":"50.3 kWh",
        "transmission":"Automatic transmission",
        "infotainment":"Android Auto and Apple Car Play"
    },
    
    #MG Gloster completed
    "MG Gloster":{
        "model": "MG Gloster",
        "colors": "Deep Golden, Metal Black, Metal Ash, Warm White",
        "price": "₹38.08 Lakh onwards",
        "engine": "1996 cc",
        "fuel_type": "Diesel",
        "seating_capacity": "6,7 Seater",
        "boot_space":"343L",
        "ground_clearance":"210mm",
        "fuel_tank":"75L",
        "transmission":"8-speed automatic transmission",
        "infotainment":"Apple CarPlay and Android Auto"
    },
    
    #mg comet working (needs boot space)
    "MG Comet":{
        "model": "MG Comet EV",
        "colors": "Candy White With Starry Black, Apple Green With Starry Black, Starry Black, Aurora Silver and Candy White",
        "price": "₹7.98 Lakh onwards",
        "engine": "Electric",
        "charging-time": "7 Hours",
        "seating_capacity": "4 Seater",
        "boot_space":"NAN", # find and update the details
        "ground_clearance":"177mm",
        "battery":"17.3 kWh",
        "transmission":"Automatic transmission",
        "infotainment":"Apple CarPlay and Android Auto"
    }  
}
# "Spiced Orange, Aurora Silver, Glaze Red, Candy White, Starry Black"

@app.post("/cars/{car_name}", tags=["car_demo"])
async def get_person_address(car_name: str):
        return my_cars[car_name]


# @app.get("/person/{person_id}/address")
# async def get_person_address(person_id: str):
#     return my_dict[person_id]["address"]

my_dict = {
    "person_1": {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zipcode": "10001"
        }
    },
    "person_2": {
        "name": "Jane",
        "age": 25,
        "address": {
            "street": "456 Second St",
            "city": "San Francisco",
            "state": "CA",
            "zipcode": "94107"
        }
    }
}


'''
boot space
grund clearance
suspension
transmission
car play
wheel size
car weight
'''



# This is the specification of the MG Astor.

# Model: Astor
# Colors: Spiced Orange, Aurora Silver, Glaze Red, Candy White, Starry Black
# Price: ₹10.52 Lakh onwards
# Engine: 1349 to 1498 cc
# Fuel Type: Petrol
# Seating Capacity: 5 Seater