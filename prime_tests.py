__author__ = 'Eliud'
import fractions
import random
import math
import probability

# Miller-Rabin test with potential witness

def is_composite(natural_num, integer_witness):

    if (natural_num % 2 == 0 or
        (1 < fractions.gcd(natural_num, integer_witness) < natural_num)):
        return True

    s = natural_num - 1
    exp = 0

    # write naturalNum as 2^(exp)*s with s odd
    while s % 2 == 0:
        exp += 1
        s /= 2

    integer_witness = pow(integer_witness, s, natural_num)

    if integer_witness == 1:
        return False

    for i in xrange(0, exp):
        # if integer_witness mod (naturalNum) == -1 mod(naturalNum), then probably prime
        if integer_witness % natural_num == natural_num - 1:
            return False
        integer_witness = pow(integer_witness, 2, natural_num)

    return True


def prime_probability(natural_num, num_trials):

    # The probability that a natural number n is composite given that is_composite
    # returns true is 100% [Pr(is_composite returns true|n is composite];
    # equivalently, the contrapositive, Pr(n is prime|is_composite returns false) = 100%

    COMPOSITE_GIVEN_ISCOMPOSITE_T = 1.0

    #For every odd composite natural number n, at least 75% of integers between 1 and n-1
    #are witness for the compositeness of n, i.e. Pr(is_composite True|n is composite) = .75
    #The complement is Pr(is_composite False|n is composite) = 1 - Pr(is_composite True|n is composite) = .25
    ISCOMPOSITE_T_GIVEN_COMPOSITE = .75

    #By the Prime Number Theorem,
    prob_randnum_prime = 1 / (math.log(natural_num))

    prime_prob = 0

    #get potential witnesses for compositeness and test them
    try:
        witness_list = random.sample(xrange(1, natural_num), num_trials)
    except IndexError:
        print 'Number of trials entered is out of range.'

    for item in witness_list:
        if is_composite(natural_num, item):
            return prime_prob

            #want to compute probability that a number is not composite (i.e., prime)
            #given that the algorithm returns false num_trials times

    prime_prob = probability.bayes_formula(prob_randnum_prime, 1 - prob_randnum_prime,
                                           COMPOSITE_GIVEN_ISCOMPOSITE_T,
                                           pow(1 - ISCOMPOSITE_T_GIVEN_COMPOSITE, num_trials))

    return prime_prob






