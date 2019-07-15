#coding=utf-8
from collections import Counter
import re
import os
import json
import time
import sys
from sys import argv
import enchant
d = enchant.Dict("en_US")

toos = ['date','goal','per','depend','evening','column','created','culturally','pardon','apart','mark','practising','previous','prime','production','programme','rate','social','spending','system','write','value','cancel','fearful','field','hit','provide','woah','zone','worst','begun','result','sale','willing','com','filing','paid','prove','rom','similar','submitted','feature','similarities','losses','particularly','popular','flying','favourite','biggest','slam','weakening','peaceful','sudden','specific','nobody','sunday','tuesday','absorbed','actually','admitted','basement','beaker','born','bringing','broke','burst','chasing','chose','developed','drove','especially','explain','forced','gazelle','glass','hall','hanging','helpless','hoping','','huh','information','labored','leg','limp','lower','married','message','perfectly','perish','power','professional','prophet','pulling','quite','refrigerator','regularly','required','respect','respected','sentence','serious','slept','somehow','substitute','surprise','swallow','tender','tiny','trip','useless','accepting','adjusting','alongside','answering','anymore','bottom','buried','caring','change','check','closing','clothes','constant','contact','deep','delight','depressed','discussion','during','eventually','fell','fine','flew','forgotten','former','gathered','glance','gotten','grow','growing','hang','happiness','helpers','horrible','hour','hug','hugged','inches','killed','kissed','lap','laughing','letting','light','machine','maple','meet','memories','moving','nice','nine','nor','ourselves','packed','pretty','process','program','promised','radio','raise','reach','real','ride','roll','rubber','scene','set','shot','six','snow','standing','stunned','surrounded','swallowed','sweat','talent','telling','tension','third','threw','tradition','trial','uncomfortable','unhappy','usually','walking','weak','wiping','wondering','word','eva','god','Instead','rob','west','york','accept','added','adult','arrived','barely','bathroom','bell','blanket','bought','choking','clear','complete','control','creating','cried','crying','dear','decay','desk','drive','easy','emotion','enjoy','entered','envy','eye','fall','familiar','favorite','finger','finish','flesh','foam','foot','forehead','full','generation','gray','grin','happen','happening','hardwood','hung','imagine','including','instead','kind','lifting','listening','lonely','lose','loving','lucky','lunch','lungs','lying','missed','missing','mourn','normal','passing','patience','physical','picked','precious','present','purpose','pushed','question','rain','reading','reason','relationship','return','senior','sent','shrugged','sick','simple','simply','sing','sixteen','soft','soul','soup','spot','stood','teaching','terrible','test','tree','true','truth','tube','unable','wanting','wear','wearing','wet','whatever','whisper','wise','wish','withered','written','rob','west','afternoon','aging','alive','already','answer','anyhow','anyone','apartment','ashamed','asking','attention','beautiful','begin','beneath','bit','blue','caught','chest','cold','comfortable','coughed','coughing','covered','dinner','does','ear','early','eat','eating','eight','embarrassed','empty','eyebrows','famous','figured','filled','floor','forgive','forward','four','glasses','goes','graduation','hibiscus','holding','hole','hope','hot','involved','jeans','kitchen','large','lay','leaned','lie','lift','lifted','loose','matter','middle','neck','newspaper','notice','number','paused','peace','perhaps','piece','play','playing','project','quiet','ran','reached','recorder','remember','remembered','rest','returned','rich','rolled','run','running','salad','self','sense','seven','shoulders','shut','sighed','sight','sixties','sleep','sleeping','slow','smiling','soon','sorry','speak','special','start','started','stay','stayed','stories','story','straight','strange','strong','studied','study','taking','thesis','thin','thirty','tissue','trouble','turned','turning','twenty','use','wait','waited','watching','wave','weakly','wife','wipe','wondered','wonderful','wore','working','wrong','yellow','yeah','afraid','dropped','fact','forget','late','list','mind','mouth','quickly','sad','skin','street','suddenly','younger','arm','dark','far','feeling','gonna','hair','learn','near','nose','nothing','outside','pain','several','shook','silence','sitting','softly','steps','touch','sometimes','age','behind','bye','coming','cry','door','everything','experience','fear','gave','gone','happened','kept','lost','mean','okay','saying','table','tape','toward','understand','almost','anything','believe','better','breath','breathing','brought','course','different','enough','front','hard','keep','live','living','lot','move','nodded','side','sit','smile','spoke','stopped','sure','talking','taught','thinking','today','try','walk','watch','well','able','again','another','any','bed','began','body','car','chair','close','doing','dying','end','ever','final','food','friend','having','hear','held','important','let','looking','morning','once','part','put','room','tell','together','tried','trying','until','whispered','window','yourself','yes','myself','sat','voice','went','away','got','house','little','talk','told','came','come','die','love','professor','saw','small','always','death','felt','knew','man','right','someone','asked','day','don','good','know','old','time','want','long','down','earlier','effort','head','helping','lives','office','party','past','place','pull','suggest','win','work','example','isn','kim','north','ten','same','chart','certain','stop','met','meaning','translated','land','split','splitting','ruling','worker','wrote','being','subject','wrote','God','losing','related','paper','poisoned','printed','printing','person','using','top','every','take','district','displace','available','call','each','face','headline','inside','million','nearly','picture','feet','made','pair','back','help','hurt','support','night','some','getting','break','big','bad','expensive','chief','majority','minister','state','why','harry','cost','couple','half','spent','open','spend','those','less','department','Chinese','month','united','states','week','mistake','most','very','report','problem','planned','planning','antic','risk','supporting','view','very','user','found','heavy','link','laugh','button','addiction','moment','black','hold','inner','shirt','twice','high','alone','reality','Thursday','really','dance','itself','stand','path','exchange','company','father','himself','five','upper','class','firm','fan','job','fixed','odd','spin','average','around','many','West','Deng','Drag','Race','drag','bar','just','recent','speech','progress','everyone','public','see','deal','extra','apply','off','seat','deny','behaviour','local','across','few','term','often','like','Office','according','rule','remain','short','human','future','point','making','money','interesting','grim','probe','favour','convicted','prose','price','onto','life','wild','turns','ice','main','world','teeth','our','left','been','major','expect','plan','won','seats','talks','leader','feared','order','chic','though','great','woman','much','non','even','now','never','decision','rather','writing','best','became','group','too','used','men','giving','idea','white','say','taken','something','role','two','first','without','air','second','both','visit','three','own','style','also','other','all','themselves','year','type','women','between','student','who','only','people','think','going','what','cut','case','son','into','way','these','through','out','cannot','which','home','year','than','more','new','said','was','how','from','such','but','there','not','with','about','the','this', 'that', 'tomorrow', 'yesterday', 'next', 'last', 'one', 'over', 'under', 'above', 'below', 'beyond', 'besides', 'except', 'among', 'along', 'for', 'except', 'because', 'due', 'before', 'after', 'ago', 'later', 'towards', 'since', 'give', 'teach', 'buy', 'lend', 'find', 'and','hand', 'leave', 'sell', 'show', 'read', 'pay', 'make', 'offer', 'build', 'pass', 'bring', 'cook', 'are', 'were', 'did', 'has', 'have', 'had', 'will', 'shall', 'would', 'should', 'can', 'could', 'may', 'might', 'must', 'shall', 'should', 'will', 'would', 'need', 'ought', 'look', 'sound', 'taste', 'smell', 'feel', 'listen', 'seem', 'appear', 'become', 'get', 'besides', 'furthermore', 'moreover', 'yet', 'still', 'however', 'nevertheless', 'else', 'otherwise', 'thus', 'hence', 'therefore', 'accordingly', 'consequently', 'when', 'while', 'as', 'although', 'that', 'where', 'you', 'him', 'they', 'them', 'she', 'her', 'your', 'his', 'itsour', 'your', 'their', 'mine', 'hers', 'its', 'ours', 'yours', 'theirs']
exclude = []

curDir = os.getcwd()
with open(os.path.join(curDir,'./simpleWords.json'),'r')as fo:
    exclude = json.load(fo)
time.sleep(1)

def notSimple(word):
    if word in exclude:
        return False
    if word.endswith('ment') or word.endswith('ness'):
        word = word[0:-4]
        if word in exclude:
            return False
    if word.endswith('tion'):
        word = word[0:-4]
        if word in exclude:
            return False
        word += 't'
        if word in exclude:
            return False
        word = word[0:-1] +'e'
        if word in exclude:
            return False

    if word.endswith('ing'):
        word = word[0:-3]
        if word in exclude:
            return False
        word += 'e'
        if word in exclude:
            return False
    if word.endswith('ies'):
        word = word[0:-3]
        if word in exclude:
            return False
        word += 'y'
        if word in exclude:
            return False
    if word.endswith('es'):
        word = word[0:-2]
        if word in exclude:
            return False
        word += 'e'
        if word in exclude:
            return False
        word += 's'

    if word.endswith('ers'):
        word = word[0:-1]
        if word in exclude:
            return False
        word = word[0:-1]
        if word in exclude:
            return False
        word = word[0:-1]
        if word in exclude:
            return False
        return True

    if word.endswith('est'):
        word = word[0:-3]
        if word in exclude:
            return False
        word = word[0:-1]
        if word in exclude:
            return False

    if word.endswith('ied'):
        word = word[0:-2]
        if word in exclude:
            return False
        word += 'y'
        if word in exclude:
            return False
        return True

    if word.endswith('ted') or word.endswith('ded'):
        word = word[0:-2]
        if word in exclude:
            return False
        word = word[0:-1]
        if word in exclude:
            return False
        return True

    if word.endswith('ed'):
        word = word[0:-2]
        if word in exclude:
            return False
        word += 'e'
        if word in exclude:
            return False
        return True

    if word.endswith('s') and len(word)>3:
        word = word[0:-1]
        if word in exclude:
            return False

    if word.endswith('ly'):
        if word.endswith('ily'):
            word = word[0:-3]+'y'
            if word in exclude:
                return False
        word = word[0:-2]
        if word in exclude:
            return False
    return True


