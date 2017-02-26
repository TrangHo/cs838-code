# classifiers:
# decision tree
# random forest
# support vector machine
# linear regression
# logistic regression
import csv
from statistics import mean
import numpy as np

from sklearn import svm, tree
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split, StratifiedShuffleSplit, KFold
from sklearn.metrics import precision_score, recall_score

from lib.constants import constants
from lib.classifiers.svmClassifier import SVMClassifier
from lib.classifiers.decisionTreeClassifier import DecisionTreeClassifier

class Classifier:
  def __init__(self, classifier_type, positive_file, negative_file):
    self.vectors = []
    self.labels = []
    self.positive_vectors = []
    self.negative_vectors = []
    self.__parse_data(positive_file, constants.POSTIVIE_LABEL)
    self.__parse_data(negative_file, constants.NEGATIVE_LABEL)
    self.__set_classifier(classifier_type)

  def fit(self):
    return self.__fit_with_cross_validation()

  def fit_test(self):
    return self.__fit_without_cross_validation()

  def __set_classifier(self, classifier_type):
    if classifier_type == constants.CLASSIFIERS['SVM']:
      self.cls = svm.SVC()
    elif classifier_type == constants.CLASSIFIERS['DECISION_TREE']:
      self.cls = tree.DecisionTreeClassifier()
    elif classifier_type == constants.CLASSIFIERS['RANDOM_FOREST']:
      self.cls = RandomForestClassifier()
    # elif classifier_type == constants.CLASSIFIERS['LINEAR_REGRESSION']:
    #   self.cls = LinearRegression()
    elif classifier_type == constants.CLASSIFIERS['LOGISTIC_REGRESSION']:
      self.cls = LogisticRegression()
    elif classifier_type == constants.CLASSIFIERS['NEURAL_NETWORK']:
      self.cls = MLPClassifier()

  def __parse_data(self, filename, label):
    with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in reader:
        parsed_row = list(map(self.__map_TF_to_int, row))
        self.vectors.append(parsed_row)
        self.labels.append(label)
        if label == constants.POSTIVIE_LABEL:
          self.positive_vectors.append(parsed_row)
        else:
          self.negative_vectors.append(parsed_row)

  def __map_TF_to_int(self, value):
    if value == 'True': return 1
    else: return 0

  def __fit_with_cross_validation(self, fold=constants.CV_FOLD):
    # fold = KFold(constants.CV_FOLD, shuffle=True)
    precisions = cross_val_score(self.cls, self.vectors, self.labels, cv=fold, scoring='precision')
    recalls = cross_val_score(self.cls, self.vectors, self.labels, cv=fold, scoring='recall')
    predictions = cross_val_predict(self.cls, self.vectors, self.labels, cv=fold)

    return dict(
      precisions = precisions,
      recalls = recalls,
      precision = mean(precisions),
      recall = mean(recalls),
      predictions = predictions
    )

  def __fit_without_cross_validation(self, test_size = constants.DEV_TEST_SIZE_RATIO):
    sss = StratifiedShuffleSplit(n_splits=1, test_size=test_size, random_state=0)
    sss.get_n_splits(self.vectors, self.labels)
    X_train = list()
    y_test = list()
    X_test = list()
    y_test = list()

    for train_idx, test_idx in sss.split(self.vectors, self.labels):
      train_index = train_idx
      test_index = test_idx

    vectors = np.array(self.vectors)
    labels = np.array(self.labels)
    X_train, X_test = vectors[train_index], vectors[test_index]
    y_train, y_test = labels[train_index], labels[test_index]


    # X_train, X_test, y_train, y_test = train_test_split(self.vectors, self.labels, test_size)
    self.cls.fit(X_train, y_train)
    predictions = self.cls.predict(X_test)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)

    return dict(
      precision = precision,
      recall = recall,
      predictions = predictions
    )
