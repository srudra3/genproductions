import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
      nEvents = cms.untracked.uint32(10000),
      outputFile = cms.string('AZHToTT_mA700_mH400.lhe'),
      scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_madgraph_gridpack.sh'),
      numberOfParameters = cms.unit32(1),
      args = cms.vstring('/afs/cern.ch/work/s/srudrabh/AZH/genproductions/bin/MadGraph5_aMCatNLO/AZHToLLtt_mA1000_mH600_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz')
)


generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
			 pythiaPylistVerbosity = cms.untracked.int32(1),
			 filterEfficiency = cms.untracked.double(1.0),
			 pythiaHepMCVerbosity = cms.untracked.bool(False),
			 comEnergy = cms.double(13000.),
			 PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        JetMatchingParameters = cms.vstring(
              'JetMatching:setMad = off',
              'JetMatching:scheme = 1',
              'JetMatching:merge = on',
              'JetMatching:jetAlgorithm = 2',
              'JetMatching:etaJetMax = 5.',
              'JetMatching:coneRadius = 1.',
              'JetMatching:slowJetPower = 1',
              'JetMatching:qCut = 20.', #this is the actual merging scale
              'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
              'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity
              'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
              ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'JetMatchingParameters'
                                     )	    
	) 
			 )

ProductionFilterSequence = cms.Sequence(generator)


