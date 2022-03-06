Class Solution():
  def Test(self):
    assert self.Add("")==0, "Wrong Output"
    assert self.Add("   ")==0, "Wrong Output"
    print("All Test Cases Passed")
  def Add(self, numbers):
    # case1 : empty string with length
    if numbers == len(numbers)*" ":
      return 0
