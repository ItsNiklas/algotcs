def main() -> None:
    # Very weird problem? Why is this in this chapter?
    # Read from stdin.
    input = [x.rstrip() for x in open(0)][1:]

    # Quick sequence iteration to print result.
    print("NO" if ('W','W') in zip(*input) else "YES")

    
if __name__ == '__main__':
    main()