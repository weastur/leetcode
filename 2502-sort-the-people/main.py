import operator

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = list(zip(names, heights))
        persons.sort(key=operator.itemgetter(1), reverse=True)
        return [person[0] for person in persons]