# Grbl support for OctoPrint

This plugin lets you use Grbl based CNC machines with OctoPrint.

**NOTE:** You still need to set a few more settings after installing
this plugin to make it work. See below.

## Installation

```bash
pip install octoprint-grbl-plugin
```

## Required Configuration

- _Serial Connection_ > _Advanced options_ > _"Hello" command_ = **M5**
- _Features_ > _Send a checksum with the command_ > **Never**
