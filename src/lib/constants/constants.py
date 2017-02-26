NO_NEG_PER_DOC = 10
PREFIX_SUFFIX_TEXT_CHARS_SPAN = 500

POSTIVIE_LABEL = 1
NEGATIVE_LABEL = 0

DEV_TEST_SIZE_RATIO = 0.33

CV_FOLD = 5

CLASSIFIERS = dict(
  SVM = 'SVM',
  DECISION_TREE = 'DT',
  RANDOM_FOREST = 'RF',
  # LINEAR_REGRESSION = 'LiR',
  LOGISTIC_REGRESSION = 'LoR',
  NEURAL_NETWORK = 'NN'
)

STATES = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming"
]
