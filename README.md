# Parker and Dubberstein's Babylonian Chronology


In their _Babylonian Chronology 626 B. C.- A.D. 45._, Richard Parker and Waldo Dubberstein published tables of the calculated dates of visible new moons and the Babylonian months and years they corresponded to, as well as intercalations made to keep their [lunisolar calendar](https://en.wikipedia.org/wiki/Babylonian_calendar) aligned with the seasons.

The "visible new moon" is the first slight crescent that can be seen by the human eye as the moon begins to wax. This is different from the "astronomical" new moon when the sun, earth and moon are aligned (called the "conjunction") and the moon between the Earth and Sun. The moment of conjunction is only visible when the Sun, Earth, and Moon are so precisely aligned that it causes a solar eclipse, but the observation of the visble new moon marks the beginning of the month in the Babylonian and many other lunisolar calendars.

The Babylonian calendar became the foundation of many other calendars in the ancient Mediterranean, such as those [used by Greeks](https://github.com/seanredmond/heniautos) as well the Jewish and Islamic calendars still in use today. Parker and Dubberstein's work is also still in use as a convenient source of ancient astronomical data (so it seems useful to have a machine-readable version).

## Format

`parker_and_dubberstein.tsv` contains 9 tab-delimited columns:


| Field| Explanation |
| -----| ----- |
| jdn          | a ["Truncated" Julian Day](https://en.wikipedia.org/wiki/Julian_day) of the date of visible new moon |                                                                                                          
| julian_year  | The Julian year. BCE is negative and 1 BCE is 0   |                                                   
| julian_month | The number of the Julian month |
| julian_day  | The Julian day of the month |
| month_number | The number of the month (1-13) in the Babylonian Calendar |
| month_name   | The name of the Babylonian month. Intercalated months are indicated with a subscript "₂" (e.g. "Addaru₂", "Ululu₂") |
| month_days   | Number of days in the Babylonian month |
| new_moon     |	The exact Julian day of the [conjunction](https://en.wikipedia.org/wiki/Conjunction_(astronomy)) of the Sun and Moon (or "astronomical new moon"). |
| diff         | The difference (in days) between the conjunction and the visible new moon |

## Other Files

| file | description |
| ---- | ----------- |
| `parker_and_dubberstein.raw.txt` | raw text, slightly formatted from Parker and Dubberstein, pages 25-46 |
| `new_moons_jdn.txt` | Julian days of new moons covered by Parker and Dubberstein's tables |
| `parse_pdubs.py` | python script used to parse the raw file into tab-delimted format |
| `parker_and_dubberstein.sql` | SQL script to create a table for importing data into a database |

## Example

A row containing this data:

| Field| Value |
| -----| -----: |
| jdn          | 1494495 |                                                                                                          
| julian_year  | -621   |                                                   
| julian_month | 9 |
| julian_day  | 15 |
| month_number | 7 |
| month_name   | Ululu₂ |
| month_days   | 29|
| new_moon     |	1494492.92662818 |
| diff         | 2.07337181689218 |

Should be interpreted to mean:

- Parker and Dubberstain calculate September 15, 622 BCE as a visible new moon (-621 = 622 BCE)
- The truncated Julian day is 1494495
- This new moon begins the 7th month of this Babylonian year
- The month is an intercalated Ululu
- The new moon conjunction occured at the Julian Day 1494492.92662818
- The visible new moon is 2.07337181689218 after the conjunction

## Importing into a Database

`parker_and_dubberstein.sql` contains a command that will create a table that can store the data in `parker_and_dubberstein.tsv`. To import the data into a Sqlite3 database named `your_database.db` for instance:

    > sqlite3 your_database.db
    sqlite> .read parker_and_dubberstein.sql
    sqlite> .mode tabs
    sqlite> .import parker_and_dubberstein.tsv parker_and_dubberstein

## Source

Parker, Richard A., and Waldo H. Dubberstein. 1942. _Babylonian Chronology 626 B. C.- A.D. 45._ Studies in Ancient Oriental Civilization 24. Chicago: The University of Chicago Press.

The original can be downloaded from [The University of Chicago](https://oi.uchicago.edu/research/publications/saoc/saoc-24-babylonian-chronology-626-bc-%E2%80%93-ad-45)
