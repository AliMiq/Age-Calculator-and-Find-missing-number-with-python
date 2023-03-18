def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
    
    # Type in agecalculator(----, -, --) when you born.
ageCalculator(2006, 6, 26)