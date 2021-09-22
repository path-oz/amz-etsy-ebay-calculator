# Amazon/Etsy/Ebay Calculator




def amazon_calc():
    """Calculates Total Profit and fees for Amazon Marketplace"""

    # Prompts
    selling_price = float(input("Selling Price:"))
    shipping_customer = float(input("Shipping Charged Customer:"))
    product_cost = float(input("Cost Of Product:"))
    shipping_cost_product = float(input("Cost To Ship Product To Customer"))
    merchant = input("Type A for Individual Plan and B for Professional Plan:")

    # Fee Variables
    avg_referall_percentage = 0.15

    #if statements to see which one user choses
    if merchant == "A":
        unit_fee = 0.99
    elif merchant == "B":
        unit_fee = 0

    # Calculations
    calc1 = (selling_price * avg_referall_percentage) + unit_fee
    calc2 = selling_price + shipping_customer
    Total_Profit = calc2 - calc1 - product_cost - shipping_cost_product
    print("Amazon Fees: %s" % (calc1))
    print("Total Profit: %s" % (Total_Profit))




def etsy_calc():
    """Calculates Total Profit and Fees for Etsy Marketplace"""

    # Fee Variables
    list_fee = 0.20
    transaction_percentage = 0.05
    shipping_percentage = 0.05
    pay_proc_percentage = 0.03
    pay_proc_percentage2 = 0.25

    # Prompts
    selling_price = float(input("Selling Price:"))
    shipping_customer = float(input("Shipping Charged Customer:"))
    product_cost = float(input("Cost Of Product:"))
    shipping_cost_product = float(input("Cost To Ship Product To Customer:"))

    # Calculations
    calc1 = selling_price * (transaction_percentage + pay_proc_percentage)
    calc2 = shipping_customer * shipping_percentage
    calc3 = calc1 + list_fee + pay_proc_percentage2 + calc2
    Total_Profit = selling_price - calc3 - product_cost - shipping_cost_product
    print("Etsy Fees: %s" % (calc3))
    print("Total Profit: %s" % (Total_Profit))






def ebay_calc():
    """Calculates Total Profit and Fees for Ebay Marketplace"""

    # Fee Variables
    list_fee = 0.35
    transaction_percentage = 0.1255
    final_value_fee = 0.30

    # Prompts
    selling_price = float(input("Selling Price:"))
    shipping_customer = float(input("Shipping Charged Customer:"))
    product_cost = float(input("Cost Of Product:"))
    shipping_cost_product = float(input("Cost To Ship Product To Customer:"))

    # Calculations
    calc1 = (selling_price + shipping_customer) * transaction_percentage
    calc2 = calc1 + final_value_fee + list_fee
    Total_Profit = (selling_price + shipping_customer) - calc2 - product_cost - shipping_cost_product

    print("Ebay Fees: %s" % (calc2))
    print("Total Profit: %s" % (Total_Profit))


#Initial Prompt
marketplace = input("Type the marketplace calculator you want to use (Amazon, Ebay, or Etsy): ")

# If then statement to see which Marketplace user chooses 
if marketplace == "Amazon":
    amazon_calc()
elif marketplace == "Ebay":
    ebay_calc()
elif marketplace == "Etsy":
    etsy_calc()
else:
    print("Make sure to type either Amazon, Ebay, or Etsy. Also, make sure to capitalize the first letter.")