a = float(input("podaj a: "))
b = float(input("podaj b: "))
print(a+b)
print(a-b)
print(b-a)
print(a*b)
print(a/b)
print(b/a)
print(a^b)
print(b^a)
print(a%b)
print(b%a)
print(a@b)

tabela_liczb=[1,2,3,4,5,6,7,8,9,0]
try:
    a and b != tabela_liczb
except Exception as e:
    print ("Wartość nie jest liczbą: ", e)
poprawny_operator = ["+", "-", "*", "/", "^", "%"]
try:
    operator != poprawny_operator
except Exception as e:
    print ("Zastosowano niepoprawny operator: ", e)
try:
    b/0 and a/0
except Exception as e:
    print ("Dzielenie przez 0 jest niepoprawną operacją: ", e)
