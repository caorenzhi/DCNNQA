import os, sys
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

inputFile = sys.argv[1]
outputFile=sys.argv[2]

if not os.path.isfile(inputFile):
    print "Input file does not exist"
    exit()

res = {
'CYSCYS': [],
'CYSASP': [],
'CYSSER': [],
'CYSGLN': [],
'CYSLYS': [],
'CYSILE': [],
'CYSPRO': [],
'CYSASN': [],
'CYSTHR': [],
'CYSPHE': [],
'CYSALA': [],
'CYSGLY': [],
'CYSHIS': [],
'CYSLEU': [],
'CYSARG': [],
'CYSTRP': [],
'CYSVAL': [],
'CYSGLU': [],
'CYSTYR': [],
'CYSMET': [],
'ASPCYS': [],
'ASPASP': [],
'ASPSER': [],
'ASPASN': [],
'ASPGLN': [],
'ASPLYS': [],
'ASPILE': [],
'ASPPRO': [],
'ASPTHR': [],
'ASPPHE': [],
'ASPALA': [],
'ASPGLY': [],
'ASPHIS': [],
'ASPLEU': [],
'ASPARG': [],
'ASPTRP': [],
'ASPVAL': [],
'ASPGLU': [],
'ASPTYR': [],
'ASPMET': [],
'SERCYS': [],
'SERASP': [],
'SERSER': [],
'SERASN': [],
'SERGLN': [],
'SERLYS': [],
'SERILE': [],
'SERPRO': [],
'SERTHR': [],
'SERPHE': [],
'SERALA': [],
'SERGLY': [],
'SERHIS': [],
'SERLEU': [],
'SERARG': [],
'SERTRP': [],
'SERVAL': [],
'SERGLU': [],
'SERTYR': [],
'SERMET': [],
'ASNCYS': [],
'ASNASP': [],
'ASNSER': [],
'ASNASN': [],
'ASNGLN': [],
'ASNLYS': [],
'ASNILE': [],
'ASNPRO': [],
'ASNTHR': [],
'ASNPHE': [],
'ASNALA': [],
'ASNGLY': [],
'ASNHIS': [],
'ASNLEU': [],
'ASNARG': [],
'ASNTRP': [],
'ASNVAL': [],
'ASNGLU': [],
'ASNTYR': [],
'ASNMET': [],
'GLNCYS': [],
'GLNASP': [],
'GLNSER': [],
'GLNASN': [],
'GLNGLN': [],
'GLNLYS': [],
'GLNILE': [],
'GLNTHR': [],
'GLNPRO': [],
'GLNPHE': [],
'GLNALA': [],
'GLNHIS': [],
'GLNGLY': [],
'GLNLEU': [],
'GLNARG': [],
'GLNTRP': [],
'GLNVAL': [],
'GLNGLU': [],
'GLNTYR': [],
'GLNMET': [],
'LYSCYS': [],
'LYSASP': [],
'LYSSER': [],
'LYSASN': [],
'LYSGLN': [],
'LYSLYS': [],
'LYSILE': [],
'LYSPRO': [],
'LYSTHR': [],
'LYSPHE': [],
'LYSALA': [],
'LYSGLY': [],
'LYSHIS': [],
'LYSLEU': [],
'LYSARG': [],
'LYSTRP': [],
'LYSVAL': [],
'LYSGLU': [],
'LYSTYR': [],
'LYSMET': [],
'ILECYS': [],
'ILEASP': [],
'ILESER': [],
'ILEASN': [],
'ILEGLN': [],
'ILELYS': [],
'ILEILE': [],
'ILEPRO': [],
'ILETHR': [],
'ILEPHE': [],
'ILEALA': [],
'ILEGLY': [],
'ILEHIS': [],
'ILELEU': [],
'ILEARG': [],
'ILETRP': [],
'ILEVAL': [],
'ILEGLU': [],
'ILETYR': [],
'ILEMET': [],
'PROCYS': [],
'PROASP': [],
'PROSER': [],
'PROASN': [],
'PROGLN': [],
'PROLYS': [],
'PROILE': [],
'PROPRO': [],
'PROTHR': [],
'PROPHE': [],
'PROALA': [],
'PROGLY': [],
'PROHIS': [],
'PROLEU': [],
'PROARG': [],
'PROTRP': [],
'PROVAL': [],
'PROGLU': [],
'PROTYR': [],
'PROMET': [],
'THRCYS': [],
'THRASP': [],
'THRSER': [],
'THRASN': [],
'THRGLN': [],
'THRLYS': [],
'THRILE': [],
'THRPRO': [],
'THRTHR': [],
'THRPHE': [],
'THRALA': [],
'THRGLY': [],
'THRHIS': [],
'THRLEU': [],
'THRARG': [],
'THRTRP': [],
'THRVAL': [],
'THRGLU': [],
'THRTYR': [],
'THRMET': [],
'PHECYS': [],
'PHEASP': [],
'PHESER': [],
'PHEASN': [],
'PHEGLN': [],
'PHELYS': [],
'PHEILE': [],
'PHEPRO': [],
'PHETHR': [],
'PHEPHE': [],
'PHEALA': [],
'PHEGLY': [],
'PHEHIS': [],
'PHELEU': [],
'PHEARG': [],
'PHETRP': [],
'PHEVAL': [],
'PHEGLU': [],
'PHETYR': [],
'PHEMET': [],
'ALACYS': [],
'ALAASP': [],
'ALASER': [],
'ALAASN': [],
'ALAGLN': [],
'ALALYS': [],
'ALAILE': [],
'ALAPRO': [],
'ALATHR': [],
'ALAPHE': [],
'ALAALA': [],
'ALAGLY': [],
'ALAHIS': [],
'ALALEU': [],
'ALAARG': [],
'ALATRP': [],
'ALAVAL': [],
'ALAGLU': [],
'ALATYR': [],
'ALAMET': [],
'GLYCYS': [],
'GLYASP': [],
'GLYSER': [],
'GLYASN': [],
'GLYGLN': [],
'GLYLYS': [],
'GLYILE': [],
'GLYPRO': [],
'GLYTHR': [],
'GLYPHE': [],
'GLYALA': [],
'GLYGLY': [],
'GLYHIS': [],
'GLYLEU': [],
'GLYARG': [],
'GLYTRP': [],
'GLYVAL': [],
'GLYGLU': [],
'GLYTYR': [],
'GLYMET': [],
'HISCYS': [],
'HISASP': [],
'HISSER': [],
'HISASN': [],
'HISGLN': [],
'HISLYS': [],
'HISILE': [],
'HISPRO': [],
'HISTHR': [],
'HISPHE': [],
'HISALA': [],
'HISGLY': [],
'HISHIS': [],
'HISLEU': [],
'HISARG': [],
'HISTRP': [],
'HISVAL': [],
'HISGLU': [],
'HISTYR': [],
'HISMET': [],
'LEUCYS': [],
'LEUASP': [],
'LEUSER': [],
'LEUASN': [],
'LEUGLN': [],
'LEULYS': [],
'LEUILE': [],
'LEUPRO': [],
'LEUTHR': [],
'LEUPHE': [],
'LEUALA': [],
'LEUGLY': [],
'LEUHIS': [],
'LEULEU': [],
'LEUARG': [],
'LEUTRP': [],
'LEUVAL': [],
'LEUGLU': [],
'LEUTYR': [],
'LEUMET': [],
'ARGCYS': [],
'ARGASP': [],
'ARGSER': [],
'ARGASN': [],
'ARGGLN': [],
'ARGLYS': [],
'ARGILE': [],
'ARGPRO': [],
'ARGTHR': [],
'ARGPHE': [],
'ARGALA': [],
'ARGGLY': [],
'ARGHIS': [],
'ARGLEU': [],
'ARGARG': [],
'ARGTRP': [],
'ARGVAL': [],
'ARGGLU': [],
'ARGTYR': [],
'ARGMET': [],
'TRPCYS': [],
'TRPASP': [],
'TRPSER': [],
'TRPASN': [],
'TRPGLN': [],
'TRPLYS': [],
'TRPILE': [],
'TRPPRO': [],
'TRPTHR': [],
'TRPPHE': [],
'TRPALA': [],
'TRPGLY': [],
'TRPHIS': [],
'TRPLEU': [],
'TRPARG': [],
'TRPTRP': [],
'TRPVAL': [],
'TRPGLU': [],
'TRPTYR': [],
'TRPMET': [],
'VALCYS': [],
'VALASP': [],
'VALSER': [],
'VALASN': [],
'VALGLN': [],
'VALLYS': [],
'VALILE': [],
'VALPRO': [],
'VALTHR': [],
'VALPHE': [],
'VALALA': [],
'VALGLY': [],
'VALHIS': [],
'VALLEU': [],
'VALARG': [],
'VALTRP': [],
'VALVAL': [],
'VALGLU': [],
'VALTYR': [],
'VALMET': [],
'GLUCYS': [],
'GLUASP': [],
'GLUSER': [],
'GLUASN': [],
'GLUGLN': [],
'GLULYS': [],
'GLUILE': [],
'GLUPRO': [],
'GLUTHR': [],
'GLUPHE': [],
'GLUALA': [],
'GLUGLY': [],
'GLUHIS': [],
'GLULEU': [],
'GLUARG': [],
'GLUTRP': [],
'GLUVAL': [],
'GLUGLU': [],
'GLUTYR': [],
'GLUMET': [],
'TYRCYS': [],
'TYRASP': [],
'TYRSER': [],
'TYRASN': [],
'TYRGLN': [],
'TYRLYS': [],
'TYRILE': [],
'TYRPRO': [],
'TYRTHR': [],
'TYRPHE': [],
'TYRALA': [],
'TYRGLY': [],
'TYRHIS': [],
'TYRLEU': [],
'TYRARG': [],
'TYRTRP': [],
'TYRVAL': [],
'TYRGLU': [],
'TYRTYR': [],
'TYRMET': [],
'METCYS': [],
'METASP': [],
'METSER': [],
'METASN': [],
'METGLN': [],
'METLYS': [],
'METILE': [],
'METPRO': [],
'METTHR': [],
'METPHE': [],
'METALA': [],
'METGLY': [],
'METHIS': [],
'METLEU': [],
'METARG': [],
'METTRP': [],
'METVAL': [],
'METGLU': [],
'METTYR': [],
'METMET': []}

with open(inputFile, "r+") as f:
    file = []
    for line in f:
        file.append(line.strip())
    f.close()
#print(file)

i = 0
for line in file:
    line = line.split()
    del line[0]
    del line[1]
    save = line[0]
    line[0] = save + line[1]
    del line[1]
    file[i] = line
    #print line
    i = i + 1

letters = []
for i in file:
    letter = i[0]
    if letter not in letters:
        letters.append(letter)
#print (letters)
#print len(res.keys())

combLine = []
for letter in letters:
    for line in file:
        if letter in line[0]:
            combLine.append(line)
#print combLine

i = 0
for lists in combLine:
    if combLine[i][0] in res.keys():
        let = combLine[i][0]
        del combLine[i][0]
        res[let].append(combLine[i])
    i = i + 1
w=open(outputFile,'w')
for key, val in res.items():
    if not res[key]:
        res[key] = 0
        w.write(str(key)+' '+'0')

    else:

        val = np.array(val, dtype=np.float64)
#	val_normed = (val - val.min(0)) / val.ptp(0)
        val_normed = list(np.array(val).sum(axis=0)/len(val))
	    val_normed = np.nan_to_num(val_normed)

        w.write(str(key)+' '+' '.join(map(str, val_normed)))
