# Parker and Dubberstein's Babylonian Chronology


In their _Babylonian Chronology 626 B. C.- A.D. 45._, Richard Parker and Waldo Dubberstein published tables of the calculated dates of visible new moons and the Babylonian months and years they corresponded to, as well as intercalations made to keep their [lunisolar calendar](https://en.wikipedia.org/wiki/Babylonian_calendar) aligned with the seasons.

This calendar became the foundation of many other calendars in the ancient Mediterranean, such as those [used by Greeks](https://github.com/seanredmond/heniautos) as well the Jewish and Islamic calendars still in use today. Parker and Dubberstein's work is also still in use as a convenient source of ancient astronomical data (so it seems useful to have a machine-readable version).

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

## Source

Parker, Richard A., and Waldo H. Dubberstein. 1942. _Babylonian Chronology 626 B. C.- A.D. 45._ Studies in Ancient Oriental Civilization 24. Chicago: The University of Chicago Press.

The original can be downloaded from [The University of Chicago](https://oi.uchicago.edu/research/publications/saoc/saoc-24-babylonian-chronology-626-bc-%E2%80%93-ad-45)
