def taking_input():
    # Loop to ensure a valid number is entered for the number of products
    while True:
        try:
            number_of_products = int(input("How many products you have: "))  # Ask user for number of products
            break  # Exit loop if input is valid
        except ValueError:  # Handle case where the input is not a valid integer
            print("❌ Please enter a valid number.")  # Show error message if input is invalid

    # Initialize lists and dictionaries to store products and sales data
    products = []
    sales = {}

    # Loop through for the number of products
    for i in range(number_of_products):
        # Loop to ensure product name is valid (only letters)
        while True:
            product_name = input(f"Enter the Product name {i+1}: ")  # Ask user for product name
            if product_name.isalpha():  # Check if input contains only letters
                break  # Exit loop if the name is valid
            else:
                print(" Please enter a valid product name!")  # Show error message if the input is invalid

        # Loop to ensure product price is a valid integer
        while True:
            try:
                product_price = int(input(f"Enter the product price {i+1}: "))  # Ask for product price
                break  # Exit loop if the input is a valid integer
            except ValueError:  # Handle case where the input is not a valid integer
                print(" Please write the valid price.")  # Show error message if input is invalid

        products.append((product_name, product_price))  # Add product and its price to the products list

        # Loop to ensure quantity sold is a valid integer
        while True:
            try:
                quantity_sold = int(input("How many quantities have you sold: "))  # Ask for quantity sold
                break  # Exit loop if input is valid
            except ValueError:  # Handle case where the input is not a valid integer
                print(" Please write the valid quantities!")  # Show error message if input is invalid

        sales[product_name] = quantity_sold  # Store the quantity sold in the sales dictionary

    return products, sales  # Return the list of products and sales data


def sale_checking():
    while True:  # Loop to allow multiple entries
        # Get the products and sales data by calling the taking_input function
        products, sales = taking_input()

        content = []

        # Loop through each product to display its details
        for i in products:
            product_name = i[0]  # Extract product name
            product_price = i[1]  # Extract product price
            sale = sales.get(product_name, None)  # Get the quantity sold from the sales dictionary

            if sale is None:  # If no sales data is found for the product
                print(f"Product: {product_name}, Price: {product_price}, Quantity sold: No sales data.")
            else:
                revenue = product_price * sale  # Calculate the total revenue for the product
                print(f"Product: {product_name}, Price: {product_price}, Quantity sold: {sale}, Total Revenue: {revenue}")
                content.append(f"Product: {product_name}, Price: {product_price}, Quantity sold: {sale}, Total Revenue: {revenue}")

        # Creating a file to save the data of a user in a file
        with open('file.txt', 'a', encoding='utf-8') as file:
            for line in content:
                file.write(line + " \n")
        # Ask the user if they want to add another product
        again = input("Do you want to add another product Y/N: ")
        again = again.upper()  # Convert to uppercase for comparison
        if again != "Y":
            break  # Exit the loop if the user does not want to add more products

# Call the sale_checking function to run the program
sale_checking()