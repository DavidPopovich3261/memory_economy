


def input_size()->int|bool:
    size=input('Please enter a size')
    try:
        size=int(size)
    except:
        print('The input is not a number')
        size=input_size()
    if (size **2) % 2 !=0:
        print("The package is not even.")
        size=input_size()
    return size


def input_cards()->list:
    card=[]
    card.append(input("x"))
    card.append(input("y"))
    try:
        card[0]=int(card[0])
        card[1]=int(card[1])
    except:
        print('The input is not a number')
        card=input_cards()
    return card


def print_metrix(deck)->None:
    print(f"{"=":3}"*len(deck))
    for i in deck:
        for j in i:
            print(f"{j:2}",end=" ")
        print()
    print(f"{"=":3}"*len(deck))
