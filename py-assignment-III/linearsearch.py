def search(num_list, x):
    for i in range(len(num_list)): 
        if num_list[i] == x: 
            return i 
    return -1
item_list = [1,2,3,4,5]
x= int(input(f'Enter item to be search in {item_list}'))
print(search(item_list,x))