
import copy


def findAllSequence(n):
    result = []

    def recursive(array, sum, limit, min):
        sub_result = array
        i = min

        while (sum + i) <= limit :
            sub_result.append(i)
            new_list = copy.deepcopy(sub_result)
            result.append(new_list)
            recursive(new_list, sum + i, limit, i)
            del sub_result[-1]
            i += 1

        return sub_result

    recursive([], 0, n, 1)
    
    return result

if __name__ == "__main__":
    if findAllSequence(1) == [[1]]: print("pass")
    else: print("fail")

    if findAllSequence(2) == [[1],[1,1],[2]]: print("pass")
    else: print("fail")

    if findAllSequence(3) == [[1],[1,1],[1,1,1],[1,2],[2],[3]]: print("pass")
    else: print("fail")

    if findAllSequence(4) == [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 2], [1, 2], [1, 3], [2], [2, 2], [3], [4]]: 
        print("pass")
    else: print("fail")

    if findAllSequence(5) == [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2], [1, 1, 3], [1, 2], [1, 2, 2], [1, 3], [1, 4], [2], [2, 2], [2, 3], [3], [4], [5]]: 
        print("pass")
    else: print("fail")

    if findAllSequence(6) == [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2], [1, 1, 2, 2], [1, 1, 3], [1, 1, 4], [1, 2], [1, 2, 2], [1, 2, 3], [1, 3], [1, 4], [1, 5], [2], [2, 2], [2, 2, 2], [2, 3], [2, 4], [3], [3, 3], [4], [5], [6]]: 
        print("pass")
    else: print("fail")

    if findAllSequence(7) == [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 2], [1, 1, 1, 1, 3], [1, 1, 1, 2], [1, 1, 1, 2, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 2], [1, 1, 2, 2], [1, 1, 2, 3], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 2], [1, 2, 2], [1, 2, 2, 2], [1, 2, 3], [1, 2, 4], [1, 3], [1, 3, 3], [1, 4], [1, 5], [1, 6], [2], [2, 2], [2, 2, 2], [2, 2, 3], [2, 3], [2, 4], [2, 5], [3], [3, 3], [3, 4], [4], [5], [6], [7]]: 
        print("pass")
    else: print("fail")