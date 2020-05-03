CREATE TABLE  users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    privilage TEXT NOT NULL
);

DROP TABLE users;

INSERT INTO users (
    username, first_name, last_name, password, privilage
)
VALUES (
    'admin', 'admin', 'admin', 'admin', 'Admin'
);

SELECT * FROM users;

SELECT * FROM weather_data;

ALTER TABLE weather_data_orig RENAME TO weather_data;

SELECT * FROM wather_data_orig;

DROP TABLE weather_data;
DROP TABLE wather_data_orig;

CREATE TABLE weather_data(id INTEGER, 
    temperature INTEGER,
    timestamp INTEGER,
    humidity INTEGER,
    precipitation INTEGER,
    cloud INTEGER,
    wind_speed INTEGER,
    wind_direction INTEGER);

INSERT INTO weather_data(timestamp, temperature, humidity, precipitation, cloud, wind_speed, wind_direction)
    SELECT timestam, temperature, humidity, precipitation, cloud, wind_speed, wind_direction" FROM wather_data_orig;

SELECT * FROM weather_data
    WHERE "index" = (SELECT MAX("index") FROM weather_data);

DELETE FROM weather_data
    WHERE "index" = (SELECT MAX("index") FROM weather_data);