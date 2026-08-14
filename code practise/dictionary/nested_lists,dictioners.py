travel_log={
    "france":["paris","lille","dijon"],
    "germany":["stuttgart","berlin"],
}

travel=travel_log["france"][1]
print(travel)

nested_list=["a","b",["c","d"]]
nested=nested_list[2][1]
print(nested)

travel_log1 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
travel1=travel_log1["Germany"]["cities_visited"][2]#dictionary is represented in[string] and lists in [int]
print(travel1)