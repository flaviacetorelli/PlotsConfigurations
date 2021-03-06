# cuts

#cuts = {}
    

#cuts['first']  = 'mll<50'
#cuts['second'] = 'mll>=50'
### supercut is added to all the other cuts


supercut = 'mll>50  \
            && ptll > 30 \
            && (Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*11 || Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-13*13 )\
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && Alt$(Lepton_pt[2],0.)<10 \
            &&(abs(CleanJet_eta[0]) <= 2.5 || abs(CleanJet_eta[0]) >= 3.2) \
            && (abs(CleanJet_eta[1]) <= 2.5 || abs(CleanJet_eta[1]) >= 3.2)  \
            && (METFixEE2017_pt > 20 || PuppiMET_pt>20) \
           '


           
### USARE METfix

##WWjj regions    
##WWjj regions      
cuts['lowmjj'] =  'Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && mjj < 500 && bVeto'
cuts['lowmjj_ee'] =  'Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && mjj < 500 && bVeto && Lepton_pdgId[0]*Lepton_pdgId[1]==-11*11'
    
cuts['lowmjj_mm'] = 'Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && mjj < 500 && bVeto && Lepton_pdgId[0]*Lepton_pdgId[1]==-13*13'
    

cuts['lowmjj_em'] = 'Alt$(CleanJet_pt[0],0.)>30 && Alt$(CleanJet_pt[1],0.)>30 && mjj < 500 && bVeto && Lepton_pdgId[0]*Lepton_pdgId[1]==-11*13'
    
