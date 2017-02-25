import os
import re
import csv
import random
from lib.constants import patterns, constants

class NegativeCandidatesGenerator:
  def __init__(self, dir_path):
    self.dir_path = dir_path
    self.negative_candidates = []
    self.__scan_directory()

  def examples(self):
    return dict(
      data = self.data,
      metadata = self.metadata
    )

  def export_to_csv(self):
    with open('negativeCandidates.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      for vector in self.negative_candidates:
        writer.writerow(vector)

  def __scan_directory(self):
    for root, dirs, files in os.walk(self.dir_path):
      for file in files:
        if file.endswith('.txt'):
          filepath = self.dir_path + '/' + file
          print("Scanning file", file)
          self.negative_candidates += self.__generate_candidates(filepath, file)

  def __generate_candidates(self, filepath, filename):
    text = open(filepath).read()
    pos_locs = self.__postive_markup_indexes(text)
    neg_candidates = []

    for pattern_info in patterns.NEG_PATTERNS:
      pattern = pattern_info[0]
      group = pattern_info[1]
      for neg_cand in re.finditer(pattern, text):
        match_str = text[neg_cand.start():neg_cand.end()]
        group_match_str = neg_cand[group]
        start = neg_cand.start() + re.search(re.compile(group_match_str), match_str).start()
        end = start + len(group_match_str)
        neg_candidates.append([start, end])

    selected_cands = []
    while len(selected_cands) < constants.NO_NEG_PER_DOC and neg_candidates:
      cand = random.choice(neg_candidates)
      if self.__is_overlaped_with_pos_markups(pos_locs, cand[0], cand[1]):
        neg_candidates.remove(cand)
        continue
      else:
        selected_cands.append([filename, text[cand[0]:cand[1]], cand[0], cand[1]])
        neg_candidates.remove(cand)

    return selected_cands

  def __postive_markup_indexes(self, text):
    result = []
    for markup in re.finditer(patterns.POS_MARKUP, text):
      result.append((markup.start(), markup.end()))

    return result

  def __is_overlaped_with_pos_markups(self, pos_locs, start, end):
    flag = False
    for pos_loc in pos_locs:
      pos_start = pos_loc[0]
      pos_end = pos_loc[1]
      if (pos_start >= start and pos_start <= end) or \
         (pos_end >= start and pos_end <= end) or \
         (start >= pos_start and start <= pos_end) or \
         (end >= pos_start and end <= pos_end):
        flag = True
        break

    return flag
