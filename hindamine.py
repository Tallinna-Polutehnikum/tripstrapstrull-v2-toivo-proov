'''
    {k7} | {k8} | {k9}
    ----------
    {k4} | {k5} | {k6}
    ----------
    {k1} | {k2} | {k3} 
'''

board = {
  'k9':9,
  'k8':8,
  'k7':7,
  'k6':6,
  'k5':5,
  'k4':4,
  'k1':'X',
  'k2':'X',
  'k3':'X'
  }


#horisontaalid
print(board['k1'] == player and board['k2'] == player and board['k3'] == player)
print(board['k4'] == player and board['k5'] == player and board['k6'] == player)
print(board['k7'] == player and board['k8'] == player and board['k9'] == player)
#vertikaalid
print(board['k1'] == player and board['k4'] == player and board['k7'] == player)
print(board['k2'] == player and board['k5'] == player and board['k8'] == player)
print(board['k3'] == player and board['k6'] == player and board['k9'] == player)
#diagonaalid
print(board['k7'] == player and board['k5'] == player and board['k3'] == player)
print(board['k1'] == player and board['k5'] == player and board['k9'] == player)