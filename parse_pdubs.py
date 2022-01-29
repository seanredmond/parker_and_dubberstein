#!/usr/bin/env python

# Parses raw text from Parker and Dubberstein and outputs
# tab-delimited data con# tiaining, for each of Parker and
# Dubberstein's visible new moons:
#
#    Julian day number (integer) of the visible new moon
#    Julian year (negative for BCE, 1 BCE is 0)
#    Julian month (number, 1-12)
#    Julian day of the month
#    Babylonian month number (1-13)
#    Babylonian month name, intercalary months identified by "₂"
#    Number of days in Babylonian month
#    Exact Julian datetime of the conjunction (float)
#    Difference between the visible new moon and conjunction
#
# USAGE:
# To parse the file save output to FILE:
#
#     cat parker_and_dubberstein.raw.txt| python parse_pdubs.py > FILE

import sys
import csv

MAX_DIFF = 5.0


class ParseError(Exception):
    pass


def to_jdn(year, month, day):
    a = int((14 - month)/12)
    y = year + 4800 - a
    m = month + 12 * a - 3

    return day + int((153 * m + 2)/5) + y * 365 + int(y/4) - 32083


def getNewMoons():
    with open("new_moons_jdn.txt") as nm:
        return [float(m.strip()) for m in nm if "#" not in m]


def nearest_new_moon(j, nm):
    return min([(j - n, n) for n in nm], key=lambda m: abs(m[0]))


def check_year(y1, y2, same):
    if same:
        if (y1 == y2):
            return y1

    if (y1 == y2 + 1):
        return y1

    raise ParseError(f"Unexpected year: {y1}. It should be {y2} or {y2 + 1}")


def convert_year(y, era, year, same=True):
    if era == "BCE":
        # This distinguishes between the '1' that is 1 BCE and the '1'
        # that is 1 CE
        if not same:
            if year == 0 and y == "1":
                # We've crossed into CE"
                return (1, "CE")

        try:
            return (check_year(int(y) * -1 + 1, year, same), era)
        except ValueError:
            raise ParseError(f"Could not convert year '{y}' to numeric year")

    return (check_year(int(y), year, same), era)


def parse_one_month(year, m, babylonian, month_i, last_jdn, new_moons):
    try:
        month, day = [int(n) for n in m.split("/")]
    except ValueError:
        raise ParseError("Could not convert all months "
                         f"to numeric months and days: {m}")

    jdn = to_jdn(year, month, day)

    if jdn - last_jdn not in (28, 29, 30, 31):
        raise ParseError(f"Too many days ({jdn-last_jdn}) "
                         f"between {last_jdn} and {jdn} "
                         f"({year}-{month}-{day})")

    diff, nearest = nearest_new_moon(jdn, new_moons)

    if diff > MAX_DIFF:
        raise ParseError(f"Difference ({diff}) too great "
                         f"between visible new moon ({jdn}) "
                         f"and nearest conjunction ({nearest})")

    return (jdn, year, month, day, month_i, babylonian,
            jdn - last_jdn, nearest, diff)


def parse_months(months, month_i, last_jdn, new_moons):
    if not months:
        return ()

    this_month = parse_one_month(*months[0], month_i, last_jdn, new_moons)
    return (this_month,) + parse_months(months[1:],
                                        month_i + 1, this_month[0], new_moons)


def parse_semester(s, era, year, last_jdn, month_i, new_moons):
    parts = [p for p in s.split(' ') if p]

    if "/" not in parts[0] and "/" not in parts[1]:
        # First Semester

        this_year, era = convert_year(parts[1], era, year, True)

        months = parse_months(tuple(zip((this_year,) * len(parts[2:]),
                                        parts[2:],
                                        M[0])), month_i, last_jdn, new_moons)

        return (months, era, this_year, months[-1][0], months[-1][4])

    # Second semester
    # Find the new year in the middle of the line
    year_part_i, year_part_t = \
        [p for p in enumerate(parts) if "/" not in p[1]][0]

    new_year, era = convert_year(year_part_t, era, year, False)

    # End of preceding year
    last_q = tuple(zip((year,) * year_part_i,
                       parts[:year_part_i],
                       M[1][:year_part_i]))

    # Begining of following year
    next_q = tuple(zip((new_year,) * len(parts[year_part_i+1:]),
                       parts[year_part_i+1:],
                       M[1][year_part_i:]))

    months = parse_months(last_q + next_q, month_i, last_jdn, new_moons)

    return (months, era, new_year, months[-1][0], months[-1][4])


def parse_half_lines(half1, half2, era, year, last_jdn, new_moons):
    semester_1, era, year, last_jdn, month_i = \
        parse_semester(half1.strip(), era, year, last_jdn, 1, new_moons)
    semester_2, era, year, last_jdn, month_i = \
        parse_semester(half2.strip(), era, year, last_jdn, month_i + 1,
                       new_moons)
    return (semester_1 + semester_2, era, year, last_jdn)


def parse_line(line, era, year, last_jdn, new_moons):
    if line[0].isnumeric():

        return parse_half_lines(line[0:42], line[42:],
                                era, year, last_jdn, new_moons)

    # the line is a king's name. Skip
    return (None, era, year, last_jdn)


M = (("Nisanu", "Aiaru", "Simanu", "Duzu", "Abu", "Ululu", "Ululu₂"),
     ("Tashritu", "Arahsamnu", "Kislimu", "Tebetu", "Shabatu", "Addaru",
      "Addaru₂"))

era = "BCE"
year = -625
last_jdn = 1492841

new_moons = getNewMoons()

writer = csv.writer(sys.stdout, delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)

writer.writerow(("jdn", "julian_year", "julian_month",
                 "julian_day", "month_number", "month_name",
                 "month_days", "new_moon", "diff"))

for line in sys.stdin:
    try:
        # era, year, last_jdn might be updated during parsing
        months, era, year, last_jdn = parse_line(
            line.strip(), era, year, last_jdn, new_moons)

        if months:
            for m in months:
                writer.writerow(m)

    except ParseError as e:
        print(line.strip())
        print(e)
        sys.exit(-1)
