car={
        "Cost":int(input("Enter the cost of car:")),
        "Age":3,
        "Brand":"Honda",#civic
        "Mileage":[10.21,15.92,26.6],
        "Driving_pattern":[30,75,40],
        "Accidents":7,      
        "4WD":False,
        "Topspeed":137
        
}
for key, value in car.items():
    print(key,':',value)


print("/**************************************/")


def expense(car):


    Vehicles={
            "tier1":["BMW","Mercedes","Tesla","Jaguar"],
            "tier2":["Toyota","Nissan","Mitsubishi","Honda"],
            "tier3":["KIA","Hyundai","Renault","Ford"]
    }


    price_of_fuel=2.420
    Mileage=car["Mileage"]
    drivingPattern=car["Driving_pattern"]
    Fuel = (drivingPattern[0]/Mileage[0]+drivingPattern[1]/Mileage[1]+drivingPattern[2]/Mileage[2])
    Fuel_consumed_actual = Fuel*price_of_fuel
    Fuel_consumed = "{:.2f}".format(Fuel_consumed_actual)
    print("Fuel Consumed:", Fuel_consumed
    )






    for deprecated in Vehicles["tier1"]:
        if deprecated==car["Brand"]:
            rate_of_deprecated=30
    for deprecated2 in Vehicles["tier2"]:
        if deprecated2==car["Brand"]:
            rate_of_deprecated=20
    for deprecated3 in Vehicles["tier3"]:
        if deprecated3==car["Brand"]:
            rate_of_deprecated=10
    print("rate_of_deprecated:",rate_of_deprecated)
    deprecated_max_value=car["Cost"]-10000
    Current_vehicle_cost=deprecated_max_value-(car["Age"]*(deprecated_max_value/rate_of_deprecated))
    print("Current_vehicle_cost:",Current_vehicle_cost)


    fixed_insurance_cost=800
    if car["Topspeed"]>100 and car["Topspeed"]<=140:
        Current_insurance_cost =  fixed_insurance_cost+(Current_vehicle_cost*(2/100))
    if car["Topspeed"]>140 and car["Topspeed"]<=200:
        Current_insurance_cost =  fixed_insurance_cost+(Current_vehicle_cost*(4/100))
    if car["Topspeed"]>200:
        Current_insurance_cost =  fixed_insurance_cost+(Current_vehicle_cost*(6/100))
    if car["Accidents"]==0:
        Current_insurance_cost=Current_insurance_cost-(Current_insurance_cost*(10/100))
    if car["Accidents"]>=1 and car["Accidents"]<=3:
        Current_insurance_cost=Current_insurance_cost+(Current_insurance_cost*(15/100))
    if car["Accidents"]>3:
        Current_insurance_cost=Current_insurance_cost+(Current_insurance_cost*(30/100))

    total=0
    for km in car["Driving_pattern"]:
        total=total+km
    offroad_percentage=total*40/100
    if car["4WD"]==True and drivingPattern[2]>offroad_percentage:
        Current_insurance_cost=Current_insurance_cost+(Current_insurance_cost*(20/100))
    print("Current_insurance_cost:",Current_insurance_cost)
    return
expense(car)