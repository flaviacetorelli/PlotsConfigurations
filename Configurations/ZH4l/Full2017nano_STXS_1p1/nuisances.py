      # nuisances
# name of samples here must match keys in samples.py 
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA']
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()


################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc)
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc)
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc)
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc)
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc)
}

###### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_4l_u)/(TriggerEffWeight_4l))*(TriggerEffWeight_4l>0.02) + (TriggerEffWeight_4l<=0.02)', '(TriggerEffWeight_4l_d)/(TriggerEffWeight_4l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp'   : directory+'__ElepTup',
    'folderDown' : directory+'__ElepTdo',
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp'   : directory+'__MupTup',
    'folderDown' : directory+'__MupTdo',
    'AsLnN': '1'
}

##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp'   : directory+'__JESup',
    'folderDown' : directory+'__JESdo',
    'AsLnN': '1'
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp'   : directory+'__METup',
    'folderDown' : directory+'__METdo',
    'AsLnN': '1'
}

# PS and UE
#FIXME: Add PS uncertainty

nuisances['PS_whss']  = {
                'name'  : 'PS_whss',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_hww'   : '1.037',
                   'ZH_hww'   : '1.037',
                   'WH_htt'    : '1.037',
                   'ggZH_hww'   : '1.037',
              #     'ZH_htt'   : '1.037',
                },
}

nuisances['UE_whss']  = {
                'name'  : 'UE_whss',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_hww'   : '1.010',
                   'ZH_hww'   : '1.010',
                   'WH_htt'    : '1.010',
                   'ggZH_hww'   : '1.010',
 #                  'ZH_htt'   : '1.010',
               },
                }

nuisances['CMS_hww_ZZ4lnorm']  = {
        'name'  : 'CMS_hww_ZZ4lnorm',
        'samples'  : {
            'ZZ' : '1.00',
            },
        'type'  : 'rateParam',
        }

##### QCD scale uncertainties for Higgs signals other than ggH
#
from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_ggH']  = {
               'name'  : 'QCDscale_ggH', 
               'samples'  : {
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_VH']  = {
               'name'  : 'QCDscale_VH', 
               'samples'  : {
                   'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                    'H_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ggZH']  = {
               'name'  : 'QCDscale_ggZH', 
               'samples'  : {
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm'),                  
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_bbH']  = {
               'name'  : 'QCDscale_bbH',
               'samples'  : {
                   'bbH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ttH']  = {
               'name'  : 'QCDscale_ttH',
               'samples'  : {
                   'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

##FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_qqbar_ACCEPT']  = {
               'name'  : 'QCDscale_qqbar_ACCEPT', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : '1.007',
                   'qqH_htt' : '1.007',
                   'WH_hww'  : '1.05',
                   'WH_htt'  : '1.05',
                   'ZH_hww'  : '1.04',
                   'ZH_htt'  : '1.04',
                    'H_htt'  : '1.04',
                   'VZ'      : '1.029',
                   },
              }

##FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT']  = {
               'name'  : 'QCDscale_gg_ACCEPT', 
               'samples'  : {
                   'ggWW'    : '1.027',
                   'ggH_hww' : '1.027',
                   'ggH_htt' : '1.027',
                   'ggZH_hww': '1.027',                   
                   },
               'type'  : 'lnN',
              }

####### pdf uncertainty

nuisances['pdf_Higgs_gg']  = {
               'name'  : 'pdf_Higgs_gg', 
               'samples'  : {
                   'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm'), 
                   'bbH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_ttH']  = {
               'name'  : 'pdf_Higgs_ttH',
               'samples'  : {
                   'ttH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                    'H_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }

#FIXME: check this 4%
nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'VZ'      : '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
                   },
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT', 
               'samples'  : {
                   'ggH_hww' : '1.005',
                   'ggH_htt' : '1.005',
                   'ggZH_hww': '1.005', 
                   },
               'type'  : 'lnN',
              }

##FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_gg_ACCEPT']  = {
               'name'  : 'pdf_gg_ACCEPT',
               'samples'  : {
                   'ggWW'    : '1.005',
                   },
               'type'  : 'lnN',
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'qqH_hww' : '1.011',
                   'qqH_htt' : '1.011',
                   'WH_hww'  : '1.007',
                   'WH_htt'  : '1.007',
                   'ZH_hww'  : '1.012',
                   'ZH_htt'  : '1.012',
                    'H_htt'  : '1.012',
                   },
              }

##FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'VZ'      : '1.005',
                   },
              }

# ggww and interference

nuisances['QCDscale_ggWW']  = {
               'name'  : 'QCDscale_ggWW',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW' : '1.15',
                   },
              }

####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }
