from greeting import hello
import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: greeter <name>")
        sys.exit(1)
    print(hello(args[0]))

if __name__ == "__main__":
    main()
