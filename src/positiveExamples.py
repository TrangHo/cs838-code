import sys
from lib.positiveExamplesGenerator import PositiveExamplesGenerator

if sys.argv[1] == 'generate':
  print("Starting positive examples generator...")
  g = PositiveExamplesGenerator(sys.argv[2])
  print("Export to csv files")
  g.export_to_csvs()
  print("Done")
else:
  print("Invalid parameters! Please use sytanx: postive_examples generate dir_path")
  print("dir_path should not have '/'' at the end")
