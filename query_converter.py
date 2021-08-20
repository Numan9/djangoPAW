import json
import re
from prettytable import PrettyTable

token="eS1waYB1pt5B"

def fnhas_operator(checkme,operators):
    foundit=0
    for symbol in operators:
        if symbol in checkme:
            foundit=1
            break
    return foundit


# In[4]:


def fnget_shortcuts():
    shortcuts=dict()
    shortcuts.update({"ATSL":"(t:points+t:line<o:points) as 'ATSL'"})
    shortcuts.update({"ATSW":"(t:points+t:line>to:points) as 'ATSW'"})
    shortcuts.update({"o:AWP":"(Average(100*(((0<o:points-t:points) as 'o:W' or (0<t:points-o:points) as 'o:L' or 1/0) and (0<o:points-t:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'"})    
    shortcuts.update({"AWP":"(Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season and site='away')) as 'AWP'"})
    shortcuts.update({"3DM":"(1*third downs made) as '3DM'"})
    shortcuts.update({"3DA":"(1*third downs attempted) as '3DA'"})
    shortcuts.update({"3DF":"(t:third downs attempted-t:third downs made) as '3DF'"})
    shortcuts.update({"3DP":"(100.*t:third downs made/t:third downs attempted) as '3DP'"})
    shortcuts.update({"4DM":"(1*fourth downs made) as '4DM'"})
    shortcuts.update({"4DA":"(1*fourth downs attempted) as '4DA'"})
    shortcuts.update({"4DF":"(t:fourth downs attempted-t:fourth downs made) as '4DF'"})
    shortcuts.update({"4DP":"(100.*t:fourth downs made/t:fourth downs attempted) as '4DP'"})
    shortcuts.update({"COMP":"(1*completions) as 'COMP'"})
    shortcuts.update({"CP":"(100.*t:completions/t:passes) as 'CP'"})
    shortcuts.update({"NDIV":"(t:division!=o:division) as 'NDIV'"})
    shortcuts.update({"DIV":"(t:division=o:division) as 'DIV'"})
    shortcuts.update({"DTD":"(t:interception touchdowns+t:fumble return touchdowns) as 'DTD'"})
    shortcuts.update({"FDP":"(100.*t:first downs/(t:rushes+t:passes+o:sacks)''"})
    shortcuts.update({"FG":"(1*field goals) as 'FG'"})
    shortcuts.update({"FUML":"(1*fumbles lost) as 'FUML'"})
    shortcuts.update({"FUM":"(1*fumbles) as 'FUM'"})
    shortcuts.update({"GTGA":"(1*goal to go attempted) as 'GTGA'"})
    shortcuts.update({"GTGF":"(1*goal to go attempted-goal to go made) as 'GTGF'"})
    shortcuts.update({"GTGM":"(1*goal to go made) as 'GTGM'"})
    shortcuts.update({"o:HWP":"(Average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'"})
    shortcuts.update({"HWP":" (Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season and site='home')) as 'HWP'"})
    shortcuts.update({"INC":"(t:passes-t:completions) as 'INC'"})
    shortcuts.update({"INT":"(1*interceptions) as 'INT'"})
    shortcuts.update({"M1":"(sum(t:quarter scores[:1])-sum(o:quarter scores[:1])) as 'M1'"})
    shortcuts.update({"M2":"(sum(t:quarter scores[:2])-sum(o:quarter scores[:2])) as 'M2'"})
    shortcuts.update({"M3":"(sum(t:quarter scores[:3])-sum(o:quarter scores[:3])) as 'M3'"})
    shortcuts.update({"NOTD":"(t:touchdowns-t:rushing touchdowns-t:passing touchdowns) as 'NOTD'"})
    shortcuts.update({"OFPL":"(t:passes+t:rushes+o:sacks) as 'OFPL'"})
    shortcuts.update({"OT":"(1*overtime) as 'OT'"})
    shortcuts.update({"P1":"(t:quarter scores[0]) as 'P1'"})
    shortcuts.update({"P2":"(t:quarter scores[1]) as 'P2'"})
    shortcuts.update({"P3":"(t:quarter scores[2]) as 'P3'"})
    shortcuts.update({"P4":"(t:quarter scores[3]) as 'P4'"})
    shortcuts.update({"PENY":"(1*penalty yards) as 'PENY'"})
    shortcuts.update({"PENFD":"(1*penalty first downs) as 'PENFD'"})
    shortcuts.update({"PEN":"(1*penalties) as 'PEN'"})
    shortcuts.update({"PFD":"(1*passing first downs) as 'PFD'"})
    shortcuts.update({"PO":"(t:playoffs=1) as 'PO'"})
    shortcuts.update({"PTD":"(1*passing touchdowns) as 'PTD'"})
    shortcuts.update({"PY":"(1*passing yards) as 'PY'"})
    shortcuts.update({"RFD":"(1*rushing first downs)''"})
    shortcuts.update({"RTD":"(1*rushing touchdowns) as 'RTD'"})
    shortcuts.update({"REG":"(t:playoffs=0) as 'REG'"})
    shortcuts.update({"RTD":"(1*rushing touchdowns) as 'RTD'"})
    shortcuts.update({"RY":"(1*rushing yards) as 'RY'"})
    shortcuts.update({"RZA":"(1*red zones attempted) as 'RZA'"})
    shortcuts.update({"RZM":"(1*red zones made) as 'RZM'"})
    shortcuts.update({"RZF":"(t:red zones attempted-red zones made) as 'RZF'"})
    shortcuts.update({"S1":"(sum(t:quarter scores[:1])) as 'S1'"})
    shortcuts.update({"S2":"(sum(t:q:uarter scores[:2])) as 'S2'"})
    shortcuts.update({"S3":"(sum(t:quarter scores[:3])) as 'S3'"})
    shortcuts.update({"SIQ":"(sum(map(lambda x: x%2!=0, t:quarter scores))) as 'SIQ'"})
    shortcuts.update({"SY":"(1*sack yards) as 'SY'"})
    shortcuts.update({"TOM":"(t:turnovers-o:turnovers) as 'TOM'"})
    shortcuts.update({"TOP":"(1*time of possession) as 'TOP'"})
    shortcuts.update({"TO":"(1*turnovers) as 'TO'"})
    shortcuts.update({"TY":"(t:passing yards+t:rushing yards) as 'TY'"})
    shortcuts.update({"o:WP":"(Average(100*(((0<o:points-t:points) as 'o:W' or (0<t:points-o:points) as 'o:L' or 1/0) and (0<o:points-t:points) as 'o:W')@o:team and o:season)) as 'o:WP'"})
    shortcuts.update({"WP":"(Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season)) as 'WP'"})
    shortcuts.update({"YPC":"(t:passing yards/t:completions) as 'YPC'"})
    shortcuts.update({"YPPL":"((1.*rushing yards+t:passing yards)/(t:rushes+t:passes+o:sacks)) as 'YPPL'"})
    shortcuts.update({"YPPT":"((1.*rushing yards+t:passing yards)/t:points) as 'YPPT'"})
    shortcuts.update({"YPPA":"(1.*passing yards/t:passes) as 'YPPA'"})
    shortcuts.update({"YPPP":"(1.*passing yards/(t:passes+o:sacks)) as 'YPPP'"})
    shortcuts.update({"YPRA":"(1.*rushing yards/t:rushes) as 'YPRA'"})
    #shortcuts.update({"o:STDRAPG":"(Average(o:rushes@o:team and o:season and o:season=season)) as 'o:STDRAPG' and game number<0 "})
    shortcuts.update({"STDRAPG":"(Average(t:rushes@team and season and season=season)) as 'STDRAPG'"})
    #shortcuts.update({"o:STDoRAPG":"(Average(oo:rushes@o:team and o:season and o:season=season)) as 'o:STDoRAPG' and game number<0"})
    shortcuts.update({"STDoRAPG":"(Average(o:rushes@team and season and season=season)) as 'STDoRAPG'"})
    shortcuts.update({"PRSW":" (Sum(((0<t:points-o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'"})

    shortcuts.update({"FD":"(1*first downs) as 'FD'"})
    shortcuts.update({"TD":"(1*touchdowns) as 'TD'"})


    singlecuts=dict()
    singlecuts.update({"A":"(t:site=='away') as 'A'"})
    singlecuts.update({"H":"(t:site=='home') as 'H'"})
    singlecuts.update({"W":"(0<t:points-o:points) as 'W'"})
    singlecuts.update({"L":"(0<o:points-t:points) as 'L'"})
    singlecuts.update({"F":"(t:line+0<0) as 'F'"})
    singlecuts.update({"D":"(t:line+0>0) as 'D'"})
    singlecuts.update({"O":"(t:total+0<t:points+o:points) as 'O'"})
    singlecuts.update({"U":"(t:points+o:points< total) as 'U'"})
    singlecuts.update({"C":"((t:conference = o:conference)) as 'C'"})
    
    return shortcuts,singlecuts


