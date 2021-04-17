def Divisors(n):
  print(n, " is divisible by: ")
  for i in range(1,n):
    if n % i == 0:
      print(i, ",")

Divisors(16)