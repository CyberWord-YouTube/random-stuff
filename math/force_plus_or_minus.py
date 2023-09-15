numbers = [3, 4, 5, 6, 7, 8]
state = 0b000000
end = False

n = "0";

while not end:
    
    
    for i, c in enumerate(numbers):
        if state & (1 << i) == 0:
            n += "+"
        else:
            n += "-"
        n += c.__str__()

    print(n.rstrip(), end=" = ")
    print(eval(n.rstrip()))

    n = "0"

    state += 1

    end = state > 0b111111