chai_list = ['Plain', 'Milk', 'Black', 'Honey', 'Ginger']

def edit_list(index, name: str):
    chai_list[index] = name

if __name__ == '__main__':
    print(chai_list)
    edit_list(1,'Elaichi') #positional argument
    print(f"After arguments edit: \n {chai_list}")

    edit_list(index=1,name='Elaichi') #keyword arguments
    print(f"After keyword arguments edit: \n {chai_list}")