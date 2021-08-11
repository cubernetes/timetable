import os
import sys
from json import loads

def import_language_json(language_files_path, lang="en"):

	language_files_names = {
		"de": "de.json",
		"en": "en.json"
	}

	if lang not in language_files_names:
		sys.exit(f'Language "{lang}" does not exist.')

	language_file_path = os.path.join(language_files_path, language_files_names[lang])
	language_file = open(language_file_path).read()
	language_json = loads(language_file)

	return language_json