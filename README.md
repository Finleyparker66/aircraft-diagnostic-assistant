

A Python-based tool designed to simulate aircraft fault diagnosis for a Cessna 172.

## Overview

This project models how aircraft engineers troubleshoot faults by analysing symptoms and identifying likely causes and diagnostic steps.

The tool allows a user to input a symptom (e.g. engine stall) and returns:

- Affected system
- Likely causes
- Recommended checks

## Example

Input:
engine stall

Output:
System: Engine / Fuel System

Likely Causes:
- Fuel starvation
- Carburettor icing
- Air intake blockage

Recommended Checks:
- Check fuel supply
- Apply carb heat
- Inspect air intake

# Engineering Approach

This project follows a structured diagnostic approach similar to real-world aircraft maintenance:

- Symptom-based fault identification
- System-level classification
- Step-by-step troubleshooting

# Future Improvements

- Add more aircraft systems (electrical, hydraulics)
- Introduce probability-based diagnosis
- Expand to full fault tree logic
- Improve user interface

# Author

Finley Parker  
Aspiring Aircraft Engineer

# aircraft-diagnostic-assistant
Cessna 172 diagnostic tool for aircraft fault troubleshooting
