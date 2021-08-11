import re
import sys
from typing import Optional

class Table():

	def __init__(self, attributes: Optional = None):
		if attributes is not None:
			if attributes.__class__.__name__ not in ["list", "tuple"]:
				print("Attributes must be a list or a tuple.")
				return None
			if len(attributes) == 0:
				print(attributes.__class__.__name__.title + " for attributes must be non-empty.")
				return None
			self.data = [attributes]
			self.cols = len(attributes)
			self.has_attributes = True
		else:
			self.data = []
			self.cols = 0
			self.has_attributes = False
		self.rows = 0

		self.HOR = "─"
		self.VER = "│"
		self.TL = "┌"
		self.TL = "╭"
		self.TR = "┐"
		self.TR = "╮"
		self.BL = "└"
		self.BL = "╰"
		self.BR = "┘"
		self.BR = "╯"
		self.CROSS = "┼"
		self.HOR_D = "┬"
		self.HOR_U = "┴"
		self.VER_R = "├"
		self.VER_L = "┤"

	def __str__(self):

		if self.has_attributes:
			max_widths = [len(attribute[0]) for attribute in self.data[0]]
			offset = 1
		else:
			max_widths = [0] * self.cols
			offset = 0

		for row in self.data[offset:]:
			for i, width in enumerate(max_widths.copy()):
				if len(str(row[i].__str__())) > width:
					max_widths[i] = len(str(row[i].__str__()))

		divider = [self.HOR * width for width in max_widths]
		string_table = self.table_line(self.TL, self.HOR_D, self.TR, max_widths, self.HOR, divider) + "\n"

		if self.has_attributes:
			string_table += self.table_line(self.VER, self.VER, self.VER, max_widths, " ", [datum[0] for datum in self.data[0]]) + "\n"
			string_table += self.table_line(self.VER_R, self.CROSS, self.VER_L, max_widths, self.HOR, divider) + "\n"

		for row in self.data[offset:]:
			string_table += self.table_line(self.VER, self.VER, self.VER, max_widths, " ", row) + "\n"

		string_table += self.table_line(self.BL, self.HOR_U, self.BR, max_widths, self.HOR, divider) + "\n"

		return string_table

	def append_row(self, row) -> None:
			if row.__class__.__name__ not in ["list", "tuple"]:
				print("Row must be a list or a tuple.")
				return None
			if len(row) != self.cols:
				print(row.__class__.__name__.title() + " for row does not have the same amount of elements as the table has columns.")
				return None

			self.data.append(row)

	def get(self) -> list:
			return self.data

	def table_line(self, left, join, right, widths, pad, values):

		return left + join.join([((str(pad) + str(value if value else '─' * width)).ljust(width + 2 + (len(str(value)) - len(re.sub(r"\x1b\[.*?m", "", str(value)))), pad)) for value, width in zip(values, widths)]) + right