# In[83]:


def fngrouping_format_check(groupby,check_data):
    grouping=0
    for g in groupby:
        if g in check_data and not '@' in check_data:
            #print(g)
            grouping=1
            
    if grouping==0:
        for item in check_data:
            if '@' in item:
                grouping=0
                break

            if ',' in item and '(' not in item and not '@' in item:
                #print(item)
                grouping=1
                
    return grouping 


# In[6]:


def fncolumn_format_check(check_data):
    column_format=0
    for s in check_data:
        at_pos=s.find("@")
        if at_pos>0:
            if "(" in s[:at_pos] and ")" in s[at_pos+1:]:
                column_format=0
            else:
                column_format=1
    return column_format    


# In[7]:


def fnget_strings():
    strings=list()
    strings.append('coach')
    strings.append('conference')
    strings.append('day')
    strings.append('division')
    strings.append('opponents')
    strings.append('site')
    strings.append('surface')
    strings.append('team')
    strings.append('time zone')
    return strings


# In[8]:


def fnsplit(splitme,delimitor):
    listoftwo=list()
    if delimitor in splitme:
        d_pos=splitme.find(delimitor)
        listoftwo.append(splitme[:d_pos])
        listoftwo.append(splitme[d_pos+1:])
        #print(listoftwo)
    else:
        listoftwo=splitme #nothing to split
    return listoftwo


