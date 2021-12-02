with open('input.txt', 'r') as f:
    lines = f.readlines()

data = [int(line) for line in lines]
data = [sum(data[i:i+3]) for i in range(len(data)-2)]

# number of data points that are strictly increasing over last
total_increase = 0
for former, current in zip(data, data[1:]):
    if current > former:
        total_increase += 1

print(f"{total_increase}")
