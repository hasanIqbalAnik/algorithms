import itertools

# allitems = ['beef', 'cheese', 'chicken', 'clothes', 'milk', 'boots']
#
# t1 = ['beef', 'chicken', 'milk']
# t2 = ['beef', 'cheese']
# t3 = ['cheese', 'boots']
# t4 = ['beef', 'cheese', 'chicken']
# t5 = ['beef', 'cheese', 'chicken', 'clothes', 'milk']
# t6 = ['chicken', 'clothes', 'milk']
# t7 = ['chicken', 'milk', 'clothes']
#
# tall = [t1, t2, t3, t4, t5, t6, t7]


allitems = [1, 2, 3, 4, 5]
t1 = [1, 3, 4]
t2 = [2, 3, 5]
t3 = [1, 2, 3, 5]
t4 = [2, 5]

tall = [t1, t2, t3, t4]

minsup = 2



def candidate_gen(frequent_keys, kmin1):
    candidate_keys = []
    to_remove = []
    if(kmin1 is 2):
        for comb in itertools.combinations(frequent_keys, kmin1):
            candidate_keys.append(list(comb))
        for subs in candidate_keys:
            for indiv in itertools.combinations(subs, kmin1):
                if list(indiv)[0] not in frequent_keys:
                    candidate_keys.remove(subs)
    else:
        joined_list = list(itertools.chain(*frequent_keys))
        set_of_items =set(joined_list)

        for comb in itertools.combinations(set_of_items, kmin1):
            candidate_keys.append(list(comb))
        for subs in candidate_keys:
            for indiv in itertools.combinations(subs, kmin1 - 1):
                if(item_in_freq_keys(list(indiv), frequent_keys) == False):
                    to_remove.append(subs)
                    break
        candidate_keys = [x for x in candidate_keys if x not in to_remove]
    return candidate_keys

def minsup_items_from_list(lst_of_items, minsup):
    joined_list = list(itertools.chain(*lst_of_items))
    set_of_items =set(joined_list)
    to_remove = []
    for item in set_of_items:
        if(joined_list.count(item) < minsup):
            to_remove.append(item)
    return sorted([x for x in set_of_items if x not in to_remove])

def compare_lists(lst1, lst2):
    flag = True
    for item in lst1:
        if(item not in lst2):
            flag = False
    return flag

def item_in_freq_keys(item, freq_keys):
    flag = False
    for sub in freq_keys:
        if(sorted(sub) == sorted(item)):
            flag = True
    return flag


def apriori(T, minsup):
    globalFreqs = []
    c1 = T
    f1 = minsup_items_from_list(c1, minsup)
    print "F1"
    print f1
    print "\n"
    fkmin1 = f1
    k = 2
    tempCtr = 0
    glbctrl = 0
    while len(fkmin1) != 0:
        ck = candidate_gen(fkmin1, k)
        print "Candidate Keys:"
        print ck
        print "\n"
        fkmin1[:] = []
        for cand in ck:
            for trns in tall:
                if (compare_lists(cand, trns)):
                    tempCtr = tempCtr + 1

            if(tempCtr >= minsup):
                fkmin1.append(cand)
            tempCtr = 0
        k = k+1
        print "Frequent Keys"
        print k-1
        print fkmin1
        print "\n"
        globalFreqs.append(fkmin1)
    return globalFreqs

apriori(tall, minsup)