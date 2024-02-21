def prime_number(num):
def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
    
    return False

  return True

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"