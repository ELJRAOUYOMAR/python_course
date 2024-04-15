import sys

def main():
    # Retrieve command-line arguments
    args = sys.argv

    # Print the command-line arguments
    print("Number of arguments:", len(args))
    print("Argument list:", args)
    print(__name__)
if __name__ == "__main__":
    main()
