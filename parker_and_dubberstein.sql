CREATE TABLE parker_and_dubberstein (
    jdn UNSIGNED INTEGER NOT NULL PRIMARY KEY,
    julian_year SMALLINT NOT NULL,
    julian_month UNSIGNED TINYINT NOT NULL,
    julian_day UNSIGNED TINYINT NOT NULL,
    month_number UNSIGNED TINYINT NOT NULL,
    month_name VARCHAR(9) NOT NULL,
    month_days UNSIGNED TINYINT,
    new_moon UNSIGNED FLOAT NOT NULL,
    diff UNSIGNED FLOAT NOT NULL);
