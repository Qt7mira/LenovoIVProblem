query = "listen to a song"
candidates = ['story', 'song', 'wake up', 'restart']


def find_best_match_basic(query, candidates):
    if len(query) == 0:
        return "The value of query is null."
    if len(candidates) == 0:
        return "The value of candidates is null."
    query2list = str(query).strip().split(' ')
    for q in query2list:
        for i in range(0, len(candidates)):
            if q == candidates[i]:
                return i
    return -1


print(find_best_match_basic(query, candidates))