def outputWords(articlePath):
    words = []
    with open(articlePath, 'r') as fwc:
        for line in fwc:
            lst = re.split('\W+',line)
            lst1 = [i for i in lst if len(i)>1 and i.isalpha()]
            words.extend(lst1)
    wordlst = Counter(words)
    dicLen = len(wordlst)
    allWordsPre = wordlst.most_common(dicLen)
    allwords = [item[0].lower() for item in allWordsPre if len(item[0]) >2 and d.check(item[0])]
    result = []
    for i in allwords:
        orw = i
        if i.endswith('ting') or i.endswith('ping') or i.endswith('ning'):
            i = i[0:-3]
            if not d.check(i):
                i = i+'e'

        if i.endswith('ings'):
            i = i[0:-4]
            if not d.check(i):
                i = i+'e'

        if i.endswith('ing'):
            i = i[0:-3]
            if not d.check(i):
                i = i+'e'

        if i.endswith('ers'):
            i = i[0:-1]
        if i.endswith('ies') or i.endswith('ied'):
            i = i[0:-3]+'y'
        if i.endswith('ded'):
            i = i[0:-2]
            if not d.check(i):
                i = i+'e'
        if i.endswith('ed'):
            su = d.suggest(i)
            le = len(i)
            for wo in su:
                if ' ' in wo:
                   wo = wo.split(' ')[0]
                if '-' in wo:
                   wo = wo.split('-')[0]
                if wo[0:le-2] == i[0:le-2] and len(wo) < le:
                     i = wo
                     break
            
        if i.endswith('s'):
            su = d.suggest(i)
            le = len(i)
            for wo in su:
                if wo[0:le-2] == i[0:le-2] and len(wo) < le:
                     i = wo
                     break

        if i in exclude:
            continue
        if d.check(i):
            result.append(i)
    result.extend(allwords)
    oo = set(result)
    return list(oo)


y18Dir = '/Users/cyang1/gitclone/economist/cleandata/The_Economist/a2018'
art18 = []
def getFiles18(ds):
    if os.path.isdir(ds):
        pa = [os.path.join(ds,i) for i in os.listdir(ds)]
        for j in pa:
            getFiles18(j)
    else:
        if 'papers' in ds:
            art18.append(ds)




y19Dir = '/Users/cyang1/gitclone/economist/cleandata/The_Economist/a2019'
art19 = []
def getFiles19(ds):
    if os.path.isdir(ds):
        pa = [os.path.join(ds,i) for i in os.listdir(ds)]
        for j in pa:
            getFiles19(j)
    else:
        if 'papers' in ds:
            art19.append(ds)

if __name__ == "__main__":
    
    getFiles18(y18Dir)
    
    outs = []
    for art1 in art18:
        print(art1)
        outs.extend(outputWords(art1))

    ab1 = list(set(outs))
    
    
    outs = []
    getFiles19(y19Dir)
    for art2 in art19:
        print(art2)
        outs.extend(outputWords(art2))
    ab2 = list(set(outs))
    ooo = list(set(ab1.extend(ab2)))
    with open('./wordsooo.txt','w') as fo1:
        fo1.write(','.join(ooo))