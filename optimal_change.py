# psuedocode prior to beginning:
# create data set of valid denominations we can provide change for (dict or list?)
# determine change due from input, need a counter?
# look through data set to figure out how many of each bill to pay (greedy style)
# have data set do part of the formatting? (maybe if i use dict?)
# format the output
valid_denominations = {
    100: ["$100 bill", "$100 bills"], 50: ["$50 bill", "$50 bills"], 20: ["$20 bill", "$20 bills"],
    10: ["$10 bill", "$10 bills"], 5: ["$5 bill", "$5 bills"], 1: ["$1 bill", "$1 bills"],
    .25: ["quarter", "quarters"], .10: ["dime", "dimes"], .05: ["nickel", "nickels"], .01: ["penny", "pennies"]
}

def optimal_change(item_cost, amount_paid): # creates a dict of denominations and total number of each
    change_due = round(amount_paid - item_cost, 2) 
    if amount_paid < item_cost: # will stop user from entering in any value less than the cost
        return "You cannot afford to purchase this item."
    elif amount_paid == item_cost:# exact payment
        return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is $0."
    total_of_each_denomination = valid_denominations.fromkeys(valid_denominations, 0) # sets total of all change to give to 0
    for key in total_of_each_denomination:
        while change_due >= key:
            total_of_each_denomination[key] += 1
            change_due = round(change_due - key, 2) # keeping precision
    return format_output(total_of_each_denomination, item_cost, amount_paid)

# loop through the return of optimal change, formatting with valid_denominations
def format_output(change_dict, item_cost, amount_paid):
    output = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    for key, value in change_dict.items():
        if value == 1: 
            output += f"{value} {valid_denominations[key][0]}, "
        elif value > 1:
            output += f"{value} {valid_denominations[key][1]}, "
    output = output[::-1].replace(" ,", '.', 1) # try refractoring this
    output = output.replace(' ,', ' dna ,', 1)
    return output[::-1]
