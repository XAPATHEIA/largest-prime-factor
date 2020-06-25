import time

try:
    composite_number = int(input("What number would you like to prime factorize?\n"))
except ValueError as v_err:
    print(f"Not integer, try again. \n {v_err}")
except Exception as err:
    print(f"Other error occurred: {err}")


# trial division
start_time = time.time()
base_primes = [2, 3, 4, 7]
for i + 1 in range(composite_number):


#print(f"--- {(time.time() - start_time)} seconds ---")