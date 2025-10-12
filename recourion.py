# def fibonacci(n):
#     if n in [0,1]:
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))
    
# for i in range(1,6):
#     print(fibonacci(i))


memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    
    if n<= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

for i in range(1,8):
    print(fibonacci(i))
