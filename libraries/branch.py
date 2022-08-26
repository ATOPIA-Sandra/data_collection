import itertools

class concatenateList(object):
    @classmethod
    def concatenate(cls, list1, list2, list3):
        result = list(itertools.chain(list1, list2, list3))
        return result

