"""
Nick Swanson
CIS 211
Waldo mini project
"""

Waldo = 'W'
Other = '.'


"""For all x, there exists y . P(y)"""


def all_row_exists_waldo(collection):

    if len(collection) == 0:
        return True

    true = 0
    false = 0

    for item in collection:
        if Waldo in item:
            true += 1
        else:
            false += 1

    if false > 0:
        return False
    else:
        return True


def all_col_exists_waldo(collection):

    if len(collection) == 0:
        return True

    elif collection == [[], []]:
        return True

    else:
        value1 = 0
        value2 = 0
        value3 = 0
        # Assigns all the column values to a new list so they are easy to access
        col0 = [item[0] for item in collection]
        col1 = [item[1] for item in collection]
        col2 = [item[2] for item in collection]
        # Determines if Waldo is in each column
        for value in col0:
            if value == Waldo:
                value1 = 1
        for value in col1:
            if value == Waldo:
                value2 = 1
        for value in col2:
            if value == Waldo:
                value3 = 1

        if value1 and value2 and value3 == 1:
            return True
        else:
            return False


"""For all x, for all y . P(y)"""


def all_row_all_waldo(collection):

    if len(collection) == 0:
        return True

    true = 0
    false = 0

    for item in collection:
        for value in item:
            if value == Waldo:
                true += 1
            else:
                false += 1

    if false > 0:
        return False
    else:
        return True


def all_col_all_waldo(collection):
    if len(collection) == 0:
        return True

    elif collection == [[], [], []]:
        return True

    else:
        true = 0
        false = 0

        col0 = [item[0] for item in collection]
        col1 = [item[1] for item in collection]
        col2 = [item[2] for item in collection]

        for value in col0:
            if value == Waldo:
                true += 1
            else:
                false += 1
        for value in col1:
            if value == Waldo:
                true += 1
            else:
                false += 1
        for value in col2:
            if value == Waldo:
                true += 1
            else:
                false += 1

        if false > 0:
            return False
        else:
            return True


"""There exists x such that there exists y . P(y)"""


def exists_row_exists_waldo(collection):
    if len(collection) == 0:
        return False

    elif collection == [[], []]:
        return False

    true = 0
    false = 0

    for item in collection:
        if Waldo in item:
            true += 1
        else:
            false += 1

    if true > 0:
        return True
    else:
        return False


def exists_col_exists_waldo(collection):

    if len(collection) == 0:
        return False

    elif collection == [[], []]:
        return False

    else:
        if len(collection) > 2:
            true = 0
            false = 0

            col0 = [item[0] for item in collection]
            col1 = [item[1] for item in collection]
            col2 = [item[2] for item in collection]

            for value in col0:
                if value == Waldo:
                    true += 1
                else:
                    false += 1
            for value in col1:
                if value == Waldo:
                    true += 1
                else:
                    false += 1
            for value in col2:
                if value == Waldo:
                    true += 1
                else:
                    false += 1

            if true > 0:
                return True
            else:
                return False
        else:
            true = 0
            false = 0

            col0 = [item[0] for item in collection]
            col1 = [item[1] for item in collection]

            for value in col0:
                if value == Waldo:
                    true += 1
                else:
                    false += 1
            for value in col1:
                if value == Waldo:
                    true += 1
                else:
                    false += 1

            if true > 0:
                return True
            else:
                return False


"""There exists x such that all y . P(y)"""


def exists_row_all_waldo(collection):

    if len(collection) == 0:
        return False

    true = 0
    false = 0

    for item in collection:
        if Other in item:
            false += 1
        else:
            true += 1

    if false > 2:
        return False
    else:
        return True


def exists_col_all_waldo(collection):

    if len(collection) == 0:
        return False

    elif collection == [[], []]:
        return False

    else:

        false0 = 0
        false1 = 0
        false2 = 0

        col0 = [item[0] for item in collection]
        col1 = [item[1] for item in collection]
        col2 = [item[2] for item in collection]

        for value in col0:
            if value == Other:
                false0 = 1

        for value in col1:
            if value == Other:
                false1 = 1

        for value in col2:
            if value == Other:
                false2 = 1

        if false0 and false1 and false2 == 1:
            return False
        else:
            return True
