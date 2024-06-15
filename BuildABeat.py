# Title: Western-Carnatic Mashup
# Composer & Singer & Coder: Shreyas Dhavala (Me)
# Description: 
#    Combining Indian classical notes with Western beats, this 
#    composition conveys the message that making the right decisions can gradually 
#    help us achieve our visions & dreams.

# Other outside instruments used: instrument in GeoShred App


from earsketch import *

#background track (whole song)
background = IRCA_LATIN_JAZZ_1_BASS

backtrack1 = THEMUSICLOVER_SASANIRIRILOW1
backtrack2 = THEMUSICLOVER_PAPAPAMADADA1
backtrack3 = THEMUSICLOVER_HIGHTOLOWSWARAS
backtrack4 = THEMUSICLOVER_SWARAMIXHIGHLOW
trackEnd =  THEMUSICLOVER_GEOEND
guitar = MILKNSIZZ_BAYSIQUE_CHOPPED_GUITAR
beat1 = AK_UNDOG_PERC_DRUMS
beat2 = DUBSTEP_PERCDRUM_002
claps = AK_UNDOG_CLAPS_SNAPS_5
poet1 = RBIRD_VOX_CLOSER_TO_YOUR_VISION
poet2 = RBIRD_VOX_MAKE_THE_DECISION

#Intro carnatic notes low
def intro(clip, start, end):
   fitMedia( clip ,2, start, end)
   drum(start)
   drum(start+1)
    
# AK_UNDOG_PERC_DRUMS beat to match the background music
def drum(measure):
    makeBeat(beat1, 3, measure, "0-000-0-0----")
    
#Verse carnatic notes with percussion
def verse(clip, start, end):
    intro(clip,start,end)
    fitMedia( beat1 ,4, start, end)
    
#Voice1 and voice 2
def melody(clip1, clip2, start, end):
    fitMedia( clip1 ,5, start+2, start+3)
    fitMedia( clip2 ,5, start+3, start+4)
    fitMedia( claps,2, start+2, start+4)
    fitMedia( guitar ,4, start, end)

#Percussion playing with final high notes
def melodymix(start):
    drum(start)
    drum(start+1)

#Sets the tempo of the song to 90
setTempo(90)
#sets the volume at track 3 to Gain 4
setEffect(3, VOLUME, GAIN, 4)

# entire background
fitMedia(background, 1, 1, 29)

#Intro carnatic notes low
intro(backtrack1, 3, 5)

#Verse carnatic notes low with percussion
verse(backtrack1, 5, 7)

#Voice1 and voice 2
melody(poet1,poet2,7,11)

#Verse carnatic notes medium 
verse(backtrack2, 11, 13)

#Voice2 and voice 1
melody(poet2,poet1,13,17)

#Carnatic notes bridging melody to ending
fitMedia(backtrack3, 3, 17, 19.1)

#Percussion playing with final high notes
melodymix(23)

#Bridge(backtrack3) plus final climax
fitMedia(backtrack4, 4, 17, 25.5)

#Low notes while high is playing (octaves)
fitMedia(backtrack1, 2, 23, 27)
setEffect(2, VOLUME, GAIN, -10, 23, -20, 27)

#A fast-paced beat for an ultimate ending
fitMedia(beat2, 5, 21,28)

#Using the GeoShred App to create a suitable ending
fitMedia(trackEnd, 6, 23, 30.25)
setEffect(6, VOLUME, GAIN, -8, 23, -20, 30.25)

