import os
import re
import csv
from lib.featureGenerator import FeatureGenerator
from lib.constants import patterns, constants

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
            # truncate text to before the markup PREFIX_SUFFIX_TEXT_CHARS_SPAN chars and after
            # markup PREFIX_SUFFIX_TEXT_CHARS_SPAN chars to help speedup finding prefix and suffix
            # as well as increasing its accuracy.
            start = markup.start()
            end = markup.end()
            markup_str = text[start:end]

            pre_newline = re.search(re.compile('\\n.+' + markup_str + '$'), text[0:end])
            pre_newline = pre_newline.start() if pre_newline is not None else 0
            sub_newline = re.search(re.compile('^' + markup_str + '.+\\n'), text[start:text_len])
            sub_newline = sub_newline.end() if sub_newline is not None else text_len - 1

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
            self.metadata.append([file, res['str'], res['prefix'], res['suffix']])
