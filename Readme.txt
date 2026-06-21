# Automated Resilient WAN Framework

A production-grade multi-branch WAN simulation built in GNS3 featuring automated baseline configuration deployment and real-time path telemetry using Python and Netmiko.

## Features
* **Core-Centric Termination:** WAN circuits terminate strictly on the Layer 3 Core Router to isolate the transit domain.
* **ECMP Path Optimization:** Native OSPFv2 dynamic path cost mapping over symmetric primary/backup ISP lines.
* **Live Telemetry Loop:** Lightweight, humanized script tracking active RIB forwarding metrics instead of simple link-state counters.

## Quick Start
1. Ensure your GNS3 topology is booted and listening on the console ports defined in `devices.py`.
2. Install dependencies: `pip install -r requirements.txt
3. run initial_deploy.py to apply intial configration for all node
4. Run the tracking suite: `python automation/orchestrator.py