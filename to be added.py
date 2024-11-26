def get_int(a):
  while True:
    try:
      num = int(input(a))
        return num
    except:
      print("error: input was not int\nTry again:")
