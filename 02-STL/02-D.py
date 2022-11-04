def main() -> None:    
    # Read from stdin.
    input = list(open(0))

    # Iterate and always store latest index in a dictionary.
    hashes = dict()
    for i, v in enumerate(input[1].split()):
        hashes.update({v : i})

    # Pretty print. Loop over all codes and return dictionary value.
    print(*[hashes.get(b.rstrip(), -1) + 1 for b in input[2:]], sep = '\n')
    
if __name__ == '__main__':
    main()