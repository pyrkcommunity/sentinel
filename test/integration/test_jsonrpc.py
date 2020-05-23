import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from pyrkd import PyrkDaemon
from pyrk_config import PyrkConfig


def test_pyrkd():
    config_text = PyrkConfig.slurp_config_file(config.pyrk_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'0x973814a07c1ae4f3af90372952c9b9709901a95df1d0ea54bd1b3bd6feff5b89'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'0x6015f9422d514ebd62d28c48b7faf86738680091d38ecb2c9bc2381b9325c13a'

    creds = PyrkConfig.get_rpc_creds(config_text, network)
    pyrkd = PyrkDaemon(**creds)
    assert pyrkd.rpc_command is not None

    assert hasattr(pyrkd, 'rpc_connection')

    # Pyrk testnet block 0 hash == 0x6015f9422d514ebd62d28c48b7faf86738680091d38ecb2c9bc2381b9325c13a
    # test commands without arguments
    info = pyrkd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert pyrkd.rpc_command('getblockhash', 0) == genesis_hash
