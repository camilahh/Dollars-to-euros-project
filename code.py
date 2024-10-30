


convert = input("would you like to convert your dollars to euros? (y/n) ")

while convert == "y":
    
    dollar = float(input("enter dollar amount to be convert: "))
    euro = dollar * .94540
    print("you will have " + str(euro) + " euros" )
    convert = input("would you like to convert your dollars to euros? (y/n) ")

print("ok then...") 

