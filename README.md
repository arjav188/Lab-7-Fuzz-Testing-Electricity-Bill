# Lab 7 — Fuzz Testing for Electricity Bill

Fuzz testing exercise using Python, pytest, and Hypothesis. Three functions were hardened against unexpected or malformed inputs.

## Files

- `electricity_bill.py`: fixed electricity bill application
- `test_electricity_bill.py`: property-based Hypothesis tests
- `requirements.txt`: test dependencies

## Run locally

```powershell
python -m pip install -r requirements.txt
python electricity_bill.py
python -m pytest test_electricity_bill.py -v
```

### Sample inputs and outputs

- Meter reading `1200:1350` → units consumed `150`
- Daily units `5,7,6` → daily average `6.0`
- Tariff code `DOM-A` → rate per unit `3`

### Testing outcome

The original application failed three Hypothesis test functions. After adding input validation and defensive handling, all three passed in the user's Windows VS Code session on November 19, 2026.

The lab implementation returns `0` for malformed input to satisfy no-crash tests. In a production billing application, invalid entries should also be clearly reported to the user.

## Attribution

Adapted from the [course-provided electricity bill starter project](https://github.com/SETAPESU26/L6_L7_17_electricity_bill) for Lab 7. Fuzz tests and input validation were added for this exercise.
