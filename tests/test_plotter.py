from your.utils.plotter import *
from your import Your

import os
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
_install_dir = os.path.abspath(os.path.dirname(__file__))


def test_save_bandpass():
    fil_file = os.path.join(_install_dir, 'data/28.fil')
    y = Your(fil_file)
    save_bandpass(y, y.bandpass(), outname='28_bp.png')
    assert os.path.isfile('28_bp.png')
    os.remove('28_bp.png')

def test_plot_h5():
    h5_file = os.path.join(_install_dir, 'data/test.h5')
    plot_h5(h5_file, publication=False)
    assert os.path.isfile('data/test.png')
    os.remove('data/test.png')

    plot_h5(h5_file, publication=True, mad_filter=True)
    assert os.path.isfile('data/test.png')
    os.remove('data/test.png')



