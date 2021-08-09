import os
import sys
import json

sys.path.append("..")

try:
	from table import Table
except ImportError:
	print("Could not import package table. Parent-directory does not contain table package.")
	sys.exit(1)

class Timetable():

	def __init__(self, lang="en"):

		if lang not in language_files_names:
			sys.exit(f'Language "{lang}" does not exist.')

		language_file_path = os.path.join(language_files_path, language_files_names[lang])
		language_file = open(language_file_path).read()
		language_json = json.loads(language_file)
		
	def __str__(self):
		return Table().__str__()



language_files_path = os.path.dirname(__file__)

language_files_names = {
	"de": "de.json",
	"en": "en.json"
}

my_timetable = Timetable()
print(my_timetable)