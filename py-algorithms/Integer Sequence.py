def sequence(n):
    result = ""
    for number in range(1,n+1):
        result += str(number)
    return result

print(sequence(5))
print(sequence(10))
print(sequence(1))
print(sequence(99))
print(sequence(0))