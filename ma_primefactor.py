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

prime_factors = []
composite_factors = []


# recursive factorisation
def factorisation(number):
    for factor in range(2, number):
        if number == 2:
            prime_factors.append(number)
        elif number % factor == 0:
            composite_factors.append(factor)
            factorisation(factor)
        else:
            continue
    if len(composite_factors) > 0:
        for i in composite_factors:
            composite_factors.remove(i)
            factorisation(i)


# trial division
def trial_division(composite_number):
    start_time = time.time()
    factorisation(composite_number)
    print(f"The largest prime factor was {prime_factors}\n {composite_factors}")
    print(f"--- {(time.time() - start_time)} seconds ---")


trial_division(user_integer)
