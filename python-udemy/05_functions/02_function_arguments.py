chai_list = ['Plain', 'Milk', 'Black', 'Honey', 'Ginger']

def edit_list(index, name: str):
    chai_list[index] = name

# *args returns tuple and **kwargs return dictionary
def special_tea(*ingredients, **extras):
    print(f"Ingredients: {ingredients}")
    print(f"Extras: {extras}")

if __name__ == '__main__':
    print(chai_list)
    edit_list(1,'Elaichi') #positional argument
    print(f"After arguments edit: \n {chai_list}")

    edit_list(index=1,name='Elaichi') #keyword arguments
    print(f"After keyword arguments edit: \n {chai_list}\n")

    special_tea("Cinnamon", "Cardamom", sweetner='Honey', foam='Yes')