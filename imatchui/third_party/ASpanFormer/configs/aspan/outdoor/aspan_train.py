import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / '../../../'))
from src.config.default import _CN as cfg

cfg.ASPAN.COARSE.COARSEST_LEVEL= [26,26]
cfg.ASPAN.MATCH_COARSE.MATCH_TYPE = 'dual_softmax'
cfg.ASPAN.MATCH_COARSE.SPARSE_SPVS = False

cfg.TRAINER.CANONICAL_LR = 8e-3
cfg.TRAINER.WARMUP_STEP = 1875  # 3 epochs
cfg.TRAINER.WARMUP_RATIO = 0.1
cfg.TRAINER.MSLR_MILESTONES = [8, 12, 16, 20, 24]

# pose estimation
cfg.TRAINER.RANSAC_PIXEL_THR = 0.5

cfg.TRAINER.OPTIMIZER = "adamw"
cfg.TRAINER.ADAMW_DECAY = 0.1
cfg.ASPAN.MATCH_COARSE.TRAIN_COARSE_PERCENT = 0.3
