-- SQLite schema for the vaccination analysis database.
-- The companion .sqlite file contains the loaded and cleaned data.
PRAGMA foreign_keys = ON;

CREATE TABLE "candidate_coverage_incidence" (
"code" TEXT,
  "name" TEXT,
  "year" REAL,
  "antigen" TEXT,
  "coverage" REAL,
  "disease" TEXT,
  "incidence_rate" REAL,
  "denominator" TEXT
);

CREATE TABLE "cases" (
"group" TEXT,
  "code" TEXT,
  "name" TEXT,
  "year" REAL,
  "disease" TEXT,
  "disease_description" TEXT,
  "cases" REAL
);

CREATE TABLE "coverage" (
"group" TEXT,
  "code" TEXT,
  "name" TEXT,
  "year" REAL,
  "antigen" TEXT,
  "antigen_description" TEXT,
  "coverage_category" TEXT,
  "coverage_category_description" TEXT,
  "target_number" REAL,
  "doses" REAL,
  "coverage" REAL
);

CREATE TABLE "coverage_admin" (
"group" TEXT,
  "code" TEXT,
  "name" TEXT,
  "year" REAL,
  "antigen" TEXT,
  "antigen_description" TEXT,
  "coverage_category" TEXT,
  "coverage_category_description" TEXT,
  "target_number" REAL,
  "doses" REAL,
  "coverage" REAL
);

CREATE TABLE "coverage_by_year_antigen" (
"year" REAL,
  "antigen" TEXT,
  "mean" REAL,
  "median" REAL,
  "count" INTEGER
);

CREATE TABLE "incidence" (
"group" TEXT,
  "code" TEXT,
  "name" TEXT,
  "year" REAL,
  "disease" TEXT,
  "disease_description" TEXT,
  "denominator" TEXT,
  "incidence_rate" REAL,
  "disease_norm" TEXT
);

CREATE TABLE "introduction" (
"iso_3_code" TEXT,
  "countryname" TEXT,
  "who_region" TEXT,
  "year" REAL,
  "description" TEXT,
  "intro" TEXT
);

CREATE TABLE "introduction_by_region" (
"who_region" TEXT,
  "description" TEXT,
  "year" REAL,
  "introduced_pct" REAL
);

CREATE TABLE "schedule" (
"iso_3_code" TEXT,
  "countryname" TEXT,
  "who_region" TEXT,
  "year" REAL,
  "vaccinecode" TEXT,
  "vaccine_description" TEXT,
  "schedulerounds" REAL,
  "targetpop" TEXT,
  "targetpop_description" TEXT,
  "geoarea" TEXT,
  "ageadministered" TEXT,
  "sourcecomment" TEXT
);
