"""
assuming the ocean's sea level increases 1.6 mm every year, display a table showing
how much it will increase each year for 25 years.
"""
AVERAGE_RAINFALL_INCREASE_UNIT_PER_YEAR = 1.6

print("YEAR\t\t\tTOTAL INCREASE")
for year in range(25):
    print((year + 1), '\t\t\t', format(
        AVERAGE_RAINFALL_INCREASE_UNIT_PER_YEAR * (year + 1), ',.2f'))
