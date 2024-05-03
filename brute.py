from runes import *



wordict = {#'L0': {'': ''},
 'L1': {'A': 'a', 'I': 'i'},
 'L2': {'TO': 'to', 'BE': 'be', 'tE': 'the', 'DO': 'do', 'OR': 'or', 'IS': 'is', 'OF': 'of', 'IT': 'it', 'AN': 'an', 'WE': 'we', 'GO': 'go', 'HE': 'he', 'AM': 'am', 'SO': 'so', 'BY': 'by', 'IF': 'if', 'VS': 'us', 'IN': 'in', 'MY': 'my', 'NO': 'no', 'ON': 'on', 'ID': 'id', 'AS': 'as', 'AT': 'at', 'OH': 'oh', 'Cg': 'king', 'TC': 'tk', 'PS': 'ps', 'tg': 'thing', 'Vi': 'via'},
 'L3': {'tIS': 'this', 'YOV': 'you', 'D)t': 'death', 'NOT': 'not', 'FOR': 'for', 'ALL': 'all', 'ARE': 'are', 'tgS': 'things', 'END': 'end', ')SY': 'easy', 'BVT': 'but', 'WHO': 'who', 'WAY': 'way', 'ONE': 'one', 'AND': 'and', 'tAT': 'that', 'OVR': 'our', 'GOg': 'going', 'MAY': 'may', 'BEg': 'being', 'LAW': 'law', ')CH': 'each', 'OWN': 'own', 'MAN': 'man', 'WIt': 'with', 'HIS': 'his', 'WAS': 'was', 'SAY': 'say', 'OFF': 'off', 'LOg': 'long', 'tEN': 'then', 'DAY': 'day', 'TOO': 'too', 'TWO': 'two', 'NOW': 'now', 'W)C': 'weak', 'tEM': 'them', 'CAN': 'can', 'tVS': 'thus', 'H)D': 'head', 'WEB': 'web', 'OVT': 'out', 'L)D': 'lead', 'FEW': 'few', 'HOW': 'how', 'GET': 'get', 'CEY': 'key', 'MIT': 'mit', 'PGP': 'pgp', 'SHA': 'sha', 'HAS': 'has', 'tAN': 'than', 'SIX': 'six', 'ADD': 'add', 'COM': 'com', 'FAR': 'far', 'VTC': 'utc', 'PoM': 'poem', 'R)D': 'read', 'NEW': 'new', 'VSg': 'using', 'TOR': 'tor', 'VRL': 'url', 'RSA': 'rsa', 'LOW': 'low', 'BIT': 'bit', 'VAR': 'var', 'DOT': 'dot', 'GNV': 'gnu', 'GPG': 'gpg', 'CAT': 'cat', 'DID': 'did', 'ANY': 'any', 'NOR': 'nor', 'ASC': 'asc', 'LIE': 'lie', 'AID': 'aid', 'VSE': 'use', 'ETC': 'etc', 'CVT': 'cut', 'SCY': 'sky', 'DVE': 'due', 'WHY': 'why', 'DoS': 'does', 'SEE': 'see', 'ITS': 'its', 'LYg': 'lying', 'BOt': 'both', 'TCP': 'tcp', 'FEB': 'feb', 'CGI': 'cgi', 'PAt': 'path', 'BIN': 'bin', 'MAP': 'map'},
 'L4': {'NOtg': 'nothing', 'FROM': 'from', 'BOOC': 'book', 'WHAT': 'what', 'CNOW': 'know', 'TRVE': 'true', 'TEST': 'test', 'FIND': 'find', 'YOVR': 'your', 'TRVt': 'truth', 'EDIT': 'edit', 'tEIR': 'their', 'SOME': 'some', 'VOID': 'void', 'FORM': 'form', 'GR)T': 'great', 'TRIP': 'trip', 'tOSE': 'those', 'HERE': 'here', 'ALOg': 'along', 'WILL': 'will', 'SELF': 'self', 'DEEP': 'deep', 'LICE': 'like', 'ONLY': 'only', 'VNTO': 'unto', 'HOLY': 'holy', 'COAN': 'coan', 'WENT': 'went', 'DOOR': 'door', 'TOLD': 'told', 'NAME': 'name', 'MORE': 'more', 'BODY': 'body', 'tINC': 'think', 'ELSE': 'else', 'COME': 'come', 'FOVR': 'four', 'LOSS': 'loss', 'tREE': 'three', 'MVCH': 'much', 'HAVE': 'have', 'tERE': 'there', 'LVCC': 'luck', 'NEED': 'need', 'MOST': 'most', 'WORt': 'worth', 'LOSE': 'lose', 'GAIN': 'gain', 'W)Lt': 'wealth', 'MIND': 'mind', 'DVRg': 'during', 'SAID': 'said', 'WHEN': 'when', 'M)NT': 'meant', 'DONT': 'dont', 'HAND': 'hand', 'TELL': 'tell', 'JVST': 'just', 'WERE': 'were', 'PAGE': 'page', 'DVTY': 'duty', 'SEEC': 'seek', 'MVST': 'must', 'SHED': 'shed', 'ROAD': 'road', 'LOOC': 'look', 'MACE': 'make', 'GOOD': 'good', 'SAYS': 'says', 'CANT': 'cant', 'GVSS': 'guss', 'CODE': 'code', 'SIGN': 'sign', 'HASH': 'hash', 'BEEN': 'been', 'EYES': 'eyes', 'ISNT': 'isnt', 'STOP': 'stop', 'MACg': 'making', 'CALL': 'call', 'TELE': 'tele', 'NINE': 'nine', 'VERY': 'very', 'DONE': 'done', 'WELL': 'well', 'OtER': 'other', 'tESE': 'these', 'NEXT': 'next', 'STEP': 'step', 'BACC': 'back', 'ONCE': 'once', 'MANY': 'many', 'WANT': 'want', 'BEST': 'best', 'FADg': 'fading', 'ALAS': 'alas', 'FREE': 'free', 'VSED': 'used', 'DAYS': 'days', 'PERL': 'perl', 'CPAN': 'cpan', 'NOTE': 'note', 'BR)C': 'break', 'SAME': 'same', 'HINT': 'hint', 'FACE': 'fake', 'WORD': 'word', 'LIST': 'list', 'SERO': 'zero', 'SEND': 'send', 'BALL': 'ball', 'ENDS': 'ends', 'tANC': 'thank', 'MONt': 'month', 'LAST': 'last', 'R)Dg': 'reading', 'CIND': 'kind', 'WROg': 'wrong', 'C)SE': 'cease', 'TIME': 'time', 'TANC': 'tank', 'ID)S': 'ideas', 'H)RD': 'heard', 'PAST': 'past', 'HELP': 'help', 'CASH': 'cash', 'H)Rg': 'hearing', 'NEWS': 'news', 'TIED': 'tied', 'CLVE': 'clue', 'B)ST': 'beast', 'P)CE': 'peace', 'ONiN': 'onion', 'M)NS': 'means', 'SOON': 'soon', 'GAME': 'game', 'RVLE': 'rule', 'LOOP': 'loop', 'NONE': 'none', 'INTO': 'into', 'COMg': 'coming', 'DARC': 'dark', 'VPON': 'upon', 'FEED': 'feed', 'LACE': 'lake', 'tATS': 'thats', 'FISH': 'fish', 'SEES': 'sees', 'PORT': 'port', 'FILE': 'file', 'POST': 'post', 'WORC': 'work', 'HTML': 'html', 'PAIR': 'pair', 'LIES': 'lies', 'M)Ng': 'meaning', 'PAtS': 'paths'},
 'L5': {'WARNg': 'warning', 'CHAgE': 'change', 'WItIN': 'within', 'EItER': 'either', 'WORDS': 'words', 'CABAL': 'cabal', 'SHAPE': 'shape', 'LIVES': 'lives', 'STVDY': 'study', 'ASCED': 'asked', 'AGAIN': 'again', 'HVMAN': 'human', 'AFTER': 'after', 'GETTg': 'getting', 'COVLD': 'could', 'ANYtg': 'anything', 'PAVSE': 'pause', 'WHICH': 'which', 'CAVSE': 'cause', 'STROg': 'strong', 'LATER': 'later', 'DOGMA': 'dogma', 'BELOg': 'belong', 'RIGHT': 'right', 'R)SON': 'reason', 'ABOVT': 'about', 'AMASS': 'amass', 'NEVER': 'never', 'VOICE': 'voice', 'OtERS': 'others', 'EVERY': 'every', 'HELLO': 'hello', 'LOOCg': 'looking', 'IMAGE': 'image', 'FINDg': 'finding', 'MEETg': 'meeting', 'C(SAR': 'caesar', 'LOOCS': 'looks', 'DECOY': 'decoy', 'DVCCS': 'ducks', 'BEGIN': 'begin', 'FRONT': 'front', 'CWEST': 'quest', 'GRAIL': 'grail', 'PHONE': 'phone', 'EIGHT': 'eight', 'PRIME': 'prime', 'CHECC': 'check', 'LINES': 'lines', 'FIRST': 'first', 'YOVVE': 'youve', 'POINT': 'point', 'PRISE': 'prize', 'NAMED': 'named', 'PL)SE': 'please', 'CR)TE': 'create', 'EMAIL': 'email', 'ENTER': 'enter', 'BELOW': 'below', 'WHILE': 'while', 'STILL': 'still', 'ORDER': 'order', 'SLASH': 'slash', 'WOVLD': 'would', 'CRYPT': 'crypt', 'BLESS': 'bless', 'SHARg': 'sharing', 'VALID': 'valid', 'GNVPG': 'gnupg', 'LINVX': 'linux', 'ASCII': 'ascii', 'GMAIL': 'gmail', 'HOVSE': 'house', 'SHORE': 'shore', 'GALON': 'galon', 'FOVND': 'found', 'TESTg': 'testing', 'CODES': 'codes', 'HVNTS': 'hunts', 'SHALL': 'shall', 'GROVP': 'group', 'DRAWN': 'drawn', 'TEXTS': 'texts', 'WARES': 'warez', 'EgAGE': 'engage', 'FOCVS': 'focus', 'HAPPY': 'happy', 'REPLY': 'reply', 'TOOLS': 'tools', 'HARMS': 'harms', 'S)RCH': 'search', 'WHOSE': 'whose', 'AWAIT': 'await', 'CNOCC': 'knock', 'SOVND': 'sound', 'FALSE': 'false', 'ABOVE': 'above', 'RIVER': 'river', 'TWICE': 'twice', 'COLOR': 'color', 'PePLE': 'people', 'GRASS': 'grass', 'GREEN': 'green', 'LIGHT': 'light', 'MINDS': 'minds', 'BRAIN': 'brain', 'REFER': 'refer', 'CNOWN': 'known', 'WRITE': 'write', 'VALVE': 'value', 'WATER': 'water', 'ROCCS': 'rocks', 'BVILD': 'build', 'ALONE': 'alone', 'VNTIL': 'until', 'INPVT': 'input', 'MAGIC': 'magic', 'PASTE': 'paste', 'PLACE': 'place', 'EMPTY': 'empty', 'SEECS': 'seeks', 'LIBER': 'liber'},
 'L6': {'EXCEPT': 'except', 'SACRED': 'sacred', 'WISDOM': 'wisdom', 'PRIMES': 'primes', 'SHOVLD': 'should', '(tER)L': 'aethereal', 'CARNAL': 'carnal', 'MOBIVS': 'mobius', 'ANALOG': 'analog', 'TOWARD': 'toward', 'R)LITY': 'reality', 'tROVGH': 'through', 'ARRIVE': 'arrive', 'INSTAR': 'instar', 'EMERGE': 'emerge', 'WIDSOM': 'widsom', 'MASTER': 'master', 'WISHES': 'wishes', 'CALLED': 'called', 'tOVGHT': 'thought', 'MOMENT': 'moment', 'MERELY': 'merely', 'ERRORS': 'errors', 'ENOVGH': 'enough', 'OBTAIN': 'obtain', 'FOLLOW': 'follow', 'BECOME': 'become', 'LESSON': 'lesson', 'INSIDE': 'inside', 'RAISED': 'raised', 'IMPOSE': 'impose', 'EXISTS': 'exists', 'HASHES': 'hashes', 'HIGHLY': 'highly', 'HIDDEN': 'hidden', 'WHOOPS': 'whoops', 'DECOYS': 'decoys', 'POSTED': 'posted', 'VIRTVE': 'virtue', 'SIGNED': 'signed', 'ALWAYS': 'always', 'NVMBER': 'number', 'MONDAY': 'monday', 'PAVSED': 'paused', 'SHARED': 'shared', 'VANISH': 'vanish', 'REMAIN': 'remain', 'VNSEEN': 'unseen', 'PVBLIC': 'public', 'BEFORE': 'before', 'APPEND': 'append', 'MODVLE': 'module', 'VERSiN': 'version', 'SCHEME': 'scheme', 'PERSON': 'person', 'VNICWE': 'unique', 'RESVLT': 'result', 'SECOND': 'second', 'CHANCE': 'chance', 'PROVEN': 'proven', 'ATTAIN': 'attain', 'VPLOAD': 'upload', 'CICADA': 'cicada', 'GARDEN': 'garden', 'SOVGHT': 'sought', 'EFFORT': 'effort', 'VNABLE': 'unable', 'VALETE': 'valete', 'SECRET': 'secret', 'HONEST': 'honest', 'EXPECT': 'expect', 'RETVRN': 'return', 'SYMBOL': 'symbol', 'COMMON': 'common', 'HACCER': 'hacker', 'EgAGED': 'engaged', 'CHOOSE': 'choose', 'ACCEPT': 'accept', 'FVTVRE': 'future', 'RIGHTS': 'rights', 'ANYONE': 'anyone', 'RIDDLE': 'riddle', 'AROVND': 'around', 'ALR)DY': 'already', 'LISTEN': 'listen', 'STRAgE': 'strange', 'CANNOT': 'cannot', 'CHAgES': 'changes', 'BETTER': 'better', 'BELIEF': 'belief', 'RARELY': 'rarely', 'NOTICE': 'notice', 'RELIED': 'relied', 'CHOICE': 'choice', 'STANDg': 'standing', 'LOVELY': 'lovely', 'PLANTS': 'plants', 'NEItER': 'neither', 'SERVER': 'server', 'EMAILS': 'emails', 'FALLEN': 'fallen', 'BEHIND': 'behind', 'SCRIPT': 'script', 'PRIMVS': 'primus', 'BEWARE': 'beware', 'VERIFY': 'verify'},
           #'unique' looks so bad lmao that better not be it
 'L7': {'BELIEVE': 'believe', 'MESSAGE': 'message', 'NVMBERS': 'numbers', 'TOTIENT': 'totient', 'FVNCTiN': 'function', 'SHADOWS': 'shadows', 'BVFFERS': 'buffers', 'OBSCVRA': 'obscura', 'WELCOME': 'welcome', 'PILGRIM': 'pilgrim', 'JOVRNEY': 'journey', 'SVFFERg': 'sufferng', 'OVTSIDE': 'outside', 'COMMAND': 'command', 'DECIDED': 'decided', 'STVDENT': 'student', 'REPLIED': 'replied', 'FINALLY': 'finally', 'SPECIES': 'species', 'STARTED': 'started', 'TRAILED': 'trailed', 'CONSVME': 'consume', 'BECAVSE': 'because', 'BELEIVE': 'beleive', 'FOLLOWg': 'following', 'CONSVMg': 'consuming', 'DESTROY': 'destroy', 'PROGRAM': 'program', 'EXPLAIN': 'explain', 'STOPPED': 'stopped', 'CWESTiN': 'question', 'PARABLE': 'parable', 'TVNNELg': 'tunneling', 'SVRFACE': 'surface', 'DEVISED': 'devised', 'FORWARD': 'forward', 'TOGEtER': 'together', 'GOODBYE': 'goodbye', 'JANVARY': 'january', 'VOLVMES': 'volumes', 'BEGINNg': 'beginning', 'PRODVCT': 'product', 'RECEIVE': 'receive', 'ADDRESS': 'address', 'SERVICE': 'service', 'ARRIVED': 'arrived', 'EXAMPLE': 'example', 'ENCRYPT': 'encrypt', 'MODVLVS': 'modulus', 'RECEIVg': 'receiving', 'SERVERS': 'servers', 'MONtLOg': 'monthlong', 'RECIEVE': 'recieve', 'DESPAIR': 'despair', 'ALtOVGH': 'although', 'TR)SVRE': 'treasure', 'HONESTY': 'honesty', 'ROSTERS': 'rosters', 'WEBSITE': 'website', 'CONTEST': 'contest', 'BELIEFS': 'beliefs', 'CAREFVL': 'careful', 'REV)LED': 'revealed', 'TYRANNY': 'tyranny', 'PRIVACY': 'privacy', 'ILLEGAL': 'illegal', 'MEMBERS': 'members', 'DECLINE': 'decline', 'HOWEVER': 'however', 'WONDERg': 'wondering', 'PRIMARY': 'primary', 'LIBERTY': 'liberty', 'ONBOARD': 'onboard', 'ANSWERS': 'answers', 'CLAIMED': 'claimed', 'NECROME': 'necrome', 'EVERYtg': 'everything', 'STANDBY': 'standby', 'REFERRg': 'referring', 'RECVRRg': 'recurring', 'MATERiL': 'material', 'BETWEEN': 'between', 'MILLiNS': 'millions', 'PROCESS': 'process', 'SIGNALS': 'signals', 'ACCORDg': 'according', 'SYSTEMS': 'systems', 'SVPPORT': 'support', 'ADDITiN': 'addition', 'MODELED': 'modeled', 'SHAMIRS': 'shamirs', 'CONCEPT': 'concept', 'LAgVAGE': 'language', 'RETVRNS': 'returns', 'WRITTEN': 'written', 'MODVLES': 'modules', 'PROVIDE': 'provide', 'IGNORED': 'ignored', 'VPLOADS': 'uploads', 'SCWARES': 'squares', 'ACCEPTS': 'accepts', 'LOCATiN': 'location', 'CONTACT': 'contact', 'ATTACCS': 'attacks', 'AGAINST': 'against', 'PLANNED': 'planned', 'CONDONE': 'condone', 'DEVOTED': 'devoted', 'OPENPGP': 'openpgp'},
 'L8': {'MOVRNFVL': 'mournful', 'STRVGGLE': 'struggle', 'ILLVSiNS': 'illusions', 'DISCOVER': 'discover', 'R)LITIES': 'realities', 'YOVRSELF': 'yourself', 'CONFVSED': 'confused', 'ANSWERED': 'answered', 'INHABITg': 'inhabiting', 'DIVINITY': 'divinity', 'BEHAViRS': 'behaviors', 'DECEPTiN': 'deception', 'PRESERVE': 'preserve', 'PRESERVg': 'preserving', 'ATTACHED': 'attached', 'PREPARED': 'prepared', 'STVDENTS': 'students', 'TIBERIVS': 'tiberivs', 'CLAVDIVS': 'clavdivs', 'MESSAGES': 'messages', 'PATIENCE': 'patience', 'ORIGINAL': 'original', 'FINALJPG': 'finaljpg', 'MVLTIPLY': 'multiply', 'REMAINED': 'remained', 'WEBBASED': 'webbased', 'RECIEVED': 'recieved', 'tEREFORE': 'therefore', 'BR)CABLE': 'breakable', 'IDENTITY': 'identity', 'CONTINVE': 'continue', 'RECEIVED': 'received', 'VERYGOOD': 'verygood', 'ARMOVRED': 'armoured', 'COMPLETE': 'complete', 'tOVSANDS': 'thousands', 'PHYSICAL': 'physical', 'WONDERED': 'wondered', 'COMPLETg': 'completing', 'ACTIVITY': 'activity', 'CWESTiNS': 'questions', 'RES)RCHg': 'researching', 'DEVELOPg': 'developing', 'ADVOCATE': 'advocate', 'SECVRITY': 'security', 'PROJECTS': 'projects', 'MAINTAIN': 'maintain', 'SOFTWARE': 'software', 'HVMANITY': 'humanity', 'RECENTLY': 'recently', 'INVOLVED': 'involved', 'DICTATED': 'dictated', 'M)NgLESS': 'meaningless', 'OBSERVED': 'observed', 'SENTENCE': 'sentence', 'HVNDREDS': 'hundreds', 'EVIDENCE': 'evidence', 'CONTRARY': 'contrary', 'OPERATiN': 'operation', 'FACEBOOC': 'facebook', 'PROTOCOL': 'protocol', 'PVBLICLY': 'publicly', 'SELECTED': 'selected', 'TEXTAR)S': 'textareas', 'GENERATE': 'generate', 'EPIPHANY': 'epiphany', 'DIRECTiN': 'direction'},
 'L9': {'CNOWLEDGE': 'knowledge', 'CONTAINED': 'contained', 'ENCRYPTED': 'encrypted', 'NECESSARY': 'necessary', 'INNOCENCE': 'innocence', 'CERTAINTY': 'certainty', 'OVRSELVES': 'ourselves', 'PROFESSOR': 'professor', 'ARBITRARY': 'arbitrary', 'IRRITATED': 'irritated', 'PRACTICES': 'practices', 'ADHERENCE': 'adherence', 'PRIMALITY': 'primality', 'EXPLAINED': 'explained', 'OVTGVSSES': 'outgusses', 'AVAILABLE': 'available', 'DIFFICVLT': 'difficult', 'ASSOCiTED': 'associated', 'MABINOGiN': 'mabinogion', 'FOLLOWERS': 'followers', 'RECOMMEND': 'recommend', 'ANONYMITY': 'anonymity', 'DISPLAYED': 'displayed', 'DECRYPTiN': 'decryption', 'DECRYPTED': 'decrypted', 'SIGNATVRE': 'signature', 'DEDICATED': 'dedicated', 'DEDICATiN': 'dedication', 'ATTEMPTED': 'attempted', 'SVCCEEDED': 'succeeded', 'ADVERTISE': 'advertise', 'OPPRESSiN': 'oppression', 'ENCRYPTiN': 'encryption', 'CONTINVES': 'continues', 'FORBIDDEN': 'forbidden', 'DESTROYED': 'destroyed', 'EMERGENCE': 'emergence', 'SOMETIMES': 'sometimes', 'IMPORTANT': 'important', 'BLINDNESS': 'blindness', 'SENSATiNS': 'sensations', 'PROGRAMMg': 'programming', 'REFLECTiN': 'reflection', 'FASCINATg': 'fascinating', 'LIBRARIES': 'libraries', 'PARENtOOD': 'parenthood', 'SYMBOLISM': 'symbolism'},
 'L10': {'EXPERIENCE': 'experience', 'VLTIMATELY': 'ultimately', 'PILGRIMAGE': 'pilgrimage', 'INSTRVCTiN': 'instruction', 'CONSVMPTiN': 'consumption', 'INFORMATiN': 'information', 'CEYSERVERS': 'keyservers', 'TWENTYNINE': 'twentynine', 'COMPRESSED': 'compressed', 'CIPHERTEXT': 'ciphertext', 'MEMBERSHIP': 'membership', 'CENSORSHIP': 'censorship', 'ACTIVITIES': 'activities', 'TECHNICWES': 'techniques', 'INDIVIDVAL': 'individual', 'FELLOWSHIP': 'fellowship', 'IMMEDiTELY': 'immediately', 'OBSERVATiN': 'observation', 'DISREGARDg': 'disregarding', 'ASSORTMENT': 'assortment', 'IMPLEMENTS': 'implements', 'ACCESSIBLE': 'accessible', 'APPROPRiTE': 'appropriate'},
 'L11': {'VNR)SONABLE': 'unreasonable', 'PRESERVATiN': 'preservation', 'ENLIGHTENED': 'enlightened', 'INTELLIGENT': 'intelligent', 'INDIVIDVALS': 'individuals', 'COLLABORATE': 'collaborate', 'RECRVITMENT': 'recruitment', 'INALIENABLE': 'inalienable', 'VNDOVBTEDLY': 'undoubtedly', 'COORDINATES': 'coordinates', 'RELATiNSHIP': 'relationship', 'CATEGORISES': 'categorises', 'MAtEMATICAL': 'mathematical', 'POSSIBILITY': 'possibility', 'ADDITiNALLY': 'additionally'},
 'L12': {'INTELLIGENCE': 'intelligence', 'CONSCiVSNESS': 'consciousness', 'INTERNATiNAL': 'international', 'ORGANISATiNS': 'organisations', 'SIMILARITIES': 'similarities', 'GPGENCRYPTED': 'gpgencrypted'},
 'L13': {'CIRCVMFERENCE': 'circumference', 'COgRATVLATiNS': 'congratulations', 'ENLIGHTENMENT': 'enlightenment', 'OPPORTVNITIES': 'opportunities', 'INDETERMINATE': 'indeterminate'},
 'L14': {'CIRCVMFERENCES': 'circumferences', 'SELFREFERENTiL': 'selfreferential', 'RESPONSIBILITY': 'responsibility'},#Nebuchadnezzar
 'L17': {'CRYPTOGRAPHICALLY': 'cryptographically'}}

