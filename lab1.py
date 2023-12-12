import re

while True:
  password = input("패스워드를 입력하세요 : ")
  if len(password) > 8 and re.search("[a-z]|[A-Z]", password) != None \
    and re.search("\d", password) != None and re.search("[_@$!]", password) != None:
    print("유효한 패스워드")
    break
  else:
    print("유효하지 않은 패스워드")