# In[9]:



def fnfix_string(sdql_parts,operators):

    for i in range(0,len(sdql_parts)):
        for string in strings:
            if string in sdql_parts[i]:
                if sdql_parts[i].find("'")<=0 and sdql_parts[i].find('""')<=0:
                    sdql_parts[i]=sdql_parts[i].replace(' ','')
                    for symbol in operators:
                        if symbol in sdql_parts[i]:
                            symbol_pos=sdql_parts[i].find(symbol)
                            sdql_parts[i]=sdql_parts[i][:symbol_pos+1]+'"'+sdql_parts[i][symbol_pos+1:]+'"'
                            sdql_parts[i]=sdql_parts[i].replace('"',"'")
                            break

                break
    return sdql_parts


# In[10]:



def fnget_sdql_data(sdql_parts_in,shortcuts):
    ##replace shortcuts

    sdql_data=list()
    #print(sdql_parts_in)
    for s in sdql_parts_in:
        if s!='and' and len(s)>1:
            #if s==s.upper():
            _count=0
            for key,value in shortcuts.items():
                _count+=1
                #print(key,_count)
                #if _count==60:
                    #3/0
                if key in s:
                #if s==key:
                    s=s.replace(key,value)
                    break
            sdql_data.append(s)
        else:
            sdql_data.append(s)
    #print("sdql_data",sdql_data)
    return sdql_data


# In[11]:


def fnget_single_parts(sdql_data):
    ##replace singlecusts

    #print(sdql_data)
    single_parts=list()
    for s in sdql_data:

        try:
            is_num=float(s)
            single_parts.append(s)
        except:

            if s!='and' and fnhas_operator(s,operators)==0 and ',' not in s:
                prefix=s[:s.find(':')+1]
                scut=s[s.find(':')+1:]
                if scut==scut.upper():
                    singles=list(scut)
                    for j in range(0,len(singles)+len(singles)-2):
                        #print(singles[j],j)
                        if singles[j].find('and')<=0:
                            singles.insert(j+1,' and ')

                    for single in singles:
                        if single.find('and')<=0:
                            single_parts.append(prefix+single)
                        else: 
                            single_parts.append(single)
                else:
                    single_parts.append(s)
            else:
                single_parts.append(s)
                #print(s)

    #print(single_parts)  

    return single_parts


# In[12]:


def fnget_sdql_parts(single_parts):

    sdql_parts=list()
    #print('single parts',single_parts)
    for s in single_parts:
        #print(s)
        if s[:1]!="(": #all shortcuts start with ( 
            has_key=0
            for key,value in shortcuts.items():
                if key in s:
                    has_key=1

            if has_key==0:
                for key,value in singlecuts.items():
                    if key in s:
                        has_key=1
            #print(s,'has key',has_key)   
            if has_key:
                if ',' in s:
                    #for groupings H,A or F,D etc.
                    pair=fnsplit(s,',')
                    #print('1',pair[0])
                    #print('2',pair[1])
                    sdql_parts=fnpush_sdql_parts(pair[0],sdql_parts)
                    sdql_parts[len(sdql_parts)-1]='('+sdql_parts[len(sdql_parts)-1]
                    sdql_parts.append("|")
                    sdql_parts=fnpush_sdql_parts(pair[1],sdql_parts)
                    sdql_parts[len(sdql_parts)-1]=sdql_parts[len(sdql_parts)-1]+')'
                else:
                    fnpush_sdql_parts(s,sdql_parts)
                
            else:
                sdql_parts.append(s)

        else:
            sdql_parts.append(s)

        #print('converted',sdql_parts[len(sdql_parts)-1])
    #sdql_parts=fnfix_string(sdql_parts,operators)
    #print('-----------------------------------------------------------------------------------------------')

    #print(sdql_parts)
        
    return sdql_parts


# In[13]:


def fnpush_sdql_parts(s,sdql_parts):

    ### fnpush_sdql_parts NOT fnsdql_parts
    
    #print('---------------------')
    #print('S',s)
    prefix=s[:s.find(':')+1]
    #print('prefix',prefix)

    scut=s[s.find(':')+1:]
    #print(s,"prefix",prefix,"suffix",scut)
    #input("Enter : ")
    as_pos=scut.find(' as ')
    if as_pos<=0:
        as_pos=len(scut)
    if scut.strip()==scut[:as_pos].upper().strip():
        #print('same as upper',s)
        for key,value in singlecuts.items():
            #print(key,':',value)
            if scut.find(key)>0 or scut==key:
                scut=scut.replace(key,value)
                break
    if prefix!='':

        for j in range(0,len(prefix)):
            if prefix[j:j+1] not in "(opPnNsS:":
                #print('J',j,prefix[j:j+1])
                #prefix=''
                break
                #j+=1    


        #print('Before:')
        #print('prefix',prefix)
        #print('scut',scut)
        prefix_used=0
        o_used=t_used=0
        for p in parameters:

            if p+':' in scut:
                #print('found',p+':',prefix)
                if p not in prefix or len(prefix)>1:
                    if p=='o':
                        #3/0
                        if o_used==0:
                            scut=scut.replace(p+':',prefix.replace(':','')+p+':')
                            o_used=1


                    else:
                        if t_used==0:
                            scut=scut.replace(p+':',p+prefix+':')
                            scut=scut.replace('::',':')
                            scut=scut.replace(p+':',prefix.replace(':','')+p+':')
                            t_used=1
                    prefix_used=1

        else:
            y=''
            #scut=prefix+scut
        if prefix_used==1:
            prefix=''
        #print('After:',prefix,scut)
        sdql_parts.append(prefix+scut)

    else:
        sdql_parts.append(scut)
    
    return sdql_parts


# In[14]:


def fnget_sdql_terms(sdql_parts,operators):
    sdql_terms=''
    p=0
    for j in sdql_parts:
        #print('*'+j+'*',p)
        if j=='and':
            j=' and '
        if p==0 or fnhas_operator(j,operators)==1:
            pad=''
            p=1
        else:
            pad=' '
        sdql_terms+=pad+j
        sdql_terms=sdql_terms.replace('p:(1*','(p:').replace('  ',' ')
    sdql_terms=sdql_terms.replace(' |',',')
    
    #print(sdql_terms)
    return sdql_terms


# In[15]:


