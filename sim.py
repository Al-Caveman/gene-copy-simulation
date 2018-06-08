import random
import sys

TRIALS = 1000
BABIES = 19
GENES = list(range(0,1000))
GENES_COPIED_CHILD_MALE = 500
GENES_COPIED_CHILD_FEMALE = 500

# run simulation
sys.stderr.write('simulating the percentage of your genes that you will replicate into babies, should you make {} babies, under the assumption that you have {} genes, {} of which gets delivered to a male baby, and {} of which gets delivered to a female baby, all while using {} trials..'.format(
    BABIES,
    len(GENES),
    GENES_COPIED_CHILD_MALE,
    GENES_COPIED_CHILD_FEMALE,
    TRIALS
))
sys.stderr.flush()
num_genes_copied_total = 0
for i in range(0, TRIALS):
    total_genes_copied = {}
    for baby in range(0, BABIES):
        # male or female?
        if random.randint(0,1):
            ismale = True
        else:
            ismale = False

        # copy your genes
        random.shuffle(GENES)
        if ismale:
            genes_copied = GENES[0:GENES_COPIED_CHILD_MALE]
        else:
            genes_copied = GENES[0:GENES_COPIED_CHILD_FEMALE]

        # some stats
        for g in genes_copied:
            total_genes_copied[g] = True

    # remember what happened with these babies
    num_genes_copied_total += len(total_genes_copied)

# print stats
sys.stderr.write(' {}% of your genes are copied.\n'.format(
    num_genes_copied_total/TRIALS/len(GENES)*100
))
sys.stderr.flush()

