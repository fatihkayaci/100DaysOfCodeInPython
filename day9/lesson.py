travel_log = {
    "France": ["paris", "lille", "dijon"],
    "Germany": ["stuttgart", "berlin"],
}

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])


travel_log = {
    "France": {
            "cities_visites": ["paris", "lille", "dijon"],
            "total_visits": 12
        },
    "Germany":{
        "cities_visites": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]["cities_visites"][2])