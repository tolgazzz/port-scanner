# Port Scanner

A fast, multithreaded port scanner built with Python. Scans ports 1-1024 and identifies open ports along with their service names.

## Features

- Multithreaded scanning for fast results
- Automatic service name detection
- Docker support
- Simple CLI interface

## Requirements

- Python 3.11+
- Docker (optional)

## Usage

### With Python

```bash
python main.py --target google.com
```

### With Docker

```bash
# Build the image
docker build -t port-scanner .

# Run the scanner
docker run --rm port-scanner python main.py --target google.com
```

## Example Output

```
A total of 2 open ports were found!
Port 80 (Service: http): Open
Port 443 (Service: https): Open
Scan completed in 2.35 seconds
```

## ⚠️ Disclaimer

This tool is intended for educational purposes only. Only scan targets you have permission to scan.
