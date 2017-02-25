import os
import re
import csv
from lib.featureGenerator import FeatureGenerator
from lib.constants import patterns

class PositiveExamplesGenerator:
  def __init__(self, dir_path):
    self.dir_path = dir_path
    self.generator = FeatureGenerator()
    self.data = []
    self.metadata = []

    self.__scan_directory()

  def examples(self):
    return dict(
      data = self.data,
      metadata = self.metadata
    )

  def export_to_csvs(self):
    with open('postiveExamples.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      for vector in self.data:
        writer.writerow(vector)

    with open('postiveExamplesMetadata.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      for vector in self.metadata:
        writer.writerow(vector)

  def __scan_directory(self):
    for root, dirs, files in os.walk(self.dir_path):
      for file in files:
        if file.endswith('.txt'):
          print("Scanning file", file)
          filepath = self.dir_path + '/' + file
          text = open(filepath).read()
          text_len = len(text)

          for markup in re.finditer(patterns.POS_MARKUP, text):
            # truncate text to before the markup 500 chars and after markup 500 chars
            # to help speedup finding prefix and suffix as well as increasing its
            # accuracy.
            context_start = markup.start() - 500 if markup.start() > 500 else 0
            context_end = markup.end() + 500 if markup.end() + 500 < text_len else text_len - 1
            if markup.start() > 500:
              start = markup.start() - context_start
              end = markup.end() - context_start
            else:
              start = markup.start()
              end = markup.end()

            res = self.generator.generate_features(text[context_start:context_end], start, end)
            self.data.append(res['features'])
            self.metadata.append([file, res['str'], res['prefix'], res['suffix']])
