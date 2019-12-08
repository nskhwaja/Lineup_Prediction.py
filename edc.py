import collections

lineups = {
2015: '''
12th Planet
3LAU
4B
A-lusion
Aaron Jackson
Above & Beyond
AC Slater
Adrenalize
Adventure Club
Afrojack
Alesso
Alex Kidd
Alison Wonderland
Aly & Fila
Amine Edge & DANCE
Andrew Rayel
Andy C
Angerfist
Armanni Reign
Armin van Buuren
Art Department
Arty
Astrix
ATB
Audien
Audiotricz
Avicii
AWE
Baggi Begovic
Bassnectar
Benny Benassi
Bingo Players
Bixel Boys
Black Sun Empire
Bones
Breach
Breathe Carolina
Brennan Heart
Brillz
Burn Unit
Calvin Harris
Camo & Krooked
Carl Cox
Carnage
Catz ‘N Dogz
Chris Liebing
Chris Lorenzo
Chuckie
Cookie Monsta
Coone
Cosmic Gate
Crisis Era
Crizzly
D-Block & S-te-Fan
Da Tweekaz
Dada Life
Dannic
Danny Avila
Darksiderz
Darren Styles
Dash Berlin
Datsik
Definitive
Deorro
Dieselboy
Dimitri From Paris
Dimitri Vegas & Like Mike
Disclosure
DJ EZ
DJ Jazzy Jeff
DJ Snake
Dom Dolla
Dr. Fresch
Dubfire
Duke Dumont
Dusky
Dyro
Dzeko & Torres
Eats Everything
Ed Rush & Optical
EDX
Enei
Eptic
Eric Prydz
Excision
Fallen
Fatboy Slim
Ferry Corsten
Firebeatz
Flosstradamus
Flume
Flux Pavilion
Foreign Concept
Freedom Fighters
Friction
FuntCase
Galantis
Get Real (Green Velvet & Claude VonStroke)
Getter
Gladiator
Graham Funke
Grandtheft
Habstrakt
Hardwell
Hook N Sling
Hotel Garuda
Ilan Bluestone
Isaac
Jack Beats
Jackal
Jason Bentley
Javi Row
John Digweed
Jon Rundell
Justin Martin
Kaskade
Kasra
Kastle
Kayzo
Kennedy Jones
Keys N Krates
Kicks N Licks
Kidnap Kid
Kiesza
Kove
Krewella
Kry Wolf
Lady Faith
Laidback Luke
Laxx
Leiel
LNY TNZ
Loco Dice
Lookas
Loudpvck
Low Steppa
Mako
Mark Knight
Markus Schulz
Martin Garrix
Martin Solveig
Metrik
MitiS
Moby
Motez
MOTi
Myon & Shane 54
Neelix
NGHTMRE
Nicky Romero
Noisia
Oliver Heldens
Ookay
Orjan Nilsen
Pan-Pot
Party Favor
Petey Clicks
Popeska
Posso
Pretty Lights
Protohype
Psyko Punkz
Pulsatorz
Ran-D
ROYL
Saeed Younan
Sander van Doorn
Sasha
Seven Lions
Showtek
Sigma
Sinden
SKisM
Slander
Snails
Speaker of the House
State of Mind
Steve Angello
Sunnery James & Ryan Marciano
TC
Technoboy
The Upbeats
Thomas Gold
Tiesto
TNT
Tokimonsta
Tommy Trash
Trent Cantrelle
TrollPhace
Troy Kurtz
Tuneboy
Umek
Vena Cava
Victor Calderone
Wilkinson
Wuki
Yellow Claw
Z-Trip
Zomboy
''',
2016: '''
12th Planet
219 Boys
4B
50 Carrot b2b Coffi
b2b Soloman
A-Trak
Above & Beyond
Ace Ventura
Adam Beyer
presents Drumcode
Adaro
Adrenalize
Adventure Club
Afrojack
Alan Fitzpatrick
Alesso
Alison Wonderland
Aly & Fila
Amtrac
Andy C
Anevo
Angerfist
Anna Lunoe
Armand Van Helden
Armanni Reign
Armin van Buuren
Aryay
Astrix
Astronomar
Audio b2b Teddy Killerz
Audiofreq
Audiotistic Stage
Audiotricz
AWE
Axwell Λ Ingrosso
Bad Boy Bill
Bad Company UK
Baggi
Bart Skils
Basscon
Bassrush Experience
Baumer
Ben Nicky
Billy Kenny
Bioweapon
BONES
Bot
Botnek
Brad Moontribe
Brennan Heart
Brennen Grey
Brian Seed (DJ Brian)
Brillz
Bro Safari
Brookes Brothers
Carnage
Caspa b2b Rusko
Chadwick
Chris Lake
Chris Liebing
Chris Lorenzo
Code Black
Cookie Monsta
Coone
Coyote Kisses
Craig WIlliams
Crisis Era
Crizzly
Culture Shock
Cyantific
D-Block & S-te-fan
Da Tweekaz
Dada Life
Danny Howard
Darksiderz
Darren Styles
Dash Berlin
Datsik
dela Moontribe
Delta Heavy
Dem Ham Boyz
Deorro
Derrick May
Des McMahon
Digital Punk
Dimension
Dimitri Vegas & Like Mike
Discovery Project
DJ Dan
DJ Isaac
DJ Snake
DJ Trance
Doc Martin
Doctor P
Don Diablo
Dreamstate Presents
Dr. Fresch
Duke Dumont
Dusky
El Dusty
Ephwurd
Eptic b2b Must Die!
Eric Prydz
Etnik
Excision
Fallen
Ferry Corsten presents Gouryella
Fester
Filthy Gorgeous
Flux Pavilion
Frankee b2b Loadstar
Frankie Bones
FuntCase
Fury
Gaia
Galantis
Gammer
Gareth Emery
Giraffage
Gladiator
Go Freek
GTA
Gunz For Hire
Habstrakt
Habu
Hannah Wants
Hardwell
Hermitude
Hot Since 82
Hotel Garuda
InsideInfo
J.Phlip
Jason Bentley
Jauz
John Askew
John Kelley
John O’Callaghan
Jordan Suckley
Joyryde
JSTJR
Juan Atkins
Julia Govor
Julian Jordan
Kaskade
Kasra
KDrew
Knife Party
KRNE
KSHMR
Kutski
Lady Faith
Landis LaPace
Lane 8
Leiel
Lenny Dee
Lione
LNY TNZ
Loco Dice
LondonBridge
Lookas
Loudpvck
LUMBERJVCK
Machete & Friends
MAKJ
Mark Farina
Markus Schulz
Marshmello
Martin Garrix
Martin Solveig
Matrix & Futurebound
Matt Black
Max Enforcer
Maximono
Maya Jane Coles
MC Dino
Mefjus
Mekanikal
Mercer
Michael Calfan
Mike Williams
Morten
My Digital Enemy
NGHTMRE
Nicole Moudaber
Nightstalker
Oliver Heldens
Ookay
Pan-Pot
Paper Diamond
Party Favor
Paul Oakenfold
Paul Ritch (Live)
Paul van Dyk
Pendulum
(DJ Set) w/ MC Verse
Pierce Fulton
Pilo
Protohype
Radical Redemption
Ran-D
Ravell
Redlight
Rell The Soundbender
Richie Hawtin
RL Grime
Rob Gee
Ron D Core
Sacha Robotti
SAYMYNAME
Seven Lions
Shaun Frank
Shiba San
Slander
Sleepy Tom
Sluggers
Snails
SNBRN
Sonny Fodera
Stephanie
Steve Loria
Stööki Sound
Suspect 44
Sylence
Taiki Nulight
Technoboy
The Chainsmokers
The Magician
The Prototypes
Thee-O
Throttle
Tiesto
TJR
TNT
Tom & Collins
Tommy Trash
Totally Enormous Extinct Dinosaurs
(DJ Set) b2b Jonas Rathsman
TrollPhace b2b P0gman
TroyBoi
Tuneboy
Two Fresh
Tycho DJ Set
UMEK
Valentino Khan
W&W
Walker & Royce
Wasted Penguinz
What So Not
Wuki
Yellow Claw
Zander
Zedd
Zomboy
''',
2017: '''
AAZAR
Above & Beyond
Ace Ventura
Adam Beyer Presents Drumcode
Afrojack
Alan Fitzpatrick
Alan Walker
Alesso
Alison Wonderland
Aly & Fila
Andrew Luce
Andrew Rayel
Andy C
ANGELZ
Angerfist
Armani Reign
Armin van Buuren
Astrix
Astronomar
ATB
ATICA
Atmozfears
Audien b2b 3LAU
Audiofreq
Autograf
Axwell ^ Ingrosso
Baggi
Barely Alive
Ben Nicky
Bijou
Billy Kenny
Bix King
Black Sun Empire
Black Tiger Sex Machine
BlackGummy
Blazer
Bleep Bloop
Bonnie X Clyde
Boombox Cartel
BORGORE
Born Dirty
Breeazy
Brennan Heart
Brennen Grey
Bro Safari
Brownies & Lemonade
Bryan Kearney
Calyx & Teebee
Camo & Krooked
Chase & Status (DJ Set)
Chet Porter
Chris Liebing
CID
Code Black
Coone
Corporate Slackers
Cosmic Gate
Craig Williams
Crisis Era
Cristoph
Cut Snake
D-Block & S-te-fan
Da Tweekaz
Danny Howard
Darksiderz
Datsik
Dena Amy
Dense & Pika
Des McMahon
Desert Hearts
Devoted To God
Dillon Francis
Diplo
Dirtyphonics
Discovery Project
DJ Isaac
DJ Khaled
Dj Tennis
Dombresky
Don Diablo
Dubloadz
Duke Dumont
Ed Rush & Optical
Ephwurd
Excision
Fallen
Ferry Corsten
Firebeatz
Flosstradamus
Flux Pavilion
Fred V & Grafix
Freedom Fighters
Friction
Frontliner
Fury
G Jones
Galantis
Gammer
Gareth Emery
Getter
Ghastly
Gramatik
Green Velvet
GRiZ
Gryffin
GTA
Gunz For Hire
Habstrakt
Happi
Hardwell
Hazen
Herobust
illenium
Infected Mushroom (DJ Set)
Jamie Jones Presents Paradise
Jauz
Jayceeoh
John Askew
John Digweed
John O’Callaghan
Jonas Blue
Joseph Capriati
JOYRYDE
JSTJR
Junkie Kid
K?D
Kungs
Kygo
Lady Faith
Laidback Luke
Lee Foss
Liquid Soul
Liquid Stranger
LNY TNZ
LO’99
Lost Frequencies
Louis the Child
Low Steppa
Mad Dog b2b DJ AniMe
Madeon
Major Lazer
Marco Faraone
Markus Schulz Presents Dakota
MaRLo
Marshmello
Martin Garrix
Martin Solveig
Maximono
MC Dino
Megalodon b2b Midnight Tyrannosaurus
Metrik
Metro Boomin
Mija
Miss K8
Monster Cat
Moon Boots
Mr. Carmack
Nathan Barato
Nebbra
NGHTMRE
Nicole Moudaber Presents MoodZone
Nightstalker
Niko Zografos
No Requests
NOA
Noisecontrollers
Nuclyea
NVOY
Oliver Heldens
Ookay
Pan-Pot
Paul Oakenfold
Paul van Dyk
Paul Woolford
Paz
Phace
Phiso b2b Ponicz
Porter Robinson
Prolix
The Prophet
Psytribe
PureNRG (Giuseppe Ottaviani & Solarstone)
Purple Haze
Quix
Radical Redemption
Ravell
Reid Speed
REZZ
RL Grime
Rockwell
Ruben De Ronde
RUFUS DU SOL
Ruthless
Sacha Robotti
Sage Armstrong
San Holo
Sean Tyas
Seven Lions
Shaun Frank
Shmitty
Showtek
Simon Patterson
Sinden
SkisM b2b Trampa
Slander
Slushii
Snails
Solardo
SoothSlayer
Space Jesus
TC
Tiesto
Los Tíoz: Noizekid & Jay Silva
TNT
Tommy Trash
Toneshifterz
Trap Nation
Treasure Fingers
Trippy Turtle
The Upbeats
Valentino Khan
Vini Vici
Virtual Riot
W&W
WAIO
Wasted Penguinz
Wildstylez
Wilkinson
Will Atkinson
Will Clarke
Will Sparks
Yellow Claw
Zatox
Zedd
Zomboy
''',

2018: '''
12th Planet b2b Kill The Noise
4B
A-Trak
AC Slater
ADIN
Adrenalize
Adriatique
AFK b2b SVDDEN DEATH
Afrojack
Alan Walker
Alpha 9
Andrew Bayer
Andy C
Angerfist
Animato
AniMe b2b Mad Dog
Arkham Knights
Armin Van Buuren
Astrix
ATB
Atmozfears
Avalon
Big Wild
BIJOU
The Binches
Black Tiger Sex Machine
BlackGummy
Blankface b2b Maze b2b BloodThinnerz b2b Definitive
Blastoyz
Boogie T b2b Squnto
Borgeous
Borgore
Born Dirty
Boys Noize
Brennan Heart
Calyx & Teebee b2b Break
Carmada
Caspa
Charlie
Charlotte de Witte
Cheat Codes
Chris Lake
Chris Lorenzo
Christofi
Cirez D
Claude VonStroke
Code Black
Cold Blue
Conrank
Coone
Cosmic Gate
Crankdat b2b Dirty Audio
Crime Family
Da Tweekaz
Dabin
Darksiderz b2b Mekanikal
Darren Styles
Dash Berlin
Dateless
Datsik
Detlef
Digital Punk
Dimitri Vegas & Like Mike
Diplo
Dirt Monkey
DJ Hype b2b Hazard
DJ Isaac
DJ Mustard
DJ Stephanie b2b Lady Faith
Dombresky
Don Diablo
Dr. Fresch
Dr Phunk
Dr. Rude
DROELOE
Drumsound & Bassline Smith b2b Tantrum Desire
Dubloadz b2b Monxx
Ekali
Elephante
Eptic
Eric Prydz
Excision
Ferry Corsten
Firebeatz vs DubVision
Fisher
Flux Pavilion b2b Doctor P
Fury b2b Fallen
G Jones b2b Eprom
Gabriel & Dresden
Gammer
Ganesh
Genix b2b Sunny Lax
Gentlemen’s Club
Getter
GG Magree
Gorgon City
GRAVEDGR
Green Velvet Presents La La Land
Griffin Stoller
Grum
Gryffin (DJ Set)
GTA
Gud Vibrations
Habstrakt
Hardwell
Headhunterz
HEKLER
Herobust
Honey Soundsystem
Hot Since 82
Ilan Bluestone
Illenium
Ivy Lab
Jace Mek
Jack Beats
Jai Wolf
Jamie Jones Presents Paradise
Jason Ross
Jauz
Jessica Audiffred
John 00 Fleming
John Digweed
Jordan Suckley Presents 3FECT
JOYRYDE
JSTJR
Junkie Kid
K?D
Kaskade
Kayzo
Keiji
Khalid
KITTENS
KSHMR
Kygo
Latmun
Lauren Lane
Lee Foss
Loadstar b2b Mind Vortex
Loco Dice
London On Da Track
Lost Frequencies
LOUDPVCK
Maceo Plex
Mariana BO
Markus Schulz
Marshmello
Martin Garrix
Master of The People
Matt Medved
MC DINO
Melé
Mija
Mike WiLL Made-It
Mister Blaqk
MK
Moksi
NGHTMRE
Nightstalker b2b SOOTHSLAYER
Notorius Two
Oliver Smith
Omair
Ookay (Live)
Parker
Paul Van Dyk
Paul Woolford
Pendulum (DJ Set)
Pulsatorz
R3HAB
Redlight
Rell The Soundbender b2b Rawtek
REZZ
Robotaki
Roger Shah (Live)
Sage Armstrong
Sam Jones
San Holo
SayMyName
Seven Lions
Shiba San
Shimon b2b Benny L
Shmitty b2b No Requests
Sinden b2b LO’99
Slander
SLATIN
Slushii
Snails
SNAVS
Solardo b2b CamelPhat
Space Jesus
spaceprodigi
Spag Heddy
Spencer Brown
Strange Club
Suae
Sub Zero Project
Subset
Tchami x Malaa [No Redemption]
The Pitcher
The Prototypes b2b TC
Tiesto
TNT aka Technoboy ‘N’ Tuneboy
Toneshifterz
Vini Vici
Virtual Self
VOLAC
Warface
Wasted Penguinz
Whethan
Will Clarke
Wongo
XIE
Yellow Claw
Yheti b2b Toadface
YOOKiE
Yultron
Yuuki Yoshiyama
Zedd
Zeds Dead
Zeke Beats
Zomboy
''',

2019: '''
13
4B
A.M.C + TURNO
A$AP ROCKY
ABOVE & BEYOND
ADAM BEYER PRESENTS DRUMCODE
ADARO
ADIN
ADRENALIZE
ADVENTURE CLUB
ALAN FITZPATRICK
ALESSO
ALISON WONDERLAND
ALY & FILA
AMELIE LENS
ANDREW BAYER
ANDREW RAYEL
ANDY C
ANGERFIST
ANNA
ARKHAM KNIGHTS
ARMIN VAN BUUREN
ARMNHMR
ARTBAT
ATMOZFEARS
ATTLAS B2B RHETT
AUDIEN
BADKLAAT
BARELY ALIVE B2B PHASEONE
BASS MODULATORS
BENDA
BIJOU
BILL NYE (OPENING CEREMONY)
BLACK COFFEE
BLACK TIGER SEX MACHINE
BLACKLIZT
BONNIE X CLYDE
BOOMBOX CARTEL
BORN DIRTY
BRENNAN HEART
BROWNIES & LEMONADE ALL STARS
BRUNO MARTINI
BRYAN KEARNEY
CALLIE REIFF
CAMELPHAT
CAMELPHAT
CAMELPHAT B2B GORGON CITY (KINETIC FIELD)
CAPTIAN HOOK
CARTA B2B YAKO
CASH CASH
CHARLOTTE DE WITTE
CHRIS LAKE
CHRIS LAKE PRESENTS BLACK BOOK
CHRIS LORENZO
CLAUDE VONSTROKE
CONSOULS B2B NIGHTSTALKER
COSMIC GATE
CRAIG CONNELLY
CRIME FAMILY
CUT SNAKE
DA TWEEKAZ
DACK JANIELS
DANNY BYRD B2B RENE LAVICE
DARREN STYLES
DAVID GRAVELL
DAVID GUETTA
DEADMAU5
DECLAN JAMES
DELTA HEAVY B2B DIRTYPHONICS
DEORRO
DIESELBOY
DILLON FRANCIS
DILLON NATHANIEL
DIMENSION B2B CULTURE SHOCK
DION TIMMER
DIPLO
DJ ISAAC
DJ THE PROPHET
DNMO
DOM DOLLA
DON DIABLO
DR PHUNK
DREZO
DUCKY (LIVE)
DUSTYCLOUD
EATS EVERYTHING B2B PATRICK TOPPING
EKALI
ELEPHANTE
ELI BROWN B2B MASON MAYNARD
ENRICO SANGIULIANO
ERIC PRYDZ
EXCISION
FALLEN B2B FURY
FERRY CORSTEN PRESENTS SYSTEM F
FISHER
FRICTION B2B METRIK
FUNTCASE
GANESH
GANJA WHITE NIGHT
GARETH EMERY
GENTECH (MARK SHERRY & SCOT PROJECT)
GENTLEMENS CLUB
GEO
GET REAL; GREEN VELVET & CLAUDE VONSTROKE
GHASTLY
GIUSEPPE OTTAVIANI LIVE 2.0
GORGON CITY (LIVE)
GREEN VELVET PRESENTS LA LA LAND
GUNZ FOR HIRE
HEKLER
HOLY GOOF
I_O
ILLENIUM
INFECTED MUSHROOM
JAMIE JONES
JASE THIRLWALL
JOHN ASKEW
JOHN O'CALLAGHAN
JOSEPH CAPRIATI
JOYRYDE
JSTJR
JUSTIN MARTIN
KAIWACHI
KASKADE
KAYZO
KENDOLL
KIKEONE
LADY FAITH
LAYTON GIORDANI B2B BART SKILS
LEIEL (Quantum Valley)
LILTEXAS
LIQUID STRANGER
LNY TNZ
LOUD LUXURY
LUCATI
MADGRRL
MALAA
MARK SIXMA
MARLO
MARTIN GARRIX
MATRIX & FUTUREBOUND B2B CYANTIFIC
MAU5TRAP
MC DINO
MEDASIN
MELE
MIHALIS SAFRAS
MONSTERGETODWN B2B RHYNO
MORELIA
NERO (DJ SET)
NGHTMRE
NIKO ZOGRAFOS
NITTI GRITTI
NO MANA
NOFONE
NOIZU
OOLACILE
PARTY FAVOR
PAUL DENTON
PAUL OAKENFOLD
PAUL VAN DYK
PHISO B2B DEFINITIVE
QUIX
RADICAL REDEMPTION
RAITO
RAN-D
RAWTEK
RED LIGHT
REZZ
RICK TRAINOR
RINZEN B2B MATT LANGE
RIOT TEN
RJ VAN XETTEN
RL GRIME
ROB GEE
RUBEN DE RONDE
SALVATORE GANACCI
SAN HOLO
SANDER VAN DOORN PRESENTS PURPLE HAZE
SAYMYNAME
SEFA
SIAN
SINOPOLI
SKREAM! B2B RUSKO (OLD SKOOL DUBSTEP SET)
SLANDER
SNAILS
SNAKEHIPS
SOLARDO B2B IDRIS ELBA
SPACE CORPS
STEVE AOKI
SUAE
SUB FOCUS B2B WILKINSON
SUB ZERO PROJECT
SVDDEN DEATH
SYLENCE
TAILS
TCHAMI X MALAA
TECHNOBOY
THE GLITCH MOB
THE MARTINEZ BROTHERS
TIESTO
TIMMY TRUMPET
TISOKI
TOKIMONSTA
TRITONAL
TSURUDA B2B GREAT DANE
TUNEBOY
TWEEKACORE
VALENTINO KHAN
VIRTUAL RIOT
VNSSA
VOLAC
VRTL VRS: VRTL DYNSTY LIVE
W&W
WALKER & ROYCE
WARFACE
WASTED PENGUINZ
WAVEDASH
WHAT SO NOT
WHIPPED CREAM
YOLANDA BE COOL
YOUSEF
YULTRON
ZAXX
ZEDS DEAD
ZEKE BEATS B2B CHAMPAGNE DRIP
ZHU
'''}

artists = collections.defaultdict(lambda: set())

for year, lineup in lineups.items():
	lineup = lineup.strip()
	lineup = lineup.lower()
	lineup = lineup.replace(' & ', '\n')
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
