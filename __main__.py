def euclideanDistance(x: int, y: int):

    return (x**2 + y**2)**.5


def minDistance(distances: list):

    return min(distances)

def main():

    points = [(1, 1), (2, 2), (3, 3), (4, 4)]
    distances = [euclideanDistance(x, y) for x, y in points]
    
    print("Minimum Euclidean Distance is:", minDistance(distances))
    input("Press Enter to exit...")
    
if __name__ == '__main__':

    main()