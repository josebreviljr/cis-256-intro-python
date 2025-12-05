
import pickle

car_inventory = {"Toyota": 5, "Honda": 3, "Ford": 2}

# Save
with open("inventory.pkl", "wb") as file:
    pickle.dump(car_inventory, file)

# Load
with open("inventory.pkl", "rb") as file:
    data = pickle.load(file)

print(data)