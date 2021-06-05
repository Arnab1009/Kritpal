from os import name

# Utility function to search for a value in collection


def find_item(data, key):
    for item in data:
        if item['name'] == key:
            return item
    return "No such item found!"

# Show selected item from collection


def show_item_handler(data):
    print("Show one item information selected")
    print("Enter the name of the item:")
    selection = input()
    returnVal = find_item(data, selection)
    if returnVal != "No such item found!":
        print(returnVal['name'] + ", " + returnVal['country'] +
              ", " + str(returnVal['price']) + ", " + str(returnVal['quantity']))
    else:
        print("No such item found!")

# Show all items from collection


def show_all_items_handler(data):
    print("Showing all items in stock")
    for item in data:
        print(item['name'] + ", " + item['country'] +
              ", " + str(item['price']) + ", " + str(item['quantity']))


# Add/Update items in collection
def update_items_handler(data):
    print("Add/Update item selected")
    print("Enter the name of the item you would like to add/update:")
    selection = input()
    obj = {'name': '', 'country': '', 'price': 0, 'quantity': 0}
    returnVal = find_item(data, selection)
    if(returnVal != "No such item found!"):
        print("Item already exists!")
        print("Enter new country of origin:")
        obj['country'] = input()
        print("What is the new price?")
        obj['price'] = int(input())
        print("How many items are in stock now?")
        obj['quantity'] = int(input())
        for item in data:
            if item['name'] == selection:
                item['country'] = obj['country']
                item['price'] = obj['price']
                item['quantity'] = obj['quantity']
    else:
        obj['name'] = selection
        print("Enter country of origin:")
        obj['country'] = input()
        print("What is the price?")
        obj['price'] = int(input())
        print("How many items are in stock?")
        obj['quantity'] = int(input())
        data.append(obj)
    return data

# Remove items from collection


def remove_item_handler(data):
    print("Remove item selected")
    print("Enter the name of the item to be removed:")
    selection = input()
    returnArr = []
    returnVal = find_item(data, selection)
    if returnVal != 'No such item found!':
        for item in data:
            if item['name'] != selection:
                returnArr.append(item)
        return returnArr
    else:
        print("No such item found!")
        return 0


# Compute total stock value of items


def compute_stock_value_handler(data):
    print("Compute stock value selected")
    total = 0
    for item in data:
        product = item['price'] * item['quantity']
        total = total + product
    print("The total stock value is: " + str(total))

# Complete execution and close application


def complete_execution_handler(data):
    print("Save data and exit selected.")
    print("Writing file A3_s3662454_stock.txt")
    out_file = open("A3_s3662454_stock.txt", "w")
    out_file.truncate(0)
    for item in data:
        line = item['name'] + "," + item['country'] + ", " + \
            str(item['price']) + "," + str(item['quantity'])
        out_file.write(line)
        out_file.write("\n")
    out_file.close()
    print("Program exit!")


# Trigger application menu controller


def trigger_menu_controller(data):
    print("Welcome to store manager")
    option = 0
    while(option != 6):
        print("What would you like to do?")
        print("1 - Show one item information")
        print("2 - Show all stock information")
        print("3 - Add/Update item")
        print("4 - Remove item")
        print("5 - Compute stock value")
        print("6 - Save data and exit")
        option = int(input())
        if option == 1:
            show_item_handler(data)
        elif option == 2:
            show_all_items_handler(data)
        elif option == 3:
            returnVal = update_items_handler(data)
            data = returnVal
        elif option == 4:
            returnVal = remove_item_handler(data)
            if returnVal != 0:
                data = returnVal
        elif option == 5:
            compute_stock_value_handler(data)
        elif option == 6:
            complete_execution_handler(data)
        else:
            print("Invalid option please try again!")

# Load data into collection


def initialize_data_sourcing():
    print("Loading data")
    print("Reading file A3_s3662454_stock.txt")
    objArr = []
    ip_file = open('A3_s3662454_stock.txt', 'r')
    ip_lines = ip_file.readlines()
    for line in ip_lines:
        tempArr = line.split(',')
        obj = {'name': tempArr[0],
               'country': tempArr[1],
               'price': int(tempArr[2]),
               'quantity': int(tempArr[3])
               }
        objArr.append(obj)
    print("All data loaded!")
    ip_file.close()
    return objArr

# Main trigger function


def start_sequence():
    data = initialize_data_sourcing()
    trigger_menu_controller(data)


# Set application entry point
if __name__ == "__main__":
    start_sequence()
