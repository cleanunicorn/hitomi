# Hitomi

[![License: Apache](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/licenses/Apache)
[![CircleCI](https://circleci.com/gh/cleanunicorn/hitomi.svg?style=shield)](https://circleci.com/gh/cleanunicorn/hitomi)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/abffb6cd07ee4a6381eab6b0b0d3f8f8)](https://www.codacy.com/manual/lucadanielcostin/hitomi)
[![PyPI](https://img.shields.io/pypi/v/hitomi.svg)](https://pypi.org/project/hitomi/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Ethereum console for any node.

## Install

```console
$ pip install hitomi
```

## Quick start

Provide a node to connect to and it will drop you into a Python REPL console.

```console
$ hitomi https://mainnet.infura.io      
Hitomi v0.1.1.

Connected to https://mainnet.infura.io.
Chain ID: 1
Block number: 9294088
Mining: False (0 hash rate)
Syncing: False

>>> 
```

The initialized `web3` object is available. All available commands are [documented here](https://github.com/ethereum/wiki/wiki/javascript-api)

```console
>>> web3.eth.blockNumber
1
>>> web3.eth.getBlock(1)
{   'difficulty': 0,
    'extraData': HexBytes('0x'),
    'gasLimit': 6721975,
    'gasUsed': 130535,
    'hash': HexBytes('0x85e4b6c1b09258ac87b135d40be27da551faeb7d47c39fd6c031bfb9e2ccb33a'),
    'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
    'miner': '0x0000000000000000000000000000000000000000',
    'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
    'nonce': HexBytes('0x0000000000000000'),
    'number': 1,
    'parentHash': HexBytes('0x0cb1921fc2953b6fff2f7db200cb9329c4f23c2aa4f9428dfe7c7af24996b16e'),
    'receiptsRoot': HexBytes('0x9d8502b53de7e5aca49e6b80af927d7b8e9cea242ea907527b406c259d3912ec'),
    'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
    'size': 1000,
    'stateRoot': HexBytes('0xb65b969d6179e8a2f8946fa9525918d0dbcabbe4e168071b273bd27603938ef2'),
    'timestamp': 1579701558,
    'totalDifficulty': 0,
    'transactions': [   HexBytes('0x46b40a1bf33d4d656734bd88966b520dce601d919d2a6f848d3b8c0bae3c3086')],
    'transactionsRoot': HexBytes('0x9138007037f44109896cba97cdb66cb31232ee83c36fb226ae28e304144540f3'),
    'uncles': []}
```

## Commands

Once you are dropped in the console there are some commands available

- [accounts](#commandaccounts)

### <a href="#commandaccounts"></a>Accounts
```python
>>> accounts
[   '0xd802f1f519E0F871C6aD07689C09F305F26b1b4a',
    '0x14a7bc9a095e8cc4c7CC3BE8F1a7F3702A942538',
    '0x1790A965472dB702d042AB3D5CAa35bC34133293',
    '0xf0ba180BDE68d5cF6c885977DC85f591CBB255a9',
    '0x269734969962453E11E12027642180a9f26b67E4',
    '0x605489943C49F294262DDCBDC8d2BC181D452084',
    '0x5486d7345809d7b68f3aAE773FD67BB2f0c388A3',
    '0xd2706e9dCe4CD06A64E4556254C800e070f42644',
    '0x98ffbeE4A7cf2E47FA343b09E4Bae737e7BcD535',
    '0xf12286180309C4fb7A644f4F08a294a9c2AA23B4']
```

<!--
## Demo

 Add asciinema demo 

-->

## Why Hitomi?

[Hitomi Tanaka](https://es.wikipedia.org/wiki/Hitomi_Tanaka)
<!-- Add ascii art picture of Hitomi -->
