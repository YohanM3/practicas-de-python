# def my_print():
#     print('This is my print')
# my_print()

# def aaa(text):
#     print(text*2)
# aaa('this is my exercise the function ')
# aaa('hi ')

# def suma(a, b):
#     print(a+b)
# suma(2 ,5)
def suma(min, max):
    sum=0
    for x in range(min, max):
        sum+=x
    return sum
result = suma(10, 20)
print(result)
resultado=suma(result, result+5)
print(resultado)