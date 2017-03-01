import sys
import csv

from lib.classifier import Classifier
from lib.constants import constants
import warnings

warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

pos_train_file = sys.argv[2]
neg_train_file = sys.argv[3]
pos_metadata_file = sys.argv[4]
neg_metadata_file = sys.argv[5]

if sys.argv[1] == 'test_classifiers':
  with open('classifiersPR.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Classifier', 'Mean precision', 'Mean recall', 'Precisions', 'Recalls'])
    for classifier_type in constants.CLASSIFIERS.keys():
      print("Initializing classifier", classifier_type)
      c = Classifier(constants.CLASSIFIERS[classifier_type], pos_train_file, neg_train_file, pos_metadata_file, neg_metadata_file)
      print("Fitting...")
      res = c.fit_cv()
      writer.writerow([classifier_type, res['precision'], res['recall'], res['precisions'], res['recalls']])
    print("End")

elif sys.argv[1] == 'classify':
  pos_test_file = sys.argv[6]
  neg_test_file = sys.argv[7]
  classifier_type = sys.argv[8]

  with open(classifier_type + '_final_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Type', 'Precision', 'Recall'])
    c = Classifier(classifier_type, pos_train_file, neg_train_file, pos_metadata_file, neg_metadata_file)
    res = c.fit()
    writer.writerow(['TRAIN', res['precision'], res['recall']])
    res = c.predict(pos_test_file, neg_test_file)
    writer.writerow(['TEST', res['precision'], res['recall']])

  print("Done")
