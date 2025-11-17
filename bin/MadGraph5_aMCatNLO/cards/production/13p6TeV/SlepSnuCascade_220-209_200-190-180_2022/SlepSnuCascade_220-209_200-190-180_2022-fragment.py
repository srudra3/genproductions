import FWCore.ParameterSet.Config as cms

Nevents = 100
externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
    #args = cms.vstring('/uscms/home/janguian/nobackup/CMSSW_12_4_14_patch3/src/genproductions/bin/MadGraph5_aMCatNLO/SMS-GlGl_mGl-1p0_mN2-250_ct0_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    #args = cms.vstring('SMS-GlGl_mGl-1p0_mN2-250_ct0_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    args = cms.vstring('root://cmseos.fnal.gov//store/user/janguian/gridpacks/SlepSnuCascade_220-209_200-190-180_2022_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(Nevents),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh'),
    generateConcurrently = cms.untracked.bool(False)
)


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *


#params from T1qqqqVV
def matchParams(mass):
  if mass < 124: return 76,0.64
  elif mass < 151: return 76, 0.6
  elif mass < 176: return 76, 0.57
  elif mass < 226: return 76, 0.54
  elif mass < 326: return 76, 0.51
  elif mass < 451: return 76, 0.48
  elif mass < 651: return 76, 0.45 
  elif mass < 1176: return 76, 0.42
  else: return 76, 0.42

model="SlepSnuCascade"
mn1=190.0
mn2=200.0
mc1=180.0
qcut, tru_eff = matchParams(mn2)
#mcm_eff = 0.258 #what is this??
#wgt = Nevents*(mcm_eff/tru_eff)

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(                          
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = %.0f' % qcut,  #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            '23:mMin = 0.1',
            '24:mMin = 0.1',
            'Check:abortIfVeto = on'
            
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
    ),
    #RandomizedParameters = cms.VPSet()
)


#generator.RandomizedParameters.append(
#        cms.PSet(
#            ConfigWeight = cms.double(wgt),
#            GridpackPath =  cms.string('/uscms/home/janguian/nobackup/CMSSW_12_4_14_patch3/src/genproductions/bin/MadGraph5_aMCatNLO/SMS-GlGl_mGl-1p0_mN2-250_ct0_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
#            ConfigDescription = cms.string('%s_%i_%i' % (model, mglu, mlsp)),
          #  SLHATableForPythia8 = cms.string('%s' % slhatable),
          #  PythiaParameters = basePythiaParameters,
#        ),
#    )

