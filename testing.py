a=["hello", "how", "is", "your", "day"]
num_of_char = []
var = 0
for item in a:
    num_of_char.append(len(item))
    var = sum(num_of_char)
    if var >= 13:
        print var
        print num_of_char
        break