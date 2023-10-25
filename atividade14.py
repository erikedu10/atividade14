sal = float(input("insira seu salário:"))

if sal > float("1250.00"):
 print("seu novo salário é", sal+(sal/100))
else:
 print("seu novo salário é", sal+(sal/150))