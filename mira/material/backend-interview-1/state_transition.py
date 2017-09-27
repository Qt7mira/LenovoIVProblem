"""
    Part one: word based matching
    Input:
        query: string, what the user has said
        candidates: list of  string, each string is a key phrase
    Output:
        int, index of the key phrase that matches the query, -1 of not of the key phrases match.
        
    Examples:
            Input: (query: "listen to a song", candidates: ['story', 'song', 'wake up', 'restart'])
            Output: 1
            
            Input: (query: "restart a story", candidates: ['restart', 'story', 'wake up'])
            Output: 0
            
            Input: (query: "listen to story", candidates: ['song','joke'])
            Output: -1
            
"""
def find_best_match_basic(query,candidates):
    pass
    #TODO: Implement this for part one


"""
    Part two: document distance based matching
    Input:
        query: string, what the user has said
        candidates: list of  string, each string is a key phrase
    Output:
        int, index of the key phrase that best matches the query (has shortest document distance)
"""
def find_best_match_document_distance(query,candidates):
    pass
    #TODO: Implement this for part two



"""
    Part three: document distance based matching with threshold
    Input:
        query: string, what the user has said
        candidates: list of  string, each string is a key phrase
    Output:
        int, index of the key phrase that best matches the query (has shortest document distance)
             or -1 if all key phrases have distance larger than threshold (from the query)

    Use samples/generated_test_cases.txt to determine best threshold. Write the best threshold in comments.
"""
def find_best_match_with_threshold(query,candidates,threshold):
    pass
    #TODO: Implement this for part three
