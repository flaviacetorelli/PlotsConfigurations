
#RAndKff  = {}

RAndKff['DYmva0p8'] = {
                      'RFile'   : '../DNN/rootFile/plots_BG_DY_NOHR_MVA080_VH.root' ,
                      'KffFile' : '../DNN/rootFile/plots_BG_DY_NOHR_MVA080_VH.root' ,             
                      'Regions' : { '2jVHee' : { 
                                               'kNum' : 'VH_ee_in/events/histo_DY' ,
                                               'kDen' : 'VH_uu_in/events/histo_DY' ,
                                               'RNum' : 'VH_ee_out/events/histo_DY' , 
                                               'RDen' : 'VH_ee_in/events/histo_DY' , 
                                             } ,
                                    '2jVHmm' : { 
                                               'kNum' : 'VH_uu_in/events/histo_DY' ,
                                               'kDen' : 'VH_ee_in/events/histo_DY' ,
                                               'RNum' : 'VH_uu_out/events/histo_DY' , 
                                               'RDen' : 'VH_uu_in/events/histo_DY' , 
                                             } ,
                                   } , 
                     }
 
#DYestim = {}

for iCut in optim:

  DYestim['hww2l2v_13TeV_2jee_vh_'+iCut] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'rsyst'   : 0.01 , 
                                   'ksyst'   : 0.01 , 
                                   'njet'    : '2jVH' , 
                                   'flavour' : 'ee' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jee_vh_'+iCut ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf_vh_'+iCut ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'NPname'  : 'DYeenorm2j' , 
                                   'AccNum'  : 'hww2l2v_13TeV_2jee_vh_HAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jee_vh_AccDen/events/histo_DY',
                                   'asyst'   : 0.01 , 
                                  } 
  
  DYestim['hww2l2v_13TeV_2jmm_vh_'+iCut] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'rsyst'   : 0.02 , 
                                   'ksyst'   : 0.01 , 
                                   'njet'    : '2jVH'    ,
                                   'flavour' : 'mm' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jmm_vh_'+iCut ,
                                   'SFinDa'  : 'DATA' ,
                                   'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf_vh_'+iCut ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'NPname'  : 'DYmmnorm2j' ,
                                   'AccNum'  : 'hww2l2v_13TeV_2jmm_vh_HAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jmm_vh_AccDen/events/histo_DY',
                                   'asyst'   : 0.01 , 
                                  } 
  
  DYestim['hww2l2v_13TeV_WW_2jee_vh_'+iCut] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'njet'    : '2jVH'    ,
                                   'flavour' : 'ee' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jee_vh_'+iCut ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf_vh_'+iCut ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'NPname'  : 'DYeenorm2j' ,
                                   'AccNum'  : 'hww2l2v_13TeV_WW_2jee_vh_WWAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jee_vh_AccDen/events/histo_DY',
                                   'asyst'   : 0.01 , 
                                     }
  
  DYestim['hww2l2v_13TeV_WW_2jmm_vh_'+iCut] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'njet'    : '2jVH'    ,
                                   'flavour' : 'mm' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jmm_vh_'+iCut ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf_vh_'+iCut ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                   'NPname'  : 'DYmmnorm2j' ,
                                   'AccNum'  : 'hww2l2v_13TeV_WW_2jmm_vh_WWAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jmm_vh_AccDen/events/histo_DY',
                                   'asyst'   : 0.01 , 
                                     }
