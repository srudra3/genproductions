import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *


baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     4.50000000E+03   # ~d_L
   2000001     4.50000000E+03   # ~d_R
   1000002     4.50000000E+03   # ~u_L
   2000002     4.50000000E+03   # ~u_R
   1000003     4.50000000E+03   # ~s_L
   2000003     4.50000000E+03   # ~s_R
   1000004     4.50000000E+03   # ~c_L
   2000004     4.50000000E+03   # ~c_R
   1000005     4.50000000E+03   # ~b_1
   2000005     4.50000000E+03   # ~b_2
   1000006     4.50000000E+03   # ~t_1
   2000006     4.50000000E+03   # ~t_2
   1000011     4.50000000E+05   # ~e_L
   2000011     4.50000000E+05   # ~e_R
   1000012     4.50000000E+05   # ~nu_eL
   1000013     4.50000000E+05          # ~mu_L
   2000013     4.50000000E+05   # ~mu_R
   1000014     4.50000000E+05   # ~nu_muL
   1000015     4.50000000E+05   # ~tau_1
   2000015     4.50000000E+05    # ~tau_2
   1000016     4.50000000E+05    # ~nu_tauL
   1000021     4.50000000E+05    # ~g
   1000022     %MLSP%           # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     4.50000000E+03   # ~chi_30
   1000035     4.50000000E+03   # ~chi_40
   1000024     %MC1%          # ~chi_1+
   1000037     4.50000000E+05   # ~chi_2+
# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000011     1.00000000E-1   # selectron_L decays
    0.25000000E+00   2    1000023   11
    0.25000000E+00   2    -1000024   12
    0.50000000E+00   2    1000022   11
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     1.00000000E-1   # snu_elL decays
    0.25000000E+00   2    1000023   12
    0.50000000E+00   2    1000024   11
    0.25000000E+00   2    1000022   12
DECAY   1000013     1.00000000E-1   # smuon_L decays
    0.25000000E+00   2    1000023   13
    0.25000000E+00   2    -1000024   14
    0.50000000E+00   2    1000022   13
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     1.00000000E-1   # snu_muL decays
    0.25000000E+00   2    1000023   14
    0.50000000E+00   2    1000024   13
    0.25000000E+00   2    1000022   14
DECAY   1000015     0.00000000E+00  # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     1.00000000E-1   # neutralino2 decays
    0.00000000E+00   3    1000022   11   -11
    0.48000000E+00   2    1000022   23
    0.24000000E+00   2    1000024   -24
    0.24000000E+00   2   -1000024   24
    0.04000000E+00   2    1000022   22
DECAY   1000024     1.00000000E-1   # chargino1+ decays
    0.00000000E+00   3    1000022   12   -11
    1.00000000E+00   2    1000022   24
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""
#The decays with BR = 0 such as "0.00000000E+00   3    1000022   12   -11" are important if there is 
#no other on-shell decay for that particle, otherwise the mother particle will be set to be stable.

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    RandomizedParameters = cms.VPSet(),
)

#model = "TChiWZ_ZToLL"
model = "SlepSnuCascade"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.506
qcut = 76
tru_eff = 0.51

weight = (100 * (mcm_eff / tru_eff))



mn2, mlsp = 200, 180
mc1 = 190
#qcut, tru_eff = matchParams(mn2)

if mlsp==0: mlsp = 1
slhatable = baseSLHATable.replace('%MN2%','%e' % mn2)
slhatable = slhatable.replace('%MC1%','%e' % mc1)
slhatable = slhatable.replace('%MLSP%','%e' % mlsp)

basePythiaParameters = cms.PSet(
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
        'JetMatching:qCut = %.0f' % qcut, #this is the actual merging scale
        'JetMatching:nQmatch = 4', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
        'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
        'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
        '23:mMin = 0.1',
        '24:mMin = 0.1',
        'Check:abortIfVeto = on',
    ), 
    parameterSets = cms.vstring('pythia8CommonSettings',
                                'pythia8CP5Settings',
                                'pythia8PSweightsSettings',
                                'processParameters'
    )
)

generator.RandomizedParameters.append(
    cms.PSet(
        ConfigWeight = cms.double(weight),
        GridpackPath = cms.string('/afs/cern.ch/work/s/srudrabh/CMSSW_13_3_1/src/SUSYCascades/GenFilters/genproductions/bin/MadGraph5_aMCatNLO/SlepSnuCascade_N2C1_200_190_2022_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
        ConfigDescription = cms.string('%s_mn2-%i_mlsp-%i' % (model, mn2, mlsp)),
        SLHATableForPythia8 = cms.string('%s' % slhatable),
        PythiaParameters = basePythiaParameters,
    ),
)



tmpGenParticles = cms.EDProducer(
    "GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator","unsmeared"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)


tmpGenParticlesForJetsNoNu = cms.EDProducer(
    "InputGenJetsParticleSelector",
    src = cms.InputTag("tmpGenParticles"),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000023, 1000024, 1000012, 1000014, 1000016,
        2000012, 2000014, 2000016, 1000039, 5100039,
        4000012, 4000014, 4000016, 9900012, 9900014, 9900016,
        39, 12, 14, 16
    ),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(False),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)

AnomalousCellParameters = cms.PSet(
    maxBadEcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999)
)

GenJetParameters = cms.PSet(
    src = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(''),
    jetType = cms.string('GenJet'),
    jetPtMin = cms.double(3.0),
    inputEtMin = cms.double(0.0),
    inputEMin = cms.double(0.0),
    doPVCorrection = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    nSigmaPU = cms.double(1.0),
    radiusPU = cms.double(0.5),
    doAreaFastjet = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    useDeterministicSeed = cms.bool(True),
    minSeed = cms.uint32(14327)
)

tmpAk4GenJetsNoNu = cms.EDProducer(
    "FastjetJetProducer",
    GenJetParameters,
    AnomalousCellParameters,
    jetAlgorithm = cms.string("AntiKt"),
    rParam = cms.double(0.4)
)

# HT filter (considers genjets above pT threshold in |eta| range)
genHTFilter = cms.EDFilter("GenHTFilter",
    src = cms.InputTag("tmpAk4GenJetsNoNu"),
    jetPtCut = cms.double(20.0),
    jetEtaCut = cms.double(2.5),
    genHTcut = cms.double(160.0)   # HT > 160 GeV
)

# GenMET: build gen MET from tmpGenParticlesForJetsNoNu (same setup as example)
tmpGenMetTrue = cms.EDProducer("GenMETProducer",
    src = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    onlyFiducialParticles = cms.bool(False),
    globalThreshold = cms.double(0.0),
    usePt = cms.bool(True),
    applyFiducialThresholdForFractions = cms.bool(False),
)

#require genMET > 80 GeV
genMETfilter1 = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("tmpGenMetTrue"),
    cut = cms.string("pt > 80")
)
genMETfilter2 = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("genMETfilter1"),
    minNumber = cms.uint32(1),
)

# Finally, chain into the production sequence
ProductionFilterSequence = cms.Sequence(
    generator
    * tmpGenParticles
    * tmpGenParticlesForJetsNoNu
    * tmpAk4GenJetsNoNu
    * genHTFilter
    * tmpGenMetTrue
    * genMETfilter1
    * genMETfilter2
)

