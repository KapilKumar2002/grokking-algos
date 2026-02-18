
def gcd(a : int, b : int)-> int:
    if b == 0:
        return a
    
    return gcd(b, a % b)


def lcm(a : int, b : int) -> int:
    return (a * b) // gcd(a, b)

if __name__ == "__main__":
    a : int = 48
    b : int = 18

    print(f"GCD of {a} and {b} is: {gcd(a, b)}")
    print(f"LCM of {a} and {b} is: {lcm(a, b)}")