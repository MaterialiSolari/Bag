import math

#Step 1 (5 pts). Read from input the number of people (int), average slices per person (float) 
# and cost of one pizza (float). Calculate the number of whole pizzas needed (8 slices per pizza). 
# There will likely be leftovers for breakfast. Hint: Use the ceil() function from the math library 
# to round up to the nearest whole number and convert to an int. Calculate and output the cost for all pizzas.

num_people = int(input('Number of people:'))
avg_slices_per_person = float(input('Average slice per person:'))
cost_per_pizza = float(input('Cost per pizza: $'))

pizzas_needed = math.ceil(num_people * avg_slices_per_person / 8)

# Calculate the total cost
total_cost = pizzas_needed * cost_per_pizza
sales_tax = (total_cost * 0.07)
delivery = 5
final_price = total_cost + sales_tax + delivery
# Step 2: Output the result
print("Friday Night Party")
print(f"{pizzas_needed} Pizzas: ${total_cost:.2f}")
print(f'Tax:${sales_tax:.2f}')
print(f"Delivery:${delivery}")
print('Total:$', final_price)

num_people_saturday = int(input('Number of people:'))
avg_slices_per_person_saturday = float(input('Average slice per person:'))
cost_per_pizza_saturday = float(input('Cost per pizza: $'))

pizzas_needed2 = math.ceil(num_people_saturday * avg_slices_per_person_saturday / 8)

# Calculate the total cost
total_cost2 = pizzas_needed2 * cost_per_pizza_saturday
sales_tax2 = (total_cost2 * 0.07)
final_price_saturday = total_cost2 + sales_tax2 + delivery
# The cost for delivery and pizza won't change during this program, I like having statics variables.
print("Saturday Night Party")
print(f"{pizzas_needed2} Pizzas: ${total_cost2:.2f}")
print(f'Tax:${sales_tax2:.2f}')
print(f"Delivery:${delivery}")
print('Total:$', final_price_saturday)

num_people_Sunday = int(input('Number of people:'))
avg_slices_per_person_Sunday = float(input('Average slice per person:'))
cost_per_pizza_Sunday = float(input('Cost per pizza: $'))

pizzas_needed3 = math.ceil(num_people_Sunday * avg_slices_per_person_Sunday / 8)

# Calculate the total cost
total_cost3 = pizzas_needed3 * cost_per_pizza_Sunday
sales_tax3 = (total_cost3 * 0.07)
final_price_Sunday = total_cost3 + sales_tax3 + delivery

print("Sunday Night Party\n")
print(f"{pizzas_needed3} Pizzas: ${total_cost3:.2f}")
print(f'Tax:${sales_tax3:.2f}')
print(f"Delivery:${delivery}")
print('Total:$', final_price_Sunday)
print(f"Final price from Friday, Saturday, and Sunday:${final_price + final_price_saturday + final_price_Sunday}")