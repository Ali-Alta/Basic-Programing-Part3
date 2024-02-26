def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def full_prima(N):
    # Mengecek apakah N adalah bilangan prima
    if not is_prime(N):
        return 'Tidak'

    # Mengecek setiap digit dari N apakah merupakan bilangan prima
    for digit in str(N):
        if not is_prime(int(digit)):
            return 'Tidak'
    
    return 'Ya'

if __name__ == '__main__':
    print(full_prima(2))  # True
    print(full_prima(3))  # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # Tidak
    print(full_prima(37)) # True
    print(full_prima(41)) # Tidak
    print(full_prima(43)) # Tidak
    print(full_prima(53)) # True