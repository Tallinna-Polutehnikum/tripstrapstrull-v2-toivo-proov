global_board = {
  'k9':9,
  'k8':8,
  'k7':7,
  'k6':6,
  'k5':5,
  'k4':4,
  'k1':1,
  'k2':2,
  'k3':3
  }
def draw_board(board):
    s1 = '''
    {k7} | {k8} | {k9}
    ----------
    {k4} | {k5} | {k6}
    ----------
    {k1} | {k2} | {k3} 
    '''.format(**board)
    print(s1)    

print ("X alustab")
player = "X"
for kord in range(9):
  sisend = input("sisesta aadress: ")
  global_board['k' + sisend] = player
  draw_board(global_board)
  if player == "X":
      player = "O"
  else:
      player = "X"
  if kord == 8:
    print ("viik!")
        


