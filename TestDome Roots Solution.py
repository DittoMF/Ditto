from math import sqrt

def find_roots(a, b, c):
    
    disc = b**2 - 4*a*c
    if disc >= 0:
        return ((-b + sqrt(disc))/(2*a),(-b - sqrt(disc))/(2*a))
    if disc < 0:
        return (-b/(2*a),"+",sqrt(disc*(-1))/(2*a),"i" \
                -b/(2*a),"-",sqrt(disc*(-1))/(2*a),"i")

print(find_roots(2, 10, 8));
