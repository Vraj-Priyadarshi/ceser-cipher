from cypherl import logo
print(logo)
def cypher(tex , shif, direct):
  cipher_text = ""
  for letter in tex:
    if letter in alphabet:
      position = alphabet.index(letter)
      direct = direction.lower()
      if direct == "encode":
        newposition = position + shif
        if newposition >25:
          newposition = newposition - 25
        newletter = alphabet[newposition]
        cipher_text += newletter
      if direct == "decode":
        new_position = position - shif
        if new_position < 0:
          new_position = new_position +26
        newletter = alphabet[new_position]
        cipher_text += newletter
    else:
      cipher_text += letter
  print(f"The text is {cipher_text}")

should_continue = True
while should_continue:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift >26:
    shift = shift % 26
  encrypted = []

  cypher(text , shift ,direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  resul = result.lower()
  if resul =='no':
    should_continue = False






