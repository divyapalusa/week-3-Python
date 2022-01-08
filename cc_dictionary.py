inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5} # given dictionary.
def print_total_snowfall(inches_snow): # declaring function name with parameter.
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches # incrementing  total_inches by inches.
    print("Total snow fall inches :",total_inches)
    
    
print_total_snowfall(inches_snow) # function call
inches_snow["Thursday"]= int(input("How many inches of snow fell on Thursday? ")) # user input.
print_total_snowfall(inches_snow) # again function call for total snowfall .