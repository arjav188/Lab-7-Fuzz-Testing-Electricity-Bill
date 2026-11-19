RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str):
        return 0
    try:
        previous, current = reading.split(":")
        previous, current = int(previous), int(current)
        if previous < 0 or current < previous:
            return 0
        return current - previous
    except (ValueError, TypeError):
        return 0


def daily_average(units_csv):
    if not isinstance(units_csv, str):
        return 0
    try:
        units = [int(u) for u in units_csv.split(",")]
        if not units or any(u < 0 for u in units):
            return 0
        return round(sum(units) / len(units), 2)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


def tariff_rate(code):
    if not isinstance(code, str):
        return 0
    try:
        category, slab = code.strip().upper().split("-")
        if category not in RATES or slab not in SLAB:
            return 0
        return RATES[category] * SLAB[slab]
    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running units_consumed ====")
    reading = input("Enter meter readings as previous:current: ")
    print("Units Consumed:", units_consumed(reading))
    print("\n==== Running daily_average ====")
    units = input("Enter daily units as CSV: ")
    print("Daily Average:", daily_average(units))
    print("\n==== Running tariff_rate ====")
    code = input("Enter a tariff code: ")
    print("Rate per Unit:", tariff_rate(code))


if __name__ == "__main__":
    main()
