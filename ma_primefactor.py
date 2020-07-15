import time

try:
    user_integer = int(input("What number would you like to prime factorize?\n"))
    while user_integer <= 1:
        user_integer = int(input("Select a number that's larger than 1.\n"))
except ValueError as v_err:
    print(f"Not integer, try again. \n {v_err}")
    exit()
except Exception as err:
    print(f"Other error occurred: {err}")
    exit()

composite_divisors = []
composite_quotients = []


# recursive factorisation
def factorisation(number):
    for factor in range(2, int(round((number ** 0.5))) + 1):
        if number % factor == 0:
            composite_divisors.append(factor)
            composite_quotients.append(int(number / factor))
            break
        else:
            continue
    if composite_quotients:
        for sub_factor in composite_quotients:
            composite_quotients.remove(sub_factor)
            factorisation(sub_factor)
    else:
        composite_divisors.append(number)


# trial division
def trial_division():
    start_time = time.time()
    factorisation(user_integer)
    prime_factors = sorted(composite_divisors, reverse=True)
    print(f"The largest prime factor was: \n{prime_factors[0]}")
    print(f"--- {(time.time() - start_time)} seconds ---")


trial_division()
