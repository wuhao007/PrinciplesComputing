"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
 
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)
 
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
 
 
def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
 
    hand: full yahtzee hand
 
    Returns an integer score 
    """
    lista_valores = list(hand)
    max_vals = []
    
    for items in lista_valores:
        ocurrencias = lista_valores.count(items)
        max_vals.append(items * ocurrencias)
    return max(max_vals)
 
def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
 
    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled
 
    Returns a floating point expected value
    """
    sequences = gen_all_sequences(enum(num_die_sides), num_free_dice)
    scores = 0.0
    for tupla in sequences:
        scores += score(held_dice + tupla)
    return scores / len(sequences)
 
def enum(number):
    """
    Genera una tupla de tamanio n
    """
    listt = []
    count = 1
    while number >= count:
        listt.append(count)
        count += 1
    return tuple(listt)
 
 
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
 
    hand: full yahtzee hand
 
    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])
    for item in list(hand):
        temp_set = set(())
        for partial_sequence in answer_set:
            for bnr in [0,1]:
                if bnr:
                    new_sequence = list(partial_sequence)
                    temp_set.add(tuple(new_sequence))
                else:
                    temp_set.add(partial_sequence+(item,)) 
        answer_set = temp_set
    return answer_set
    
    #return set([(), (1,)])  
    #return set([()])
 
 
 
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
 
    hand: full yahtzee hand
    num_die_sides: number of sides on each die
 
    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = tuple(gen_all_holds(hand))
    list_expect  = []
    for hold in all_holds:
        expect = expected_value(hold, num_die_sides, len(hand) - len(hold))
        list_expect.append((expect , (hold)))
    maximum = max(list_expect)
    return (maximum)
 
    # ((1,), 6)
    # (3.5, ())
 
 
def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    score(hand)
    hand_score, hold = strategy(hand, num_die_sides)
    
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()
#gen_all_holds((1, 2))
 
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)