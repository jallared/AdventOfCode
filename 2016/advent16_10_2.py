import re

def gi(reg, s):
  return map(int, re.match(reg, s).groups())

def gm(reg, s):
  return re.match(reg, s).groups()

d = open('input16_10.txt', 'r').read().strip().split('\n')

bots = {}

rules = {}

outputs = {}

def ins(x, k, v):
  if k not in x:
    x[k] = []
  x[k] = list(sorted(x[k] + [v]))

for line in d:
  try:
    bot, dlow, low, dhigh, high = gm(r'bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)', line)
    bot, low, high = map(int, (bot, low, high))
    rules[bot] = (dlow, low, dhigh, high)
  except:
    pass
  try:
    value, bot = gi(r'value (\d+) goes to bot (\d+)', line)
    ins(bots, bot, value)
  except:
    pass

bots_with_two = len([b for b in bots if len(bots[b]) == 2])

ds = {'output': outputs, 'bot': bots}
while bots_with_two > 0:
  bot = [b for b in bots if len(bots[b]) == 2][0]
  dlow, low, dhigh, high = rules[bot]
  lv, hv = bots[bot]
  if lv == 17 and hv == 61:
    print "part a", bot
  ins(ds[dlow], low, lv)
  ins(ds[dhigh], high, hv)
  bots[bot] = []
  bots_with_two = len([b for b in bots if len(bots[b]) == 2])

print "part b", outputs[0][0] * outputs[1][0] * outputs[2][0]
