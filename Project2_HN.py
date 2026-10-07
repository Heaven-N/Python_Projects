#Project 2
#Heaven Neumann

#Task 1
#Make use that program displays meaningful output to the user
def get_input():
    print("Please enter some text:", end=" ")
    userInput = input("")
    print(f"You typed '{userInput}' which has {len(userInput)} character(s)")
'''
How may characters does a word have?
Please enter some text: Pneumonoultramicroscopicsilicovolcanoconiosis
You typed 'Pneumonoultramicroscopicsilicovolcanoconiosis' which has 45 character(s)
'''

def get_num_of_letters(txt):
    num_of_letters = 0
    for char in txt:
        if char.isalpha():
            num_of_letters += 1
    return num_of_letters
'''
How many letters does a word have?
Please enter a mix of letters, numbers and special characters: L0st_my_m1nd-1n-p4r!$
The number of letters in the text is 11
'''

def get_acronym(txt):
    words = txt.split(" ")
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym
'''
Let's create an acronym from the text
Please enter what you wnat to make an acronym from: Python Programming Language
The acronym for 'Python Programming Language' is 'PPL'
'''

def task1():
    print("How may characters does a word have?")
    get_input()
    print()
    print("How many letters does a word have?")
    txt1 = input("Please enter a mix of letters, numbers and special characters: ")
    print(f"The number of letters in the text is {get_num_of_letters(txt1)}")
    print()
    print("Let's create an acronym from the text")
    txt2 = input("Please enter what you wnat to make an acronym from: ")
    print(f"The acronym for '{txt2}' is '{get_acronym(txt2)}'")
    print()



#Task 2
def inf_num_gen():
    num = 0
    while True:
        yield num
        num += 1

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_gen():
    for num in inf_num_gen():
        if is_prime(num):
            yield num

def print_primes():
    prime_count = 0
    for prime in prime_gen():
        print(prime, end=" ")
        prime_count += 1
        if prime_count % 20 == 0:
            print()
        if prime_count == 100:
            break
    print()
'''
Printing the first 100 prime numbers:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 
179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 
283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 
419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 
'''

def print_20_primes_from_110th():
    prime_count = 0
    num_count = 0
    for prime in prime_gen():
        prime_count += 1
        if prime_count >= 110:
            print(prime, end=" ")
            num_count += 1
            if num_count % 20 == 0:
                print()
            if prime_count == 130:
                break
    print()
'''
Printing the first 20 prime numbers starting from the 110th prime:
601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 
733
'''

def count_primes():
    prime_count = 0
    count = 0
    for prime in prime_gen():
        prime_count += 1
        if prime_count >= 110:
            count += 1
            if prime > 5000:
                print(f"There are {count} primes between the 110th prime number and 5000")
                break
'''
Counting the number of primes between the 110th prime and 5000:
There are 561 primes between the 110th prime number and 5000
'''


def task2():
    print("Printing the first 100 prime numbers:")
    print_primes()
    print()
    print("Printing the first 20 prime numbers starting from the 110th prime:")
    print_20_primes_from_110th()
    print()
    print("Counting the number of primes between the 110th prime and 5000:")
    count_primes()
    print()


def main():
    print("Exexuting task 1:")
    task1()
    print("Executing task 2:")
    task2()

main()

