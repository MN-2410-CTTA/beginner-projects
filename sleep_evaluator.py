def sleep_quality(hours):
    if hours >= 7:
        return "Good"
    elif hours >= 5:
        return "Needs improvement"
    else:
        return "Critical"

hours = int(input("Hours slept: "))
print(sleep_quality(hours))
