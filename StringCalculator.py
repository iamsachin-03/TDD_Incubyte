Class Solution():
  def Test(self):
    assert self.Add("")==0, "Wrong Output"
    assert self.Add("   ")==0, "Wrong Output"
    assert self.Add("23456")==23456, "Wrong Output"
    print("All Test Cases Passed")
  def Add(self, numbers):
    # case1 : empty string with length >1
    if numbers == len(numbers)*" ":
      return 0
    # case 2: non empty string
    elif len(numbers)>=1 and "," not in numbers and "\n" not in numbers:
      return int(numbers)
