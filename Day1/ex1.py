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
    
    dist = 0
    for i in range(0, 1000):
        dist += abs(left[i] - right[i])
    print(dist)
        


if __name__ == "__main__":
    main()