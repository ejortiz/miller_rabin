Probabilistic Prime Testing (Miller-Rabin Test)

The Miller-Rabin test determines if an entered value is composite or probably not composite, i.e. prime.
In this sense, this procedure does not prove that an entered value is prime, but for practical purposes, we can
get to near 100% certainty.

The following gives a superficial explanation of the inner workings of the algorithm, but for details and further
explanation, consult the sources at the bottom of this readme.

1)  prime_tests.is_composite

    by Fermat's little theorem we know that if p is prime, then a^p (mod p) = a, for some integer a.
    The equivalent contrapositive of this statement is if a^p (mod p) != a, then p is not prime.

    To attempt to check if a value n is prime, we can try different values of 'a.' If a^n (mod n)! = a, then clearly,
    n is not prime. In this case, we call 'a' a witness for compositeness of n.

    If we keep attempting to find a witness for n but can't, then in some sense, the probability of n being prime
    should increase. There do exist Carmichael Numbers: for a composite natural number c, a^c (mod c) = a (mod c) for
    all integers a, so we need a better way to test for primes.

    Proposition: Let p be an odd prime and write  p-1 = 2^k with q odd. Let a be an integer not divisible by p. Then,
    one of the following occurs:
    i) a^q (mod p) = 1 (mod p)
    ii) one of a^q, a^2q,...,a^((2^k-1)q) is congruent to -1 mod p

    Informal proof: Again, this deals with Fermat's Little Theorem, since a^(p-1) (mod p) = a^(2^k)q (mod p) = 1 (mod p).
    So either a^q (mod p) = 1 (mod p) or  one of a^q, a^2q,...,a^(2^k)q is congruent to -1 modulo p or 1 mod p, since
    a^((2^k)q) (mod p) = 1 (mod p), and if we take a square root, either a^((2^k-1)q) (mod p) = -1 (mod p), or
    a^((2^k-1)q) (mod p) = 1 (mod p). If the latter, we repeat the above process and eventually, we will get our desired
    property.

    Thus, we call an integer 'a,' with gcd(a,n) = 1, a Miller-Rabin witness for the compositeness of n if BOTH
    i) a^q (mod n)  != 1 (mod n)
    ii) a^((2^j)q) != -1 (mod n)
     are true.

    Therefore, by repeating the test for multiple values of 'a' and not finding a Miller-Rabin witness, this should
    continuously increase the probability of a natural number being prime.

2)  prime_tests.prime_probability

    Our algorithm in the functions is_composite does that: it checks for compositeness of a natural number.
    To calculate the probability of a natural number N being prime after running 'is_composite' on N
    Q times we define two events:

    E = N is not composite, i.e. prime
    F = is_composite returns FALSE Q times

    We want to calculate the probability of E given F. In notation Pr(E|F)

    By Bayes' Formula (http://en.wikipedia.org/wiki/Bayes%27_theorem), we must first find certain probabilities
    to compute:

    Pr(F|E): We must find Pr(is_composite False|not composite). In words we calculate the probability:
             If N is not composite, then is_composite returns False. The contrapositive:
             If is_composite returns True, then N is composite. The probability of the previous statement is
             100%, since that is what is_composite tests for. Thus, running Q times,
             [Pr(is_composite False|N is not composite)]^Q = 1^Q =1

    Pr(E): The probability of a randomly-chosen natural number N being prime is approximately 1/ln(N)
           by the Prime Number Theorem (http://en.wikipedia.org/wiki/Prime_number_theorem)

    Pr(E complement): We calculated Pr(E), so simply Pr(E comp) = 1 - Pr(E)

    Pr(F|E comp): First, without proof--but resource for proof given ([2], Theorem 10.3)--we know that,
                  If N is an odd composite number, then at least 75% of the integers between 1 and N-1
                  are Miller-Rabin witnesses for N.
                  Thus, Pr(is_composite True| N is composite) = .75
                  So Pr(F|E) = Pr(is_composite False| N is composite)^Q
                  = [1 - Pr(is_composite True| N is composite)]^Q = (1 - .75)^Q = .25^Q

    We then have the necessary info to compute the probability.

3) probability.bayes_formula
    simple Bayes' Formula calculation



Sources:

1. Hoffstein, Pipher, Silverman. An Introduction to Mathematical Cryptography. 2008. Springer
2. Shoup, Victor. A Computational Introduction to Number Theory and Algebra (version 2).
       http://shoup.net/ntb/
3. Bayes' Theorem. http://en.wikipedia.org/wiki/Bayes%27_theorem
4. Prime Number Theorem. http://en.wikipedia.org/wiki/Prime_number_theorem







