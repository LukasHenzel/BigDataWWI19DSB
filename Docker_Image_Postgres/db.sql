CREATE DATABASE big_data_db;
 
CREATE TABLE casenumbers_full (
dateRep VARCHAR(10),
year INT,
month INT,
day INT,
cases INT,
deaths INT,
countriesAndTerritories VARCHAR(30),
geold VARCHAR(2),
popData2020 INT,
countryterritoryCode VARCHAR(3),
continentExp VARCHAR(20)
);


CREATE TABLE casenumbers (
    dateinz VARCHAR(20),
    inzidenz INT,
    CountryCode VARCHAR(15)
);

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('01/09/2021', 2021, 9, 1, 500, 11, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('01/09/2021', 2021, 9, 1, 500, 11, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('31/08/2021', 2021, 8, 31, 510, 20, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('30/08/2021', 2021, 8, 30, 490, 13, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('29/08/2021', 2021, 8, 29, 500, 18, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('28/08/2021', 2021, 8, 28, 450, 2, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('27/08/2021', 2021, 8, 27, 530, 6, 'germany', 'DE', 83166711, 'DEU', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('26/08/2021', 2021, 8, 26, 490, 19, 'germany', 'DE', 83166711, 'DEU', 'Europe');


INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('01/09/2021', 2021, 9, 1, 310, 2, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('31/08/2021', 2021, 8, 31, 310, 2, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('30/08/2021', 2021, 8, 30, 290, 1, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('29/08/2021', 2021, 8, 29, 300, 1, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('28/08/2021', 2021, 8, 28, 250, 2, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('27/08/2021', 2021, 8, 27, 330, 3, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('26/08/2021', 2021, 8, 26, 290, 1, 'Austria', 'AT', 8901064, 'AUT', 'Europe');

INSERT INTO casenumbers_full (dateRep, year, month, day, cases, deaths, countriesAndTerritories, geold, popData2020, countryterritoryCode, continentExp)
VALUES ('25/08/2021', 2021, 8, 25, 300, 1, 'Austria', 'AT', 8901064, 'AUT', 'Europe');