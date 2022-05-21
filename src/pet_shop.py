# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed_input):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_input:
            breed_list.append(pet)

    return breed_list


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    for index, pet in enumerate(pet_shop["pets"]):
        if pet["name"] == pet_name:
            pet_shop["pets"].pop(index)


def add_pet_to_stock(pet_shop, new_pet):
    for pet in pet_shop["pets"]:
        new_addition = new_pet
        pet["new_addition"] = new_pet
        pet_shop["pets"].append(new_addition)
        return pet["new_addition"]


def get_customer_cash(customer_number):
    return customer_number["cash"]


def remove_customer_cash(customer_number, cash_input):
    variable_a = customer_number["cash"]
    variable_b = cash_input
    new_total = variable_a - variable_b
    customer_number["cash"] = new_total

    return customer_number["cash"]


def get_customer_pet_count(customer_number):
    pet_variable = customer_number["pets"]
    return len(pet_variable)


def add_pet_to_customer(customer_number, new_pet):
    current_pet = customer_number["pets"]
    new_addition = new_pet
    current_pet.append(new_addition)
    return customer_number["pets"]


def customer_can_afford_pet(customer_number, new_pet):
    variable_a = customer_number["cash"]
    variable_b = new_pet["price"]
    if variable_a >= variable_b:
        result = True
    else:
        result = False
    return result


def sell_pet_to_customer(pet_shop, pet, customer_number):
    if pet is not None and customer_can_afford_pet(customer_number, pet) == True:
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer_number, pet)
        remove_customer_cash(customer_number, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
