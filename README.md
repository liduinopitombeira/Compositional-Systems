# Compositional-Systems
Short compositional systems in algorithmic format used in papers and pieces

1 Sistema_SCR.py - creates melodics fragments based on the randomic choices of three types of basic movements: S - skip (interval>2 semitones), C - conjunct motion (0<interval<=2 semitones), R - repetition.

2 Sistema_DESORD.py - The compositional system is semi-open and its core is formed by four generic objects: O1, O2, O3 and O4. These objects interconnect through transposition operations controlled by twelve keys controlled by a random generator. The order of the system is therefore random. The initial object, as well as its value (in MIDI number), is chosen during compositional planning. The other objects are loaded with the value 60 (middle C of the piano in MIDI value). The size of the system's operating cycle is also chosen in the compositional planning phase. Data is only sent to the output when there is a modification to any of the objects. As the system only provides pitches, all other parameters must be complemented in the compositional planning phase.
