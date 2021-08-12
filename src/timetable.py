import os
import re
import sys
from typing import Optional
from datetime import datetime, time, timezone

# Necessary for ANSI escaoe codes to work
os.system("")

try:
	from table import Table
	from language import import_language_json
except ImportError:
	print("Could not import package table. Parent-directory does not contain table package.")
	sys.exit(1)

class Teacher():

	def __init__(self, firstname, surname, gender, lang="en"):

		self.firstname = firstname
		self.surname = surname
		self.gender = gender.lower()

		language_json = import_language_json(os.path.join(os.path.dirname(__file__), "..", "lang"), lang=lang)

		titles = {
			"male": language_json["mr"],
			"female": language_json["ms"]
		}

		if gender not in ["male", "female", "diverse"]:
			self.gender = "Unknown"
			self.title = ""
		else:
			self.title = titles[gender]


	def __str__(self):
		return self.title + " " + self.surname

class Subject():

	def __init__(self, name: str, short_name: str, advanced: bool, block: int, teacher: str, rgb: tuple):

		self.name = name
		self.short_name = short_name
		self.block = block
		self.teacher = teacher
		self.rgb = rgb

		self.short_name = f"\x1b[38;2;{';'.join(map(str, self.rgb))}m{self.short_name}\x1b[0m"

	def __str__(self):
		return f"{self.short_name}"

class Timetable(Table):

	def __init__(self, lang="en"):

		language_json = import_language_json(os.path.join(os.path.dirname(__file__), "..", "lang"), lang=lang)

		attributes = [(language_json['class_ordinal'], str), (language_json['time'], str), (language_json['break'], int), (language_json['monday'], Subject), (language_json['tuesday'], Subject), (language_json['wednesday'], Subject), (language_json['thursday'], Subject), (language_json['friday'], Subject)]

		super().__init__(attributes)

	def __str__(self, color=True):

		if self.has_attributes:
			max_widths = [len(attribute[0]) for attribute in self.data[0]]
			offset = 1
		else:
			max_widths = [0] * self.cols
			offset = 0

		for row in self.data[offset:]:
			for i, width in enumerate(max_widths):
				if isinstance(row[i], tuple):
					if isinstance(row[i][0], time):
						if (len_ := len(self.format_time(row[i]))) > width:
							max_widths[i] = len_
					else:
						if (len_ := len(self.remove_formatting(row[i][0]) + " " + self.remove_formatting(row[i][1]))) > width:
							max_widths[i] = len_
				else:
					if (len_ := (len(self.remove_formatting(row[i])))) > width:
						max_widths[i] = len_

		divider = [self.HOR * width for width in max_widths]
		string_table = self.table_line(self.TL, self.HOR_D, self.TR, max_widths, self.HOR, divider) + "\n"

		if self.has_attributes:
			string_table += self.table_line(self.VER, self.VER, self.VER, max_widths, " ", [datum[0] for datum in self.data[0]]) + "\n"
			string_table += self.table_line(self.VER_R, self.CROSS, self.VER_L, max_widths, self.HOR, divider) + "\n"

		for row in self.data[offset:]:
			row_values = [row[0]]

			if self.is_time_between(row[1][0], row[1][1]):
				row_values.append(self.format_time(row[1], "\x1b[33m"))
			else:
				row_values.append(self.format_time(row[1]))

			if self.is_time_between(row[1][1], time(*divmod(row[1][1].hour * 60 + row[1][1].minute + row[2], 60))):
				row_values.append(f"\x1b[33m{row[2]}\x1b[0m")
			else:
				row_values.append(row[2])

			for i in range(3,8):
				if isinstance(row[i], tuple):
					row_values.append(f"{row[i][0]} {row[i][1]}")
				else:
					row_values.append(row[i])

			string_table += self.table_line(self.VER, self.VER, self.VER, max_widths, " ", row_values) + "\n"

		string_table += self.table_line(self.BL, self.HOR_U, self.BR, max_widths, self.HOR, divider) + "\n"

		if color:
			return string_table
		else:
			return re.sub(r"\x1b\[.*?m", "", string_table)
	def is_time_between(self, begin_time, end_time, check_time=None):
		# If check time is not given, default to current UTC time
		check_time = check_time or datetime.now().time()
		if begin_time < end_time:
			return check_time >= begin_time and check_time <= end_time
		else: # crosses midnight
			return check_time >= begin_time or check_time <= end_time

	def format_time(self, times, color: Optional = None):
		return f"{color if color else ''}{str(times[0].hour).zfill(2)}:{str(times[0].minute).zfill(2)}–{str(times[1].hour).zfill(2)}:{str(times[1].minute).zfill(2)}" + ('\x1b[0m' if color else '')

	def remove_formatting(self, s):
		return re.sub(r"\x1b\[.*?m", "", str(s))
