
dollar = float(input("enter dollar amount to be convert: "))
euro = dollar * .94540

convert = input("would you like to convert your dollars to euros? ")
if convert == "yes":
    print("you will have " + str(euro) + " euros" )
else:
    print("ok then...") 
    exit()