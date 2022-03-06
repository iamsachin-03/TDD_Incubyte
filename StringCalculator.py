Class Solution():
  def Test(self):
    assert Add("")==0, "Doesn't return 0"
    assert Add("   ")==0, "Doesn't return 0"
    print("All Test Cases Passed")
  def Add(self, numbers):
    # case1 : empty string with length
    if len(numbers)==0:
      return 0
