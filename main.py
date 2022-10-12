y = 0
x = int(input("First Number: "))
divisor = int(input("second Number: "))
while x >= divisor:
  x -= divisor
  y += 1

print(f'Quotient: {y} & remainder {x}')