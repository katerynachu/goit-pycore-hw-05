def caching_fibonacci():
    cache ={} #Initialize the cache dictionary
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache :#Caching Check
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #Recursive Calculation
        return cache[n]
    return fibonacci  # Return the inner function

def main():

    fib = caching_fibonacci()

    print(fib(10)) 
    print(fib(15)) 

if __name__ == '__main__':
    main() 
