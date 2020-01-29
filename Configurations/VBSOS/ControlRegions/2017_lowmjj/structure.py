'''structure['NAME']  = { # NAME should match the names in samples.py
     'isSignal' : VALUE, # 0/1 with obvious meaning
     'isData'   : VALUE, # 0/1 with obvious meaning 
     'removeFromCuts' : []  #OPTIONAL list of cuts that should not be run for this sample (default is empty)
  }'''
structure['DATA'] = {
     'iSignal' : 0, 
     'isData' : 1, 
     'removeFromCuts': [signal_region]

   }
