
# This file contains the function that will be called in the main file to check if Eggy is hungry or not.

# Eggy has 4 meals a day, one portion for each meal, and each portion size is 10 grams -> TODO to look up
# Now the portion numnber is customable
# It is also possible to have more than one portion size 

import numpy as np

portion_size = 10 # grams
meal_number_per_day = 4 # default
portion_each_meal = np.ones(meal_number_per_day) # default 1 portion per meal
food_in = 1000 # grams

def eggy_food_warning(portion_size = portion_size, portion_each_meal = portion_each_meal, eggy_food = food_in):
    eggy_daily_consumpt = (portion_size * portion_each_meal).sum()
    run_out_day = eggy_food // eggy_daily_consumpt
    run_out_meal = eggy_food % eggy_daily_consumpt * meal_number_per_day
    print(":( Eggy is hungi!" + "\n" + "Eggy will run out of food in " + str(run_out_day) + " days and " + str(run_out_meal*portion_size) + " grams left.")    
    return run_out_day, run_out_meal

day, meal = eggy_food_warning(portion_size, portion_each_meal, food_in)