# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                 

import os.path

massesAndModelsFile = "massesAndModels.py"

if os.path.exists(massesAndModelsFile) :
  handle = open(massesAndModelsFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesAndModelsFile, " does not exist."

for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    structure['ggH_hww_'+m+'_'+model_name]  = {
                    'isSignal' : 1,
                    'isData'   : 0
                    }
    structure['ggH_hww_SBI'+m+'_'+model_name]  = {
                    'isSignal' : 1,
                    'isData'   : 0
                    }
    structure['qqH_hww_'+m+'_'+model_name]  = {
                    'isSignal' : 1,
                    'isData'   : 0
                    }
    structure['qqH_hww_SBI'+m+'_'+model_name]  = {
                    'isSignal' : 1,
                    'isData'   : 0
                    }


structure['ggH_hww_750_NWA']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }

structure['qqH_hww_750_NWA']  = {
                  'isSignal' : 1,
                  'isData'   : 0
              }             
   
structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['DYLO']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }


structure['DY2jet']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['EWKZ2jet']  = {
                  'isSignal' : 0,
                  'isData'   : 0
              }

structure['Wjets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['FakeSF']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['ttbar'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['singletop'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['qqWWqq']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['WW2J']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggWW_Int']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['Wg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Zg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggH'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['WH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['H_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['H_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }




