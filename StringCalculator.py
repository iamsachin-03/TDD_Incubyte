import pytest
Class Solution():
  def Test(self):
    assert self.Add("")==0, "Wrong Output"
    assert self.Add("   ")==0, "Wrong Output"
    assert self.Add("23456")==23456, "Wrong Output"
    assert self.Add("\n100\n  22\n25  ") == 147, "Wrong Output"
    assert self.Add("2\n5  \n3, 57, 62\n21")==150 , "Wrong Output"
    assert self.Add("//;34\n23  \n2 ; 254; 23; 2 ")== 338, "Wrong Output"
    with pytest.raises(ValueError, match = r'negatives not allowed [-3, -4, -5]"):
      self.Add("-3,\n-4\n823\n  -5")
    print("All Test Cases Passed")
  def Add(self, numbers):
      if "-" in numbers: # negative numbers are also present here
        if numbers[:2] == "//":
          delimit = numbers[2]
          numbers = numbers[3:]
        else:
          delimit = ","
        res = ""
        num = numbers.split(delimit)
        for x in num:
          if "\n" in x:
            x1 = x.split("\n")
            for y in x1:
              if y != len(y)*" " and int(y)<0:
                res += str(int(y))
          else:
            if int(x)<0:
              res+= str(int(x))
        raise ValueError("negatives not allowed ", +str(res))
      else:
        # case1 : empty string with length >1
        if numbers == len(numbers)*" ":
          return 0
        # case 2: one number without \n and ,
        elif len(numbers)>=1 and "," not in numbers and "\n" not in numbers:
          return int(numbers)
        # case 3: numbers separated by \n and without having any delimiter
        elif len(numbers)>1 and "," not in numbers and "\n" in numbers and numbers[:2] != "//":
          number = numbers.split("\n")
          sum = 0
          for num in number:
            if num != len(num)*" ":
              sum += int(num)
          return sum
        # case 4: comma separated numbers without having delimiters
        elif len(numbers)>2 and "," in numbers and numbers[:2]!="//":
          number = numbers.split(",")
          sum = 0
          for num in number:
            if "\n" in num:
              x = num.split("\n")
              for i in x:
                if i != len(i)*" ":
                  sum += int(i)
            else:
              sum += int(num)
          return sum 
        # case 5: delimiters present
        elif len(numbers)>2 and numbers[:2]=="//":
          delimit = numbers[2]
          numbers = numbers[3:]
          number = numbers.split(delimit)
          sum = 0
          for num in number:
            if "\n" in num:
              x = num.split("\n")
              for i in x:
                if i != len(i)*" ":
                  sum += int(i)
            else:
              sum += int(num)
          return sum 
      
    
    
