# cuts

supercut = 'nLepton==2 && Lepton_pt[0]>25 && Lepton_pt[1]>13 \
            && fabs(Lepton_eta[0])<2.5 && fabs(Lepton_eta[1])<2.5 \
            && mtw1 > 20 \
            && PuppiMET_pt > 20 \
            && fabs(Lepton_pdgId[1])==11 \
            && Alt$(Electron_jetIdx[Lepton_electronIdx[1]],-1)>0 \
           '
##Loose
 
cuts['e_eloose_noiso']  = '(fabs(Lepton_pdgId[0]) == 11)   \
                      && Lepton_isTightElectron_cut_WP_Tight80X[0]==1 \
                      && Electron_pfRelIso03_all[Lepton_electronIdx[0]]<0.06 \
                    '

cuts['m_eloose_noiso']  =  '(fabs(Lepton_pdgId[0]) == 13)   \
                      && Lepton_isTightMuon_cut_Tight80x[0]==1 \
                     '

cuts['e_eloose_iso']  = '(fabs(Lepton_pdgId[0]) == 11)   \
                      && Lepton_isTightElectron_cut_WP_Tight80X[0]==1 \
                      && Electron_pfRelIso03_all[Lepton_electronIdx[0]]<0.06 \
                      && Electron_pfRelIso03_all[Lepton_electronIdx[1]]<0.06 \
                    '

cuts['m_eloose_iso']  =  '(fabs(Lepton_pdgId[0]) == 13)   \
                      && Lepton_isTightMuon_cut_Tight80x[0]==1 \
                      && Electron_pfRelIso03_all[Lepton_electronIdx[1]]<0.06  \
                     '

##Tight
'''
cuts['e_etight_iso']  = ' fabs(Lepton_pdgId[0]) == 11 \
                      && Lepton_isTightElectron_cut_WP_Tight80X[0]==1 && Electron_pfRelIso03_all[Lepton_electronIdx[0]]<0.06  \
                      && Lepton_isTightElectron_cut_WP_Tight80X[1]==1 && Electron_pfRelIso03_all[Lepton_electronIdx[1]]<0.06  \
                     '

cuts['m_etight_iso']  = ' fabs(Lepton_pdgId[0]) == 13   \
                      && Lepton_isTightMuon_cut_Tight80x[0]==1 \
                      && Lepton_isTightElectron_cut_WP_Tight80X[1]==1 && Electron_pfRelIso03_all[Lepton_electronIdx[1]]<0.06  \
                     '

cuts['e_etight_noiso']  = ' fabs(Lepton_pdgId[0]) == 11 \
                      && Lepton_isTightElectron_cut_WP_Tight80X[0]==1\
                      && Lepton_isTightElectron_cut_WP_Tight80X[1]==1\
                     '

cuts['m_etight_noiso']  = ' fabs(Lepton_pdgId[0]) == 13   \
                      && Lepton_isTightMuon_cut_Tight80x[0]==1 \
                      && Lepton_isTightElectron_cut_WP_Tight80X[1]==1\
                     '
'''