def fncolumn_format(jsondata,headers,columns):
    #headers = data['headers']
    #headers.append('sdql as terms')
    columns = [d['columns'] for d in jsondata['groups']]
    sdqls = ["".join(d['sdql as terms']) for d in jsondata['groups']]
    
    for col, sdql in zip(columns, sdqls):
        col.append([sdql])
    
    tables = []
    for c in columns:
        pt = PrettyTable()
        for header, column in zip(headers, c):
            if len(column) != len(pt._rows):
                column += ['-'] * (len(pt._rows) - len(column))
            pt.add_column(header, column)
        tables.append(pt)

    tables_json = []
    all_data = []
    for table in tables:
        tables_json.append(json.loads(table.get_json_string()))

    for table in tables_json:
        for t in table:
            if t == headers:
                continue
            all_data.append(t)

    big_table = PrettyTable()
    #print(headers)
    big_table.field_names = headers
    for row in all_data:
        values = []
        for header in headers:
            values.append(row[header])
        big_table.add_row(values)
    return big_table

def get_converted_query(query):
    sdql_parts_in=list(query.split(" "))
    sdql_data=fnget_sdql_data(sdql_parts_in,shortcuts)
    grouping_format=fngrouping_format_check(groupby,sdql_data)
    column_format=fncolumn_format_check(sdql_data)
    single_parts=fnget_single_parts(sdql_data)
    sdql_parts=fnget_sdql_parts(single_parts)
    sdql_terms=fnget_sdql_terms(sdql_parts,operators)
    format_no = 0
    converted_query = ""
    if grouping_format == 1:
        converted_query = "t:team,t:points,o:points,t:line,total@"+sdql_terms
        format_no = 1
    else:
        if column_format == 1:
            ##Column format
            ## has an @
            converted_query = sdql_terms
            format_no = 3
        else:
            ##Detail format
            #Always being with date,season,day,site,week,line,total,overtime,t:team,t:points,t:rushes,t:rushing yards,t:passes,t:passing yards,t:completions,t:quarter scores,t:turnovers,o:team,o:points,o:rushes,o:rushing yards,o:passes,o:passing yards,o:completions,o:quarter scores,o:turnovers@
            converted_query = "date,season,day,site,week,line,total,overtime,t:team,t:points,t:rushes,t:rushing yards,t:passes,t:passing yards,t:completions,t:quarter scores,t:turnovers,o:team,o:points,o:rushes,o:rushing yards,o:passes,o:passing yards,o:completions,o:quarter scores,o:turnovers@"+sdql_terms
            format_no = 2

    return converted_query, format_no

groupby=list()
groupby=['RSWL','ats margin','ats streak','average punt yards','biggest lead','blocked extra points','blocked field goals','blocked punts','close line','close total','coach','completions','conference','date','day','division','dpa','dps','drives','field goals','field goals attempted','first downs','fourth downs attempted','fourth downs made','fumble return touchdowns','fumble return yards','fumbles','fumbles lost','game number','goal to go attempted','goal to go made','interception return yards','interception returns','interception touchdowns','interceptions','kicking extra points','kicking extra points attempted','kickoff return touchdowns','kickoff return yards','kickoff returns','kickoffs','kickoffs for touchback','kickoffs in end zone','lead changes','line','line sdb','losses','margin','margin after the first','margin after the third','margin at the half','matchup losses','matchup wins','money line','month','open line','open total','opponents','ou margin','ou streak','overtime','passes','passing first downs','passing touchdowns','passing yards','penalties','penalty first downs','penalty yards','playoffs','plays','points','punt return touchdowns','punt return yards','punt returns','punts','quarter scores','red zones attempted','red zones made','regular season wins line','rest','return yards','rushes','rushes for a loss','rushing first downs','rushing touchdowns','rushing yards','rushing yards lost','sack yards','sacks','safeties','scored first','season','site','site streak','snf','start time','streak','surface','team','temperature','third downs attempted','third downs made','time of possession','time zone','times tied','total','touchdowns','turnover margin','turnovers','two point conversion attempts','two point conversions','two point conversions attempted','week','wins']

shortcuts,singlecuts=fnget_shortcuts()
strings=fnget_strings()
operators=['!','=','>','<','+','/','-','*']
parameters=['t','o','p','P','n','N','s','S']

