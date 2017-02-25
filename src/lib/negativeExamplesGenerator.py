import csv
import re
from lib.featureGenerator import FeatureGenerator
from lib.negativeCandidatesGenerator import NegativeCandidatesGenerator
from lib.constants import patterns, constants

class NegativeExamplesGenerator:
  def __init__(self, filename, dir_path):
    self.dir_path = dir_path
    self.generator = FeatureGenerator()
    self.data = []
    self.metadata = []
    self.__generate_negative_candidates_from_file(filename)

  def examples(self):
    return dict(
      data = self.data,
      metadata = self.metadata
    )

  def export_to_csvs(self):
    with open('negativeExamples.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      for vector in self.data:
        writer.writerow(vector)

    with open('negativeExamplesMetadata.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      for vector in self.metadata:
        writer.writerow(vector)

  def __generate_negative_candidates_from_file(self, filename):
    with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in reader:
        print(["Parsing candidates"] + row)
        self.__parse_csv_row(row)

  def __parse_csv_row(self, row):
    filename = row[0]
    filepath = self.dir_path + '/' + filename
    start = int(row[2])
    end = int(row[3])

    text = open(filepath).read()
    text_len = len(text)

    pre_newline = re.search(re.compile('\\n.+' + row[1] + '$'), text[0:end])
    pre_newline = pre_newline.start() if pre_newline is not None else 0
    sub_newline = re.search(re.compile('^' + row[1] + '.+\\n'), text[start:text_len])
    sub_newline = sub_newline.start() if sub_newline is not None else text_len - 1

    pre_span = start - pre_newline if start > pre_newline and start - pre_newline < constants.PREFIX_SUFFIX_TEXT_CHARS_SPAN \
               else constants.PREFIX_SUFFIX_TEXT_CHARS_SPAN
    end_span = sub_newline - end if sub_newline > end and sub_newline - end < constants.PREFIX_SUFFIX_TEXT_CHARS_SPAN \
               else constants.PREFIX_SUFFIX_TEXT_CHARS_SPAN

    context_start = start - pre_span if start > pre_span else 0
    context_end = end + end_span if end + end_span < text_len else text_len - 1

    if start > pre_span:
      start = start - context_start
      end = end - context_start

    res = self.generator.generate_features(text[context_start:context_end], start, end)
    self.data.append(res['features'])
    self.metadata.append([filename, res['str'], res['prefix'], res['suffix']])
