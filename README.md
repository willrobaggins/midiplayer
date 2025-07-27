*text_to_midi.pyw*                 - generate a midi file from notes in input_notes.txt, they must follow certain formatting rules (see below)

*play.pyw*                         - automatically call text_to_midi.pyw and will then play the resulting output.midi

*input_saver.pyw/output_saver.pyw* - save their respective files to an archive file within this directory.

**HOW TO FORMAT**

To use the midiplayer, simply input notes you would like to play in the order you would like to hear them. You can indicate octaves and specify a rhythmic pattern using spaces.

MAXIMUM: 128 quarter note intervals.

**FORMATTING RULES:**

*NOTES*
-Aside from a B note, the midiplayer will accept either lowercase or capitalized characters for the NOTES. 
ACCEPTABLE NOTES:
        C D E F G A B c d e f g a
IMPORTANT: B note must always be capital. Otherwise you will confuse the player with flats.

-You may use either flats or sharps to play the black keys ('#' - or - 'b') 
IMPORTANT: if you would like to use flats, be sure that the ‘b’ is lowercase.
DO: C#, c#, Bb,
DONT: bB (flats should always be lowercase ‘b’, and ‘B note’ should always be capital)

*OCTAVES*
-You may specify the octave of a given note, by adding the octave number to the note.
EX: “C4” would play a C note on the 4th octave.
IMPORTANT: If you do not indicate an octave, the player will default to the 3rd octave for that given note.

*SPACING & RHYTHM*
-Spaces indicates a new interval
EX: “E B” would play an E quarter note, followed by a B quarter note.

-You can use multiple spaces to indicate a longer note.
EX: “E  B” would play an E half note, followed by a B quarter note.
1 space = quarter note 
2 spaces = half note
4 spaces = whole note, etc

*CHORDS & MULTINOTES*
-To play chords, you may group several notes together without using spaces.
EX: “CEG” would play a C major chord.
You may use the same rhythmic rules with chords as well (ie, “CEA  “ would play a C major chord for a half note interval) 
