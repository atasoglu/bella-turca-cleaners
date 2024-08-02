import re



def contains_too_many_mistakes(text):
  if not text: return True
  bad_patterns = r"\b(\w \w \w \w|\w\w \w\w \w\w|\w\w \w\w \w|\w\w'\w\w| @\w|\w@ |\w\w \w \w \w|\w \w \w \w\w|\w \w \w\w|\w \w\w \w\w|\w \w \w\w|\w \w\w \w\w|\w \w \w\w|\w \w\w \w\w)\b"
  bad_matches = re.findall(bad_patterns, text)
  print(bad_matches)
  return len(bad_matches)



def filter(text):
  wrds = len(text.split()) 
  bm = contains_too_many_mistakes(text)
  if bm >= wrds // 20: return True
  return False

