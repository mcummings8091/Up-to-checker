def isupto(a, k):
  check = [i for i in range(1, k)]
  if all(item in a for item in check):
    return True
  else:
    return False

  for num in check:
    if num not in a:
      print(f"Your array is missing {num}")
