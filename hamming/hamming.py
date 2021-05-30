def distance (strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('sequences must have equal length')
    return sum(1 for item_a, item_b in zip(strand_a, strand_b) if item_a != item_b)

# old solution
# def distance(strand_a, strand_b):
#     Hamming_Distance = 0
#     if len(strand_a) != len(strand_b):
#         raise ValueError('sequences must have equal length')
#     i = 0
#     while i < len(strand_a):
#         if strand_a[i] != strand_b[i]:
#             Hamming_Distance += 1
#         i += 1
#     return Hamming_Distance