#shortened wordlist for brutal, since words 3-4 chars and below tend to show
#up by chance too easily
brutedict = {
    'L4': wordict['L4'],
    'L5': wordict['L5'],
    'L6': wordict['L6'],
    'L7': wordict['L7'],
    'L8': wordict['L8'],
    'L9': wordict['L9'],
    'L10': wordict['L10'],
    'L11': wordict['L11'],
    'L12': wordict['L12'],
    'L13': wordict['L13'],
    'L14': wordict['L14']
}



#try to vignere-decode text with a key, using all "rotations" of the key. so
#like divinity, ivinityd, vinitydi,... ydivinit... this accounts for skips
def vig_section(text, key):
    k = 0
    q = len(key)

    arreys = []
    for m in range(0,q):
        arreys.append('')

    for char in text:
        if char in pseudo or char in runes:
            for m in range(0,q):
                arreys[m] += sub( char, key[(k+m)%q])
            k = (k+1)%q
        else:
            for m in range(0,q):
                arreys[m] += char
    #print(arreys)
    return arreys


def brute_text(text, key, n):
  #takes a single piece of text, so a single [] of arrey
  #key and n are just used to label the outcome so you can put in whatever
    for dic in brutedict:
      for word in brutedict[dic]:#isolate word
        worb = ['-'+word+'-',
                '.'+word+'-',
                '-'+word+'.',
                ' '+word+' ',
                '.'+word+' ',
                ' '+word+'.',
           ]
        for worg in worb:
          #assume text is a sentence:labeled page
          for line in text.split('\n'):
            if line.find(worg) >0:
              print(key,n,word,'  ',line)

def brute_vig_section(text, key):
    q = len(key)
    arreys = vig_section(text, key)

    #brute
    #for n in arreys call brute_text
    for ay in range( len(arreys) ):
      #print(ay)
      brute_text(arreys[ay], key, ay)


#replace with a file that doesn't have the fs stripped pls
file = open('rune-solved/03.txt','r', encoding = 'utf8')
text = ""
for m in file:
    text+=m
file.close()

brute_vig_section(text,'DIVINITY')


file = open('rune-solved/14.txt','r', encoding = 'utf8')
text = ""
for m in file:
    text+=m
file.close()

brute_vig_section(text,'FIRFVMFERENFE')


