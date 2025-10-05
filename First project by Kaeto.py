monthly_income = float(input("What is a rough idea of your monthly income? ")) #gain an idea of how much we have
savings = float(input("How much out of this do you want to save? ")) # suggest saving to individual and gain idea of how much they want to save

food = float(input("Give an estimate of how much you spend on the following in a month: Food? ")) #gain idea of how much gets spent on food
transport = float(input("How much do you spend on transport? ")) #gain idea of how much gets spent on transport

house_items = float(input("How much do you spend on cleaning supplies and household items? ")) #gain idea of how much gets spent on household items
health_products = float(input("How much do you spend on health and beauty products? ")) #gain idea of how much gets spent on health products

other = float(input("How much do you spend on other things not specified? ")) #gain idea of other expenses
total_expenses = savings + food + transport + house_items + health_products + other #total expenses

weekly_savings = savings/4 #how much to be saved in a week
weekly_food = food/4 #how much to be spent in a week on food

weekly_transport = transport/4 #how much to be spent in a week on transport
weekly_houseitems = house_items/4 #how much to be spent in a week on household items

weekly_healthproducts = health_products/4 #how much to be spent in a week on health products
weekly_other = other/4 #how much to be spent in a week on other

print("This week, save £" + str(weekly_savings))
print("This week, spend £" + str(weekly_food) + " on food")

print("This week, try spend £" + str(weekly_transport) + " on transport")
print("You can spend £" + str(weekly_houseitems) + " on household items this week")

print("Enjoy shopping for health products this week with £" + str(weekly_healthproducts))
print("Finally, incase there are other expenses, you have £" + str(weekly_other) + " to save the day")
