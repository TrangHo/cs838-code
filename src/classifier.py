# classifiers:
# decision tree
# random forest
# support vector machine
# linear regression
# logistic regression
import csv

from lib.constants import constants
from lib.classifiers.svmClassifier import SVMClassifier

class Classifier:
  def __init__(self, positive_file, negative_file):
    self.vectors = []
    self.labels = []
    self.positive_vectors = []
    self.negative_vectors = []
    self.__parse_data(positive_file, constants.POSTIVIE_LABEL)
    self.__parse_data(negative_file, constants.NEGATIVE_LABEL)

  def fit(self, classifier_type):
    if classifier_type == constants.CLASSIFIERS.SVM:
      cls = SVMClassifier(self.vectors, self.labels)
      return cls.fit()

  def fit_test(self):
    if classifier_type == constants.CLASSIFIERS.SVM:
      cls = SVMClassifier(self.vectors, self.labels)
      return cls.fit()

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

