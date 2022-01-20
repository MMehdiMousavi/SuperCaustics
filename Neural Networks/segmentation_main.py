import argparse

"""Note: check default_ap for runtime argument usage"""
from easytorch import default_ap, EasyTorch
from segmentation import *

sep = os.sep


def same(x): return x


SEG_DATASET = {
    'name': 'SEG',
    'data_dir': 'Picture_Caustic',
    'label_dir': 'Seg_Processed',
    # 'split_dir': 'AIP-DEMO' + sep + 'splits',
    'label_getter': same,
    'patch_shape': (388, 388),
    'patch_offset': (350, 350),
    'expand_by': (184, 184)
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(parents=[default_ap], add_help=False)
    ap.add_argument('-ms', '--model_scale', default=1, type=int, help='model_scale')
    ap.add_argument('-cls', '--classification_mode', default='Multi', type=str,
                    help='Classification mode(Multiclass classifier...)')

    """Run as: python segmentation_main.py -ph train -b 4 -e 251 -ms 1 -data datasets"""
    runner = EasyTorch(dataspecs=[SEG_DATASET], args=ap, load_sparse=True, num_channel=3)
    runner.run(SEGTrainer, SEGDataset)
