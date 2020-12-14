import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from sklearn.linear_model import SGDClassifier

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x_train = []
    y_train = []
    with open('trainingdata.txt','r') as f:
        i = 0
        for line in f:
            if i == 0:
                training_len = int(line.strip())
                i+=1
            else:
                y_train.append(int(line[0]))
                x_train.append(line[2:].strip())
    
    count_vect = CountVectorizer()
    x_train_count = count_vect.fit_transform(x_train)
    clf = SGDClassifier()
    clf.fit(x_train_count, y_train)

    test_len = int(input().strip())
    x_test = []
    for _ in range(test_len):
        x_test.append(input().strip())

    x_test_count = count_vect.transform(x_test)
    y_test = clf.predict(x_test_count)
    for y in y_test:
        fptr.write(str(y) + '\n')

    fptr.close()
