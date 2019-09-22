import datetime
import json

DEFAULT_TEMP = 0


class Alarm(object):
	def __init__(self):
		self.status = ""
		self.front_garage_door = ""
		self.sliding_glass_door = ""
		self.living_great = ""
		self.master = ""
		self.offices = ""
		self.west_wing = ""
		self.bike_garage = ""
		self.mc_garage = ""
		self.main_garage = ""


class Pool(object):
	def __init__(self):
		self.light = ""
		self.temp = DEFAULT_TEMP


class Spa(object):
	def __init__(self):
		self.pump = ""
		self.temp = DEFAULT_TEMP


class SensorSmall(object):
	def __init__(self):
		self.temp = DEFAULT_TEMP
		self.humidity = 0.0
		self.fan = ""
		self.time = ""


class Sensor6In1(object):

	def __init__(self):
		self.temp = DEFAULT_TEMP
		self.humidity = 0.0
		self.lux = 0
		self.fan = ""


class SensorMajor(object):

	def __init__(self):
		self.temp = DEFAULT_TEMP
		self.dew_point = 0.0
		self.humidity = 0.0
		self.wind_direction = ""
		self.wind_speed = 0.0
		self.wind_gust = 0.0
		self.wind_chill = 0.0
		self.pressure = 0
		self.rain_rate = 0.0
		self.rain_total = 0.0


class SensorThermostat(object):

	def __init__(self):
		self.temp = DEFAULT_TEMP
		self.mode = ""
		self.heat_set = 0.0
		self.cool_set = 0.0


class WeatherData(object):

	def __init__(self):
		self.theater_window = SensorSmall()
		self.theater = Sensor6In1()
		self.back_yard = SensorMajor()
		self.master_bedroom_window = SensorSmall()
		self.library = SensorSmall()
		self.humidor = SensorSmall()
		self.main_garage_temp = SensorSmall()
		self.front_door = SensorSmall()
		self.living_room = Sensor6In1()
		self.master_bedroom_thermostat = SensorThermostat()
		self.kitchen_thermostat = SensorThermostat()
		self.living_room_window = SensorSmall()
		self.alarm = Alarm()
		self.pool = Pool()
		self.spa = Spa()
		self.date_generated = datetime.datetime.now().strftime("%m-%d-%y %I:%M %p")

	def to_json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
