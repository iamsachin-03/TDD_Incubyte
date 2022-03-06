Class Solution():
  def Test(self):
    assert Add("")==0, "Doesn't return 0"
  def Add(self, numbers):
    # case1 : empty string with length 0
    if len(numbers)==0:
      return 0
