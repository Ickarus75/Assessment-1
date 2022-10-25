from optimal_change import optimal_change

print(f"1: {optimal_change(62.15, 100)}")# basic test, single denomination
print(f"2: {optimal_change(62.15, 30)}")# if user doesn't have enough money to purchase item
print(f"3: {optimal_change(62.15, 1000)}")# if the user puts in an excessive amount of money
print(f"4: {optimal_change(62.15, 100.37)}")# if the user adds change to the value
print(f"5: {optimal_change(1, 299.92)}")# tests plurals, 2x$50 is 100 so 50 plural should never show, same for $10. $5, $0.05
print(f"6: {optimal_change(1, 187.41)}")# 186.46 test singular punctuaction in the formatting for each denomination
print(f"7: {optimal_change(100, 100)}")# Exact payment
