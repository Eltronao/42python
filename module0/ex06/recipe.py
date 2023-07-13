'''recipe = {
"ingredients"   : ingredients
"meal"          : meal
"prep_time"     : unsigned integer mins
}'''

Sandwich = {
"ingredients"   : ("ham", "bread", "cheese", "tomatoes"),
"meal"          : "lunch",
"prep_time"     : 10
}
Cake = {
"ingredients"   : ("flour", "sugar", "eggs"),
"meal"          : "dessert",
"prep_time"     : 60
}
Salad = {
"ingredients"   : ("avocado", "arugula", "tomatoes", "spinach"),
"meal"          : "lunch",
"prep_time"     : 15
}
cookbook ={
    "Sandwich"  : Sandwich,
    "Cake"      : Cake,
    "Salad"     : Salad
}

def print_names():
    print("The available recipes are:")
    for key, value in cookbook.items():
        print(key)
    print("")
    
def print_details(rec_name):
    my_rec = 0
    for key, value in cookbook.items():
        if rec_name == key:
            my_rec = value
    if my_rec == 0:
        return
    print("Recipe for " + rec_name + ":")
    i = 0
    for key, value in my_rec.items():
        if i == 0:
            print("{} list: {}".format(key, value[0::]))
        elif i == 1:
            print("To be eaten for {}".format(value))
        else:
            print("Takes {} minutes to do it".format(value))

def delete_rec(rec_name):
    del cookbook [rec_name]

def add_recipe():
    new_rec = dict()
    name = input("Enter a name:\n>>>")
    if (name in cookbook):
        print("Recipe already exists")
        return
    ingredients = tuple()
    new_ing = input("Enter ingredients:\n>>>")
    while new_ing != "":
        ingredients + tuple(new_ing)
        new_ing = input(">>>")
    new_rec.update({"ingredients" : ingredients})
    new_rec.update({"meal" : input("Enter a meal type:\n>>>")})
    new_rec.update({"prep_time" : input("Enter a preparation time:\n>>>")})
    cookbook.update({name : new_rec})

def print_options():
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def main():
    insertion = 1
    print("Welcome to Python Cookbook!")
    print("List of available options:")
    while insertion != 5:
        print_options()
        try:
            insertion = int(input("Enter an option\n>>>"))
        except ValueError:
            print("Please enter a number as input.")
        if insertion > 0 and insertion < 6:
            if insertion == 1:
                add_recipe()
            elif insertion == 2:
                delete_rec(input("Enter a recipe name\n>>>"))
            elif insertion == 3:
                print_details(input("Enter a recipe name to get a description\n>>>"))
            elif insertion == 4:
                print_names()
        else:
            print("Invalid input value.")
    print("Cookbook closed. Bye!")

main()