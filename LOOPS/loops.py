# cars = ['ford','bugatti','toyota','tata']

# # for car in cars:
# #     print(car)

# # for car in cars[1:3]:
# #     print(car)

# for car in cars:
#     if car == 'bugatti':
#         print(f'{car}- Chiron Sport')
#         break
#     else:
#         print(car)

age = 25
num = 0

while num < age:
    if num == 0:
        num +=2
        continue
    if num % 2 == 0:
        print(num)
    if num == 10:
        break
    num +=2
   