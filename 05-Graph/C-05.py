def main() -> None:
    # Read & execute from stdin.
    # No graph-theory needed, just Python.
    print(eval(open(0).read(), {}))


if __name__ == '__main__':
    main()