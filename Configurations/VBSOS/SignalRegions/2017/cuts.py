# cuts

#cuts = {}
    

#cuts['first']  = 'mll<50'
#cuts['second'] = 'mll>=50'
### supercut is added to all the other cuts

supercut = 'mll>50  \
            && ptll > 30 \
            && (Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13)\
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && Alt$(Lepton_pt[2],0.)<10 \
            &&(abs(CleanJet_eta[0]) <= 2.5 || abs(CleanJet_eta[0]) >= 3.2) \
            && (abs(CleanJet_eta[1]) <= 2.5 || abs(CleanJet_eta[1]) >= 3.2)  \
            && (METFixEE2017_pt > 20 || PuppiMET_pt>20) \
           '


           
### USARE METfix

##signal region        
cuts['sr']  = 'mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
              '         
cuts['sr_me']  = 'mjj>500 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
              '       

cuts['sr_ee']  = 'mjj>500 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
               '
cuts['sr_mm']  = 'mjj>500 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                 '
##signal region   tight

cuts['sr_T']  = '         mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVetoT \
                 '         
cuts['sr_T_em']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVetoT \
                 '    
cuts['sr_T_ee']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVetoT \
                 '  
cuts['sr_T_mm']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVetoT \
                 '           


##signal region  central veto
cuts['sr_cv']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          && (Alt$(CleanJet_eta[2],-9999)==-9999 || centralVeto) \
                 '          
cuts['sr_cv_em']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          && (Alt$(CleanJet_eta[2],-9999)==-9999 || centralVeto) \
                 '    
cuts['sr_cv_ee']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          && (Alt$(CleanJet_eta[2],-9999)==-9999 || centralVeto) \
                 '  
cuts['sr_cv_mm']  = '        mjj>500 \
                          && detajj > 3.5 \
                          && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13 \
                          && Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 \
                          && bVeto \
                          && (Alt$(CleanJet_eta[2],-9999)==-9999 || centralVeto) \
                 '                  



 
