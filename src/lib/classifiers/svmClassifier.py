from sklearn import svm
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split
from sklearn.metrics import precision_score, recall_score
from lib.constants import constants

class SVMClassifier:
  def __init__(self, vectors, labels):
    self.vectors = vectors
    self.labels = labels
    self.clf = svm.SVC()

  def fit(self):
    return self.__fit_without_cross_validation()

  def fit_test(self):
    return self.__fit_without_cross_validation()

  def __fit_with_cross_validation(self, fold=constants.CV_FOLD):
    precision = cross_val_score(self.clf, self.vectors, self.labels, cv=fold, scoring='precision')
    recall = cross_val_score(self.clf, self.vectors, self.labels, cv=fold, scoring='recall')
    predictions = cross_val_predict(self.clf, self.vectors, self.labels, cv=fold)

    return dict(
      precision = precision,
      recall = recall,
      predictions = predictions
    )

  def __fit_without_cross_validation(self, test_size = constants.DEV_TEST_SIZE_RATIO):
    X_train, X_test, y_train, y_test = train_test_split(self.vectors, self.labels, test_size)
    self.cls.fit(X_train, y_train)
    predictions = cls.predict(X_test)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)

    return dict(
      precision = precision,
      recall = recall,
      predictions = predictions
    )
