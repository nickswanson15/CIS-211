'''
Nick Swanson
CIS 211
Sweeping practice
'''

def all_same(l: list) -> bool:
    '''
    returns True if all the items in the list are the same and false if not
    '''
    if len(l) == 0:
        print('no values in list')
        return True
    else:
        first = l[0]
        result_1 = True
        for item in l:
            if first != item:
                result_1 = False
                break
        if result_1 == True:
            return True
        else:
            return False

def dedup(l: list) -> list:
    '''
    returns a list with no duplicate numbers from original list
    '''
    if len(l) == 0:
        print('no values in list')
        return []
    else:
        result = []
        for item in l:
            if item not in result:
                result.append(item)
        return result

def max_run(l: list) -> int:
    '''
    returns the max number of same integers in a row given a list of numbers
    '''
    if len(l) == 0:
        print('no values in list')
        return 0
    else:
        max = 1
        run = 1

        for i in range(len(l) - 1):
            if l[i] == l[i+1]:
                run += 1
            else:
                run = 1
            if run > max:
                max = run
        return max
