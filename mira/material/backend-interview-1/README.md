#Coding challenge: state transitions

##Overview

Dialog systems respond differently to different things our user say. For example, when the user says "tell me a story", the dialog system will ask what story the user wants to listen to, or continue the story. When the user says "I want to play a game", the system will start a game with the user. Engineers have developed different modules for the dialog system, such as story, song, game, joke, etc. Interally, this dialog system is a state machine and each module represents a different state and each of the modules listed above is a state.

For this coding challenge, we will implement mutiple versions of a function that returns the next state this system should transition to. The function takes several inputs. One of them is what the user has said, which we refer to as the **query**. Each state has **key phrase** that represents the content of the state. For example, for a state in which this system sings a song, the key phrases can be "sing", "song", "music". All key phrases of all possible next states are also inputs for this function. For simplicity, we assume that each state only has one key phrase, which is a string, and 'next state' is only determined by the key phrases of possible next states and the query. Essentially, we want to implement a function that takes **query**(string) and a list of **key phrases**(string) as input, and returns the index of the key phrase that best matches the query.

Below is the detailed instruction of this coding challenge. **Write all your code in state_transition.py and create a seperate branch for you code. Name the branch with your name. After you're done, push your branch of code onto Github**. Feel free to Google for whatever algorithm(s) you need and to use any utility libraries you think will be helpful. Please keep your code clean and organized (breaking up your code with helper functions is encouraged!), with comments if the logic is particularly complex. When evaluating your code, this will be just as important to us as functionality and speed.

##Language and system requirements

python2 or python3  <br>
16GB free space on disk (for downloading word vector) <br>
8GB RAM <br>
good internet connection as we will download a ~8GB word vector file.

##Part one: word based matching
The most simple way to determine if a query **matches** a key phrase is to check if they have common words. For example, "I want to play a game", and "start game" has a common word "game". For simplicity, assume no punctuation exsits in the query and key phrases, but keep in mind that both the query and key phrase may contain multiple words, separated by space. 

For part one, implement the function that returns the index of the key phrase that matches the query. If a query matches mutliple key phrases, returns the index of the first one. If none of the key phrases match, return -1.

##Part two: document distance based matching
The obvious drawback of word based matching is that query has to contain the exact word in the key phrase to get a match. If the user says "I want to sing" and the key phrase is "song", there is no match. That can be improved by using word embeddings. Word embedding is a vector representation of a word. Each word is mapped to a unique position in this multi-dimentional vector space. Word embeddings are generated so that words that have similar meaning or share same context will be closer in this space. For example, the distance word "sing" and "song" is smaller than the distance between "car" and "song". The distance of two words is the eucleandian distance of their vectors/embeddings.

Now that we can calculate the distance between two words, we can use it to calculate the distanace between any two strings, which have multiple words. <http://vene.ro/blog/word-movers-distance-in-python.html> gives a excellent description of the method to compute this distance. Read it carefully and feel free to use the code in this blog post. In this blog post, Google's [word embeddings](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) are used. For our implementation, however, we want to use better word embeddings, which can be downloaded at <https://github.com/LuminosoInsight/conceptnet-numberbatch>. (There is no need to clone code and build code in this repository. Just download the word vectors, which link are provided in README section of the repo). If you can't figure out how to use "numberbatch" word embedding, use Google's word embedding instead.

For part two, implement the function that calculates the distance of each key phrase to the query and return the index of the key phrase with the shortest distance. (**Extra credit: there is a way to drastically reduce the memory usage, if we need to run the function repeatedly. Implement it**).

##Part three: document distance based matching with threshold
Sometimes none of the available key phrases matches the query, and simply picking the one with the shortest distance is not a good idea. For this version of the matching function, we want to it to return -1 if all distances to all key phrases are larger than a certain threshold (a float). You can think about the threshold as a very simple linear classifier. For this problem, we do not need to learn a more complicated classifer than that.

**This threshold can be learned from a training set, which is provided in the repo. The task is to try different thresholds (using code, not hand, of course!) and pick the threshold that gives the best accuracy on the training set.** "Accuracy" is defined by the number of test cases where the function gives correct index as output, divided by the total number of test cases. Since we are only learning one parameter: the threshold, we do not need to worry about overfitting. There is no need to split the data into training and test. 

For part three, implement the matching function with a threshold. Report the threshold (a single number), accuracy, and include the code used to learn the threshold. **Samples/generated_test_cases.txt** is a JSON file that contains the training set.

##Additional tips
Make sure you consider and handle edge cases. Not all edge cases appear in training set.
