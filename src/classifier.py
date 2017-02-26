import sys
import csv

from lib.classifier import Classifier
from lib.constants import constants

with open('classifiersPR.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Classifier', 'Mean precision', 'Mean recall', 'Precisions', 'Recalls'])
  for classifier_type in constants.CLASSIFIERS.keys():
    print("Initializing classifier", classifier_type)
    c = Classifier(constants.CLASSIFIERS[classifier_type], sys.argv[1], sys.argv[2])
    print("Fitting...")
    res = c.fit()
    writer.writerow([classifier_type, res['precision'], res['recall'], res['precisions'], res['recalls']])

  print("End")
