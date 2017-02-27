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
  def __init__(self, classifier_type, positive_file, negative_file, pos_metadata, neg_metadata):
    self.classifier_type = classifier_type
    self.vectors = []
    self.labels = []
    self.metadatas = []
    self.__parse_data(positive_file, constants.POSTIVIE_LABEL, self.vectors, self.labels)
    self.__import_metadata(pos_metadata)
    self.__parse_data(negative_file, constants.NEGATIVE_LABEL, self.vectors, self.labels)
    self.__import_metadata(neg_metadata)
    self.__set_classifier(classifier_type)

    self.vectors = np.array(self.vectors)
    self.labels = np.array(self.labels)

  def fit(self):
    res = self.__fit_with_cross_validation()
    with open('predictions_' + self.classifier_type + '.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      writer.writerow(['Label', 'Predicted Label', 'File', 'term', 'prefix', 'suffix',
                        '01', '02', '03', '04', '05',
                        '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15',
                        '16', '17'])
      for index in range(len(res['indexes'])):
        i = res['indexes'][index]
        row = [self.labels[i], res['predictions'][index]] + list(self.metadatas[i]) + list(self.vectors[i])
        writer.writerow(row)

    return res

  def predict(self, positive_file, negative_file):
    vectors = []
    labels = []
    self.__parse_data(positive_file, constants.POSTIVIE_LABEL, vectors, labels)
    self.__parse_data(negative_file, constants.NEGATIVE_LABEL, vectors, labels)

    predictions = self.cls.predict(vectors)
    precision = precision_score(labels, predictions)
    recall = recall_score(labels, predictions)

    return dict(
      precision = precision,
      recall = recall,
      predictions = predictions
    )

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

  def __parse_data(self, filename, label, vectors, labels):
    with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in reader:
        parsed_row = list(map(self.__map_TF_to_int, row))
        vectors.append(parsed_row)
        labels.append(label)

  def __import_metadata(self, filename):
    with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in reader:
        self.metadatas.append(row)

  def __map_TF_to_int(self, value):
    if value == 'True': return 1
    else: return 0

  def __fit_with_cross_validation(self, no_fold=constants.CV_FOLD):
    # fold = KFold(constants.CV_FOLD, shuffle=True)
    k_fold = KFold(n_splits=no_fold, shuffle=True)
    precisions = []
    recalls = []
    indexes = []
    predictions = []

    for train_indices, test_indices in k_fold.split(self.vectors):
      X_train, X_test = self.vectors[train_indices], self.vectors[test_indices]
      y_train, y_test = self.labels[train_indices], self.labels[test_indices]
      self.cls.fit(X_train, y_train)

      cv_prediction = self.cls.predict(X_test)
      predictions += list(cv_prediction)
      precisions.append(precision_score(y_test, cv_prediction))
      recalls.append(recall_score(y_test, cv_prediction))
      indexes += list(test_indices)

    return dict(
      precisions = precisions,
      recalls = recalls,
      precision = mean(precisions),
      recall = mean(recalls),
      predictions = predictions,
      indexes = indexes
    )
