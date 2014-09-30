__author__ = 'Eliud'

#calculates the probability of event E given event F for two total outcomes
#events are 'e' and 'f'; Probabilities are merely denoted as e,f, eGivenF, etc.
def bayes_formula(e, e_comp, f_given_e, f_given_e_comp):

    numerator = f_given_e * e
    denominator = (f_given_e * e) + (f_given_e_comp * e_comp)

    return numerator/denominator
