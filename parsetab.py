
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUAL QUOTE SAY SPACE TEXT\n    say : SAY QUOTE TEXT QUOTE\n        | SAY SPACE TEXT \n    '
    
_lr_action_items = {'SAY':([0,],[2,]),'$end':([1,6,7,],[0,-2,-1,]),'QUOTE':([2,5,],[3,7,]),'SPACE':([2,],[4,]),'TEXT':([3,4,],[5,6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'say':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> say","S'",1,None,None,None),
  ('say -> SAY QUOTE TEXT QUOTE','say',4,'p_say_onlyText','complier.py',49),
  ('say -> SAY SPACE TEXT','say',3,'p_say_onlyText','complier.py',50),
]
