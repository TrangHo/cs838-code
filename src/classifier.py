import sys
import csv

from lib.classifier import Classifier
from lib.constants import constants

pos_train_file = sys.argv[1]
neg_train_file = sys.argv[2]
pos_metadata_file = sys.argv[3]
neg_metadata_file = sys.argv[4]
pos_test_file = sys.argv[5]
neg_test_file = sys.argv[6]
with open('classifiersPR.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Classifier', 'Action Type', 'Mean precision', 'Mean recall', 'Precisions', 'Recalls'])
  for classifier_type in constants.CLASSIFIERS.keys():
    print("Initializing classifier", classifier_type)
    c = Classifier(constants.CLASSIFIERS[classifier_type], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print("Fitting...")
    res = c.fit()
    writer.writerow([classifier_type, 'TRAIN', res['precision'], res['recall'], res['precisions'], res['recalls']])
    print("Predicting Test set...")
    res = c.predict(pos_test_file, neg_test_file)
    writer.writerow([classifier_type, 'TEST', res['precision'], res['recall'], '', ''])
  print("End")
