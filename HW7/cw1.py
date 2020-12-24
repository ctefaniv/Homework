def count_positives_sum_negatives(arr):
    positives = []
    negatives = []
    for i in arr:
        if i > 0:
            positives.append(i) 
        elif i < 0:
            negatives.append(i)         
    return [len(positives), sum(negatives)] if arr != [] else []