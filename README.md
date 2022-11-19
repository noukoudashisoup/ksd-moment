# ksd-moment
A research repository for the paper "Controlling Moments with Kernel Stein Discrepancies."

This repository contains a Python 3.6 implementation of the experiments
in [this paper](https://arxiv.org/abs/2211.05408):

    Controlling Moments with Kernel Stein Discrepancies
    Heishiro Kanagawa, Arthur Gretton, Lester Mackey,
    https://arxiv.org/abs/2211.05408

## Installation

Use the `pip` command to install the package.
It will be necessary to edit out codes for replicating the experiment results; we therefore recommend to install the package as follows:

1. Clone the repository with  `git clone git@github.com:noukoudashisoup/ksd-moment.git`
2. In the cloned directory (after `cd` ), run `pip install -e .`

## Requirements

The package requires `numpy`, `scipy` (these will be installed when you install the package).

We require `pytorch>=1.10.1` and refer to [the official page](https://pytorch.org/) for installation.
We also require the `scem` package. This can be obtained from [its git
  repository](https://github.com/noukoudashisoup/score-EM).