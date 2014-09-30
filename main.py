__author__ = 'Eliud'

import prime_tests


def main():

    is_natural_num = False
    valid_num_trials = False

    print "Welcome to the Miller-Rabin Test!"

    natural_num = raw_input("Enter your natural number for primality testing: ")

    while is_natural_num is False:
        try:
            natural_num = int(natural_num)
            if natural_num < 1:
                natural_num = raw_input("Please enter a natural number (1,2,3,...,n,...:) ")
            else:
                is_natural_num = True
        except ValueError:
            natural_num = raw_input("Please enter a natural number (1,2,3,...,n,...:) ")

    num_trials = raw_input("Enter the number of trials (between 1 and " + str(natural_num-1) + "): ")

    while valid_num_trials is False:
        try:
            num_trials = int(num_trials)
            if num_trials < 1 or num_trials > natural_num-1:
                num_trials = raw_input("Please enter the number of trials (between 1 and " + str(natural_num-1) + "): ")
            else:
                valid_num_trials = True
        except ValueError:
            num_trials = raw_input("Please enter the number of trials (between 1 and " + str(natural_num-1) + "): ")


    prime_prob = prime_tests.prime_probability(natural_num, num_trials)

    if prime_prob == 0:
        print natural_num, "is composite. Prime probability:", prime_prob, "%"
    else:
        print "Prime probability of", natural_num, ":", prime_prob * 100, "%"


if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it