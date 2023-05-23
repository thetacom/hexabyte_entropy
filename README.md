# Hexabyte Extended Info Plugin

[![Version](https://img.shields.io/pypi/v/hexabyte_entropy.svg)](https://pypi.python.org/pypi/hexabyte_entropy)
[![Status](https://img.shields.io/pypi/status/hexabyte_entropy)](https://pypi.python.org/pypi/hexabyte_entropy)
[![Wheel](https://img.shields.io/pypi/wheel/hexabyte_entropy)](https://pypi.org/project/hexabyte_entropy/)
[![Downloads](https://img.shields.io/pypi/dm/hexabyte_entropy)](https://pypi.python.org/pypi/hexabyte_entropy)
[![License](https://img.shields.io/pypi/l/hexabyte_entropy.svg)](https://pypi.python.org/pypi/hexabyte_entropy)
[![Python Implementation](https://img.shields.io/pypi/implementation/hexabyte_entropy)](https://pypi.org/project/hexabyte_entropy/)
[![Python Version](https://img.shields.io/pypi/pyversions/hexabyte_entropy)](https://pypi.org/project/hexabyte_entropy/)

[![Lint](https://github.com/thetacom/hexabyte_entropy/actions/workflows/lint.yml/badge.svg)](https://github.com/thetacom/hexabyte_entropy/actions/)
[![Test](https://github.com/thetacom/hexabyte_entropy/actions/workflows/test.yml/badge.svg)](https://github.com/thetacom/hexabyte_entropy/actions/)
[![Release](https://github.com/thetacom/hexabyte_entropy/actions/workflows/release.yml/badge.svg)](https://github.com/thetacom/hexabyte_entropy/actions/)
[![Publish](https://github.com/thetacom/hexabyte_entropy/actions/workflows/publish.yml/badge.svg)](https://github.com/thetacom/hexabyte_entropy/actions/)

[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

A hexabyte plugin for displaying the entropy of file chunks.

The entropy values are mapped to color codes and then displayed in a scrollable sidebar. Clicking on a chunk will jump the active editor to the location of the selected chunk.

## User

### Install

```bash
~/$ pip install hexabyte-entropy
...
```

Add `hexabyte_entropy` to the plugins list inside your hexabyte config (`~/.config/hexabyte/config.toml`).

```toml
plugins = [ "hexabyte_entropy",]
```

## x86_64 Hello World

![Hello World Entropy](imgs/hello_world_entropy.png)

## MacOS Bash

![MacOS Bash Entropy](imgs/bin_bash_diff_entropy.png)

## Developer

```bash
~/$ git clone https://github.com/thetacom/hexabyte_entropy
...
~/$ cd hexabyte_entropy
hexabyte_entropy/$ poetry install
...
```

### Test

```bash
hexabyte_entropy/$ make test
...
```
