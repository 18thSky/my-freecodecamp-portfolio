def square_root_bisection(number,tolerance =5,iterations =5):
        if number < 0:
            raise ValueError("Square root of negative number is not defined in real numbers")
        elif number == 0 or number == 1:
            print(f"The square root of {number} is {number}")
            return number
        elif number > 0:
            low = 0
            high = max(1, number)
            for iteration in range(iterations):
                mid = (low+high)/2
                if mid * mid > number:
                    high = mid
                else:
                    low = mid
                if high - low <= tolerance:
                    print(f"The square root of {number} is approximately {mid}")
                    return mid
                print(f"Failed to converge within {iterations} iterations")

square_root_bisection(0.001, 1e-7, 50)