import re
from lib.features import feature01;
from lib.features import feature02;
from lib.features import feature03;
from lib.features import feature04;
from lib.features import feature05;
from lib.features import feature06;
from lib.features import feature07;
from lib.features import feature08;
from lib.features import feature09;
from lib.features import feature10;
from lib.features import feature11;
from lib.features import feature12;
from lib.features import feature13;
from lib.features import feature14;
from lib.features import feature15;
from lib.features import feature16;

class FeatureGenerator:
  def generate_features(self, text, begin, end):
    self.str = re.sub(r'((<pos>)|(</pos>))', '', text[begin:end])
    self.prefix = self.__get_prefix(text, begin, end)
    self.suffix = self.__get_suffix(text, begin, end)
    self.features = self.__generate_features()
    return dict(
      str = self.str,
      prefix = self.prefix,
      suffix = self.suffix,
      features = self.features
    )

  def __get_prefix(self, text, begin, end):
    # (\\t|\s|\w|\d|\'|,|-)*
    # Regex which matches all strings which contains tab, space, \w, \d, apostrophe, comma, dash

    # (?:\s+(([A-Z]|[A-Z][a-z](?:[A-Z])?)\.)+([A-Z]|[A-Z][a-z](?:[A-Z])?)(?:\.)?\s+)?
    # Regex which match M.B.A or M.B.A. or PhD. this regex is optional in the pattern
    # this regex might not match case like this: He received a M.B.A and a Ph.D.
    pattern = re.compile('(\.|\\n)(\\t|\s|\w|\d|\'|,|-)*(?:\s+(([A-Z]|[A-Z][a-z](?:[A-Z])?)\.)+([A-Z]|[A-Z][a-z](?:[A-Z])?)(?:\.)?\s+)?(\\t|\s|\w|\d|\'|,|-)*' + text[begin:end] + '$')
    prefix = text[0:end]
    match = re.search(pattern, prefix)
    if match is not None:
      prefix = prefix[(match.start() + 1):begin]
    else:
      prefix = text[0:begin]

    prefix = prefix.strip()
    return prefix

  def __get_suffix(self, text, begin, end):
    pattern = re.compile('^' + text[begin:end] + '((\\t|\s|\w|\d|\'|,|-)*(?:\s+(([A-Z]|[A-Z][a-z](?:[A-Z])?)\.)+([A-Z]|[A-Z][a-z](?:[A-Z])?)(?:\.)?)?)+(\\t|\s|\w|\d|\'|,|-)*((\.\s+[A-Z])|(\s*\\n)|(\.\s*\'(?:\')?))')
    suffix = text[begin:len(text)]
    match = re.search(pattern, suffix)
    if match is not None:
      suffix = suffix[(end - begin):(match.end() - 1)]
    else:
      suffix = text[end:len(text)]

    suffix = suffix.strip()
    return suffix

  def __generate_features(self):
    return [
      feature01.test(self.str),
      feature02.test(self.str),
      feature03.test(self.str),
      feature04.test(self.str),
      feature05.test(self.str),
      feature06.test(self.str, self.prefix),
      feature07.test(self.str, self.prefix),
      feature08.test(self.str, self.prefix),
      feature09.test(self.str, self.prefix),
      feature10.test(self.str, self.suffix),
      feature11.test(self.str, self.suffix),
      feature12.test(self.str, self.suffix),
      feature13.test(self.str, self.prefix),
      feature14.test(self.str, self.suffix),
      feature15.test(self.str, self.prefix),
      feature16.test(self.str)
    ]
