def saddle_points(matrix):
    count_row = []
    count_column = []
    iter_count = 0
    while iter_count < len(matrix):
        for n in range(1, len(matrix[iter_count]) + 1):
            count_row.append(n)
        for n in range(1, len(matrix) + 1):
            count_column.append(n)
        row_numerated = tuple(zip([elem for elem in matrix[iter_count]], count_row))

        max_row_item = 0
        index_max_row_item = 0

        print(f'iter_count:     {iter_count}')
        print(f'len(matrix):    {len(matrix)}')

        print(f'row_numerated:  {row_numerated}')
        for item, counter in row_numerated:
            if item > max_row_item:
                max_row_item = item
                index_max_row_item = counter
        print(max_row_item, index_max_row_item)
        selected_column_numerated = tuple(zip([elem[index_max_row_item - 1] for elem in matrix], count_column))
        print(f'selected_column_numerated:  {selected_column_numerated}')
        min_column_item = selected_column_numerated[iter_count][0]
        index_min_column_item = 1
        list_min_column_item = []

        # min_column = []
        # min_column.append(min_column_item)
        # min_column.append(index_min_column_item)
        # list_min_column_item.append(min_column)
        # print(list_min_column_item)
        compare_counter = 0
        for item, counter in selected_column_numerated:
            while compare_counter < len(matrix):
                print(f'compare_counter:    {compare_counter}')
                # print('начинается сравнение')
                # print(f'item:{item}')
                # print(f'min_column_item:{min_column_item}')
                if item == min_column_item:
                    min_column_item = item
                    index_min_column_item = counter
                    list_min_column_item.append([min_column_item, index_min_column_item])
                    compare_counter += 1
                elif item < min_column_item:
                    iter_count += 1
                    break
                    # list_min_column_item.clear()
                    # min_column_item = item
                    # index_min_column_item = counter
                    # list_min_column_item.append([min_column_item, index_min_column_item])
                elif item > min_column_item:
                    compare_counter += 1
                    # min_column.append(min_column_item)
                    # min_column.append(index_min_column_item)
                    # list_min_column_item.append(min_column)
                break
        print(f'result:{list_min_column_item}')
        break

    print(min_column_item, index_min_column_item)
    for el in list_min_column_item:
        result = {
            'row': el[1],
            'column': index_max_row_item
        }
        print(result)


if __name__ == "__main__":
    matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
    saddle_points(matrix)
