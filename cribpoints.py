from crunes import *
import pyinputplus as pyip

#crib attempter for various 'points of interest' in liber
#these include: quotation mark passages, apostrophe word passages,
#long words, groups of short words, that one random 7

things = [
'03 6:eYgJgMWCN-BY)-OoGR-MRMPiW-(oto-PXJL-RLRBAPTXLT-MXI\'W',
'03 13:"(LALGA-SHg-LtB-SCVCOi"-LCJ-XANeX',
'08 15:iJMt)TA-BWY-TJHt(-LAR(otONoIE-iFG-SFtT-)i)IViegD-XTFBHVSCReW-ePSVLAPVCEFDX-t)egH-YRM-oNL',
'15 16:AI-GJBiM-DPAC)GS-TP-OSTMRYSX-IJLgLI-XV)MeVSH-CXJO-FJF-IYIo-TGRt-iBSC-eVG-LR-IMR-MgHP(-gS(-EPI-BeW(VJCB-tSWt(-ioGL-DLVoi-RDRBJCV)-OXX-giJ-I(o-EMW-EXtMASX-Dt-iV-XM(SCE-C()-DCG-OIe-NoGYCtCt-MY-PABP-HVHNT(BeOIP-(O\'Y-iYMG-FRiLT-EoOPLOGIo)-DECMIY-PL-IWSJW-oiA-tEOJGSgYMoH-MFtXt(SPYOF-PoSE(eMLPN-iFCNOJSi-(JtA)-PHSo-MW-RYIV-XWSR-DPtPO-DJO-VPEA(X(-TRoTB-)-(CN-EgtJJFLNOB-XG-AOL-AV-DHCWLiDe-oOiLC-iCX-g)gGgDJT-)P-WPM-PR-(TEVg(i-NI)HtY)-(-OXSO-JFTG-WIAIOI-g)-N-GMWtE',
'15 18:BAOEViJWTRWo-tCMtF(H-iF)YAtLTBVg-ESMR-AWB-WBMRNMHMINAD-"iEO-NWi-VJt)-LCGLe-o))A"',
'33 10:PE\'T-JXgL-TXOYgFOY-IH-o(GJgiNMYoi-gGEX-oXPLSX)-Li-RAD-)G-R-CeH-MAoG-DASiH-PGECoRoV-I(ot-JRi-REtYTgiOB-TtC-XC-SA(-MFJRE-ieIeoXCWAE-SVX-SoL-JN-PeB-tt-I(LSgJJi-oHeVL-IR-iHLTWXe-RT)-I(LM-IRGT)-eoHoCSTNO-IRG-W-DVYLIMBV-LR-TIV-GCFe-LeYT-T(V-()eYN-VWgH-GYR-OI-LNX-NOP-F)((O-XNSo(L-N(-tV)Y(-PIeVRJ-PoJAgPtPAg-YMo-XBVTeMP(Y-X(YR(YFFMi-XE-RVTGVYR-iVOeI-JFPJD-ItOHiGH',
'40 3:")PL-DOLIX)gER"-NPEWi-NJTY',
'40 5:IH-oLNT-"FDR)G-POeOM)B-Ji-SMF-TF(O-oCLDiL-OCgV-PWT-GCS-VoGt-FXFT-CSXo-GFXND-BT)i"',
'40 41:")XYeR-OPSC(Me-NJ-EFS-EFAg-VgJeGFgRIt-JV(-YSFEVS(Y)-IToRToO-GNH-DMOCDET-WXDL-O(J-eVB"-MT-DME',
'solved 03:ᚱᛇᚢᚷᛈᛠᛠ-ᚠᚹᛉᛏᚳᛚᛠ-ᚣᛗ-ᛠᛇ-ᛏᚳᚾᚫ-ᛝᛗᛡᛡᛗᛗᚹ-ᚫᛈᛞᛝᛡᚱ-ᚩᛠ-ᛡᛗᛁ-ᚠᚠ-ᛖᚢᛝ-ᛇᚢᚫ'
]

'''40 10:"FCtMJWRAL-OgRVPRoi-CXR-eTtN-Re(DoH-BNY-FiAiE(DJVE-tR-OeRi-YIXeHO)-(Hig)t-NY-NFIg"
40 11:"THW(-Be-iHXB-DgRJtH-AGYIFG-ITD)BFOP-eioWRNOT-SWV
40 12:EiEit-XAGPN-SRFDgHEJD-Ji-RW-GgAB-JPJ-TFX-AJ-IFXVOYHt-HNIB-ioiSPYX-)V)L-FgMH-tBO-ML-O)St)-eSX-FMB-(SeNiN-V(W-D)VNgFNE(HJ-IETi-GION-CV(MPSAi-GLYWo"-FV-XF(DFiJN
'''

options = ['03 6 ...MXI\'W', '03 13 "(LALGA...', '08 15 ePSVLAPVCEFDX',
           '15 16 ...(O\'Y...', '15 18 "iEO...', '33 10 PE\'T', '40 3 "',
           '40 5 "FDR)G...', '40 41 "', 'solved 03']

resp = pyip.inputMenu(options, numbered=True)
print(things[options.index(resp)])

strip = things[options.index(resp)].split(':')[1]
words = strip.split('-')

prepkey = ""
for char in strip:
    if char in pseudo:
        prepkey += 'f'
    else:
        prepkey += char
keys = prepkey.split('-')

cribs = prepkey.split('-')

n=0
for w in words:
    print(w.ljust(13), cribs[n].ljust(13), keys[n].ljust(13), n)#, sep = '\t\t')
    n+=1
#print(n)

e=True
while(e):
    #mode or something
    print("Pick a word to crib, or -1 to back out.")
    resp = pyip.inputNum()
    if resp == -1:#dump key? set that to -2 maybe
        e = False
    elif resp >= n:
        print("Number too big ):")
    else:
        print( words[resp], 'runic length', rlen(words[resp]) )
        #apostrophee
        if "'" in words[resp]:
            print("watch for apostrophes")
        f = True
        while f:
            print('Enter a valid crib, or nothing to back out')
            trycrib = input()
            if trycrib == '':
                f = False
            else:
                if rlen(words[resp]) != rlen(trycrib):
                    print("Bad length ):")
                else:#crib key
                    key = ""
                    n=0
                    for char in words[resp]:
                        if char in pseudo or char in runes:
                            key += sub(char, trycrib[n])
                            n+=1
                        else:
                            key+=char
                    f=False
                    print(key)
                    cribs[resp] = trycrib
                    keys[resp] = key

                    n=0
                    for w in words:
                        print(w.ljust(13), cribs[n].ljust(13), keys[n].ljust(13), n)#, sep = '\t\t')
                        n+=1
