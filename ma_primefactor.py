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
        print(f"Number mod Factor = {number % factor}")
        if number % factor == 0 and number != factor:
            print("i was here")
            composite_factors.append(factor)
            factorisation(factor)
        elif number % factor == 0 and number == factor:
            prime_factors.append(factor)
            print("i was here 2")
        else:
            print("i was here 3")
            continue
    if len(composite_factors) > 0:
        for i in composite_factors:
            composite_factors.remove(i)
            factorisation(i)


# trial division
def trial_division():
    start_time = time.time()
    factorisation(user_integer)
    print(f"The largest prime factor was: \n {prime_factors}\n {composite_factors}")
    print(f"--- {(time.time() - start_time)} seconds ---")


trial_division()
