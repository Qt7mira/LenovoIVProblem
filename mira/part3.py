import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import euclidean_distances
import numpy as np
from sklearn.linear_model import LogisticRegression


def load():
    with open('C:/Users/Administrator/Desktop/backend-interview-1/samples/generated_test_cases.txt', 'r',
              encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def get_word_embeddings():
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


def get_min(target_list):
    min_num = target_list[0]
    for i in target_list:
        if i < min_num:
            min_num = i
    return min_num


def get_min_index(target_list):
    min_num = target_list[0]
    for i in target_list:
        if i < min_num:
            min_num = i
    return target_list.index(min_num)


def find_match_document_distance(query, candidates, W):
    if len(query) == 0:
        return "The value of query is null."
    if len(candidates) == 0:
        return "The value of candidates is null."

    vec1 = CountVectorizer(stop_words="english").fit([str(query)])
    vec2 = CountVectorizer(stop_words="english").fit([str(candidates)])

    if len(vec1.get_feature_names()) == 0 or len(vec2.get_feature_names()) == 0:
        return -1

    # print("Query Features:", ", ".join(vec1.get_feature_names()))
    # print("Candidates Features:", ", ".join(vec2.get_feature_names()))

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

    return get_min(t_list)


def get_model(W):
    json_data = load()
    print(len(json_data))

    list_X = []
    list_Y = []
    try:
        for i in range(0, len(json_data)):
            aaa = find_match_document_distance(str(json_data[i]['query']), str(json_data[i]['candidates']), W)
            list_X.append(aaa)
            if json_data[i]['correct_index'] >= 0:
                list_Y.append("1")
            else:
                list_Y.append("-1")
    except Exception as e:
        print(i)
        print("word_embeddings中未含有该词")

    print(len(list_X))
    print(len(list_Y))

    x = np.array(list_X).reshape(-1, 1)
    y = np.array(list_Y)

    lr = LogisticRegression(C=1000.0, random_state=0)
    lr.fit(x, y)
    # print(lr.predict(x))
    from sklearn.model_selection import cross_val_score
    acy = cross_val_score(lr, x, y)
    print(acy.mean())
    return lr


def find_best_match_with_threshold(query, candidates, lr, W):

    if len(query) == 0:
        return "The value of query is null."
    if len(candidates) == 0:
        return "The value of candidates is null."

    vec1 = CountVectorizer(stop_words="english").fit([query])
    vec2 = CountVectorizer(stop_words="english").fit([str(candidates)])

    if len(vec1.get_feature_names()) == 0 or len(vec2.get_feature_names()) == 0:
        return -1

    print("Features:", ", ".join(vec1.get_feature_names()))
    print("Features:", ", ".join(vec2.get_feature_names()))

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
    # print(lr.predict(get_min(t_list))[0])
    if lr.predict(get_min(t_list))[0] == "-1":
        return -1
    else:
        return candidates.index(result[get_min_index(t_list)]['c'])


W = get_word_embeddings()
lr = get_model(W)
query = "i am really hungry"
candidates = ['story', 'song', 'wake up', 'restart']
print(find_best_match_with_threshold(query, candidates, lr, W))


