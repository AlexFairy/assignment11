# Task 1: Flight Route Comparison
# 1. Destinations that both airlines fly to. 
# 2. Destinations unique to your airline. 
#3. Whether there are any destinations that neither airline shares. 
"""
def view_first_route(route1):
  for routes1a in enumerate(route1):
    print(f"{routes1a}")

def view_second_route(route2):
  for index, routes2b in enumerate(route2):
    print(f"Flight#{index + 1}: {routes2b}")

def both_airlines_fly_to(route1, route2):
  shared_values = set.intersection(route1, route2)
  print("The destination that both airlines fly to:")
  print(f"{shared_values}")

def unique_destinations(route1, route2):
  unique_values = route1.difference(route2)
  print(f"Unique destinations are: {unique_values}")

def neither_airlines_share(route1, route2):
  neither_shared = route1.symmetric_difference(route2)
  print(f"Neither shared routes are: {neither_shared}")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True:
  print("\nMake a selection")
  print("1. View Individual Routes")
  print("2. Check: Destinations that both airlines fly to")
  print("3. Destinations unique to our airline")
  print("4. Destinations that neither airline shares")
  print("5. Exit")
  user_input = input("Make a selection: ")

  if user_input == '1':

    print("Please select from the choices below")
    print("Choice A - View flights from 'Our Flights'")
    print("Choice B - View flights from 'Competitor Routes")
    routeABC = input("Select [*Flights are unordered] (A/B): ")

    if routeABC.lower() == 'a':
      view_first_route(our_routes)
    elif routeABC.lower() == 'b':
      view_second_route(competitor_routes)
    else:
      print("Incorrect selection")
  
  elif user_input == '2':
    both_airlines_fly_to(our_routes, competitor_routes)
  elif user_input == '3':
    unique_destinations(our_routes, competitor_routes)
  elif user_input == '4':
    neither_airlines_share(our_routes, competitor_routes)
  elif user_input == '5':
    print("Exiting program")
    break
  else:
    print("Incorrect selection")
"""

#Task 1: 
# Duplicate Entries Cleanup You are given a list of customer IDs, 
# some of which are duplicated. 
# Write a Python script to remove duplicates and 
# display the unique customer IDs. 

#Version 1
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
set_customerIDS = set(customer_ids)
print(sorted(set_customerIDS))

#Version 2
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
set_customerIDS = set(customer_ids)
unique_IDs = set.difference(set_customerIDS)
unique_IDsA = set(unique_IDs)
print(unique_IDs)