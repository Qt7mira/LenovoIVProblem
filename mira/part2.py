query = "i really want to sing"
candidates = ['story', 'song', 'wake up', 'restart']


def get_word_embeddings():
    import numpy as np
    embeddings = {}
    with open('C:/Users/Administrator/Desktop/numberbatch-en.txt', encoding='utf-8') as em:
        for embed in em:
            em_line = embed.split(' ')
            if len(em_line) > 2:
                word = em_line[0]
                embedding = np.array(em_line[1:])
                embeddings[word] = embedding
    print('Word embeddings:', len(embeddings))
    return embeddings


def get_min_index(target_list):
    min_num = target_list[0]
    for i in target_list:
        if i < min_num:
            min_num = i
    return target_list.index(min_num)


def find_best_match_document_distance(query, candidates):

    if len(query) == 0:
        return "The value of query is null."
    if len(candidates) == 0:
        return "The value of candidates is null."

    from sklearn.feature_extraction.text import CountVectorizer
    vec1 = CountVectorizer(stop_words="english").fit([query])
    vec2 = CountVectorizer(stop_words="english").fit([str(candidates)])

    if len(vec1.get_feature_names()) == 0 or len(vec2.get_feature_names()) == 0:
        return -1

    print("Features:", ", ".join(vec1.get_feature_names()))
    print("Features:", ", ".join(vec2.get_feature_names()))
    W = get_word_embeddings()
    from sklearn.metrics import euclidean_distances
    W1 = [W[w] for w in vec1.get_feature_names()]
    W2 = [W[w] for w in vec2.get_feature_names()]

    result = []
    for i in range(0, len(W1)):
        for j in range(0, len(W2)):
            res = {}
            res['q'] = vec1.get_feature_names()[i]
            res['c'] = vec2.get_feature_names()[j]
            res['r'] = float(euclidean_distances([W1[i]], [W2[j]])[0][0])
            result.append(res)

    t_list = []
    for i in range(0, len(result)):
        t_list.append(float(result[i]['r']))

    # print(t_list)
    return candidates.index(result[get_min_index(t_list)]['c'])


print(find_best_match_document_distance(query, candidates))
