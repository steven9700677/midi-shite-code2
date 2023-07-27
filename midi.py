from mido import MidiFile
import numpy as np
import shutil
import csv
import py_midicsv as pm
import inspect
np.set_printoptions(threshold=np.inf)

mid_name = input("Enter the name of the MIDI file (excluding .mid): ")
midi_file_path = f"{mid_name}.mid"

mid = MidiFile(midi_file_path, clip=True)
csv_string = pm.midi_to_csv(midi_file_path)
csv_string2 = pm.midi_to_csv(midi_file_path)
with open(f"{mid_name}_converted.csv", "w") as f:
    f.writelines(csv_string)

with open(f"{mid_name}_converted_og.csv", "w") as f:
    f.writelines(csv_string2)


midi_object = pm.csv_to_midi(csv_string)
midi_object2 = pm.csv_to_midi(csv_string2)
with open(f"{mid_name}_converted(og).mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)
with open(f"{mid_name}_converted_og.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object2)
    
# Initialize an empty list
notes = []

# Open the CSV file in read mode
with open(f"{mid_name}_converted.csv", 'r') as file:
    # Read the CSV content
    reader = csv.reader(file)
    csv_data = list(reader)

    # Define the values you want to search for
    search_value = ' Note_on_c'
    search_value2 = ' Note_off_c'

    # Iterate over each row in the CSV data
    for row_index, row in enumerate(csv_data):
        # Iterate over each cell in the row
        for cell in row:
            # Check if the cell contains the search value
            if cell == search_value:
                # Print the row and column index of the cell
                column_index = row.index(cell) + 2
                #print(f"Found at row {row_index}, column {column_index}")

                looked_up_value = csv_data[row_index][column_index]
                notes.append([looked_up_value])
                #print(notes)

            if cell == search_value2:
                # Print the row and column index of the cell
                column_index = row.index(cell) + 2
                #print(f"Found at row {row_index}, column {column_index}")

                looked_up_value = csv_data[row_index][column_index]
                notes.append([looked_up_value])
                #print(notes)

# Convert the list to a NumPy array
notes = np.array(notes, dtype=object).astype(int)


g=(0)
fss=(0)
f=(0)
e=(0)
dss=(0)
d=(0)
css=(0)
c=(0)
b=(0)
ass=(0)
a=(0)
gss=(0)            

ag=np.array([115,103,91,79,67,55,43,31])
afss=np.array([114,102,90,78,66,54,42,30])
af=np.array([113,101,89,77,65,53,41,29])
ae=np.array([112,100,88,76,64,52,40,28])
adss=np.array([111,99,87,75,63,51,39,27])
ad=np.array([110,98,86,74,62,50,38,26])
acss=np.array([109,97,85,73,61,49,37,25])
ac=np.array([108,96,84,72,60,48,36,24])
ab=np.array([107,95,83,71,59,47,35,23])
aass=np.array([106,94,82,70,58,46,34,22])
aa=np.array([105,93,81,69,57,45,33,21])
agss=np.array([116,104,92,80,68,56,44,32])

aallnotes=np.array([ag,afss, af, ae, adss, ad, acss, ac, ab, aass, aa, agss, ], dtype=object)

g = notes[np.isin(notes, ag)]
fss = notes[np.isin(notes, afss)]
f = notes[np.isin(notes, af)]
e = notes[np.isin(notes, ae)]
dss = notes[np.isin(notes, adss)]
d = notes[np.isin(notes, ad)]
css = notes[np.isin(notes, acss)]
c = notes[np.isin(notes, ac)]
b = notes[np.isin(notes, ab)]
ass = notes[np.isin(notes, aass)]
a = notes[np.isin(notes, aa)]
gss = notes[np.isin(notes, agss)]

max_length = max(len(g), len(fss), len(f), len(e), len(dss), len(d), len(css), len(c), len(b), len(ass), len(a), len(gss))
g = np.pad(g, (0, max_length - len(g)), mode='constant')
fss = np.pad(fss, (0, max_length - len(fss)), mode='constant')
f = np.pad(f, (0, max_length - len(f)), mode='constant')
e = np.pad(e, (0, max_length - len(e)), mode='constant')
dss = np.pad(dss, (0, max_length - len(dss)), mode='constant')
d = np.pad(d, (0, max_length - len(d)), mode='constant')
css = np.pad(css, (0, max_length - len(css)), mode='constant')
c = np.pad(c, (0, max_length - len(c)), mode='constant')
b = np.pad(b, (0, max_length - len(b)), mode='constant')
ass = np.pad(ass, (0, max_length - len(ass)), mode='constant')
a = np.pad(a, (0, max_length - len(a)), mode='constant')
gss = np.pad(gss, (0, max_length - len(gss)), mode='constant')
g=g[0]
fss =fss[0]
f =f[0]
e =e[0]
dss =dss[0]
d =d[0]
css =css[0]
c =c[0]
b =b[0]
ass =ass[0]
a =a[0]
gss =gss[0]


allnotes = np.array([g, fss, f, e, dss, d, css, c, b, ass, a, gss], dtype=object)

lowest_positive = np.min(allnotes[allnotes > 0])

#if g==0:
nearest_index = np.argmin(np.abs(ag - lowest_positive))
nearest_number = ag[nearest_index]
g=nearest_number
#if gss==0:
nearest_index = np.argmin(np.abs(agss - lowest_positive))
nearest_number = agss[nearest_index]
gss=nearest_number
#if a==0:
nearest_index = np.argmin(np.abs(aa - lowest_positive))
nearest_number = aa[nearest_index]
a=nearest_number
#if ass==0:
nearest_index = np.argmin(np.abs(aass - lowest_positive))
nearest_number = aass[nearest_index]
ass=nearest_number
#if b==0:
nearest_index = np.argmin(np.abs(ab - lowest_positive))
nearest_number = ab[nearest_index]
b=nearest_number
#if c==0:
nearest_index = np.argmin(np.abs(ac - lowest_positive))
nearest_number = ac[nearest_index]
c=nearest_number
#if css==0:
nearest_index = np.argmin(np.abs(acss - lowest_positive))
nearest_number = acss[nearest_index]
css=nearest_number
#if d==0:
nearest_index = np.argmin(np.abs(ad - lowest_positive))
nearest_number = ad[nearest_index]
d=nearest_number
#if dss==0:
nearest_index = np.argmin(np.abs(adss - lowest_positive))
nearest_number = adss[nearest_index]
dss=nearest_number
#if e==0:
nearest_index = np.argmin(np.abs(ae - lowest_positive))
nearest_number = ae[nearest_index]
e=nearest_number
#if f==0:
nearest_index = np.argmin(np.abs(af - lowest_positive))
nearest_number = af[nearest_index]
f=nearest_number
#if fss==0:
nearest_index = np.argmin(np.abs(afss - lowest_positive))
nearest_number = afss[nearest_index]
fss=nearest_number


g=g+12
fss=fss+12
f=f+12
e=e+12
dss=dss+12
d=d+12
css=css+12
c=c+12
b=b+12
ass=ass+12
a=a+12
gss=gss+12

allnotes = np.array([g, fss, f, e, dss, d, css, c, b, ass, a, gss], dtype=object)
allnotesnames3 = np.array(["g", "fss", "f", "e", "dss", "d", "css", "c", "b", "ass", "a", "gss"], dtype=object)

#conversions
convc=np.array([c	,	b	,	ass	,	a	,	gss	,	g	,	fss	,	f	,	e	,	dss	,	d	,	css
], dtype=object)
convcss=np.array([d	,	css	,	c	,	b	,	ass	,	a	,	gss	,	g	,	fss	,	f	,	e	,	dss
], dtype=object)
convd=np.array([e	,	dss	,	d	,	css	,	c	,	b	,	ass	,	a	,	gss	,	g	,	fss	,	f
], dtype=object)
convdss=np.array([fss	,	f	,	e	,	dss	,	d	,	css	,	c	,	b	,	ass	,	a	,	gss	,	g
], dtype=object)
conve=np.array([gss	,	g	,	fss	,	f	,	e	,	dss	,	d	,	css	,	c	,	b	,	ass	,	a
], dtype=object)
convf=np.array([ass	,	a	,	gss	,	g	,	fss	,	f	,	e	,	dss	,	d	,	css	,	c	,	b
], dtype=object)
convdssle=np.array([g	,	fss	,	f	,	e	,	dss	,	d	,	css	,	c	,	b	,	ass	,	a	,	gss
], dtype=object)
convelf=np.array([a	,	gss	,	g	,	fss	,	f	,	e	,	dss	,	d	,	css	,	c	,	b	,	ass
], dtype=object)
convflfss=np.array([b	,	ass	,	a	,	gss	,	g	,	fss	,	f	,	e	,	dss	,	d	,	css	,	c
], dtype=object)
convfsslg=np.array([css	,	c	,	b	,	ass	,	a	,	gss	,	g	,	fss	,	f	,	e	,	dss	,	d
], dtype=object)
convglgss=np.array([dss	,	d	,	css	,	c	,	b	,	ass	,	a	,	gss	,	g	,	fss	,	f	,	e
], dtype=object)
convgssla=np.array([f	,	e	,	dss	,	d	,	css	,	c	,	b	,	ass	,	a	,	gss	,	g	,	fss
], dtype=object)

supconv=np.array([convc,convcss,convd,convdss,conve,convf,convdssle,convelf,convflfss,convfsslg,convglgss,convgssla])
supconvnum=np.array([0,2,4,6,8,10,7,9,11,1,3,5])

supconvallnotes=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)



#number value
convcnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convcssnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convdnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convdssnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convenum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convfnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convdsslenum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convelfnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convflfssnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convfsslgnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convglgssnum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
convgsslanum=np.array([c, css, d, dss, e, f, fss, g, gss, a, ass, b], dtype=object)
numg=(2)
numfss=(0)
numf=(10)
nume=(8)
numdss=(6)
numd=(4)
numcss=(2)
numc=(0)
numb=(10)
numass=(8)
numa=(6)
numgss=(4)
numnumnumnotes=np.array([numg,numfss,numf,nume,numdss,numd,numcss,numc,numb,numass,numa,numgss])
numnumnumnotesnote=np.array(["g","fss","f","e","dss","d","css","c","b","ass","a","gss"])
numper5th	=	7
numdim5th	=	6
numaug5th	=	8
nummaj3rd	=	4
nummin3rd	=	3
nummaj7th	=	11
nummin7th	=	10
numsuploc	=	0
nummodearray=np.array([numper5th,numdim5th,numaug5th,nummaj3rd,nummin3rd,nummaj7th,nummin7th,numsuploc])
#print(mode1[1,0])-1=which array,0=note in scale
####################maj
cmaj	=np.array	([	c	,	d	,	e	,	f	,	g	,	a	,	b	])
cssmaj	=np.array	([	css	,	dss	,	f	,	fss	,	gss	,	ass	,	c	])
dmaj	=np.array	([	d	,	e	,	fss	,	g	,	a	,	b	,	css	])
dssmaj	=np.array	([	dss	,	f	,	g	,	gss	,	ass	,	c	,	d	])
emaj	=np.array	([	e	,	fss	,	gss	,	a	,	b	,	css	,	dss	])
fmaj	=np.array	([	f	,	g	,	a	,	ass	,	c	,	d	,	e	])
fssmaj	=np.array	([	fss	,	gss	,	ass	,	b	,	css	,	dss	,	f	])
gmaj	=np.array	([	g	,	a	,	b	,	c	,	d	,	e	,	fss	])
gssmaj	=np.array	([	gss	,	ass	,	c	,	css	,	dss	,	f	,	g	])
amaj	=np.array	([	a	,	b	,	css	,	d	,	e	,	fss	,	gss	])
assmaj	=np.array	([	ass	,	c	,	d	,	dss	,	f	,	g	,	a	])
bmaj	=np.array	([	b	,	css	,	dss	,	e	,	fss	,	gss	,	ass	])


mode1=np.array([[	c	,	d	,	e	,	f	,	g	,	a	,	b	],[	css	,	dss	,	f	,	fss	,	gss	,	ass	,	c	],[	d	,	e	,	fss	,	g	,	a	,	b	,	css	],[	dss	,	f	,	g	,	gss	,	ass	,	c	,	d	],[	e	,	fss	,	gss	,	a	,	b	,	css	,	dss	],[	f	,	g	,	a	,	ass	,	c	,	d	,	e	],[	fss	,	gss	,	ass	,	b	,	css	,	dss	,	f	],[	g	,	a	,	b	,	c	,	d	,	e	,	fss	],[	gss	,	ass	,	c	,	css	,	dss	,	f	,	g	],[	a	,	b	,	css	,	d	,	e	,	fss	,	gss	],[	ass	,	c	,	d	,	dss	,	f	,	g	,	a	],[	b	,	css	,	dss	,	e	,	fss	,	gss	,	ass	]])

amode1=np.array([[	cmaj	],[	cssmaj	],[	dmaj	],[	dssmaj	],[	emaj	],[	fmaj	],[	fssmaj	],[	gmaj	],[	gssmaj	],[	amaj	],[	assmaj	],[	bmaj	]])

negcmaj	=np.array	([	e	,	d	,	c	,	b	,	a	,	g	,	f	])
negcssmaj	=np.array	([	f	,	dss	,	css	,	c	,	ass	,	gss	,	fss	])
negdmaj	=np.array	([	fss	,	e	,	d	,	css	,	b	,	a	,	g	])
negdssmaj	=np.array	([	g	,	f	,	dss	,	d	,	c	,	ass	,	gss	])
negemaj	=np.array	([	gss	,	fss	,	e	,	dss	,	css	,	b	,	a	])
negfmaj	=np.array	([	a	,	g	,	f	,	e	,	d	,	c	,	ass	])
negfssmaj	=np.array	([	ass	,	gss	,	fss	,	f	,	dss	,	css	,	b	])
neggmaj	=np.array	([	b	,	a	,	g	,	fss	,	e	,	d	,	c	])
neggssmaj	=np.array	([	c	,	ass	,	gss	,	g	,	f	,	dss	,	css	])
negamaj	=np.array	([	css	,	b	,	a	,	gss	,	fss	,	e	,	d	])
negassmaj	=np.array	([	d	,	c	,	ass	,	a	,	g	,	f	,	dss	])
negbmaj	=np.array	([	dss	,	css	,	b	,	ass	,	gss	,	fss	,	e	])

negmode1=np.array([[	e	,	d	,	c	,	b	,	a	,	g	,	f	],[	f	,	dss	,	css	,	c	,	ass	,	gss	,	fss	],[	fss	,	e	,	d	,	css	,	b	,	a	,	g	],[	g	,	f	,	dss	,	d	,	c	,	ass	,	gss	],[	gss	,	fss	,	e	,	dss	,	css	,	b	,	a	],[	a	,	g	,	f	,	e	,	d	,	c	,	ass	],[	ass	,	gss	,	fss	,	f	,	dss	,	css	,	b	],[	b	,	a	,	g	,	fss	,	e	,	d	,	c	],[	c	,	ass	,	gss	,	g	,	f	,	dss	,	css	],[	css	,	b	,	a	,	gss	,	fss	,	e	,	d	],[	d	,	c	,	ass	,	a	,	g	,	f	,	dss	],[	dss	,	css	,	b	,	ass	,	gss	,	fss	,	e	]])

negamode1=np.array([[	negcmaj	],[	negcssmaj	],[	negdmaj	],[	negdssmaj	],[	negemaj	],[	negfmaj	],[	negfssmaj	],[	neggmaj	],[	neggssmaj	],[	negamaj	],[	negassmaj	],[	negbmaj	]])
####################dor
cdor	=np.array	([	d	,	e	,	f	,	g	,	a	,	b	,	c	])
cssdor	=np.array	([	dss	,	f	,	fss	,	gss	,	ass	,	c	,	css	])
ddor	=np.array	([	e	,	fss	,	g	,	a	,	b	,	css	,	d	])
dssdor	=np.array	([	f	,	g	,	gss	,	ass	,	c	,	d	,	dss	])
edor	=np.array	([	fss	,	gss	,	a	,	b	,	css	,	dss	,	e	])
fdor	=np.array	([	g	,	a	,	ass	,	c	,	d	,	e	,	f	])
fssdor	=np.array	([	gss	,	ass	,	b	,	css	,	dss	,	f	,	fss	])
gdor	=np.array	([	a	,	b	,	c	,	d	,	e	,	fss	,	g	])
gssdor	=np.array	([	ass	,	c	,	css	,	dss	,	f	,	g	,	gss	])
ador	=np.array	([	b	,	css	,	d	,	e	,	fss	,	gss	,	a	])
assdor	=np.array	([	c	,	d	,	dss	,	f	,	g	,	a	,	ass	])
bdor	=np.array	([	css	,	dss	,	e	,	fss	,	gss	,	ass	,	b	])

mode2=np.array([[	d	,	e	,	f	,	g	,	a	,	b	,	c	],[	dss	,	f	,	fss	,	gss	,	ass	,	c	,	css	],[	e	,	fss	,	g	,	a	,	b	,	css	,	d	],[	f	,	g	,	gss	,	ass	,	c	,	d	,	dss	],[	fss	,	gss	,	a	,	b	,	css	,	dss	,	e	],[	g	,	a	,	ass	,	c	,	d	,	e	,	f	],[	gss	,	ass	,	b	,	css	,	dss	,	f	,	fss	],[	a	,	b	,	c	,	d	,	e	,	fss	,	g	],[	ass	,	c	,	css	,	dss	,	f	,	g	,	gss	],[	b	,	css	,	d	,	e	,	fss	,	gss	,	a	],[	c	,	d	,	dss	,	f	,	g	,	a	,	ass	],[	css	,	dss	,	e	,	fss	,	gss	,	ass	,	b	]])

amode2=np.array([[	cdor	],[	cssdor	],[	ddor	],[	dssdor	],[	edor	],[	fdor	],[	fssdor	],[	gdor	],[	gssdor	],[	ador	],[	assdor	],[	bdor	]])

negcdor	=np.array	([	d	,	c	,	b	,	a	,	g	,	f	,	e	])
negcssdor=np.array	([	dss	,	css	,	c	,	ass	,	gss	,	fss	,	f	])
negddor	=np.array	([	e	,	d	,	css	,	b	,	a	,	g	,	fss	])
negdssdor=np.array	([	f	,	dss	,	d	,	c	,	ass	,	gss	,	g	])
negedor	=np.array	([	fss	,	e	,	dss	,	css	,	b	,	a	,	gss	])
negfdor	=np.array	([	g	,	f	,	e	,	d	,	c	,	ass	,	a	])
negfssdor=np.array	([	gss	,	fss	,	f	,	dss	,	css	,	b	,	ass	])
neggdor	=np.array	([	a	,	g	,	fss	,	e	,	d	,	c	,	b	])
neggssdor=np.array	([	ass	,	gss	,	g	,	f	,	dss	,	css	,	c	])
negador	=np.array	([	b	,	a	,	gss	,	fss	,	e	,	d	,	css	])
negassdor=np.array	([	c	,	ass	,	a	,	g	,	f	,	dss	,	d	])
negbdor	=np.array	([	css	,	b	,	ass	,	gss	,	fss	,	e	,	dss	])

negmode2=np.array([[	d	,	c	,	b	,	a	,	g	,	f	,	e	],[	dss	,	css	,	c	,	ass	,	gss	,	fss	,	f	],[	e	,	d	,	css	,	b	,	a	,	g	,	fss	],[	f	,	dss	,	d	,	c	,	ass	,	gss	,	g	],[	fss	,	e	,	dss	,	css	,	b	,	a	,	gss	],[	g	,	f	,	e	,	d	,	c	,	ass	,	a	],[	gss	,	fss	,	f	,	dss	,	css	,	b	,	ass	],[	a	,	g	,	fss	,	e	,	d	,	c	,	b	],[	ass	,	gss	,	g	,	f	,	dss	,	css	,	c	],[	b	,	a	,	gss	,	fss	,	e	,	d	,	css	],[	c	,	ass	,	a	,	g	,	f	,	dss	,	d	],[	css	,	b	,	ass	,	gss	,	fss	,	e	,	dss	]])

negamode2=np.array([[	negcdor	],[	negcssdor	],[	negddor	],[	negdssdor	],[	negedor	],[	negfdor	],[	negfssdor	],[	neggdor	],[	neggssdor	],[	negador	],[	negassdor	],[	negbdor	]])

####################phr
cphr	=np.array	([	e	,	f	,	g	,	a	,	b	,	c	,	d	])
cssphr	=np.array	([	f	,	fss	,	gss	,	ass	,	c	,	css	,	dss	])
dphr	=np.array	([	fss	,	g	,	a	,	b	,	css	,	d	,	e	])
dssphr	=np.array	([	g	,	gss	,	ass	,	c	,	d	,	dss	,	f	])
ephr	=np.array	([	gss	,	a	,	b	,	css	,	dss	,	e	,	fss	])
fphr	=np.array	([	a	,	ass	,	c	,	d	,	e	,	f	,	g	])
fssphr	=np.array	([	ass	,	b	,	css	,	dss	,	f	,	fss	,	gss	])
gphr	=np.array	([	b	,	c	,	d	,	e	,	fss	,	g	,	a	])
gssphr	=np.array	([	c	,	css	,	dss	,	f	,	g	,	gss	,	ass	])
aphr	=np.array	([	css	,	d	,	e	,	fss	,	gss	,	a	,	b	])
assphr	=np.array	([	d	,	dss	,	f	,	g	,	a	,	ass	,	c	])
bphr	=np.array	([	dss	,	e	,	fss	,	gss	,	ass	,	b	,	css	])

mode3=np.array([[	e	,	f	,	g	,	a	,	b	,	c	,	d	],[	f	,	fss	,	gss	,	ass	,	c	,	css	,	dss	],[	fss	,	g	,	a	,	b	,	css	,	d	,	e	],[	g	,	gss	,	ass	,	c	,	d	,	dss	,	f	],[	gss	,	a	,	b	,	css	,	dss	,	e	,	fss	],[	a	,	ass	,	c	,	d	,	e	,	f	,	g	],[	ass	,	b	,	css	,	dss	,	f	,	fss	,	gss	],[	b	,	c	,	d	,	e	,	fss	,	g	,	a	],[	c	,	css	,	dss	,	f	,	g	,	gss	,	ass	],[	css	,	d	,	e	,	fss	,	gss	,	a	,	b	],[	d	,	dss	,	f	,	g	,	a	,	ass	,	c	],[	dss	,	e	,	fss	,	gss	,	ass	,	b	,	css	]])

amode3=np.array([[	cphr	],[	cssphr	],[	dphr	],[	dssphr	],[	ephr	],[	fphr	],[	fssphr	],[	gphr	],[	gssphr	],[	aphr	],[	assphr	],[	bphr	]])

negcphr	=np.array	([	c	,	b	,	a	,	g	,	f	,	e	,	d	])
negcssphr=np.array	([	css	,	c	,	ass	,	gss	,	fss	,	f	,	dss	])
negdphr	=np.array	([	d	,	css	,	b	,	a	,	g	,	fss	,	e	])
negdssphr=np.array	([	dss	,	d	,	c	,	ass	,	gss	,	g	,	f	])
negephr	=np.array	([	e	,	dss	,	css	,	b	,	a	,	gss	,	fss	])
negfphr	=np.array	([	f	,	e	,	d	,	c	,	ass	,	a	,	g	])
negfssphr=np.array	([	fss	,	f	,	dss	,	css	,	b	,	ass	,	gss	])
neggphr	=np.array	([	g	,	fss	,	e	,	d	,	c	,	b	,	a	])
neggssphr=np.array	([	gss	,	g	,	f	,	dss	,	css	,	c	,	ass	])
negaphr	=np.array	([	a	,	gss	,	fss	,	e	,	d	,	css	,	b	])
negassphr=np.array	([	ass	,	a	,	g	,	f	,	dss	,	d	,	c	])
negbphr	=np.array	([	b	,	ass	,	gss	,	fss	,	e	,	dss	,	css	])

negmode3=np.array([[	c	,	b	,	a	,	g	,	f	,	e	,	d	],[	css	,	c	,	ass	,	gss	,	fss	,	f	,	dss	],[	d	,	css	,	b	,	a	,	g	,	fss	,	e	],[	dss	,	d	,	c	,	ass	,	gss	,	g	,	f	],[	e	,	dss	,	css	,	b	,	a	,	gss	,	fss	],[	f	,	e	,	d	,	c	,	ass	,	a	,	g	],[	fss	,	f	,	dss	,	css	,	b	,	ass	,	gss	],[	g	,	fss	,	e	,	d	,	c	,	b	,	a	],[	gss	,	g	,	f	,	dss	,	css	,	c	,	ass	],[	a	,	gss	,	fss	,	e	,	d	,	css	,	b	],[	ass	,	a	,	g	,	f	,	dss	,	d	,	c	],[	b	,	ass	,	gss	,	fss	,	e	,	dss	,	css	]])

negamode3=np.array([[	negcphr	],[	negcssphr	],[	negdphr	],[	negdssphr	],[	negephr	],[	negfphr	],[	negfssphr	],[	neggphr	],[	neggssphr	],[	negaphr	],[	negassphr	],[	negbphr	]])

####################mix
cmix	=np.array	([	f	,	g	,	a	,	b	,	c	,	d	,	e	])
cssmix	=np.array	([	fss	,	gss	,	ass	,	c	,	css	,	dss	,	f	])
dmix	=np.array	([	g	,	a	,	b	,	css	,	d	,	e	,	fss	])
dssmix	=np.array	([	gss	,	ass	,	c	,	d	,	dss	,	f	,	g	])
emix	=np.array	([	a	,	b	,	css	,	dss	,	e	,	fss	,	gss	])
fmix	=np.array	([	ass	,	c	,	d	,	e	,	f	,	g	,	a	])
fssmix	=np.array	([	b	,	css	,	dss	,	f	,	fss	,	gss	,	ass	])
gmix	=np.array	([	c	,	d	,	e	,	fss	,	g	,	a	,	b	])
gssmix	=np.array	([	css	,	dss	,	f	,	g	,	gss	,	ass	,	c	])
amix	=np.array	([	d	,	e	,	fss	,	gss	,	a	,	b	,	css	])
assmix	=np.array	([	dss	,	f	,	g	,	a	,	ass	,	c	,	d	])
bmix	=np.array	([	e	,	fss	,	gss	,	ass	,	b	,	css	,	dss	])

mode4=np.array([[	f	,	g	,	a	,	b	,	c	,	d	,	e	],[	fss	,	gss	,	ass	,	c	,	css	,	dss	,	f	],[	g	,	a	,	b	,	css	,	d	,	e	,	fss	],[	gss	,	ass	,	c	,	d	,	dss	,	f	,	g	],[	a	,	b	,	css	,	dss	,	e	,	fss	,	gss	],[	ass	,	c	,	d	,	e	,	f	,	g	,	a	],[	b	,	css	,	dss	,	f	,	fss	,	gss	,	ass	],[	c	,	d	,	e	,	fss	,	g	,	a	,	b	],[	css	,	dss	,	f	,	g	,	gss	,	ass	,	c	],[	d	,	e	,	fss	,	gss	,	a	,	b	,	css	],[	dss	,	f	,	g	,	a	,	ass	,	c	,	d	],[	e	,	fss	,	gss	,	ass	,	b	,	css	,	dss	]])

amode4=np.array([[	cmix	],[	cssmix	],[	dmix	],[	dssmix	],[	emix	],[	fmix	],[	fssmix	],[	gmix	],[	gssmix	],[	amix	],[	assmix	],[	bmix	]])

negcmix	=np.array	([	b	,	a	,	g	,	f	,	e	,	d	,	c	])
negcssmix=np.array	([	c	,	ass	,	gss	,	fss	,	f	,	dss	,	css	])
negdmix	=np.array	([	css	,	b	,	a	,	g	,	fss	,	e	,	d	])
negdssmix=np.array	([	d	,	c	,	ass	,	gss	,	g	,	f	,	dss	])
negemix	=np.array	([	dss	,	css	,	b	,	a	,	gss	,	fss	,	e	])
negfmix	=np.array	([	e	,	d	,	c	,	ass	,	a	,	g	,	f	])
negfssmix=np.array	([	f	,	dss	,	css	,	b	,	ass	,	gss	,	fss	])
neggmix	=np.array	([	fss	,	e	,	d	,	c	,	b	,	a	,	g	])
neggssmix=np.array	([	g	,	f	,	dss	,	css	,	c	,	ass	,	gss	])
negamix	=np.array	([	gss	,	fss	,	e	,	d	,	css	,	b	,	a	])
negassmix=np.array	([	a	,	g	,	f	,	dss	,	d	,	c	,	ass	])
negbmix	=np.array	([	ass	,	gss	,	fss	,	e	,	dss	,	css	,	b	])

negmode4=np.array([[	b	,	a	,	g	,	f	,	e	,	d	,	c	],[	c	,	ass	,	gss	,	fss	,	f	,	dss	,	css	],[	css	,	b	,	a	,	g	,	fss	,	e	,	d	],[	d	,	c	,	ass	,	gss	,	g	,	f	,	dss	],[	dss	,	css	,	b	,	a	,	gss	,	fss	,	e	],[	e	,	d	,	c	,	ass	,	a	,	g	,	f	],[	f	,	dss	,	css	,	b	,	ass	,	gss	,	fss	],[	fss	,	e	,	d	,	c	,	b	,	a	,	g	],[	g	,	f	,	dss	,	css	,	c	,	ass	,	gss	],[	gss	,	fss	,	e	,	d	,	css	,	b	,	a	],[	a	,	g	,	f	,	dss	,	d	,	c	,	ass	],[	ass	,	gss	,	fss	,	e	,	dss	,	css	,	b	]])

negamode4=np.array([[	negcmix	],[	negcssmix	],[	negdmix	],[	negdssmix	],[	negemix	],[	negfmix	],[	negfssmix	],[	neggmix	],[	neggssmix	],[	negamix	],[	negassmix	],[	negbmix	]])

####################lyd
clyd	=np.array	([	g	,	a	,	b	,	c	,	d	,	e	,	f	])
csslyd	=np.array	([	gss	,	ass	,	c	,	css	,	dss	,	f	,	fss	])
dlyd	=np.array	([	a	,	b	,	css	,	d	,	e	,	fss	,	g	])
dsslyd	=np.array	([	ass	,	c	,	d	,	dss	,	f	,	g	,	gss	])
elyd	=np.array	([	b	,	css	,	dss	,	e	,	fss	,	gss	,	a	])
flyd	=np.array	([	c	,	d	,	e	,	f	,	g	,	a	,	ass	])
fsslyd	=np.array	([	css	,	dss	,	f	,	fss	,	gss	,	ass	,	b	])
glyd	=np.array	([	d	,	e	,	fss	,	g	,	a	,	b	,	c	])
gsslyd	=np.array	([	dss	,	f	,	g	,	gss	,	ass	,	c	,	css	])
alyd	=np.array	([	e	,	fss	,	gss	,	a	,	b	,	css	,	d	])
asslyd	=np.array	([	f	,	g	,	a	,	ass	,	c	,	d	,	dss	])
blyd	=np.array	([	fss	,	gss	,	ass	,	b	,	css	,	dss	,	e	])

mode5=np.array([[	g	,	a	,	b	,	c	,	d	,	e	,	f	],[	gss	,	ass	,	c	,	css	,	dss	,	f	,	fss	],[	a	,	b	,	css	,	d	,	e	,	fss	,	g	],[	ass	,	c	,	d	,	dss	,	f	,	g	,	gss	],[	b	,	css	,	dss	,	e	,	fss	,	gss	,	a	],[	c	,	d	,	e	,	f	,	g	,	a	,	ass	],[	css	,	dss	,	f	,	fss	,	gss	,	ass	,	b	],[	d	,	e	,	fss	,	g	,	a	,	b	,	c	],[	dss	,	f	,	g	,	gss	,	ass	,	c	,	css	],[	e	,	fss	,	gss	,	a	,	b	,	css	,	d	],[	f	,	g	,	a	,	ass	,	c	,	d	,	dss	],[	fss	,	gss	,	ass	,	b	,	css	,	dss	,	e	]])

amode5=np.array([[	clyd	],[	csslyd	],[	dlyd	],[	dsslyd	],[	elyd	],[	flyd	],[	fsslyd	],[	glyd	],[	gsslyd	],[	alyd	],[	asslyd	],[	blyd	]])

negclyd	=np.array	([	a	,	g	,	f	,	e	,	d	,	c	,	b	])
negcsslyd=np.array	([	ass	,	gss	,	fss	,	f	,	dss	,	css	,	c	])
negdlyd	=np.array	([	b	,	a	,	g	,	fss	,	e	,	d	,	css	])
negdsslyd=np.array	([	c	,	ass	,	gss	,	g	,	f	,	dss	,	d	])
negelyd	=np.array	([	css	,	b	,	a	,	gss	,	fss	,	e	,	dss	])
negflyd	=np.array	([	d	,	c	,	ass	,	a	,	g	,	f	,	e	])
negfsslyd=np.array	([	dss	,	css	,	b	,	ass	,	gss	,	fss	,	f	])
negglyd	=np.array	([	e	,	d	,	c	,	b	,	a	,	g	,	fss	])
neggsslyd=np.array	([	f	,	dss	,	css	,	c	,	ass	,	gss	,	g	])
negalyd	=np.array	([	fss	,	e	,	d	,	css	,	b	,	a	,	gss	])
negasslyd=np.array	([	g	,	f	,	dss	,	d	,	c	,	ass	,	a	])
negblyd	=np.array	([	gss	,	fss	,	e	,	dss	,	css	,	b	,	ass	])

negmode5=np.array([[	a	,	g	,	f	,	e	,	d	,	c	,	b	],[	ass	,	gss	,	fss	,	f	,	dss	,	css	,	c	],[	b	,	a	,	g	,	fss	,	e	,	d	,	css	],[	c	,	ass	,	gss	,	g	,	f	,	dss	,	d	],[	css	,	b	,	a	,	gss	,	fss	,	e	,	dss	],[	d	,	c	,	ass	,	a	,	g	,	f	,	e	],[	dss	,	css	,	b	,	ass	,	gss	,	fss	,	f	],[	e	,	d	,	c	,	b	,	a	,	g	,	fss	],[	f	,	dss	,	css	,	c	,	ass	,	gss	,	g	],[	fss	,	e	,	d	,	css	,	b	,	a	,	gss	],[	g	,	f	,	dss	,	d	,	c	,	ass	,	a	],[	gss	,	fss	,	e	,	dss	,	css	,	b	,	ass	]])

negamode5=np.array([[	negclyd	],[	negcsslyd	],[	negdlyd	],[	negdsslyd	],[	negelyd	],[	negflyd	],[	negfsslyd	],[	negglyd	],[	neggsslyd	],[	negalyd	],[	negasslyd	],[	negblyd	]])

####################min
cmin	=np.array	([	a	,	b	,	c	,	d	,	e	,	f	,	g	])
cssmin	=np.array	([	ass	,	c	,	css	,	dss	,	f	,	fss	,	gss	])
dmin	=np.array	([	b	,	css	,	d	,	e	,	fss	,	g	,	a	])
dssmin	=np.array	([	c	,	d	,	dss	,	f	,	g	,	gss	,	ass	])
emin	=np.array	([	css	,	dss	,	e	,	fss	,	gss	,	a	,	b	])
fmin	=np.array	([	d	,	e	,	f	,	g	,	a	,	ass	,	c	])
fssmin	=np.array	([	dss	,	f	,	fss	,	gss	,	ass	,	b	,	css	])
gmin	=np.array	([	e	,	fss	,	g	,	a	,	b	,	c	,	d	])
gssmin	=np.array	([	f	,	g	,	gss	,	ass	,	c	,	css	,	dss	])
amin	=np.array	([	fss	,	gss	,	a	,	b	,	css	,	d	,	e	])
assmin	=np.array	([	g	,	a	,	ass	,	c	,	d	,	dss	,	f	])
bmin	=np.array	([	gss	,	ass	,	b	,	css	,	dss	,	e	,	fss	])

mode6=np.array([[	a	,	b	,	c	,	d	,	e	,	f	,	g	],
[	ass	,	c	,	css	,	dss	,	f	,	fss	,	gss	],
[	b	,	css	,	d	,	e	,	fss	,	g	,	a	],
[	c	,	d	,	dss	,	f	,	g	,	gss	,	ass	],
[	css	,	dss	,	e	,	fss	,	gss	,	a	,	b	],
[	d	,	e	,	f	,	g	,	a	,	ass	,	c	],
[	dss	,	f	,	fss	,	gss	,	ass	,	b	,	css	],
[	e	,	fss	,	g	,	a	,	b	,	c	,	d	],
[	f	,	g	,	gss	,	ass	,	c	,	css	,	dss	],
[	fss	,	gss	,	a	,	b	,	css	,	d	,	e	],
[	g	,	a	,	ass	,	c	,	d	,	dss	,	f	],
[	gss	,	ass	,	b	,	css	,	dss	,	e	,	fss	]])

amode6=np.array([[	cmin	],
[	cssmin	],
[	dmin	],
[	dssmin	],
[	emin	],
[	fmin	],
[	fssmin	],
[	gmin	],
[	gssmin	],
[	amin	],
[	assmin	],
[	bmin	]])

negcmin	=np.array	([	g	,	f	,	e	,	d	,	c	,	b	,	a	])
negcssmin=np.array	([	gss	,	fss	,	f	,	dss	,	css	,	c	,	ass	])
negdmin	=np.array	([	a	,	g	,	fss	,	e	,	d	,	css	,	b	])
negdssmin=np.array	([	ass	,	gss	,	g	,	f	,	dss	,	d	,	c	])
negemin	=np.array	([	b	,	a	,	gss	,	fss	,	e	,	dss	,	css	])
negfmin	=np.array	([	c	,	ass	,	a	,	g	,	f	,	e	,	d	])
negfssmin=np.array	([	css	,	b	,	ass	,	gss	,	fss	,	f	,	dss	])
neggmin	=np.array	([	d	,	c	,	b	,	a	,	g	,	fss	,	e	])
neggssmin=np.array	([	dss	,	css	,	c	,	ass	,	gss	,	g	,	f	])
negamin	=np.array	([	e	,	d	,	css	,	b	,	a	,	gss	,	fss	])
negassmin=np.array	([	f	,	dss	,	d	,	c	,	ass	,	a	,	g	])
negbmin	=np.array	([	fss	,	e	,	dss	,	css	,	b	,	ass	,	gss	])

negmode6=np.array([[	g	,	f	,	e	,	d	,	c	,	b	,	a	],
[	gss	,	fss	,	f	,	dss	,	css	,	c	,	ass	],
[	a	,	g	,	fss	,	e	,	d	,	css	,	b	],
[	ass	,	gss	,	g	,	f	,	dss	,	d	,	c	],
[	b	,	a	,	gss	,	fss	,	e	,	dss	,	css	],
[	c	,	ass	,	a	,	g	,	f	,	e	,	d	],
[	css	,	b	,	ass	,	gss	,	fss	,	f	,	dss	],
[	d	,	c	,	b	,	a	,	g	,	fss	,	e	],
[	dss	,	css	,	c	,	ass	,	gss	,	g	,	f	],
[	e	,	d	,	css	,	b	,	a	,	gss	,	fss	],
[	f	,	dss	,	d	,	c	,	ass	,	a	,	g	],
[	fss	,	e	,	dss	,	css	,	b	,	ass	,	gss	]])

negamode6=np.array([[	negcmin	],
[	negcssmin	],
[	negdmin	],
[	negdssmin	],
[	negemin	],
[	negfmin	],
[	negfssmin	],
[	neggmin	],
[	neggssmin	],
[	negamin	],
[	negassmin	],
[	negbmin	]])

####################loc
cloc	=np.array	([	b	,	c	,	d	,	e	,	f	,	g	,	a	])
cssloc	=np.array	([	c	,	css	,	dss	,	f	,	fss	,	gss	,	ass	])
dloc	=np.array	([	css	,	d	,	e	,	fss	,	g	,	a	,	b	])
dssloc	=np.array	([	d	,	dss	,	f	,	g	,	gss	,	ass	,	c	])
eloc	=np.array	([	dss	,	e	,	fss	,	gss	,	a	,	b	,	css	])
floc	=np.array	([	e	,	f	,	g	,	a	,	ass	,	c	,	d	])
fssloc	=np.array	([	f	,	fss	,	gss	,	ass	,	b	,	css	,	dss	])
gloc	=np.array	([	fss	,	g	,	a	,	b	,	c	,	d	,	e	])
gssloc	=np.array	([	g	,	gss	,	ass	,	c	,	css	,	dss	,	f	])
aloc	=np.array	([	gss	,	a	,	b	,	css	,	d	,	e	,	fss	])
assloc	=np.array	([	a	,	ass	,	c	,	d	,	dss	,	f	,	g	])
bloc	=np.array	([	ass	,	b	,	css	,	dss	,	e	,	fss	,	gss	])

mode7=np.array([[	b	,	c	,	d	,	e	,	f	,	g	,	a	],
[	c	,	css	,	dss	,	f	,	fss	,	gss	,	ass	],
[	css	,	d	,	e	,	fss	,	g	,	a	,	b	],
[	d	,	dss	,	f	,	g	,	gss	,	ass	,	c	],
[	dss	,	e	,	fss	,	gss	,	a	,	b	,	css	],
[	e	,	f	,	g	,	a	,	ass	,	c	,	d	],
[	f	,	fss	,	gss	,	ass	,	b	,	css	,	dss	],
[	fss	,	g	,	a	,	b	,	c	,	d	,	e	],
[	g	,	gss	,	ass	,	c	,	css	,	dss	,	f	],
[	gss	,	a	,	b	,	css	,	d	,	e	,	fss	],
[	a	,	ass	,	c	,	d	,	dss	,	f	,	g	],
[	ass	,	b	,	css	,	dss	,	e	,	fss	,	gss	]])

amode7=np.array([[	cloc	],
[	cssloc	],
[	dloc	],
[	dssloc	],
[	eloc	],
[	floc	],
[	fssloc	],
[	gloc	],
[	gssloc	],
[	aloc	],
[	assloc	],
[	bloc	]])

negcloc	=np.array	([	f	,	e	,	d	,	c	,	b	,	a	,	g	])
negcssloc=np.array	([	fss	,	f	,	dss	,	css	,	c	,	ass	,	gss	])
negdloc	=np.array	([	g	,	fss	,	e	,	d	,	css	,	b	,	a	])
negdssloc=np.array	([	gss	,	g	,	f	,	dss	,	d	,	c	,	ass	])
negeloc	=np.array	([	a	,	gss	,	fss	,	e	,	dss	,	css	,	b	])
negfloc	=np.array	([	ass	,	a	,	g	,	f	,	e	,	d	,	c	])
negfssloc=np.array	([	b	,	ass	,	gss	,	fss	,	f	,	dss	,	css	])
neggloc	=np.array	([	c	,	b	,	a	,	g	,	fss	,	e	,	d	])
neggssloc=np.array	([	css	,	c	,	ass	,	gss	,	g	,	f	,	dss	])
negaloc	=np.array	([	d	,	css	,	b	,	a	,	gss	,	fss	,	e	])
negassloc=np.array	([	dss	,	d	,	c	,	ass	,	a	,	g	,	f	])
negbloc	=np.array	([	e	,	dss	,	css	,	b	,	ass	,	gss	,	fss	])

negmode7=np.array([[	f	,	e	,	d	,	c	,	b	,	a	,	g	],
[	fss	,	f	,	dss	,	css	,	c	,	ass	,	gss	],
[	g	,	fss	,	e	,	d	,	css	,	b	,	a	],
[	gss	,	g	,	f	,	dss	,	d	,	c	,	ass	],
[	a	,	gss	,	fss	,	e	,	dss	,	css	,	b	],
[	ass	,	a	,	g	,	f	,	e	,	d	,	c	],
[	b	,	ass	,	gss	,	fss	,	f	,	dss	,	css	],
[	c	,	b	,	a	,	g	,	fss	,	e	,	d	],
[	css	,	c	,	ass	,	gss	,	g	,	f	,	dss	],
[	d	,	css	,	b	,	a	,	gss	,	fss	,	e	],
[	dss	,	d	,	c	,	ass	,	a	,	g	,	f	],
[	e	,	dss	,	css	,	b	,	ass	,	gss	,	fss	]])

negamode7=np.array([[	negcloc	],
[	negcssloc	],
[	negdloc	],
[	negdssloc	],
[	negeloc	],
[	negfloc	],
[	negfssloc	],
[	neggloc	],
[	neggssloc	],
[	negaloc	],
[	negassloc	],
[	negbloc	]])
###minaug##################################################
cminaug=cmin[[0,1,2,3,5,4,6]]
cssminaug=cssmin[[0,1,2,3,5,4,6]]
dminaug=dmin[[0,1,2,3,5,4,6]]
dssminaug=dssmin[[0,1,2,3,5,4,6]]
eminaug=emin[[0,1,2,3,5,4,6]]
fminaug=fmin[[0,1,2,3,5,4,6]]
fssminaug=fssmin[[0,1,2,3,5,4,6]]
gminaug=gmin[[0,1,2,3,5,4,6]]
gssminaug=gssmin[[0,1,2,3,5,4,6]]
aminaug=amin[[0,1,2,3,5,4,6]]
assminaug=assmin[[0,1,2,3,5,4,6]]
bminaug=bmin[[0,1,2,3,5,4,6]]

cnegminaug=np.array([	g	,	f	,	e	,	d	,	b	,	c	,	a	])
cssnegminaug=np.array([	gss	,	fss	,	f	,	dss	,	c	,	css	,	ass	])
dnegminaug=np.array([	a	,	g	,	fss	,	e	,	css	,	d	,	b	])
dssnegminaug=np.array([	ass	,	gss	,	g	,	f	,	d	,	dss	,	c	])
enegminaug=np.array([	b	,	a	,	gss	,	fss	,	dss	,	e	,	css	])
fnegminaug=np.array([	c	,	ass	,	a	,	g	,	e	,	f	,	d	])
fssnegminaug=np.array([	css	,	b	,	ass	,	gss	,	f	,	fss	,	dss	])
gnegminaug=np.array([	d	,	c	,	b	,	a	,	fss	,	g	,	e	])
gssnegminaug=np.array([	dss	,	css	,	c	,	ass	,	g	,	gss	,	f	])
anegminaug=np.array([	e	,	d	,	css	,	b	,	gss	,	a	,	fss	])
assnegminaug=np.array([	f	,	dss	,	d	,	c	,	a	,	ass	,	g	])
bnegminaug=np.array([	fss	,	e	,	dss	,	css	,	ass	,	b	,	gss	])

negamode8	=np.array([	[cnegminaug],	[cssnegminaug],	[dnegminaug],	[dssnegminaug],	[enegminaug],	[fnegminaug],	[fssnegminaug],	[gnegminaug],	[gssnegminaug],	[anegminaug],	[assnegminaug],	[bnegminaug]])
amode8	=np.array([	[cminaug],	[cssminaug],	[dminaug],	[dssminaug],	[eminaug],	[fminaug],	[fssminaug],	[gminaug],	[gssminaug],	[aminaug],	[assminaug],	[bminaug]])

##locaug##################
clocaug=cloc[[0,1,2,3,5,4,6]]
csslocaug=cssloc[[0,1,2,3,5,4,6]]
dlocaug=dloc[[0,1,2,3,5,4,6]]
dsslocaug=dssloc[[0,1,2,3,5,4,6]]
elocaug=eloc[[0,1,2,3,5,4,6]]
flocaug=floc[[0,1,2,3,5,4,6]]
fsslocaug=fssloc[[0,1,2,3,5,4,6]]
glocaug=gloc[[0,1,2,3,5,4,6]]
gsslocaug=gssloc[[0,1,2,3,5,4,6]]
alocaug=aloc[[0,1,2,3,5,4,6]]
asslocaug=assloc[[0,1,2,3,5,4,6]]
blocaug=bloc[[0,1,2,3,5,4,6]]

cneglocaug=np.array([	f	,	e	,	d	,	c	,	a	,	b	,	g	])
cssneglocaug=np.array([	fss	,	f	,	dss	,	css	,	ass	,	c	,	gss	])
dneglocaug=np.array([	g	,	fss	,	e	,	d	,	b	,	css	,	a	])
dssneglocaug=np.array([	gss	,	g	,	f	,	dss	,	c	,	d	,	ass	])
eneglocaug=np.array([	a	,	gss	,	fss	,	e	,	css	,	dss	,	b	])
fneglocaug=np.array([	ass	,	a	,	g	,	f	,	d	,	e	,	c	])
fssneglocaug=np.array([	b	,	ass	,	gss	,	fss	,	dss	,	f	,	css	])
gneglocaug=np.array([	c	,	b	,	a	,	g	,	e	,	fss	,	d	])
gssneglocaug=np.array([	css	,	c	,	ass	,	gss	,	f	,	g	,	dss	])
aneglocaug=np.array([	d	,	css	,	b	,	a	,	fss	,	gss	,	e	])
assneglocaug=np.array([	dss	,	d	,	c	,	ass	,	g	,	a	,	f	])
bneglocaug=np.array([	e	,	dss	,	css	,	b	,	gss	,	ass	,	fss	])

negamode9	=np.array([	[cneglocaug],	[cssneglocaug],	[dneglocaug],	[dssneglocaug],	[eneglocaug],	[fneglocaug],	[fssneglocaug],	[gneglocaug],	[gssneglocaug],	[aneglocaug],	[assneglocaug],	[bneglocaug]])
amode9	=np.array([	[clocaug],	[csslocaug],	[dlocaug],	[dsslocaug],	[elocaug],	[flocaug],	[fsslocaug],	[glocaug],	[gsslocaug],	[alocaug],	[asslocaug],	[blocaug]])

##suploc#################
csuploc=cmix[[0,1,2,4,3,5,6]]
csssuploc=cssmix[[0,1,2,4,3,5,6]]
dsuploc=dmix[[0,1,2,4,3,5,6]]
dsssuploc=dssmix[[0,1,2,4,3,5,6]]
esuploc=emix[[0,1,2,4,3,5,6]]
fsuploc=fmix[[0,1,2,4,3,5,6]]
fsssuploc=fssmix[[0,1,2,4,3,5,6]]
gsuploc=gmix[[0,1,2,4,3,5,6]]
gsssuploc=gssmix[[0,1,2,4,3,5,6]]
asuploc=amix[[0,1,2,4,3,5,6]]
asssuploc=assmix[[0,1,2,4,3,5,6]]
bsuploc=bmix[[0,1,2,4,3,5,6]]

fssnegsuploc=np.array([	f	,	dss	,	css	,	ass	,	b	,	gss	,	fss	])
gnegsuploc=np.array([	fss	,	e	,	d	,	b	,	c	,	a	,	g	])
gssnegsuploc=np.array([	g	,	f	,	dss	,	c	,	css	,	ass	,	gss	])
anegsuploc=np.array([	gss	,	fss	,	e	,	css	,	d	,	b	,	a	])
assnegsuploc=np.array([	a	,	g	,	f	,	d	,	dss	,	c	,	ass	])
bnegsuploc=np.array([	ass	,	gss	,	fss	,	dss	,	e	,	css	,	b	])
cnegsuploc=np.array([	b	,	a	,	g	,	e	,	f	,	d	,	c	])
cssnegsuploc=np.array([	c	,	ass	,	gss	,	f	,	fss	,	dss	,	css	])
dnegsuploc=np.array([	css	,	b	,	a	,	fss	,	g	,	e	,	d	])
dssnegsuploc=np.array([	d	,	c	,	ass	,	g	,	gss	,	f	,	dss	])
enegsuploc=np.array([	dss	,	css	,	b	,	gss	,	a	,	fss	,	e	])
fnegsuploc=np.array([	e	,	d	,	c	,	a	,	ass	,	g	,	f	])

negamode10	=np.array([	[cnegsuploc],	[cssnegsuploc],	[dnegsuploc],	[dssnegsuploc],	[enegsuploc],	[fnegsuploc],	[fssnegsuploc],	[gnegsuploc],	[gssnegsuploc],	[anegsuploc],	[assnegsuploc],	[bnegsuploc]])
amode10	=np.array([	[csuploc],	[csssuploc],	[dsuploc],	[dsssuploc],	[esuploc],	[fsuploc],	[fsssuploc],	[gsuploc],	[gsssuploc],	[asuploc],	[asssuploc],	[bsuploc]])

##loc7########
cloc7=cloc[[0,1,2,3,6,5,4]]
cssloc7=cssloc[[0,1,2,3,6,5,4]]
dloc7=dloc[[0,1,2,3,6,5,4]]
dssloc7=dssloc[[0,1,2,3,6,5,4]]
eloc7=eloc[[0,1,2,3,6,5,4]]
floc7=floc[[0,1,2,3,6,5,4]]
fssloc7=fssloc[[0,1,2,3,6,5,4]]
gloc7=gloc[[0,1,2,3,6,5,4]]
gssloc7=gssloc[[0,1,2,3,6,5,4]]
aloc7=aloc[[0,1,2,3,6,5,4]]
assloc7=assloc[[0,1,2,3,6,5,4]]
bloc7=bloc[[0,1,2,3,6,5,4]]

enegloc7=np.array([	a	,	gss	,	fss	,	e	,	b	,	css	,	dss	])
fnegloc7=np.array([	ass	,	a	,	g	,	f	,	c	,	d	,	e	])
fssnegloc7=np.array([	b	,	ass	,	gss	,	fss	,	css	,	dss	,	f	])
gnegloc7=np.array([	c	,	b	,	a	,	g	,	d	,	e	,	fss	])
gssnegloc7=np.array([	css	,	c	,	ass	,	gss	,	dss	,	f	,	g	])
anegloc7=np.array([	d	,	css	,	b	,	a	,	e	,	fss	,	gss	])
assnegloc7=np.array([	dss	,	d	,	c	,	ass	,	f	,	g	,	a	])
bnegloc7=np.array([	e	,	dss	,	css	,	b	,	fss	,	gss	,	ass	])
cnegloc7=np.array([	f	,	e	,	d	,	c	,	g	,	a	,	b	])
cssnegloc7=np.array([	fss	,	f	,	dss	,	css	,	gss	,	ass	,	c	])
dnegloc7=np.array([	g	,	fss	,	e	,	d	,	a	,	b	,	css	])
dssnegloc7=np.array([	gss	,	g	,	f	,	dss	,	ass	,	c	,	d	])

negamode11	=np.array([	[cnegloc7],	[cssnegloc7],	[dnegloc7],	[dssnegloc7],	[enegloc7],	[fnegloc7],	[fssnegloc7],	[gnegloc7],	[gssnegloc7],	[anegloc7],	[assnegloc7],	[bnegloc7]])
amode11	=np.array([	[cloc7],	[cssloc7],	[dloc7],	[dssloc7],	[eloc7],	[floc7],	[fssloc7],	[gloc7],	[gssloc7],	[aloc7],	[assloc7],	[bloc7]])

##lyd7#########################
clyd7=clyd[[0,1,2,3,6,5,4]]
csslyd7=csslyd[[0,1,2,3,6,5,4]]
dlyd7=dlyd[[0,1,2,3,6,5,4]]
dsslyd7=dsslyd[[0,1,2,3,6,5,4]]
elyd7=elyd[[0,1,2,3,6,5,4]]
flyd7=flyd[[0,1,2,3,6,5,4]]
fsslyd7=fsslyd[[0,1,2,3,6,5,4]]
glyd7=glyd[[0,1,2,3,6,5,4]]
gsslyd7=gsslyd[[0,1,2,3,6,5,4]]
alyd7=alyd[[0,1,2,3,6,5,4]]
asslyd7=asslyd[[0,1,2,3,6,5,4]]
blyd7=blyd[[0,1,2,3,6,5,4]]

gssneglyd7=np.array([	f	,	dss	,	css	,	c	,	g	,	gss	,	ass	])
aneglyd7=np.array([	fss	,	e	,	d	,	css	,	gss	,	a	,	b	])
assneglyd7=np.array([	g	,	f	,	dss	,	d	,	a	,	ass	,	c	])
bneglyd7=np.array([	gss	,	fss	,	e	,	dss	,	ass	,	b	,	css	])
cneglyd7=np.array([	a	,	g	,	f	,	e	,	b	,	c	,	d	])
cssneglyd7=np.array([	ass	,	gss	,	fss	,	f	,	c	,	css	,	dss	])
dneglyd7=np.array([	b	,	a	,	g	,	fss	,	css	,	d	,	e	])
dssneglyd7=np.array([	c	,	ass	,	gss	,	g	,	d	,	dss	,	f	])
eneglyd7=np.array([	css	,	b	,	a	,	gss	,	dss	,	e	,	fss	])
fneglyd7=np.array([	d	,	c	,	ass	,	a	,	e	,	f	,	g	])
fssneglyd7=np.array([	dss	,	css	,	b	,	ass	,	f	,	fss	,	gss	])
gneglyd7=np.array([	e	,	d	,	c	,	b	,	fss	,	g	,	a	])

negamode12	=np.array([	[cneglyd7],	[cssneglyd7],	[dneglyd7],	[dssneglyd7],	[eneglyd7],	[fneglyd7],	[fssneglyd7],	[gneglyd7],	[gssneglyd7],	[aneglyd7],	[assneglyd7],	[bneglyd7]])
amode12	=np.array([	[clyd7],	[csslyd7],	[dlyd7],	[dsslyd7],	[elyd7],	[flyd7],	[fsslyd7],	[glyd7],	[gsslyd7],	[alyd7],	[asslyd7],	[blyd7]])
#####################################################

#####################################################
csumsum	=np.sum	([	c	,	d	,	e	,	f	,	g	,	a	,	b	])
csssumsum	=np.sum	([	css	,	dss	,	f	,	fss	,	gss	,	ass	,	c	])
dsumsum	=np.sum	([	d	,	e	,	fss	,	g	,	a	,	b	,	css	])
dsssumsum	=np.sum	([	dss	,	f	,	g	,	gss	,	ass	,	c	,	d	])
esumsum	=np.sum	([	e	,	fss	,	gss	,	a	,	b	,	css	,	dss	])
fsumsum	=np.sum	([	f	,	g	,	a	,	ass	,	c	,	d	,	e	])
fsssumsum	=np.sum	([	fss	,	gss	,	ass	,	b	,	css	,	dss	,	f	])
gsumsum	=np.sum	([	g	,	a	,	b	,	c	,	d	,	e	,	fss	])
gsssumsum	=np.sum	([	gss	,	ass	,	c	,	css	,	dss	,	f	,	g	])
asumsum	=np.sum	([	a	,	b	,	css	,	d	,	e	,	fss	,	gss	])
asssumsum	=np.sum	([	ass	,	c	,	d	,	dss	,	f	,	g	,	a	])
bsumsum	=np.sum	([	b	,	css	,	dss	,	e	,	fss	,	gss	,	ass	])
sumsum=np.array([csumsum,csssumsum,dsumsum,dsssumsum,esumsum,fsumsum,fsssumsum,gsumsum,gsssumsum,asumsum,asssumsum,bsumsum])
############################
amode1=np.ravel(amode1)
amode2=np.ravel(amode2)
amode3=np.ravel(amode3)
amode4=np.ravel(amode4)
amode5=np.ravel(amode5)
amode6=np.ravel(amode6)
amode7=np.ravel(amode7)
amode8=np.ravel(amode8)
amode9=np.ravel(amode9)
amode10=np.ravel(amode10)
amode11=np.ravel(amode11)
amode12=np.ravel(amode12)

negamode1=np.ravel(negamode1)
negamode2=np.ravel(negamode2)
negamode3=np.ravel(negamode3)
negamode4=np.ravel(negamode4)
negamode5=np.ravel(negamode5)
negamode6=np.ravel(negamode6)
negamode7=np.ravel(negamode7)
negamode8=np.ravel(negamode8)
negamode9=np.ravel(negamode9)
negamode10=np.ravel(negamode10)
negamode11=np.ravel(negamode11)
negamode12=np.ravel(negamode12)
#####################
omnikey=np.array([amode1,amode2,amode3,amode4,amode5,amode6,amode7,amode8,amode9,amode10,amode11,amode12,negamode1,negamode2,negamode3,negamode4,negamode5,negamode6,negamode7,negamode8,negamode9,negamode10,negamode11,negamode12], dtype=object)
print(omnikey)
#####################
def compare_arrays(arr1, arr2):
    if isinstance(arr1, np.ndarray) and isinstance(arr2, np.ndarray):
        return np.array_equal(arr1, arr2)

    if isinstance(arr1, list) and isinstance(arr2, list):
        if len(arr1) != len(arr2):
            return False
        for a, b in zip(arr1, arr2):
            if not compare_arrays(a, b):
                return False
        return True

    return False

def find_array_position(arr1, target_array1, position1=None):
    if position1 is None:
        position1 = []

    matching_positions1 = []

    for idx1, inner_array1 in enumerate(arr1):
        if compare_arrays(inner_array1, target_array1):
            matching_positions1.append(position1 + [idx1])

        if isinstance(inner_array1, (np.ndarray, list)):
            result1 = find_array_position(inner_array1, target_array1, position1 + [idx1])
            if result1:
                matching_positions1.extend(result1)

    return matching_positions1

def find_array_in_globals(target_array1):
    # Get the caller's global variables
    caller_globals1 = inspect.currentframe().f_back.f_globals
    matching_positions1 = find_array_position(caller_globals1["negamode1"], target_array1)

    if matching_positions1:
        for position1 in matching_positions1:
            current_array1 = caller_globals1["negamode1"]
            for idx1 in position1:
                current_array1 = current_array1[idx1]

            for var_name1, var_value1 in caller_globals1.items():
                if compare_arrays(var_value1, current_array1):
                    return var_name1

    return None

#####################
variableaallnotes=0
column_index= 4  # Example: the third column (zero-based indexing)
while variableaallnotes < 12:
    
    search_values = aallnotes[variableaallnotes] # Example array to search within

    matching_rows = []
    with open(f'{mid_name}_converted.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row_number, row in enumerate(csv_reader):
            if len(row) > column_index and int(row[column_index]) in search_values:
                matching_rows.append(row_number)
        for row_number in matching_rows:
            data = []
            with open(f'{mid_name}_converted.csv', 'r') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
                data[row_number][column_index] = allnotes[variableaallnotes]
            with open(f'{mid_name}_converted.csv','w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
    variableaallnotes=variableaallnotes+1






#start#
questionkey=input("what key? c,c# etc")
questionkey = questionkey.replace("#", "ss")
print("what mode?")
print("1=maj")
print("2=dor")
print("3=phr")
print("4=mix")
print("5=lyd")
print("6=min")
print("7=loc")
print("8=min aug")
print("9=loc aug")
print("10=suploc")
print("11=loc7th")
print("12=lyd7th")
questionmode=int(input(""))
print("What interval for operation?")
if questionmode==1:
    print("1-per5th")
    print("4-maj3rd")
    print("6-maj7th")
    modename="maj"
    questioninterval=int(input(""))
    if questioninterval not in [1, 4, 6]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==2:
    print("1-per5th")
    print("5-min3rd")
    print("7-min7th")
    modename="dor"
    questioninterval=int(input(""))
    if questioninterval not in [1, 5, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==3:
    print("1-per5th")
    print("3-aug5th")    
    print("5-min3rd")
    print("7-min7th")
    modename="phr"
    questioninterval=int(input(""))
    if questioninterval not in [1, 3, 5, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==4:
    print("1-per5th")
    print("2-dim5th")
    print("4-maj3rd")
    print("6-maj7th")
    print("8-superloc")
    modename="mix"
    questioninterval=int(input(""))
    if questioninterval not in [1,2, 4, 6,8]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==5:
    print("1-per5th")
    print("4-maj3rd")
    print("7-min7th")
    modename="lyd"
    questioninterval=int(input(""))
    if questioninterval not in [1, 4, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==6:
    print("1-per5th")
    print("3-aug5th")
    print("5-min3rd")
    print("7-min7th")
    modename="min"
    questioninterval=int(input(""))
    if questioninterval not in [1, 3, 5, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==7:
    print("2-dim5th")
    print("3-aug5th")
    print("5-min3rd")
    print("7-min7th")
    print("8-superloc")
    modename="loc"
    questioninterval=int(input(""))
    if questioninterval not in [2, 3, 5, 7, 8]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==8:
    print("1-per5th")
    print("3-aug5th")
    print("5-min3rd")
    print("7-min7th")
    modename="minaug"
    questioninterval=int(input(""))
    if questioninterval not in [1, 3, 5, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==9:
    print("2-dim5th")
    print("3-aug5th")
    print("5-min3rd")
    print("7-min7th")
    print("8-superloc")
    modename="locaug"
    questioninterval=int(input(""))
    if questioninterval not in [2, 3, 5, 7, 8]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==10:
    print("loc or mix root ya think blood?")
    print("1=loc")
    print("2=mix")
    loclyd=int(input(""))
    if loclyd==1:
        print("2-dim5th")
        print("3-aug5th")
        print("5-min3rd")
        print("7-min7th")
        print("8-superloc")
        modename="suploc"
        questioninterval=int(input(""))
        if questioninterval not in [2, 3, 5, 7, 8]:
            print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
    if loclyd==2:
        print("1-per5th")
        print("2-dim5th")
        print("4-maj3rd")
        print("6-maj7th")
        print("8-superloc")
        modename="loc7"
        questioninterval=int(input(""))
        if questioninterval not in [1,2, 4, 6,8]:
            print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
    else:
        print("you broke me ya cunt bitch!")
if questionmode==11:
    print("2-dim5th")
    print("3-aug5th")
    print("5-min3rd")
    print("7-min7th")
    print("8-superloc")
    questioninterval=int(input(""))
    if questioninterval not in [2, 3, 5, 7, 8]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
if questionmode==12:
    print("1-per5th")
    print("4-maj3rd")
    print("7-min7th")
    modename="lyd7"
    questioninterval=int(input(""))
    if questioninterval not in [1, 4, 7]:
        print("You fucking ass hole, this is some borked as fucking coding, do only the options shown!")
        
realquestioninterval=questioninterval
questioninterval=(questioninterval-1)
intervalopervationnum=np.array([7,6,8,4,3,11,10,0])
aorbinp=input("a or b? pick one (a is most likely right but tbh it doesn't fucking matter)")
aorbinpnum=input("pick a number 0-11")
aorbans=aorbinp+aorbinpnum

calclength=int(input("how many times do you want this calculation to go on for? (this is times two due to there being a positive and negative to each fucking calculation!"))
calclength=calclength*2

###################################
curmode=questionkey+modename
nameofmode=curmode
strquestionmode=str(questionmode)
amodeans="amode"+strquestionmode
jim=0
if amodeans == "amode1":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode1, curmode))
    rootrealans=amode1[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode2":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode2, curmode))
    rootrealans=amode2[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode3":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode3, curmode))
    rootrealans=amode3[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode4":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode4, curmode))
    rootrealans=amode4[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode5":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode5, curmode))
    rootrealans=amode5[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode6":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode6, curmode))
    rootrealans=amode6[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode7":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode7, curmode))
    rootrealans=amode7[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode8":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode8, curmode))
    rootrealans=amode8[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode9":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode9, curmode))
    rootrealans=amode9[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode10":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode10, curmode))
    rootrealans=amode10[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode11":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode11, curmode))
    rootrealans=amode11[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
    
if amodeans == "amode12":
    curmode=globals()[curmode]
    #change theses (amode1)
    rootans=np.where(np.isin(amode12, curmode))
    rootrealans=amode12[rootans][0]
    
    noterealans=np.where(allnotes == rootrealans)[0]
    noterealans=int(numnumnumnotes[noterealans])
    print(noterealans)
    questioninterval=int(intervalopervationnum[questioninterval])
    print(questioninterval)
    questioninterval=questioninterval+noterealans
    print(questioninterval)
    currentconv=np.where(supconvnum==questioninterval)
    currentconv=np.array(supconv[currentconv]).flatten()
    print(currentconv)
number=1
currentname=f'{number}{nameofmode}{mid_name}'
pastname=currentname
shutil.copyfile(f'{mid_name}_converted.csv',f'{currentname}.csv')
print(nameofmode)
############################################

#############################################
#midi_file_path = f'{mid_name}_converted.csv'

#midi_object = pm.csv_to_midi(midi_file_path)

#with open(f'{currentname}_converted.mid', "wb") as output_file:
    #midi_writer = pm.FileWriter(output_file)
    #midi_writer.write(midi_object)
#############################################
nameofmode=globals()[nameofmode]
twelve=0
tempkey=np.array([], dtype=int)
print(nameofmode)
print(len(nameofmode))
temparray=np.array([], dtype=int)
while twelve < len(nameofmode):
    
    temparrayindx=np.where(supconvallnotes == nameofmode[twelve])
    temparray=np.append(temparray, temparrayindx)     
    twelve=twelve+1
print(temparray)
twelve=0
while twelve < len(temparray):
    tempkey=np.append(tempkey,currentconv[int(temparray[twelve])])
    twelve=twelve+1
nameofmode=str(nameofmode)
pastofmode=str(nameofmode)
print(tempkey,"temp")
resultadgadgadg = find_array_in_globals(negdssmaj)
print(resultadgadgadg)
#print(isdgiubisg)
tempcalcran=1
#while tempcalcran < 12:
    #isdgiubisg = find_array_in_globals(tempkey)
#############################################
variableaallnotes = 0
column_index = 4  # Example: the third column (zero-based indexing)
######################################
with open(f'{mid_name}_converted.csv', 'r') as lookup_file:
    lookup_data = list(csv.reader(lookup_file))

with open(f'{currentname}.csv', 'r') as data_file:
    data = list(csv.reader(data_file))

for variableaallnotes in range(12):
    search_value = supconvallnotes[variableaallnotes]  # Single value, not iterable

    matching_rows = []
    for row_number, row in enumerate(lookup_data):
        if len(row) > column_index and int(row[column_index]) == search_value:
            matching_rows.append(row_number)

    for row_number in matching_rows:
        data[row_number][column_index] = str(currentconv[variableaallnotes])

with open(f'{currentname}.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
###############################

with open(f'{mid_name}_converted.csv', 'r') as lookup_file:
    lookup_data = list(csv.reader(lookup_file))

with open(f'{currentname}.csv', 'r') as data_file:
    data = list(csv.reader(data_file))

for variableaallnotes in range(12):
    search_value = supconvallnotes[variableaallnotes]  # Single value, not iterable

    matching_rows = []
    for row_number, row in enumerate(lookup_data):
        if len(row) > column_index and int(row[column_index]) == search_value:
            matching_rows.append(row_number)

    for row_number in matching_rows:
        data[row_number][column_index] = str(currentconv[variableaallnotes])

with open(f'{currentname}.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)




#############
midi_file_path = f"{currentname}.csv"

midi_object = pm.csv_to_midi(midi_file_path)

with open(f"{currentname}.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)

######

questionintervalnum=np.array([1,2,3,4,5,6,7,8])
questioninterval1or2=np.array([1,2,2,2,1,1,2,2])
print(realquestioninterval)
questionintervalindex=np.where(np.isin(questionintervalnum,realquestioninterval))
typeofconv=int(questioninterval1or2[questionintervalindex])
typeofconvstr=str(typeofconv)
currentaorbmaths="_"+typeofconvstr+aorbans
print(currentaorbmaths)
####
_1a0=np.array([	0	,	6	,	3	,	1	,	1	,	1	,	11	,	1	,	11	,	1	])
_1a1	=np.array([	0	,	6	,	3	,	1	,	0	,	0	,	0	,	0	,	0	,	0	])
_1a2	=np.array([	0	,	6	,	3	,	1	,	0	,	11	,	1	,	11	,	1	,	11	])
_1a3	=np.array([	0	,	6	,	3	,	10	,	1	,	1	,	11	,	1	,	11	,	1	])
_1a4	=np.array([	0	,	6	,	3	,	10	,	0	,	0	,	0	,	0	,	0	,	0	])
_1a5	=np.array([	0	,	6	,	3	,	10	,	0	,	11	,	1	,	11	,	1	,	11	])
_1a6	=np.array([	0	,	6	,	9	,	1	,	1	,	1	,	11	,	1	,	11	,	1	])
_1a7	=np.array([	0	,	6	,	9	,	1	,	0	,	0	,	0	,	0	,	0	,	0	])
_1a8	=np.array([	0	,	6	,	9	,	1	,	0	,	11	,	1	,	11	,	1	,	11	])
_1a9	=np.array([	0	,	6	,	9	,	10	,	1	,	1	,	11	,	1	,	11	,	1	])
_1a10	=np.array([	0	,	6	,	9	,	10	,	0	,	0	,	0	,	0	,	0	,	0	])
_1a11	=np.array([	0	,	6	,	9	,	10	,	0	,	11	,	1	,	11	,	1	,	11	])

_1b0	=np.array([	0	,	6	,	3	,	2	,	0	,	1	,	11	,	1	,	11	,	1	])
_1b1	=np.array([	0	,	6	,	3	,	2	,	0	,	0	,	0	,	0	,	0	,	0	])
_1b2	=np.array([	0	,	6	,	3	,	2	,	11	,	11	,	1	,	11	,	1	,	11	])
_1b3	=np.array([	0	,	6	,	3	,	11	,	0	,	1	,	11	,	1	,	11	,	1	])
_1b4	=np.array([	0	,	6	,	3	,	11	,	0	,	0	,	0	,	0	,	0	,	0	])
_1b5	=np.array([	0	,	6	,	3	,	11	,	11	,	11	,	1	,	11	,	1	,	11	])
_1b6	=np.array([	0	,	6	,	9	,	2	,	0	,	1	,	11	,	1	,	11	,	1	])
_1b7	=np.array([	0	,	6	,	9	,	2	,	0	,	0	,	0	,	0	,	0	,	0	])
_1b8	=np.array([	0	,	6	,	9	,	2	,	11	,	11	,	1	,	11	,	1	,	11	])
_1b9	=np.array([	0	,	6	,	9	,	11	,	0	,	1	,	11	,	1	,	11	,	1	])
_1b10	=np.array([	0	,	6	,	9	,	11	,	0	,	0	,	0	,	0	,	0	,	0	])
_1b11	=np.array([	0	,	6	,	9	,	11	,	11	,	11	,	1	,	11	,	1	,	11	])

_2a0	=np.array([	0	,	6	,	3	,	1	,	1	,	1	,	11	,	1	,	11	,	1	])
_2a1	=np.array([	0	,	6	,	3	,	1	,	0	,	0	,	0	,	0	,	0	,	0	])
_2a2	=np.array([	0	,	6	,	3	,	1	,	0	,	11	,	1	,	11	,	1	,	11	])
_2a3	=np.array([	0	,	6	,	3	,	10	,	1	,	1	,	11	,	1	,	11	,	1	])
_2a4	=np.array([	0	,	6	,	3	,	10	,	0	,	0	,	0	,	0	,	0	,	0	])
_2a5	=np.array([	0	,	6	,	3	,	10	,	0	,	11	,	1	,	11	,	1	,	11	])
_2a6	=np.array([	0	,	6	,	9	,	1	,	1	,	1	,	11	,	1	,	11	,	1	])
_2a7	=np.array([	0	,	6	,	9	,	1	,	0	,	0	,	0	,	0	,	0	,	0	])
_2a8	=np.array([	0	,	6	,	9	,	1	,	0	,	11	,	1	,	11	,	1	,	11	])
_2a9	=np.array([	0	,	6	,	9	,	10	,	1	,	1	,	11	,	1	,	11	,	1	])
_2a10	=np.array([	0	,	6	,	9	,	10	,	0	,	0	,	0	,	0	,	0	,	0	])
_2a11	=np.array([	0	,	6	,	9	,	10	,	0	,	11	,	1	,	11	,	1	,	11	])

_2b0	=np.array([	0	,	6	,	3	,	2	,	0	,	1	,	11	,	1	,	11	,	1	])
_2b1	=np.array([	0	,	6	,	3	,	2	,	0	,	0	,	0	,	0	,	0	,	0	])
_2b2	=np.array([	0	,	6	,	3	,	2	,	11	,	11	,	1	,	11	,	1	,	11	])
_2b3	=np.array([	0	,	6	,	3	,	11	,	0	,	1	,	11	,	1	,	11	,	1	])
_2b4	=np.array([	0	,	6	,	3	,	11	,	0	,	0	,	0	,	0	,	0	,	0	])
_2b5	=np.array([	0	,	6	,	3	,	11	,	11	,	11	,	1	,	11	,	1	,	11	])
_2b6	=np.array([	0	,	6	,	9	,	2	,	0	,	1	,	11	,	1	,	11	,	1	])
_2b7	=np.array([	0	,	6	,	9	,	2	,	0	,	0	,	0	,	0	,	0	,	0	])
_2b8	=np.array([	0	,	6	,	9	,	2	,	11	,	11	,	1	,	11	,	1	,	11	])
_2b9	=np.array([	0	,	6	,	9	,	11	,	0	,	1	,	11	,	1	,	11	,	1	])
_2b10	=np.array([	0	,	6	,	9	,	11	,	0	,	0	,	0	,	0	,	0	,	0	])
_2b11	=np.array([	0	,	6	,	9	,	11	,	11	,	11	,	1	,	11	,	1	,	11	])
tenth=0
while tenth < len(allnotes):
    print(allnotes[tenth])
    print(allnotesnames3[tenth])
    tenth=tenth+1

print(negdssmaj)
print(tempkey,"temp")
iugbaidbida = np.array_equal(tempkey, negdssmaj)
print(iugbaidbida)
array_dtype = negdssmaj.dtype
print(array_dtype)
#####
if typeofconv==1:
    print(1)
    

if typeofconv==2:
    print(2)
