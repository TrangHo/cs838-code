import sys
from lib.negativeExamplesGenerator import NegativeExamplesGenerator
from lib.negativeCandidatesGenerator import NegativeCandidatesGenerator

if sys.argv[1] == 'candidates':
  print("Starting negative candidates generator...")
  g = NegativeCandidatesGenerator(sys.argv[2])
  print("Export to csv files")
  g.export_to_csv()
  print("Done")
elif sys.argv[1] == 'generate':
  print("Starting negative example generator...")
  g = NegativeExamplesGenerator(sys.argv[2], sys.argv[3])
  print("Export to csv files")
  g.export_to_csvs()
  print("Done")
else:
  print("Invalid parameters! Please use sytanxes:")
  print("negative_examples candidates dir_path")
  print("negative_examples generate candidate_file dir_path")
  print("dir_path should not have '/'' at the end")
