import timeit


def findLongestConsecutivePrimeSum(*sums):
    sums_len = len(sums)

    # 인자의 각 원소의 결과, left_border, right_border 리스트 생성
    result = [0 for _ in range(sums_len)]
    left_border = [0 for _ in range(sums_len)]
    right_border = [0 for _ in range(sums_len)]

    # 인자의 최대값을 찾아서, 최대값을 기준으로 prime sieve 함수 호출
    max_value = max(sums)
    ps = findPrimes(max_value)
    ps_len = len(ps)

    # 최대값 이하의 소수로만 이루어진 리스트 생성
    prime_numbers = []

    for i in range(0, ps_len):
        if ps[i] == True:
            prime_numbers.append(i)

    prime_numbers_len = len(prime_numbers)

    # table의 한 행을 나타내는 리스트 생성, cur_sn은 현재 시작수의 index를 나타냄
    cur_sn = 0
    table_row = [0 for _ in range(0, ps_len)]

    # table 첫 행 초기화
    table_row[0] = prime_numbers[0]

    for i in range(1, prime_numbers_len):
        table_row[i] = table_row[i - 1] + prime_numbers[i]

    # 초기 right_border 초기화
    for i in range(sums_len):
        right_border[i] = binarySearch(table_row, 0, prime_numbers_len - 1, sums[i]) - 1

    # 인자의 각 원소에 대하여 탐색 시작 (한행씩)
    while True:
        change_flag = False

        for i in range(sums_len):
            if left_border[i] > right_border[i]:
                continue

            original_left_border = left_border[i]

            for j in range(right_border[i], left_border[i] - 1, -1):
                if ps[table_row[j]] == True :
                    result[i] = (table_row[j], j - cur_sn + 1)
                    left_border[i] = j + 2
                    change_flag = True
                    break

            if original_left_border == left_border[i]:
                left_border[i] += 1
                change_flag = True

        if change_flag == True:
            for i in range(prime_numbers_len):
                table_row[i] -= prime_numbers[cur_sn]

            cur_sn += 1

            for i in range(sums_len):
                right_border[i] = binarySearch(table_row, 0, prime_numbers_len - 1, sums[i]) - 1
        else:
            break

    return result

def findPrimes(maxN):
    prime = [True for _ in range(maxN+1)] 
    prime[0] = prime[1] = False
    i=2
    while i*i <= maxN:
        if prime[i]:
            prime[i*i::i] = [False] * ((maxN - i*i) // i + 1)
        i += 1 

    return prime

def binarySearch(array, from_index, to_index, I):
    if from_index > to_index:
        return from_index
    
    mid = (from_index + to_index) // 2

    if array[mid] == I:
        return mid
    elif array[mid] < I:
        return binarySearch(array, mid+1, to_index, I)
    else:
        return binarySearch(array, from_index, mid-1, I)
    



def speedCompare1(*sums):
    '''
    Compute the entire 2D table in advance
    This function is used to evaluate the execution time of findLongestConsecutivePrimeSum()
    '''
    maxSum = max(sums)
    
    prime = [True for _ in range(maxSum)]
    prime[0] = prime[1] = False
    p = 2    
    while p*p <= maxSum:
        if prime[p]:
            for i in range(p*p, maxSum, p): prime[i] = False
        p += 1
    
    primeSumFirstRow = []
    sum = 0    
    for p in range(maxSum):
        if prime[p]: 
            sum += p
            primeSumFirstRow.append(sum)

    primeSums = [primeSumFirstRow]
    for row in range(1, len(primeSumFirstRow)):
        primeSumCurrentRow = []
        for i in range(len(primeSumFirstRow)):
            if i < row: primeSumCurrentRow.append(None)
            else: primeSumCurrentRow.append(primeSumFirstRow[i] - primeSumFirstRow[row-1])
        primeSums.append(primeSumCurrentRow)

def speedCompare2(*sums):
    '''
    Perform prime sieve for each N in sums
    This function is used to evaluate the execution time of findLongestConsecutivePrimeSum()
    '''
    for sum in sums:
        prime = [True for _ in range(sum)]
        prime[0] = prime[1] = False
        p = 2    
        while p*p <= sum:
            if prime[p]:
                for i in range(p*p, sum, p): prime[i] = False
            p += 1
        
        primeSumFirstRow = []
        sum = 0    
        for p in range(sum):
            if prime[p]: 
                sum += p
                primeSumFirstRow.append(sum)    


if __name__ == "__main__":
    print("Correctness test for findLongestConsecutivePrimeSum()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    correct = True

    if findLongestConsecutivePrimeSum(100,200,300) == [(41, 6), (197, 12), (281, 14)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(500,600,700,800,900,1000) == [(499, 17), (499, 17), (499, 17), (499, 17), (857, 19), (953, 21)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False
        
    if findLongestConsecutivePrimeSum(2000,5000,10000,20000,50000) == [(1583, 27), (4651, 45), (9521, 65), (16823, 81), (49279, 137)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(60000,70000,80000,90000,100000) == [(55837, 146), (66463, 158), (78139, 167), (86453, 178), (92951, 183)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(1000000,5000000,8000000) == [(997651, 543), (4975457, 1150), (7998491, 1433)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(10000000) == [(9951191, 1587)]: print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    print()
    print()
    print("Speed test for findLongestConsecutivePrimeSum()")
    if not correct: print("fail (since the algorithm is not correct)")
    else:
        repeat = 10
        sums = [5000]
        tSpeedCompare1 = timeit.timeit(lambda: speedCompare1(*sums), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(lambda: findLongestConsecutivePrimeSum(*sums), number=repeat)/repeat    
        print(f"For input sums: {sums}")
        print(f"Average running times of the submitted code and the code that computes the entire 2D table in advance: {tSubmittedCode:.10f} and {tSpeedCompare1:.10f}")    
        if tSubmittedCode < tSpeedCompare1: print("pass")
        else: print("fail")
        print()

        sums = [10000,20000,30000,40000,50000,60000,70000,80000,90000]
        tSpeedCompare2 = timeit.timeit(lambda: speedCompare2(*sums), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(lambda: findLongestConsecutivePrimeSum(*sums), number=repeat)/repeat    
        print(f"For input sums: {sums}")
        print(f"Average running times of the submitted code and the code that performs sieve for each sum in sums: {tSubmittedCode:.10f} and {tSpeedCompare2:.10f}")
        if tSubmittedCode < tSpeedCompare2: print("pass")
        else: print("fail")
    

    

