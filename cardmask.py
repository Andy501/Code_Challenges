# return masked string
def maskify(cc):
  hasher = (len(cc) - 4)
  tag = "#"
  hasher = (tag * hasher) #converting # into count of string len - last 4
  catcher = cc[::-1]
  last_4 = catcher[0:4]
  last_4 =  last_4[::-1] #in accending order

  hashedcard = (hasher + last_4)
  return (hashedcard)