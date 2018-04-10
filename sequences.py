import argparse

def calc_sequence(initial, length, verbose=False):
    """

    Use an iterative approach to calculate a self-summing sequence, in which
    the previous `initial` numbers are used to generate the next number.
    The sequence begins with the first `initial` numbers, beginning from 0.
    A total of `length` entries in the sequence are returned, if `length` is
    larger than `initial`, otherwise `initial` entries are returned.

    input:
    ------
    initial : (integer) indicates the number of entries to sum for the next 
              entry, and therefore, also the initial length of the sequence
    length : (integer) the number of entries to include in the sequence
    verbose : (bool) whether or not to print extra output [optional]

    output:
    -------
    seq : list(integer) the resulting sequence of integers
    """
    
    if verbose:
        print("Will calculate a sequence starting with {0} numbers and showing {1} terms from that sequence.".format(initial,length))

    seq = list(range(initial))
    while len(seq)<length:
        seq.append(sum(seq[-initial:]))

    return seq

if __name__ == "__main__":
          
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--number", type=int, default=2, required=False,
                        help="Determines how many initial numbers are used/necessary to compute the sequence.")

    parser.add_argument("-l", "--length", type=int, default=10, required=False,
                        help="Determines how many terms in the sequence to calculate and print.")

    parser.add_argument("-v", "--verbose", action='store_true', required=False,
                        help="Print extra information to the screen during calculation.")

    args = parser.parse_args()

    seq = calc_sequence(args.number, args.length, args.verbose)

    print(seq)
