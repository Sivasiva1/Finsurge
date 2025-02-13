''':
Units Consumed: 250
Tariff Slabs (Per Unit Rate):
0 - 100 units → ₹3/unit
101 - 200 units → ₹5/unit
Above 200 units → ₹8/unit
Tax: 5%
'''

units_charged = 250 

charges = 0 
#base case 
if units_charged < 0:
     print("its not a valid input")

elif units_charged <= 100 :
     print("You have to pay :")
     charges = units_charged * 3 
     including_tax = (charges + ((5/100) *charges)) 
     print("Original Charges ",charges)
     print("Including tax ",including_tax)

elif units_charged <=200:
     print("You have to pay :")
     charges = (100*3) + ((units_charged - 100)*5) 
     including_tax = (charges + ((5/100) *charges))
     print("Original Charges ",charges)
     print("Including tax ",including_tax)
     
else:
     print("you have to pay ")
     charges = (100*3) + (100*5) + ( (units_charged - 200) * 8 )
     including_tax = (charges + ((5/100) *charges)) 
     print("Original Charges " , charges)
     print("Including tax ",including_tax)