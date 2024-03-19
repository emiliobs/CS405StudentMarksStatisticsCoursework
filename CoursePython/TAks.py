def add_three(input_var):
    output_var = input_var + 3
    return output_var


result = add_three(55)

print(result)

print("----------------------------------------------------------------------")

def get_pay(num_hours):
    # Pre-tax pay, based on receiving £15/hours
    pay_pretax = num_hours * 15 
    # After-tax pay, based on being in12% tax bracket
    pay_aftertax = pay_pretax * (1 - 0.12)
    
    return pay_aftertax

pretax = get_pay(32)
print("£", pretax)

print("----------------------------------------------------------------------")


def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretext = num_hours *  hourly_wage
    # After-tax pay
    pay_aftettax = pay_pretext * (1 - tax_bracket)
    return pay_aftettax
pay_aftertax = get_pay_with_more_inputs(40, 15, .12)

print("£", pay_aftertax)

print("----------------------------------------------------------------------")

# Define the fucntion with no arguments and with no return
def print_hello():
 print("Hello, You!")
 print("Good Morning!")
 
 # Call the function


print_hello()


print("----------------------------------------------------------------------")

def get_expected_cost(beds, baths):
    
    if(beds <= 0 and baths <=0):
        return value = 80000
    elif(beds == 1 and baths == 1):
         return value = (80000 + 120000)
    elif(beds == 2 and baths == 1):
        return value = 80000 + 150000
    else:
        return "Plase, You must enter a valid Beads and Baths Numbers."      
        
get_cost = get_expected_cost(0,0)

print(get_cost)               
 