def reverse_strings(s):
    return s[::-1]
print(reverse_strings("Hello"))
print(reverse_strings("Pravin"))

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Race car"))
print(is_palindrome("hello"))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(10))

def primes_up_to(p):
    primes = []

    for num in range(2, p+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(primes_up_to(20))

def word_frequency(text):
    import string
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_freq = dict(sorted(freq.items(),
                              key= lambda x : x[1], reverse= True))
    return sorted_freq

print(word_frequency("The cat sat on the mat the cat"))

def main():
    while True:
        print("\n=== String & Number Toolkit ===")
        print("1. Reverse a string")
        print("2. Check palindrome")
        print("3. Find primes up to N")
        print("4. Calculate factorial")
        print("5. Word frequency")
        print("6. Exit")

        choice = input("\nEnter Choice (1-6): ")

        if choice == "1":
            s = input("Enter string: ")
            print(reverse_strings(s))
        elif choice == "2":
            s = input("Enter string: ")
            print(is_palindrome(s))
        elif choice == "3":
            n = int(input("Enter N: "))
            print(primes_up_to(n))
        elif choice == "4":
            n = int(input("Enter N: "))
            print(factorial(n))
        elif choice == "5":
            text = input("Enter text: ")
            print(word_frequency(text))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()