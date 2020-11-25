import sys

def main(username):
    print("Hello " + username)

if __name__ == "__main__":
    username = ""
    if (len(sys.argv) > 1):
        username = sys.argv[1]
    else:
        username = "World"
    main(username)