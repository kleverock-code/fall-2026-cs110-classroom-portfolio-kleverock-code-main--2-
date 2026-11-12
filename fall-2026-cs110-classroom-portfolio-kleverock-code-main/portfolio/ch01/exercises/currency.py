rate = float(input("Please enter the conversion rate:"))
eur = float(input("Please enter how much you want to convert:"))
usd = float(eur) * float(rate) - 3
total = round(usd, 2)
print("Your converted amount is:", total)