# Hexabyte Extended Info Plugin

A hexabyte plugin for displaying the entropy of file chunks.

The entropy values are mapped to color codes and then displayed in a scrollable sidebar. Clicking on a chunk will jump the active editor to the location of the selected chunk.

## Install

```bash
~/$ pip install hexabyte_entropy
...
```

Add `hexabyte_entropy` to the plugins list inside your hexabyte config (`~/.config/hexabyte/config.toml`).

```toml
plugins = [ "hexabyte_entropy",]
```
