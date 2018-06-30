# coding: utf-8

DB_HOST_PATH = "sqlite:///../db.sqlite3"

CENTER_LATITUDE = 40.75
CENTER_LONGITUDE = -73.90
LAT_WIDTH = 18.0 / 60
LON_WIDTH = 18.0 / 60
MIN_LAT, MIN_LON = CENTER_LATITUDE - LAT_WIDTH / 2.0, CENTER_LONGITUDE - LON_WIDTH / 2.0
MAX_LAT, MAX_LON = CENTER_LATITUDE + LAT_WIDTH / 2.0, CENTER_LONGITUDE + LON_WIDTH / 2.0
BOUNDING_BOX = [[MIN_LAT, MIN_LON], [MAX_LAT, MAX_LON]]

DELTA_LON = 24.0 / 3600
DELTA_LAT = 16.0 / 3600
MAP_WIDTH = int(LON_WIDTH / DELTA_LON) + 1
MAP_HEIGHT = int(LAT_WIDTH / DELTA_LAT) + 1

START_TIME = 1462075200 + 3600 * 4
TIMESTEP = 60
NUM_SIMULATION_DAYS = 7
NUM_SIMULATION_STEPS = int(60 * 60 * 24 * NUM_SIMULATION_DAYS / TIMESTEP)
DEMAND_AMPLIFICATION_FACTOR = 1.0

MIN_UPDATE_CYCLE = TIMESTEP * 5
IDLE_DURATION_LIMIT = TIMESTEP * 10
REST_PROBABILITY = 0.02
REST_DURATION = 3600 * 2
NUM_VEHICLES = 9000
