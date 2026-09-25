chai_list = ['Plain', 'Milk', 'Black', 'Honey', 'Ginger']

def edit_list(index, name: str):
    chai_list[index] = name

if __name__ == '__main__':
    print(chai_list)
    edit_list(1,'Elaichi')
    print(f"After edit: \n {chai_list}")