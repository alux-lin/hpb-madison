# happy birthday weewoo haha this is alex at 5AM
# also i would never make u type that out here it is "werCdreNehTmhtriByppaHif~RfinxtsKwt"
def descramble(scrambled_message):
  part3 = scrambled_message[:12]
  part1 = scrambled_message[12:22]
  part2 = scrambled_message[22:]
  part1 = part1[::-1]
  part3 = part3[::-1]
  part2 = ''.join(chr((ord(char) - 5) % 128) for char in part2)
  original = part1 + part2 + part3
  return original
