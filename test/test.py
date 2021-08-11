import sys
import os
from datetime import time

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from timetable import Teacher, Subject, Timetable

nickel =     Teacher("Susanne", "Nickel",     "female", "de")
wichert =    Teacher("Vorname", "Wichert",    "male",   "de")
koch =       Teacher("Katrin",  "Koch",       "female", "de")
lehmann =    Teacher("Elvira",  "Lehmann",    "female", "de")
buch =       Teacher("Vorname", "Buch",       "female", "de")
schoessler = Teacher("Anja?",   "Schoessler", "female", "de")
schmidt =    Teacher("Roland",  "Schmidt",    "male",   "de")
krohs =      Teacher("André",   "Krohs",      "male",   "de")
friedemann = Teacher("Vorname", "Friedemann", "male",   "de")

mathematik =  Subject("Mathematik",  "Mat",     True,   1, nickel,     (61, 122, 135)  )
informatik =  Subject("Informatik",  "Inf",     True,   2, koch,       (5, 168, 192)   )
deutsch =     Subject("Deutsch",     "Deu",     False,  1, schoessler, (237, 156, 128) )
englisch =    Subject("Englisch",    "Eng",     False,  9, lehmann,    (254, 245, 64)  )
geschichte =  Subject("Geschichte",  "Ges",     False,  4, buch,       (135, 73, 43)   )
psychologie = Subject("Psychologie", "Psy",     False,  7, schmidt,    (60, 186, 177)  )
physik =      Subject("Physik",      "Phy",     False,  8, wichert,    (209, 182, 73)  )
sport =       Subject("Sport",       "Spo",     False,  5, buch,       (190, 100, 42)  )
musik =       Subject("Musik",       "Mus",     False,  2, krohs,      (95, 155, 71)   )
seminarkurs = Subject("Seminarkurs", "Sem",     False,  3, schmidt,    (218, 145, 176) )
musikschule = Subject("Musikschule", "MusSchu", True,  -1, friedemann, (52, 92, 67)    )

myTimetable = Timetable(lang="de")

myTimetable.append_row(["1",   (time(7,20), time(8,5)),    10, None,                 (physik, "105"),     None,                (englisch, "229"),    (sport, "Hal")      ])
myTimetable.append_row(["2",   (time(8,15), time(9,0)),    10, (psychologie, "219"), (informatik, "227"), None,                (deutsch, "018"),     (physik, "105")     ])
myTimetable.append_row(["3",   (time(9,10), time(9,55)),   20, (deutsch, "008"),     (mathematik, "117"), (musik, "003"),      (psychologie, "219"), (physik, "105")     ])
myTimetable.append_row(["4",   (time(10,15), time(11,0)),  10, (deutsch, "008"),     (mathematik, "117"), (mathematik, "121"), (psychologie, "219"), (geschichte, "019") ])
myTimetable.append_row(["5+6", (time(11,10), time(12,40)), 30, (musik, "003"),       (deutsch, "019"),    (informatik, "227"), (mathematik, "123"),  (informatik, "227") ])
myTimetable.append_row(["7",   (time(13,15), time(14,0)),  10, (seminarkurs, "227"), (sport, "Hal"),      None,                None,                 (englisch, "213")   ])
myTimetable.append_row(["8",   (time(14,10), time(14,55)), 20, (seminarkurs, "227"), (sport, "Hal"),      None,                None,                 (englisch, "213")   ])
myTimetable.append_row(["9",   (time(15,15), time(16,0)),   0, None,                 musikschule,         None,                None,                 None                ])

print(myTimetable.__str__(color=True), end="")