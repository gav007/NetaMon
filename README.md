# NetaMon — Part 1: Local Network Monitoring

NetaMon is a Python program that collects network information from a local Linux computer and saves it as JSON.

## Requirements

- Linux (tested on an Ubuntu virtual machine)
- Python 3
- The `ip` command (`iproute2` package)

## How to run

Open a terminal in the NetaMon project folder and run:

```bash
python3 localmon.py
```

The program collects network details, writes `data/local_network.json`, and displays a summary in the terminal.

## Information collected

- Hostname
- Network interface names, MTU, MAC addresses, flags and operational states
- IPv4 and IPv6 addresses
- Route destinations and gateways (where available)

## How it works

The Part 1 program uses Python's `subprocess` module to run these Linux commands:

```bash
ip -json link show
ip -json address show
ip -json route show
hostname
```

It organises the results into Python dictionaries and lists, then uses the `json` module to save them to a file.

The OS and Pexpect versions, where present, are separate practice exercises and are not required for the Part 1 subprocess version.
