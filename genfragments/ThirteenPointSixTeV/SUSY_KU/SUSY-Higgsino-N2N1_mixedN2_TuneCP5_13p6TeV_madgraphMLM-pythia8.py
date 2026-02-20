import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *


baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05          # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05    # ~tau_2
   1000016     1.00000000E+05    # ~nu_tauL
   1000021     1.00000000E+05    # ~g
   1000022     %MN1%           # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%          # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
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
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
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

model = "Higgsino-N2N1"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.495

def matchParams(mass):
  elif mass < 221.: return 76,0.513
  elif mass < 261.: return 76,0.512
  elif mass < 301.: return 76,0.504
  elif mass < 341.: return 76,0.497
  elif mass < 381.: return 76,0.483
  elif mass < 421.: return 76,0.487
  elif mass < 461.: return 76,0.462
  elif mass < 501.: return 76,0.462
  else: return 76,0.5

# Parameters that define the grid in the bulk and diagonal
   
mn2_points = [101,126,151,176,201,226,251,276,301,326,351,376,401,426,451,476,501]
dm_points  = [0.6,0.8,1,1.5,2,3,5,6,7.5,10,15,20,25,30,40,50,60,70,80,90,100,120,140]

nev_per_point = 200

from itertools import product

for mn2, dm in product(mn2_points, dm_points):

    # Enforce MN1 >= 1
    if mn2 - dm < 1:
        continue

    mn1 = mn2 - dm
    mc1 = (mn2 + mn1) / 2.

    qcut, tru_eff = matchParams(mn2)
    wgt = nev_per_point / tru_eff

    mn2Str = str(int(mn2))
    mn1Str = "{0:.2f}".format(mn1).replace(".","p")
    mc1Str = "{0:.2f}".format(mc1).replace(".","p")

    slhatable = baseSLHATable.replace('%MN2%','%e' % mn2)
    slhatable = slhatable.replace('%MC1%','%e' % mc1)
    slhatable = slhatable.replace('%MN1%','%e' % mn1)


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
            ConfigWeight = cms.double(wgt),
            GridpackPath = cms.string(''),  ##FIXME
            ConfigDescription = cms.string('%s_MN2-%i_MN1-%i' % (model, mn2Str, mn1Str)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
      )

##   Filter Setup

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
    genHTcut = cms.double(50.0)   # HT > 50 GeV
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
    minNumber = cms.uint32(1)
)

genLeptonsAll = cms.EDFilter(
    "GenParticleSelector",
    src = cms.InputTag("tmpGenParticles"),
    cut = cms.string(
        "(abs(pdgId) == 11 || abs(pdgId) == 13) && status == 1"
    ),
    filter = cms.bool(False)
)

genLeptonsFromHardProcess = cms.EDFilter(
    "GenParticleSelector",
    src = cms.InputTag("tmpGenParticles"),
    cut = cms.string(
        "(abs(pdgId) == 11 || abs(pdgId) == 13)"
        " && status == 1"
        " && (statusFlags().fromHardProcess() || statusFlags().isDirectHardProcessTauDecayProduct())"
    ),
    filter = cms.bool(False)
)

genAtLeastTwoLeptons = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("genLeptonsAll"),
    minNumber = cms.uint32(2)
)

genAtLeastTwoLeptonsFromHardProcess = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("genLeptonsFromHardProcess"),
    minNumber = cms.uint32(2)
)

dileptonSequence = cms.Sequence(
    genAtLeastTwoLeptons
  * genAtLeastTwoLeptonsFromHardProcess
)


htmetSequence = cms.Sequence(
    genHTFilter
  * genMETfilter1
  * genMETfilter2
)


# Finally, chain into the production sequence
ProductionFilterSequence = cms.Sequence(
    generator
  * tmpGenParticles
  * tmpGenParticlesForJetsNoNu
  * tmpAk4GenJetsNoNu
  * tmpGenMetTrue
  * genLeptonsAll
)

