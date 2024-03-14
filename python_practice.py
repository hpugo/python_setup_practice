# 

user = 'Henry'
def hello():
    print("Hello ", user)
hello()


def pack(item1, item2, item3):
    return [item1, item2, item3]
print(pack(1, 2, 3))

def eat_lunch(lunch_list):
    if not lunch_list:
        print("My lunchbox is empty")
    else:
        print("Firsr I eat ", lunch_list[0])
        for food in lunch_list[1:]:
            print("Next I eat", food)

eat_lunch(['Apples', "Oranges", "Pears"])
eat_lunch([])
