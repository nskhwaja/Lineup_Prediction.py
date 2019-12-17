import collections

lineups = {
2015: '''
Baggi
Carnage
Discovery Project
DJ Snake
Flux Pavilion
Kaskade
Mercer
Pierce Fulton
Yellow Claw
Alison Wonderland
Discovery Project
Oliver Heldens
Rustie(?)
Sleepy Tom
TJR
Trippy Turtle
What So Not
Cookie Monsta b2b Funtcase
Cyantific b2b Mob Tactics b2b Inside Info
Delta Heavy
Eptic b2b Habstrakt
Fallen
Megalodon b2b Truth
Metrik b2b TC
Minnesota b2b G Jones
Nightstalker
''',
2016: '''
Alison Wonderland
Baggi
BASSRUSH Experience
Carnage
Cookie Monsta b2b Funtcase
Cyantific b2b Insideinfo b2b Mob Tactics
Delta Heavy
Discovery Project
DJ Snake
Eptic b2b Habstrakt
Fallen + MC Dino
Flux Pavilion
HI-LO
Kaskade
Mercer
Metrik b2b TC
Minnesota b2b G Jones
Nightstalker
Pierce Fulton
Sleepy Tom
TJR
Trippy Turtle
Truth b2b Megalodon
What So Not
Yellow Claw
''',
2017: '''
4b
Bassrush Experience
Borgore
Born Dirty
BROHUG
Conrank
Datsik
Deadmau5
Devault
Dieselboy
Dimension
Diplo
Discovery Project
DJ Mustard
Dombresky
ETC!ETC! B2b JSJTR
Flosstradamus
Flux Pavilion
Funtcase
G Jones
Infekt
JAI wolf
Jauz b2b Zeds Dead
Joyryde
Kai Wachi
Kasra b2b Ivy Lab b2b Emperor
Kayoh
MC Dino
Melvv
Mercer
Monxx B2B Pogman
Noisia
Parker
Porter Robinson
Shiba San
Spag Heddy
Two Owls
W&W
What So Not
Wongo
Yellow Claw
''',
2018: '''
Adam Auburn
Afrojack
Alison Wonderland
Andrew Rayel
Camelphat
CID
Dillon Francis
Dion Timmer
Friction
GG Magree
Graves
Lisbona Sisters
Loud Luxury
Loudpvck
Omnom
Party Favor
The Prototypes
RL Grime
Sage Armstrong b2b Bruno Furlan
Shiba San
Shlump
Snails
Solardo
Tiesto
Xie
Yultron
Zedd
Zeke Beats b2b Champagne Drip
Zomboy
''',
2019: '''
12th Planet
Alesso
ATLiens
Bassrush
Blunts N Blondes
Borgore
The Chainsmokers
Chris Lorenzo
CID
Codes
David Steven
Discovery Project
Dombresky
Dr Fresch
Elephante
Eliminate
ETC!ETC!
Franklyn Watts b2b Steady Rock
Galantis
Gentlemens Club
Gryffin (DJ Set)
Insomniac Records
Jai Wolf (DJ Set)
JSTJTR
Lost Kings
Luke Andy
Metric b2b Tk
Nitti Gritti
Noizu
Oliver Heldens
Porter Robinson (DJ Set)
Raiser
Richter b2b Fallen x MC Dino
Said the Sky
Saymyname
Svdden Death Presents Voyd
Tisoki
Tom & Collins
VNSSA
 '''}



artists = collections.defaultdict(lambda: set())

for year, lineup in lineups.items():
	lineup = lineup.strip()
	lineup = lineup.lower()
	lineup = lineup.replace(' & ', '\n')
    #lineup = lineup.replace(' ! ', '\n')
	lineup = lineup.replace(' x ', '\n')
	lineup = lineup.replace(' b2b ', '\n')
	lineup = lineup.replace(' aka ', '\n')
	lineup = lineup.replace('(dj set)', '')

	lineup = lineup.splitlines()
	lineups[year] = set(lineup)

	for artist in lineup:
		artists[artist].add(year)

def years_played(artist):
	return len(artists[artist])

for artist in sorted(artists, key=years_played, reverse=True):
	years = sorted(artists[artist])
	num_years = len(years)
	years = ', '.join(map(str, years))

	print ('%-15s (%s) %s' % (artist, num_years, years))
