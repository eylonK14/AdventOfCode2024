def main():
    left = []
    right = []
    
    with open("input.txt") as f:
        for  line in f:
            row = line.split("   ")
            left.append(int(row[0]))
            right.append(int(row[1]))
    f.close()
    
    left.sort()
    right.sort()
    
    sim = 0
    for i in range(0, 1000):
        sim += abs(right.count(left[i]) * left[i])
    print(sim)
        


if __name__ == "__main__":
    main()