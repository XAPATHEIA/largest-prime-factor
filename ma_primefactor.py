import time

try:
    user_integer = int(input("What number would you like to prime factorize?\n"))
    while user_integer <= 0:
        user_integer = int(input("Select a number that's larger than 0.\n"))
except ValueError as v_err:
    print(f"Not integer, try again. \n {v_err}")
    exit()
except Exception as err:
    print(f"Other error occurred: {err}")
    exit()

composite_factors = []


# recursive factorisation
def factorisation(number):
    for factor in range(2, int(round((number ** 0.5))) + 1):
        print(factor)
        if number % factor == 0:
            composite_factors.append(factor)
        else:
            continue


# trial division
# def trial_division():
    # start_time = time.time()
    # prime2_factors, composite2_factors = factorisation(user_integer)
    # print(f"The largest prime factor was: \n {prime2_factors}\n {composite2_factors}")
    # print(f"--- {(time.time() - start_time)} seconds ---")


factorisation(user_integer)
print(composite_factors)
