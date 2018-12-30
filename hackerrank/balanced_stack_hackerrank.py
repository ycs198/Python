def is_matched(expr):
  lefty = "({["  # opening delimiters
  righty = ")}]" # respective closing delims
  S = []
  for c in expr:
    if c in lefty:
      S.append(c) # push left delimiter on stack
    elif c in righty:
      if not S:
        return False # nothing to match with
      if righty.index(c) != lefty.index(S.pop( )):
        return False # mismatched
  if not S:
    return True
  else:
    return False

num_cases = int(input())
while num_cases:
  input_text = raw_input()
  if (is_matched(input_text) == True):
    print "YES"
  else:
    print "NO"
  num_cases = num_cases -1
