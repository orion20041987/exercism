def saddle_points(matrix):
    count_row = []
    count_column = []
    for n in range(0, len(matrix[0])):
        count_row.append(n)
    for n in range(0, len(matrix)):
        count_column.append(n)
    first_row_numerated = tuple(zip([elem for elem in matrix[0]], count_row))
    print(first_row_numerated)
    max_row_item = 0
    index_max_row_item = 0
    for item, counter in first_row_numerated:
        if item > max_row_item:
            max_row_item = item
            index_max_row_item = counter
    print(max_row_item, index_max_row_item)
    selected_column_numerated = tuple(zip([elem[index_max_row_item] for elem in matrix], count_column))
    print(selected_column_numerated)
    min_column_item = selected_column_numerated[0][0]
    index_min_column_item = 0
    # list_min_column_item = []
    # min_column = []
    # min_column.append(min_column_item)
    # min_column.append(index_min_column_item)
    # list_min_column_item.append(min_column)
    # print(list_min_column_item)
    for row, counter in selected_column_numerated:
        if row < min_column_item:
            min_column_item = row
            index_min_column_item = counter
        elif row == min_column_item:
            pass
            # min_column.append(min_column_item)
            # min_column.append(index_min_column_item)
            # list_min_column_item.append(min_column)


    print(min_column_item, index_min_column_item)
    # print(list_min_column_item)






matrix = [[8, 17, 9, 11], [6, 3, 6, 3], [3, 8, 5, 4]]
saddle_points(matrix)
