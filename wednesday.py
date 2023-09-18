from datetime import date, datetime, timedelta


def next_wednesday():
    # today = date.fromisoformat("2023-08-27")
    today = datetime.now()
    # Calculate days until next Wednesday (0=Monday, 1=Tuesday, ..., 6=Sunday)
    days_until_wednesday = (2 - today.weekday()) % 7

    if days_until_wednesday == 0:
        days_until_wednesday = 7  # If today is Wednesday, add 7 days to get the next Wednesday

    next_wednesday_date = today + timedelta(days=days_until_wednesday)
    return next_wednesday_date


def is_first_wednesday(wednesday_date: datetime.date):
    # Check if the date is a Wednesday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    if wednesday_date.weekday() != 2:  # 2 corresponds to Wednesday
        return False

    # Check if the date is within the first 7 days of the month
    if wednesday_date.day <= 7:
        return True
    else:
        return False


if __name__ == '__main__':
    wed = next_wednesday()

    print(wed)
    print(is_first_wednesday(wed))
