# import json
# import re
# from prettytable import PrettyTable

# token="eS1waYB1pt5B"

# def fnhas_operator(checkme,operators):
#     foundit=0
#     for symbol in operators:
#         if symbol in checkme:
#             foundit=1
#             break
#     return foundit


# # In[4]:


# def fnget_shortcuts():
#     shortcuts=dict()
#     shortcuts.update({"ATSL":"(t:points+t:line<o:points) as 'ATSL'"})
#     shortcuts.update({"ATSW":"(t:points+t:line>to:points) as 'ATSW'"})
#     shortcuts.update({"o:AWP":"(Average(100*(((0<o:points-t:points) as 'o:W' or (0<t:points-o:points) as 'o:L' or 1/0) and (0<o:points-t:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'"})    
#     shortcuts.update({"AWP":"(Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season and site='away')) as 'AWP'"})
#     shortcuts.update({"3DM":"(1*third downs made) as '3DM'"})
#     shortcuts.update({"3DA":"(1*third downs attempted) as '3DA'"})
#     shortcuts.update({"3DF":"(t:third downs attempted-t:third downs made) as '3DF'"})
#     shortcuts.update({"3DP":"(100.*t:third downs made/t:third downs attempted) as '3DP'"})
#     shortcuts.update({"4DM":"(1*fourth downs made) as '4DM'"})
#     shortcuts.update({"4DA":"(1*fourth downs attempted) as '4DA'"})
#     shortcuts.update({"4DF":"(t:fourth downs attempted-t:fourth downs made) as '4DF'"})
#     shortcuts.update({"4DP":"(100.*t:fourth downs made/t:fourth downs attempted) as '4DP'"})
#     shortcuts.update({"COMP":"(1*completions) as 'COMP'"})
#     shortcuts.update({"CP":"(100.*t:completions/t:passes) as 'CP'"})
#     shortcuts.update({"NDIV":"(t:division!=o:division) as 'NDIV'"})
#     shortcuts.update({"DIV":"(t:division=o:division) as 'DIV'"})
#     shortcuts.update({"DTD":"(t:interception touchdowns+t:fumble return touchdowns) as 'DTD'"})
#     shortcuts.update({"FDP":"(100.*t:first downs/(t:rushes+t:passes+o:sacks)''"})
#     shortcuts.update({"FG":"(1*field goals) as 'FG'"})
#     shortcuts.update({"FUML":"(1*fumbles lost) as 'FUML'"})
#     shortcuts.update({"FUM":"(1*fumbles) as 'FUM'"})
#     shortcuts.update({"GTGA":"(1*goal to go attempted) as 'GTGA'"})
#     shortcuts.update({"GTGF":"(1*goal to go attempted-goal to go made) as 'GTGF'"})
#     shortcuts.update({"GTGM":"(1*goal to go made) as 'GTGM'"})
#     shortcuts.update({"o:HWP":"(Average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'"})
#     shortcuts.update({"HWP":" (Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season and site='home')) as 'HWP'"})
#     shortcuts.update({"INC":"(t:passes-t:completions) as 'INC'"})
#     shortcuts.update({"INT":"(1*interceptions) as 'INT'"})
#     shortcuts.update({"M1":"(sum(t:quarter scores[:1])-sum(o:quarter scores[:1])) as 'M1'"})
#     shortcuts.update({"M2":"(sum(t:quarter scores[:2])-sum(o:quarter scores[:2])) as 'M2'"})
#     shortcuts.update({"M3":"(sum(t:quarter scores[:3])-sum(o:quarter scores[:3])) as 'M3'"})
#     shortcuts.update({"NOTD":"(t:touchdowns-t:rushing touchdowns-t:passing touchdowns) as 'NOTD'"})
#     shortcuts.update({"OFPL":"(t:passes+t:rushes+o:sacks) as 'OFPL'"})
#     shortcuts.update({"OT":"(1*overtime) as 'OT'"})
#     shortcuts.update({"P1":"(t:quarter scores[0]) as 'P1'"})
#     shortcuts.update({"P2":"(t:quarter scores[1]) as 'P2'"})
#     shortcuts.update({"P3":"(t:quarter scores[2]) as 'P3'"})
#     shortcuts.update({"P4":"(t:quarter scores[3]) as 'P4'"})
#     shortcuts.update({"PENY":"(1*penalty yards) as 'PENY'"})
#     shortcuts.update({"PENFD":"(1*penalty first downs) as 'PENFD'"})
#     shortcuts.update({"PEN":"(1*penalties) as 'PEN'"})
#     shortcuts.update({"PFD":"(1*passing first downs) as 'PFD'"})
#     shortcuts.update({"PO":"(t:playoffs=1) as 'PO'"})
#     shortcuts.update({"PTD":"(1*passing touchdowns) as 'PTD'"})
#     shortcuts.update({"PY":"(1*passing yards) as 'PY'"})
#     shortcuts.update({"RFD":"(1*rushing first downs)''"})
#     shortcuts.update({"RTD":"(1*rushing touchdowns) as 'RTD'"})
#     shortcuts.update({"REG":"(t:playoffs=0) as 'REG'"})
#     shortcuts.update({"RTD":"(1*rushing touchdowns) as 'RTD'"})
#     shortcuts.update({"RY":"(1*rushing yards) as 'RY'"})
#     shortcuts.update({"RZA":"(1*red zones attempted) as 'RZA'"})
#     shortcuts.update({"RZM":"(1*red zones made) as 'RZM'"})
#     shortcuts.update({"RZF":"(t:red zones attempted-red zones made) as 'RZF'"})
#     shortcuts.update({"S1":"(sum(t:quarter scores[:1])) as 'S1'"})
#     shortcuts.update({"S2":"(sum(t:q:uarter scores[:2])) as 'S2'"})
#     shortcuts.update({"S3":"(sum(t:quarter scores[:3])) as 'S3'"})
#     shortcuts.update({"SIQ":"(sum(map(lambda x: x%2!=0, t:quarter scores))) as 'SIQ'"})
#     shortcuts.update({"SY":"(1*sack yards) as 'SY'"})
#     shortcuts.update({"TOM":"(t:turnovers-o:turnovers) as 'TOM'"})
#     shortcuts.update({"TOP":"(1*time of possession) as 'TOP'"})
#     shortcuts.update({"TO":"(1*turnovers) as 'TO'"})
#     shortcuts.update({"TY":"(t:passing yards+t:rushing yards) as 'TY'"})
#     shortcuts.update({"o:WP":"(Average(100*(((0<o:points-t:points) as 'o:W' or (0<t:points-o:points) as 'o:L' or 1/0) and (0<o:points-t:points) as 'o:W')@o:team and o:season)) as 'o:WP'"})
#     shortcuts.update({"WP":"(Average(100*(((0<t:points-o:points) as 'W' or (0<o:points-t:points) as 'L' or 1/0) and (0<t:points-o:points) as 'W')@team and season)) as 'WP'"})
#     shortcuts.update({"YPC":"(t:passing yards/t:completions) as 'YPC'"})
#     shortcuts.update({"YPPL":"((1.*rushing yards+t:passing yards)/(t:rushes+t:passes+o:sacks)) as 'YPPL'"})
#     shortcuts.update({"YPPT":"((1.*rushing yards+t:passing yards)/t:points) as 'YPPT'"})
#     shortcuts.update({"YPPA":"(1.*passing yards/t:passes) as 'YPPA'"})
#     shortcuts.update({"YPPP":"(1.*passing yards/(t:passes+o:sacks)) as 'YPPP'"})
#     shortcuts.update({"YPRA":"(1.*rushing yards/t:rushes) as 'YPRA'"})
#     #shortcuts.update({"o:STDRAPG":"(Average(o:rushes@o:team and o:season and o:season=season)) as 'o:STDRAPG' and game number<0 "})
#     shortcuts.update({"STDRAPG":"(Average(t:rushes@team and season and season=season)) as 'STDRAPG'"})
#     #shortcuts.update({"o:STDoRAPG":"(Average(oo:rushes@o:team and o:season and o:season=season)) as 'o:STDoRAPG' and game number<0"})
#     shortcuts.update({"STDoRAPG":"(Average(o:rushes@team and season and season=season)) as 'STDoRAPG'"})
#     shortcuts.update({"PRSW":" (Sum(((0<t:points-o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'"})

#     shortcuts.update({"FD":"(1*first downs) as 'FD'"})
#     shortcuts.update({"TD":"(1*touchdowns) as 'TD'"})


#     singlecuts=dict()
#     singlecuts.update({"A":"(t:site=='away') as 'A'"})
#     singlecuts.update({"H":"(t:site=='home') as 'H'"})
#     singlecuts.update({"W":"(0<t:points-o:points) as 'W'"})
#     singlecuts.update({"L":"(0<o:points-t:points) as 'L'"})
#     singlecuts.update({"F":"(t:line+0<0) as 'F'"})
#     singlecuts.update({"D":"(t:line+0>0) as 'D'"})
#     singlecuts.update({"O":"(t:total+0<t:points+o:points) as 'O'"})
#     singlecuts.update({"U":"(t:points+o:points< total) as 'U'"})
#     singlecuts.update({"C":"((t:conference = o:conference)) as 'C'"})
    
#     return shortcuts,singlecuts


# # In[83]:


# def fngrouping_format_check(groupby,check_data):
#     grouping=0
#     for g in groupby:
#         if g in check_data and not '@' in check_data:
#             #print(g)
#             grouping=1
            
#     if grouping==0:
#         for item in check_data:
#             if '@' in item:
#                 grouping=0
#                 break

#             if ',' in item and '(' not in item and not '@' in item:
#                 #print(item)
#                 grouping=1
                
#     return grouping 


# # In[6]:


# def fncolumn_format_check(check_data):
#     column_format=0
#     for s in check_data:
#         at_pos=s.find("@")
#         if at_pos>0:
#             if "(" in s[:at_pos] and ")" in s[at_pos+1:]:
#                 column_format=0
#             else:
#                 column_format=1
#     return column_format    


# # In[7]:


# def fnget_strings():
#     strings=list()
#     strings.append('coach')
#     strings.append('conference')
#     strings.append('day')
#     strings.append('division')
#     strings.append('opponents')
#     strings.append('site')
#     strings.append('surface')
#     strings.append('team')
#     strings.append('time zone')
#     return strings


# # In[8]:


# def fnsplit(splitme,delimitor):
#     listoftwo=list()
#     if delimitor in splitme:
#         d_pos=splitme.find(delimitor)
#         listoftwo.append(splitme[:d_pos])
#         listoftwo.append(splitme[d_pos+1:])
#         #print(listoftwo)
#     else:
#         listoftwo=splitme #nothing to split
#     return listoftwo


# # In[9]:



# def fnfix_string(sdql_parts,operators):

#     for i in range(0,len(sdql_parts)):
#         for string in strings:
#             if string in sdql_parts[i]:
#                 if sdql_parts[i].find("'")<=0 and sdql_parts[i].find('""')<=0:
#                     sdql_parts[i]=sdql_parts[i].replace(' ','')
#                     for symbol in operators:
#                         if symbol in sdql_parts[i]:
#                             symbol_pos=sdql_parts[i].find(symbol)
#                             sdql_parts[i]=sdql_parts[i][:symbol_pos+1]+'"'+sdql_parts[i][symbol_pos+1:]+'"'
#                             sdql_parts[i]=sdql_parts[i].replace('"',"'")
#                             break

#                 break
#     return sdql_parts


# # In[10]:



# def fnget_sdql_data(sdql_parts_in,shortcuts):
#     ##replace shortcuts

#     sdql_data=list()
#     #print(sdql_parts_in)
#     for s in sdql_parts_in:
#         if s!='and' and len(s)>1:
#             #if s==s.upper():
#             _count=0
#             for key,value in shortcuts.items():
#                 _count+=1
#                 #print(key,_count)
#                 #if _count==60:
#                     #3/0
#                 if key in s:
#                 #if s==key:
#                     s=s.replace(key,value)
#                     break
#             sdql_data.append(s)
#         else:
#             sdql_data.append(s)
#     #print("sdql_data",sdql_data)
#     return sdql_data


# # In[11]:


# def fnget_single_parts(sdql_data):
#     ##replace singlecusts

#     #print(sdql_data)
#     single_parts=list()
#     for s in sdql_data:

#         try:
#             is_num=float(s)
#             single_parts.append(s)
#         except:

#             if s!='and' and fnhas_operator(s,operators)==0 and ',' not in s:
#                 prefix=s[:s.find(':')+1]
#                 scut=s[s.find(':')+1:]
#                 if scut==scut.upper():
#                     singles=list(scut)
#                     for j in range(0,len(singles)+len(singles)-2):
#                         #print(singles[j],j)
#                         if singles[j].find('and')<=0:
#                             singles.insert(j+1,' and ')

#                     for single in singles:
#                         if single.find('and')<=0:
#                             single_parts.append(prefix+single)
#                         else: 
#                             single_parts.append(single)
#                 else:
#                     single_parts.append(s)
#             else:
#                 single_parts.append(s)
#                 #print(s)

#     #print(single_parts)  

#     return single_parts


# # In[12]:


# def fnget_sdql_parts(single_parts):

#     sdql_parts=list()
#     #print('single parts',single_parts)
#     for s in single_parts:
#         #print(s)
#         if s[:1]!="(": #all shortcuts start with ( 
#             has_key=0
#             for key,value in shortcuts.items():
#                 if key in s:
#                     has_key=1

#             if has_key==0:
#                 for key,value in singlecuts.items():
#                     if key in s:
#                         has_key=1
#             #print(s,'has key',has_key)   
#             if has_key:
#                 if ',' in s:
#                     #for groupings H,A or F,D etc.
#                     pair=fnsplit(s,',')
#                     #print('1',pair[0])
#                     #print('2',pair[1])
#                     sdql_parts=fnpush_sdql_parts(pair[0],sdql_parts)
#                     sdql_parts[len(sdql_parts)-1]='('+sdql_parts[len(sdql_parts)-1]
#                     sdql_parts.append("|")
#                     sdql_parts=fnpush_sdql_parts(pair[1],sdql_parts)
#                     sdql_parts[len(sdql_parts)-1]=sdql_parts[len(sdql_parts)-1]+')'
#                 else:
#                     fnpush_sdql_parts(s,sdql_parts)
                
#             else:
#                 sdql_parts.append(s)

#         else:
#             sdql_parts.append(s)

#         #print('converted',sdql_parts[len(sdql_parts)-1])
#     #sdql_parts=fnfix_string(sdql_parts,operators)
#     #print('-----------------------------------------------------------------------------------------------')

#     #print(sdql_parts)
        
#     return sdql_parts


# # In[13]:


# def fnpush_sdql_parts(s,sdql_parts):

#     ### fnpush_sdql_parts NOT fnsdql_parts
    
#     #print('---------------------')
#     #print('S',s)
#     prefix=s[:s.find(':')+1]
#     #print('prefix',prefix)

#     scut=s[s.find(':')+1:]
#     #print(s,"prefix",prefix,"suffix",scut)
#     #input("Enter : ")
#     as_pos=scut.find(' as ')
#     if as_pos<=0:
#         as_pos=len(scut)
#     if scut.strip()==scut[:as_pos].upper().strip():
#         #print('same as upper',s)
#         for key,value in singlecuts.items():
#             #print(key,':',value)
#             if scut.find(key)>0 or scut==key:
#                 scut=scut.replace(key,value)
#                 break
#     if prefix!='':

#         for j in range(0,len(prefix)):
#             if prefix[j:j+1] not in "(opPnNsS:":
#                 #print('J',j,prefix[j:j+1])
#                 #prefix=''
#                 break
#                 #j+=1    


#         #print('Before:')
#         #print('prefix',prefix)
#         #print('scut',scut)
#         prefix_used=0
#         o_used=t_used=0
#         for p in parameters:

#             if p+':' in scut:
#                 #print('found',p+':',prefix)
#                 if p not in prefix or len(prefix)>1:
#                     if p=='o':
#                         #3/0
#                         if o_used==0:
#                             scut=scut.replace(p+':',prefix.replace(':','')+p+':')
#                             o_used=1


#                     else:
#                         if t_used==0:
#                             scut=scut.replace(p+':',p+prefix+':')
#                             scut=scut.replace('::',':')
#                             scut=scut.replace(p+':',prefix.replace(':','')+p+':')
#                             t_used=1
#                     prefix_used=1

#         else:
#             y=''
#             #scut=prefix+scut
#         if prefix_used==1:
#             prefix=''
#         #print('After:',prefix,scut)
#         sdql_parts.append(prefix+scut)

#     else:
#         sdql_parts.append(scut)
    
#     return sdql_parts


# # In[14]:


# def fnget_sdql_terms(sdql_parts,operators):
#     sdql_terms=''
#     p=0
#     for j in sdql_parts:
#         #print('*'+j+'*',p)
#         if j=='and':
#             j=' and '
#         if p==0 or fnhas_operator(j,operators)==1:
#             pad=''
#             p=1
#         else:
#             pad=' '
#         sdql_terms+=pad+j
#         sdql_terms=sdql_terms.replace('p:(1*','(p:').replace('  ',' ')
#     sdql_terms=sdql_terms.replace(' |',',')
    
#     #print(sdql_terms)
#     return sdql_terms


# # In[15]:


# def fncolumn_format(jsondata,headers,columns):
#     #headers = data['headers']
#     #headers.append('sdql as terms')
#     columns = [d['columns'] for d in jsondata['groups']]
#     sdqls = ["".join(d['sdql as terms']) for d in jsondata['groups']]
    
#     for col, sdql in zip(columns, sdqls):
#         col.append([sdql])
    
#     tables = []
#     for c in columns:
#         pt = PrettyTable()
#         for header, column in zip(headers, c):
#             if len(column) != len(pt._rows):
#                 column += ['-'] * (len(pt._rows) - len(column))
#             pt.add_column(header, column)
#         tables.append(pt)

#     tables_json = []
#     all_data = []
#     for table in tables:
#         tables_json.append(json.loads(table.get_json_string()))

#     for table in tables_json:
#         for t in table:
#             if t == headers:
#                 continue
#             all_data.append(t)

#     big_table = PrettyTable()
#     #print(headers)
#     big_table.field_names = headers
#     for row in all_data:
#         values = []
#         for header in headers:
#             values.append(row[header])
#         big_table.add_row(values)
#     return big_table

# def get_converted_query(query):
#     sdql_parts_in=list(query.split(" "))
#     sdql_data=fnget_sdql_data(sdql_parts_in,shortcuts)
#     grouping_format=fngrouping_format_check(groupby,sdql_data)
#     column_format=fncolumn_format_check(sdql_data)
#     single_parts=fnget_single_parts(sdql_data)
#     sdql_parts=fnget_sdql_parts(single_parts)
#     sdql_terms=fnget_sdql_terms(sdql_parts,operators)
#     format_no = 0
#     converted_query = ""
#     if grouping_format == 1:
#         converted_query = "t:team,t:points,o:points,t:line,total@"+sdql_terms
#         format_no = 1
#     else:
#         if column_format == 1:
#             ##Column format
#             ## has an @
#             converted_query = sdql_terms
#             format_no = 3
#         else:
#             ##Detail format
#             #Always being with date,season,day,site,week,line,total,overtime,t:team,t:points,t:rushes,t:rushing yards,t:passes,t:passing yards,t:completions,t:quarter scores,t:turnovers,o:team,o:points,o:rushes,o:rushing yards,o:passes,o:passing yards,o:completions,o:quarter scores,o:turnovers@
#             converted_query = "date,season,day,site,week,line,total,overtime,t:team,t:points,t:rushes,t:rushing yards,t:passes,t:passing yards,t:completions,t:quarter scores,t:turnovers,o:team,o:points,o:rushes,o:rushing yards,o:passes,o:passing yards,o:completions,o:quarter scores,o:turnovers@"+sdql_terms
#             format_no = 2

#     return converted_query, format_no

# groupby=list()
# groupby=['RSWL','ats margin','ats streak','average punt yards','biggest lead','blocked extra points','blocked field goals','blocked punts','close line','close total','coach','completions','conference','date','day','division','dpa','dps','drives','field goals','field goals attempted','first downs','fourth downs attempted','fourth downs made','fumble return touchdowns','fumble return yards','fumbles','fumbles lost','game number','goal to go attempted','goal to go made','interception return yards','interception returns','interception touchdowns','interceptions','kicking extra points','kicking extra points attempted','kickoff return touchdowns','kickoff return yards','kickoff returns','kickoffs','kickoffs for touchback','kickoffs in end zone','lead changes','line','line sdb','losses','margin','margin after the first','margin after the third','margin at the half','matchup losses','matchup wins','money line','month','open line','open total','opponents','ou margin','ou streak','overtime','passes','passing first downs','passing touchdowns','passing yards','penalties','penalty first downs','penalty yards','playoffs','plays','points','punt return touchdowns','punt return yards','punt returns','punts','quarter scores','red zones attempted','red zones made','regular season wins line','rest','return yards','rushes','rushes for a loss','rushing first downs','rushing touchdowns','rushing yards','rushing yards lost','sack yards','sacks','safeties','scored first','season','site','site streak','snf','start time','streak','surface','team','temperature','third downs attempted','third downs made','time of possession','time zone','times tied','total','touchdowns','turnover margin','turnovers','two point conversion attempts','two point conversions','two point conversions attempted','week','wins']

# shortcuts,singlecuts=fnget_shortcuts()
# strings=fnget_strings()
# operators=['!','=','>','<','+','/','-','*']
# parameters=['t','o','p','P','n','N','s','S']































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
    shortcuts.update({"tS(M1)": "Sum((sum(quarter scores[:1])-sum(to:quarter scores[:1])) as 'M1'@ team and season) as 'tS(M1)'"})
    shortcuts.update({"tA(M1)": "average((sum(quarter scores[:1])-sum(to:quarter scores[:1])) as 'M1'@ team and season) as 'tA(M1)'"})
    shortcuts.update({"tpS(M1)": "(Sum((sum(quarter scores[:1])-sum(to:quarter scores[:1])) as 'M1'@ team and season)[ team and season-1]) as 'tpS(M1)'"})
    shortcuts.update({"oS(M1)": "Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M1'@ o:team and o:season) as 'oS(M1)'"})
    shortcuts.update({"oA(M1)": "average((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M1'@ o:team and o:season) as 'oA(M1)'"})
    shortcuts.update({"opS(M1)": "(Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M1'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(M1)'"})
    shortcuts.update({"tp:M1": "(sum(tp:quarter scores[:1])-sum(too:quarter scores[:1])) as 'tp:M1'"})
    shortcuts.update({"to:M1": "(sum(to:quarter scores[:1])-sum(poo:quarter scores[:1])) as 'to:M1'"})
    shortcuts.update({"op:M1": "(sum(op:quarter scores[:1])-sum(oto:quarter scores[:1])) as 'op:M1'"})
    shortcuts.update({"t:M1": "(sum(t:quarter scores[:1])-sum(tp:quarter scores[:1])) as 't:M1'"})
    shortcuts.update({"p:M1": "(sum(p:quarter scores[:1])-sum(to:quarter scores[:1])) as 'p:M1'"})
    shortcuts.update({"o:M1": "(sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M1'"})
    shortcuts.update({"M1": "(sum(quarter scores[:1])-sum(to:quarter scores[:1])) as 'M1'"})
    shortcuts.update({"tS(M2)": "Sum((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M2'@ team and season) as 'tS(M2)'"})
    shortcuts.update({"tA(M2)": "average((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M2'@ team and season) as 'tA(M2)'"})
    shortcuts.update({"tpS(M2)": "(Sum((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M2'@ team and season)[ team and season-1]) as 'tpS(M2)'"})
    shortcuts.update({"oS(M2)": "Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M2'@ o:team and o:season) as 'oS(M2)'"})
    shortcuts.update({"oA(M2)": "average((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M2'@ o:team and o:season) as 'oA(M2)'"})
    shortcuts.update({"opS(M2)": "(Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M2'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(M2)'"})
    shortcuts.update({"tp:M2": "(sum(tp:quarter scores[:2])-sum(too:quarter scores[:2])) as 'tp:M2'"})
    shortcuts.update({"to:M2": "(sum(to:quarter scores[:2])-sum(poo:quarter scores[:2])) as 'to:M2'"})
    shortcuts.update({"op:M2": "(sum(op:quarter scores[:2])-sum(oto:quarter scores[:2])) as 'op:M2'"})
    shortcuts.update({"t:M2": "(sum(t:quarter scores[:2])-sum(tp:quarter scores[:2])) as 't:M2'"})
    shortcuts.update({"p:M2": "(sum(p:quarter scores[:2])-sum(to:quarter scores[:2])) as 'p:M2'"})
    shortcuts.update({"o:M2": "(sum(o:quarter scores[:2])-sum(oo:quarter scores[:2])) as 'o:M2'"})
    shortcuts.update({"M2": "(sum(quarter scores[:2])-sum(to:quarter scores[:2])) as 'M2'"})
    shortcuts.update({"tS(M3)": "Sum((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M3'@ team and season) as 'tS(M3)'"})
    shortcuts.update({"tA(M3)": "average((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M3'@ team and season) as 'tA(M3)'"})
    shortcuts.update({"tpS(M3)": "(Sum((sum(quarter scores[:1])-sum(tp:quarter scores[:1])) as 'M3'@ team and season)[ team and season-1]) as 'tpS(M3)'"})
    shortcuts.update({"oS(M3)": "Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M3'@ o:team and o:season) as 'oS(M3)'"})
    shortcuts.update({"oA(M3)": "average((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M3'@ o:team and o:season) as 'oA(M3)'"})
    shortcuts.update({"opS(M3)": "(Sum((sum(o:quarter scores[:1])-sum(oo:quarter scores[:1])) as 'o:M3'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(M3)'"})
    shortcuts.update({"tp:M3": "(sum(tp:quarter scores[:3])-sum(too:quarter scores[:3])) as 'tp:M3'"})
    shortcuts.update({"to:M3": "(sum(to:quarter scores[:3])-sum(poo:quarter scores[:3])) as 'to:M3'"})
    shortcuts.update({"op:M3": "(sum(op:quarter scores[:3])-sum(oto:quarter scores[:3])) as 'op:M3'"})
    shortcuts.update({"t:M3": "(sum(t:quarter scores[:3])-sum(tp:quarter scores[:3])) as 't:M3'"})
    shortcuts.update({"p:M3": "(sum(p:quarter scores[:3])-sum(to:quarter scores[:3])) as 'p:M3'"})
    shortcuts.update({"o:M3": "(sum(o:quarter scores[:3])-sum(oo:quarter scores[:3])) as 'o:M3'"})
    shortcuts.update({"M3": "(sum(quarter scores[:3])-sum(to:quarter scores[:3])) as 'M3'"})
    shortcuts.update({"tS(ATSL)": "Sum((points+line<tp:points) as 'ATSL')"})
    shortcuts.update({"tpS(ATSL)": "(Sum((points+line<tp:points) as 'ATSL'@ team and season)[ team and season-1]) as 'tpS(ATSL)"})
    shortcuts.update({"tA(ATSL)": "average((points+line<tp:points) as 'ATSL'@ team and season) as 'tA(ATSL)'"})
    shortcuts.update({"oS(ATSL)": "Sum((o:points+o:line<oo:points) as 'o:ATSL'@ o:team and o:season) as 'oS(ATSL)'"})
    shortcuts.update({"oA(ATSL)": "average((o:points+o:line<oo:points) as 'o:ATSL'@ o:team and o:season) as 'oA(ATSL)'"})
    shortcuts.update({"opS(ATSL)": "(Sum((o:points+o:line<oo:points) as 'o:ATSL'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(ATSL)'"})
    shortcuts.update({"t:ATSL": "(t:points+t:line<tp:points) as 't:ATSL"})
    shortcuts.update({"p:ATSL": "(p:points+p:line<to:points) as 'p:ATSL'"})
    shortcuts.update({"o:ATSL": "(o:points+o:line<oo:points) as 'o:ATSL'"})
    shortcuts.update({"tp:ATSL": "((tp:points+tp:line<too:points) as 'tp:ATSL'"})
    shortcuts.update({"to:ATSL": "(to:points+to:line<poo:points) as 'to:ATSL'"})
    shortcuts.update({"op:ATSL": "(op:points+op:line<oto:points) as 'op:ATSL'"})
    shortcuts.update({"ATSL": "(points+line<tp:points) as 'ATSL'"})
    shortcuts.update({"tS(ATSW)": "Sum((points+line>tp:points) as 'ATSW')"})
    shortcuts.update({"tpS(ATSW)": "(Sum((points+line>tp:points) as 'ATSW'@ team and season)[ team and season-1]) as 'tpS(ATSW)'"})
    shortcuts.update({"tA(ATSW)": "average((points+line>tp:points) as 'ATSW'@ team and season) as 'tA(ATSW)'"})
    shortcuts.update({"oS(ATSW)": "Sum((o:points+o:line>oo:points) as 'o:ATSW'@ o:team and o:season) as 'oS(ATSW)'"})
    shortcuts.update({"oA(ATSW)": "average((o:points+o:line>oo:points) as 'o:ATSW'@ o:team and o:season) as 'oA(ATSW)'"})
    shortcuts.update({"opS(ATSW)": "(Sum((o:points+o:line>oo:points) as 'o:ATSW'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(ATSW)'"})
    shortcuts.update({"t:ATSW": "(t:points+t:line>tp:points) as 't:ATSW"})
    shortcuts.update({"p:ATSW": "(p:points+p:line>to:points) as 'p:ATSW'"})
    shortcuts.update({"o:ATSW": "(o:points+o:line>oo:points) as 'o:ATSW'"})
    shortcuts.update({"tp:ATSW": "((tp:points+tp:line>too:points) as 'tp:ATSW'"})
    shortcuts.update({"to:ATSW": "(to:points+to:line>poo:points) as 'to:ATSW'"})
    shortcuts.update({"op:ATSW": "(op:points+op:line>oto:points) as 'op:ATSW'"})
    shortcuts.update({"ATSW": "(points+line>tp:points) as 'ATSW'"})
    shortcuts.update({"tS(NDIV)": "Sum((division!=to:division) as 'NDIV'@ team and season) as 'tS(NDIV)'"})
    shortcuts.update({"tA(NDIV)": "average((division!=to:division) as 'NDIV'@ team and season) as 'tA(NDIV)'"})
    shortcuts.update({"tpS(NDIV)": "(Sum((division!=to:division) as 'NDIV'@ team and season)[ team and season-1]) as 'tpS(NDIV)'"})
    shortcuts.update({"oS(NDIV)": "Sum((o:division!=oo:division) as 'o:NDIV'@ o:team and o:season) as 'oS(NDIV)'"})
    shortcuts.update({"oA(NDIV)": "average((o:division!=oo:division) as 'o:NDIV'@ o:team and o:season) as 'oA(NDIV)'"})
    shortcuts.update({"opS(NDIV)": "(Sum((o:division!=oo:division) as 'o:NDIV'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(NDIV)'"})
    shortcuts.update({"tp:NDIV": "(tp:division!=tpo:division) as 'tp:NDIV'"})
    shortcuts.update({"to:NDIV": " (to:division!=too:division) as 'to:NDIV'"})
    shortcuts.update({"op:NDIV": "(op:division!=opo:division) as 'op:NDIV'"})
    shortcuts.update({"t:NDIV": "(t:division!=to:division) as 't:NDIV'"})
    shortcuts.update({"p:NDIV": "(p:division!=po:division) as 'p:NDIV'"})
    shortcuts.update({"o:NDIV": "(o:division!=oo:division) as 'o:NDIV'"})
    shortcuts.update({"NDIV": "(division!=to:division) as 'NDIV' "})
    shortcuts.update({"tS(DIV)": "Sum((division=tp:division) as 'DIV'@ team and season) as 'tS(DIV)'"})
    shortcuts.update({"tA(DIV)": "average((division=tp:division) as 'DIV'@ team and season) as 'tS(DIV)'"})
    shortcuts.update({"tpS(DIV)": "(Sum((division=tp:division) as 'DIV'@ team and season)[ team and season-1]) as 'tpS(DIV)'"})
    shortcuts.update({"oS(DIV)": "Sum((o:division=oo:division) as 'o:DIV'@ o:team and o:season) as 'oS(DIV)'"})
    shortcuts.update({"oA(DIV)": "average((o:division=oo:division) as 'o:DIV'@ o:team and o:season) as 'oS(DIV)'"})
    shortcuts.update({"opS(DIV)": "(Sum((o:division=oo:division) as 'o:DIV'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(DIV)'"})
    shortcuts.update({"tp:DIV": "(tp:division=too:division) as 'tp:DIV' "})
    shortcuts.update({"to:DIV": "(to:division=poo:division) as 'to:DIV' "})
    shortcuts.update({"op:DIV": "(op:division=oto:division) as 'op:DIV'  "})
    shortcuts.update({"t:DIV": "(t:division=tp:division) as 't:DIV' "})
    shortcuts.update({"p:DIV": "(p:division=to:division) as 'p:DIV' "})
    shortcuts.update({"o:DIV": "(o:division=oo:division) as 'p:DIV' "})
    shortcuts.update({"DIV": "(division=tp:division) as 'DIV'"})
    shortcuts.update({"tS(3DM)": "Sum((1*third downs made) as '3DM'@ team and season) as 'tS(3DM)'"})
    shortcuts.update({"tA(3DM)": "average((1*third downs made) as '3DM'@ team and season) as 'tS(3DM)'"})
    shortcuts.update({"tpS(3DM)": "(Sum((1*third downs made) as '3DM'@ team and season)[ team and season-1]) as 'tpS(3DM)'"})
    shortcuts.update({"oS(3DM)": "Sum((1*o:third downs made) as 'o:3DM'@ o:team and o:season) as 'oS(3DM)'"})
    shortcuts.update({"oA(3DM)": "average((1*o:third downs made) as 'o:3DM'@ o:team and o:season) as 'oS(3DM)'"})
    shortcuts.update({"opS(3DM)": "(Sum((1*third downs made) as '3DM'@ team and season)[ team and season-1]) as 'tpS(3DM)'"})
    shortcuts.update({"t:3DM": "(1*third downs made) as '3DM'"})
    shortcuts.update({"tp:3DM": "(1*tp:third downs made) as 'tp:3DM'"})
    shortcuts.update({"to:3DM": "(1*to:third downs made) as 'to:3DM'"})
    shortcuts.update({"op:3DM": "(1*op:third downs made) as 'op:3DM'"})
    shortcuts.update({"t:3DM": "(1*t:third downs made) as 't:3DM'"})
    shortcuts.update({"p:3DM": "(1*p:third downs made) as 'p:3DM'"})
    shortcuts.update({"o:3DM": "(1*o:third downs made) as 'o:3DM'"})
    shortcuts.update({"3DM": "(1*third downs made) as '3DM'"})
    shortcuts.update({"tS(3DA)": "Sum((1*third downs attempted) as '3DA'@ team and season) as 'tS(3DA)'"})
    shortcuts.update({"tA(3DA)": "average((1*third downs attempted) as '3DA'@ team and season) as 'tS(3DA)'"})
    shortcuts.update({"tpS(3DA)": "(Sum((1*third downs attempted) as '3DA'@ team and season)[ team and season-1]) as 'tpS(3DA)'"})
    shortcuts.update({"oS(3DA)": "Sum((1*o:third downs attempted) as 'o:3DA'@ o:team and o:season) as 'oS(3DA)'"})
    shortcuts.update({"oA(3DA)": "average((1*o:third downs attempted) as 'o:3DA'@ o:team and o:season) as 'oS(3DA)'"})
    shortcuts.update({"opS(3DA)": "(Sum((1*third downs attempted) as '3DA'@ team and season)[ team and season-1]) as 'tpS(3DA)'"})
    shortcuts.update({"tp:3DA": "(1*tp:third downs attempted) as 'tp:3DA'"})
    shortcuts.update({"to:3DA": "(1*to:third downs attempted) as 'to:3DA'"})
    shortcuts.update({"op:3DA": "(1*op:third downs attempted) as 'op:3DA'"})
    shortcuts.update({"t:3DA": "(1*t:third downs attempted) as 't:3DA'"})
    shortcuts.update({"p:3DA": "(1*p:third downs attempted) as 'p:3DA'"})
    shortcuts.update({"o:3DA": "(1*o:third downs attempted) as 'o:3DA'"})
    shortcuts.update({"3DA": "(1*third downs attempted) as '3DA'"})
    shortcuts.update({"tS(3DF)": "Sum((third downs attempted-third downs made) as '3DF'@ team and season) as 'tS(3DF)'"})
    shortcuts.update({"tA(3DF)": "average((third downs attempted-third downs made) as '3DF'@ team and season) as 'tS(3DF)'"})
    shortcuts.update({"tpS(3DF)": "(Sum((third downs attempted-third downs made) as '3DF'@ team and season)[ team and season-1]) as 'tpS(3DF)'"})
    shortcuts.update({"oS(3DF)": "Sum((o:third downs attempted-o:third downs made) as 'o:3DF'@ o:team and o:season) as 'oS(3DF)'"})
    shortcuts.update({"oA(3DF)": "average((o:third downs attempted-o:third downs made) as 'o:3DF'@ o:team and o:season) as 'oS(3DF)'"})
    shortcuts.update({"opS(3DF)": "(Sum((o:third downs attempted-o:third downs made) as 'o:3DF'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(3DF)'"})
    shortcuts.update({"tp:3DF": "(tp:third downs attempted-tp:third downs made) as 'tp:3DF'"})
    shortcuts.update({"to:3DF": "(to:third downs attempted-to:third downs made) as 'to:3DF' "})
    shortcuts.update({"op:3DF": "(op:third downs attempted-op:third downs made) as 'op:3DF'"})
    shortcuts.update({"t:3DF": "(t:third downs attempted-t:third downs made) as 't:3DF'"})
    shortcuts.update({"p:3DF": "(p:third downs attempted-p:third downs made) as 'p:3DF' "})
    shortcuts.update({"o:3DF": "(o:third downs attempted-o:third downs made) as 'o:3DF' "})
    shortcuts.update({"3DF": "(third downs attempted-third downs made) as '3DF' "})
    shortcuts.update({"tS(3DP)": "Sum((third downs made-third downs attempted) as '3DP'@ team and season) as 'tS(3DP)'"})
    shortcuts.update({"tA(3DP)": "average((third downs made-third downs attempted) as '3DP'@ team and season) as 'tS(3DP)'"})
    shortcuts.update({"tpS(3DP)": "(Sum((third downs made-third downs attempted) as '3DP'@ team and season)[ team and season-1]) as 'tpS(3DP)'"})
    shortcuts.update({"oS(3DP)": "Sum((o:third downs made-o:third downs attempted) as 'o:3DP'@ o:team and o:season) as 'oS(3DP)'"})
    shortcuts.update({"oA(3DP)": "average((o:third downs made-o:third downs attempted) as 'o:3DP'@ o:team and o:season) as 'oS(3DP)'"})
    shortcuts.update({"opS(3DP)": "(Sum((o:third downs made-o:third downs attempted) as 'o:3DP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(3DP)'"})
    shortcuts.update({"tp:3DP": "(tp:third downs made-tp:third downs attempted) as 'tp:3DP'"})
    shortcuts.update({"to:3DP": "(to:third downs made-to:third downs attempted) as 'to:3DP' "})
    shortcuts.update({"op:3DP": "(op:third downs made-op:third downs attempted) as 'op:3DP'"})
    shortcuts.update({"t:3DP": "(t:third downs made-t:third downs attempted) as 't:3DP'"})
    shortcuts.update({"p:3DP": "(p:third downs made-p:third downs attempted) as 'p:3DP' "})
    shortcuts.update({"o:3DP": "(o:third downs made-o:third downs attempted) as 'o:3DP' "})
    shortcuts.update({"3DP": "(third downs made-third downs attempted) as '3DP' "})
    shortcuts.update({"tS(4DM)": "Sum((1*fourth downs made) as '4DM'@ team and season) as 'tS(4DM)'"})
    shortcuts.update({"tA(4DM)": "average((1*fourth downs made) as '4DM'@ team and season) as 'tS(4DM)'"})
    shortcuts.update({"tpS(4DM)": "(Sum((1*fourth downs made) as '4DM'@ team and season)[ team and season-1]) as 'tpS(4DM)'"})
    shortcuts.update({"oS(4DM)": "Sum((1*o:fourth downs made) as 'o:4DM'@ o:team and o:season) as 'oS(4DM)'"})
    shortcuts.update({"oA(4DM)": "average((1*o:fourth downs made) as 'o:4DM'@ o:team and o:season) as 'oS(4DM)'"})
    shortcuts.update({"opS(4DM)": "(Sum((1*fourth downs made) as '4DM'@ team and season)[ team and season-1]) as 'tpS(4DM)'"})
    shortcuts.update({"tp:4DM": "(1*tp:fourth downs made) as 'tp:4DM'"})
    shortcuts.update({"to:4DM": "(1*to:fourth downs made) as 'to:4DM'"})
    shortcuts.update({"op:4DM": "(1*op:fourth downs made) as 'op:4DM'"})
    shortcuts.update({"t:4DM": "(1*t:fourth downs made) as 't:4DM'"})
    shortcuts.update({"p:4DM": "(1*p:fourth downs made) as 'p:4DM'"})
    shortcuts.update({"o:4DM": "(1*o:fourth downs made) as 'o:4DM'"})
    shortcuts.update({"t:4DM": "(1*fourth downs made) as '4DM'"})
    shortcuts.update({"tS(4DA)": "Sum((1*fourth downs attempted) as '4DA'@ team and season) as 'tS(4DA)'"})
    shortcuts.update({"tA(4DA)": "average((1*fourth downs attempted) as '4DA'@ team and season) as 'tS(4DA)'"})
    shortcuts.update({"tpS(4DA)": "(Sum((1*fourth downs attempted) as '4DA'@ team and season)[ team and season-1]) as 'tpS(4DA)'"})
    shortcuts.update({"oS(4DA)": "Sum((1*o:fourth downs attempted) as 'o:4DA'@ o:team and o:season) as 'oS(4DA)'"})
    shortcuts.update({"oA(4DA)": "average((1*o:fourth downs attempted) as 'o:4DA'@ o:team and o:season) as 'oS(4DA)'"})
    shortcuts.update({"opS(4DA)": "(Sum((1*fourth downs attempted) as '4DA'@ team and season)[ team and season-1]) as 'tpS(4DA)'"})
    shortcuts.update({"tp:4DA": "(1*tp:fourth downs attempted) as 'tp:4DA'"})
    shortcuts.update({"to:4DA": "(1*to:fourth downs attempted) as 'to:4DA'"})
    shortcuts.update({"op:4DA": "(1*op:fourth downs attempted) as 'op:4DA'"})
    shortcuts.update({"t:4DA": "(1*t:fourth downs attempted) as 't:4DA'"})
    shortcuts.update({"p:4DA": "(1*p:fourth downs attempted) as 'p:4DA'"})
    shortcuts.update({"o:4DA": "(1*o:fourth downs attempted) as 'o:4DA'"})
    shortcuts.update({"4DA": "(1*fourth downs attempted) as '4DA'"})
    shortcuts.update({"tS(4DF)": "Sum((fourth downs attempted-fourth downs made) as '4DF'@ team and season) as 'tS(4DF)'"})
    shortcuts.update({"tA(4DF)": "average((fourth downs attempted-fourth downs made) as '4DF'@ team and season) as 'tS(4DF)'"})
    shortcuts.update({"tpS(4DF)": "(Sum((fourth downs attempted-fourth downs made) as '4DF'@ team and season)[ team and season-1]) as 'tpS(4DF)'"})
    shortcuts.update({"oS(4DF)": "Sum((o:fourth downs attempted-o:fourth downs made) as 'o:4DF'@ o:team and o:season) as 'oS(4DF)'"})
    shortcuts.update({"oA(4DF)": "average((o:fourth downs attempted-o:fourth downs made) as 'o:4DF'@ o:team and o:season) as 'oS(4DF)'"})
    shortcuts.update({"opS(4DF)": "(Sum((o:fourth downs attempted-o:fourth downs made) as 'o:4DF'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(4DF)'"})
    shortcuts.update({"tp:4DF": "(tp:fourth downs attempted-tp:fourth downs made) as 'tp:4DF'"})
    shortcuts.update({"to:4DF": "(to:fourth downs attempted-to:fourth downs made) as 'to:4DF' "})
    shortcuts.update({"op:4DF": "(op:fourth downs attempted-op:fourth downs made) as 'op:4DF'"})
    shortcuts.update({"t:4DF": "(t:fourth downs attempted-t:fourth downs made) as 't:4DF'"})
    shortcuts.update({"p:4DF": "(p:fourth downs attempted-p:fourth downs made) as 'p:4DF' "})
    shortcuts.update({"o:4DF": "(o:fourth downs attempted-o:fourth downs made) as 'o:4DF' "})
    shortcuts.update({"4DF": "(fourth downs attempted-fourth downs made) as '4DF' "})
    shortcuts.update({"tS(4DP)": "Sum((fourth downs made-fourth downs attempted) as '4DP'@ team and season) as 'tS(4DP)'"})
    shortcuts.update({"tA(4DP)": "average((fourth downs made-fourth downs attempted) as '4DP'@ team and season) as 'tS(4DP)'"})
    shortcuts.update({"tpS(4DP)": "(Sum((fourth downs made-fourth downs attempted) as '4DP'@ team and season)[ team and season-1]) as 'tpS(4DP)'"})
    shortcuts.update({"oS(4DP)": "Sum((o:fourth downs made-o:fourth downs attempted) as 'o:4DP'@ o:team and o:season) as 'oS(4DP)'"})
    shortcuts.update({"oA(4DP)": "average((o:fourth downs made-o:fourth downs attempted) as 'o:4DP'@ o:team and o:season) as 'oS(4DP)'"})
    shortcuts.update({"opS(4DP)": "(Sum((o:fourth downs made-o:fourth downs attempted) as 'o:4DP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(4DP)'"})
    shortcuts.update({"tp:4DP": "(tp:fourth downs made-tp:fourth downs attempted) as 'tp:4DP'"})
    shortcuts.update({"to:4DP": "(to:fourth downs made-to:fourth downs attempted) as 'to:4DP'"})
    shortcuts.update({"op:4DP": "(op:fourth downs made-op:fourth downs attempted) as 'op:4DP'"})
    shortcuts.update({"t:4DP": "(t:fourth downs made-t:fourth downs attempted) as 't:4DP'"})
    shortcuts.update({"p:4DP": "(p:fourth downs made-p:fourth downs attempted) as 'p:4DP'"})
    shortcuts.update({"o:4DP": "(o:fourth downs made-o:fourth downs attempted) as 'o:4DP'"})
    shortcuts.update({"4DP": "(fourth downs made-fourth downs attempted) as '4DP'"})
    shortcuts.update({"tS(COMP)": "Sum((1*completions) as 'COMP'@ team and season) as 'tS(COMP)'"})
    shortcuts.update({"tA(COMP)": "average((1*completions) as 'COMP'@ team and season) as 'tS(COMP)'"})
    shortcuts.update({"tpS(COMP)": "(Sum((1*completions) as 'COMP'@ team and season)[ team and season-1]) as 'tpS(COMP)'"})
    shortcuts.update({"oS(COMP)": "Sum((1*o:completions) as 'o:COMP'@ o:team and o:season) as 'oS(COMP)'"})
    shortcuts.update({"oA(COMP)": "average((1*o:completions) as 'o:COMP'@ o:team and o:season) as 'oS(COMP)'"})
    shortcuts.update({"opS(COMP)": "(Sum((1*completions) as 'COMP'@ team and season)[ team and season-1]) as 'tpS(COMP)'"})
    shortcuts.update({"tp:COMP": "(1*tp:completions) as 'tp:COMP'"})
    shortcuts.update({"to:COMP": "(1*to:completions) as 'to:COMP'"})
    shortcuts.update({"op:COMP": "(1*op:completions) as 'op:COMP'"})
    shortcuts.update({"t:COMP": "(1*t:completions) as 't:COMP'"})
    shortcuts.update({"p:COMP": "(1*p:completions) as 'p:COMP'"})
    shortcuts.update({"o:COMP": "(1*o:completions) as 'o:COMP'"})
    shortcuts.update({"COMP": "(1*completions) as 'COMP'"})
    shortcuts.update({"tS(CP)": "Sum((100.*completions/passes) as 'CP'@ team and season) as 'tS(CP)'"})
    shortcuts.update({"tA(CP)": "average((100.*completions/passes) as 'CP'@ team and season) as 'tS(CP)'"})
    shortcuts.update({"tpS(CP)": "(Sum((100.*completions/passes) as 'CP'@ team and season)[ team and season-1]) as 'tpS(CP)'"})
    shortcuts.update({"oS(CP)": "Sum((100.*o:completions/o:passes) as 'o:CP'@ o:team and o:season) as 'oS(CP)'"})
    shortcuts.update({"oA(CP)": "average((100.*o:completions/o:passes) as 'o:CP'@ o:team and o:season) as 'oS(CP)'"})
    shortcuts.update({"opS(CP)": "(Sum((100.*o:completions/o:passes) as 'o:CP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(CP)'"})
    shortcuts.update({"tp:CP": "(100.*tp:completions/tp:passes) as 'tp:CP'"})
    shortcuts.update({"to:CP": "(100.*to:completions/to:passes) as 'to:CP'"})
    shortcuts.update({"op:CP": "(100.*op:completions/op:passes) as 'op:CP'"})
    shortcuts.update({"t:CP": "(100.*t:completions/t:passes) as 't:CP'"})
    shortcuts.update({"p:CP": "(100.*p:completions/p:passes) as 'p:CP'"})
    shortcuts.update({"o:CP": "(100.*o:completions/o:passes) as 'o:CP'"})
    shortcuts.update({"CP": "(100.*completions/passes) as 'CP'"})
    shortcuts.update({"tS(DTD)": "Sum((interception touchdowns+fumble return touchdowns) as 'DTD'@ team and season) as 'tS(DTD)'"})
    shortcuts.update({"tA(DTD)": "average((interception touchdowns+fumble return touchdowns) as 'DTD'@ team and season) as 'tS(DTD)'"})
    shortcuts.update({"tpS(DTD)": "(Sum((interception touchdowns+fumble return touchdowns) as 'DTD'@ team and season)[ team and season-1]) as 'tpS(DTD)'"})
    shortcuts.update({"oS(DTD)": "Sum((o:interception touchdowns+o:fumble return touchdowns) as 'o:DTD'@ o:team and o:season) as 'oS(DTD)'"})
    shortcuts.update({"oA(DTD)": "average((o:interception touchdowns+o:fumble return touchdowns) as 'o:DTD'@ o:team and o:season) as 'oS(DTD)'"})
    shortcuts.update({"opS(DTD)": "(Sum((o:interception touchdowns+o:fumble return touchdowns) as 'o:DTD'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(DTD)' "})
    shortcuts.update({"tp:DTD": "(tp:interception touchdowns+tp:fumble return touchdowns) as 'tp:DTD'"})
    shortcuts.update({"to:DTD": "(to:interception touchdowns+to:fumble return touchdowns) as 'to:DTD'"})
    shortcuts.update({"op:DTD": "(op:interception touchdowns+op:fumble return touchdowns) as 'op:DTD'"})
    shortcuts.update({"t:DTD": "(t:interception touchdowns+t:fumble return touchdowns) as 't:DTD'"})
    shortcuts.update({"p:DTD": "(p:interception touchdowns+p:fumble return touchdowns) as 'p:DTD'"})
    shortcuts.update({"o:DTD":  "(o:interception touchdowns+o:fumble return touchdowns) as 'o:DTD'"})
    shortcuts.update({"DTD": "(interception touchdowns+fumble return touchdowns) as 'DTD'"})
    shortcuts.update({"tS(FDP)": "Sum((100.*first downs/(rushes+passes+tp:sacks)) as 'FDP'@ team and season) as 'tS(FDP)'"})
    shortcuts.update({"tA(FDP)": "average((100.*first downs/(rushes+passes+tp:sacks)) as 'FDP'@ team and season) as 'tS(FDP)'"})
    shortcuts.update({"tpS(FDP)": "(Sum((100.*first downs/(rushes+passes+tp:sacks)) as 'FDP'@ team and season)[ team and season-1]) as 'tpS(FDP)'"})
    shortcuts.update({"oS(FDP)": "Sum((100.*o:first downs/(o:rushes+o:passes+oo:sacks)) as 'o:FDP'@ o:team and o:season) as 'oS(FDP)'"})
    shortcuts.update({"oA(FDP)": "average((100.*o:first downs/(o:rushes+o:passes+oo:sacks)) as 'o:FDP'@ o:team and o:season) as 'oS(FDP)'"})
    shortcuts.update({"opS(FDP)": "(Sum((100.*o:first downs/(o:rushes+o:passes+oo:sacks)) as 'o:FDP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(FDP)'"})
    shortcuts.update({"tp:FDP": "(100.*tp:first downs/(tp:rushes+tp:passes+too:sacks)) as 'tp:FDP'"})
    shortcuts.update({"to:FDP": "(100.*to:first downs/(to:rushes+to:passes+too:sacks)) as 'to:FDP'"})
    shortcuts.update({"op:FDP": "(100.*op:first downs/(op:rushes+op:passes+too:sacks)) as 'op:FDP'"})
    shortcuts.update({"t:FDP": "(100.*t:first downs/(t:rushes+t:passes+too:sacks)) as 't:FDP'"})
    shortcuts.update({"p:FDP": "(100.*p:first downs/(p:rushes+p:passes+too:sacks)) as 'p:FDP'"})
    shortcuts.update({"o:FDP": "(100.*o:first downs/(o:rushes+o:passes+too:sacks)) as 'o:FDP'"})
    shortcuts.update({"FDP": "(100.*first downs/(rushes+passes+tp:sacks)) as 'FDP'"})
    shortcuts.update({"tS(GTGA)": "Sum((1*goal to go attempted) as 'GTGA'@ team and season) as 'tS(GTGA)'"})
    shortcuts.update({"tA(GTGA)": "average((1*goal to go attempted) as 'GTGA'@ team and season) as 'tS(GTGA)'"})
    shortcuts.update({"tpS(GTGA)": "(Sum((1*goal to go attempted) as 'GTGA'@ team and season)[ team and season-1]) as 'tpS(GTGA)'"})
    shortcuts.update({"oS(GTGA)": "Sum((1*o:goal to go attempted) as 'o:GTGA'@ o:team and o:season) as 'oS(GTGA)'"})
    shortcuts.update({"oA(GTGA)": "average((1*o:goal to go attempted) as 'o:GTGA'@ o:team and o:season) as 'oS(GTGA)'"})
    shortcuts.update({"opS(GTGA)": "(Sum((1*goal to go attempted) as 'GTGA'@ team and season)[ team and season-1]) as 'tpS(GTGA)'"})
    shortcuts.update({"tp:GTGA": "(1*tp:goal to go attempted) as 'tp:GTGA'"})
    shortcuts.update({"to:GTGA": "(1*to:goal to go attempted) as 'to:GTGA'"})
    shortcuts.update({"op:GTGA": "(1*op:goal to go attempted) as 'op:GTGA'"})
    shortcuts.update({"t:GTGA": "(1*t:goal to go attempted) as 't:GTGA'"})
    shortcuts.update({"p:GTGA": "(1*p:goal to go attempted) as 'p:GTGA'"})
    shortcuts.update({"o:GTGA": "(1*o:goal to go attempted) as 'o:GTGA'"})
    shortcuts.update({"GTGA": "(1*goal to go attempted) as 'GTGA'"})
    shortcuts.update({"tS(GTGM)": "Sum((1*goal to go made) as 'GTGM'@ team and season) as 'tS(GTGM)'"})
    shortcuts.update({"tA(GTGM)": "average((1*goal to go made) as 'GTGM'@ team and season) as 'tS(GTGM)'"})
    shortcuts.update({"tpS(GTGM)": "(Sum((1*goal to go made) as 'GTGM'@ team and season)[ team and season-1]) as 'tpS(GTGM)'"})
    shortcuts.update({"oS(GTGM)": "Sum((1*o:goal to go made) as 'o:GTGM'@ o:team and o:season) as 'oS(GTGM)'"})
    shortcuts.update({"oA(GTGM)": "average((1*o:goal to go made) as 'o:GTGM'@ o:team and o:season) as 'oS(GTGM)'"})
    shortcuts.update({"opS(GTGM)": "(Sum((1*goal to go made) as 'GTGM'@ team and season)[ team and season-1]) as 'tpS(GTGM)'"})
    shortcuts.update({"tp:GTGM": "(1*tp:goal to go made) as 'tp:GTGM'"})
    shortcuts.update({"to:GTGM": "(1*to:goal to go made) as 'to:GTGM'"})
    shortcuts.update({"op:GTGM": "(1*op:goal to go made) as 'op:GTGM'"})
    shortcuts.update({"t:GTGM": "(1*t:goal to go made) as 't:GTGM'"})
    shortcuts.update({"p:GTGM": "(1*p:goal to go made) as 'p:GTGM'"})
    shortcuts.update({"o:GTGM": "(1*o:goal to go made) as 'o:GTGM'"})
    shortcuts.update({"GTGM": "(1*goal to go made) as 'GTGM'"})
    shortcuts.update({"tS(INC)": "Sum((passes-completions) as 'INC'@ team and season) as 'tS(INC)' "})
    shortcuts.update({"tA(INC)": "average((passes-completions) as 'INC'@ team and season) as 'tS(INC)' "})
    shortcuts.update({"tpS(INC)": "(Sum((passes-completions) as 'INC'@ team and season)[ team and season-1]) as 'tpS(INC)'"})
    shortcuts.update({"oS(INC)": "Sum((o:passes-o:completions) as 'o:INC'@ o:team and o:season) as 'oS(INC)'"})
    shortcuts.update({"oA(INC)": "average((o:passes-o:completions) as 'o:INC'@ o:team and o:season) as 'oS(INC)'"})
    shortcuts.update({"opS(INC)": "(Sum((o:passes-o:completions) as 'o:INC'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(INC)' "})
    shortcuts.update({"tp:INC": "(tp:passes-tp:completions) as 'tp:INC'"})
    shortcuts.update({"to:INC": "(to:passes-to:completions) as 'to:INC'"})
    shortcuts.update({"op:INC": "(op:passes-op:completions) as 'op:INC'"})
    shortcuts.update({"t:INC": "(t:passes-t:completions) as 't:INC'"})
    shortcuts.update({"p:INC": "(p:passes-p:completions) as 'p:INC'"})
    shortcuts.update({"o:INC": "(o:passes-o:completions) as 'o:INC'"})
    shortcuts.update({"INC": "(passes-completions) as 'INC'"})
    shortcuts.update({"tS(INT)": "Sum((1*interceptions) as 'INT'@ team and season) as 'tS(INT)'"})
    shortcuts.update({"tA(INT)": "average((1*interceptions) as 'INT'@ team and season) as 'tS(INT)'"})
    shortcuts.update({"tpS(INT)": "(Sum((1*interceptions) as 'INT'@ team and season)[ team and season-1]) as 'tpS(INT)'"})
    shortcuts.update({"oS(INT)": "Sum((1*o:interceptions) as 'o:INT'@ o:team and o:season) as 'oS(INT)'"})
    shortcuts.update({"oA(INT)": "average((1*o:interceptions) as 'o:INT'@ o:team and o:season) as 'oS(INT)'"})
    shortcuts.update({"opS(INT)": "(Sum((1*interceptions) as 'INT'@ team and season)[ team and season-1]) as 'tpS(INT)'"})
    shortcuts.update({"tp:INT": "(1*tp:interceptions) as 'tp:INT'"})
    shortcuts.update({"to:INT": "(1*to:interceptions) as 'to:INT'"})
    shortcuts.update({"op:INT": "(1*op:interceptions) as 'op:INT'"})
    shortcuts.update({"t:INT": "(1*t:interceptions) as 't:INT'"})
    shortcuts.update({"p:INT": "(1*p:interceptions) as 'p:INT'"})
    shortcuts.update({"o:INT": "(1*o:interceptions) as 'o:INT'"})
    shortcuts.update({"INT": "(1*interceptions) as 'INT'"})
    shortcuts.update({"tS(NOTD)": "Sum((touchdowns-rushing touchdowns-passing touchdowns) as 'NOTD'@ team and season) as 'tS(NOTD)'"})
    shortcuts.update({"tA(NOTD)": "average((touchdowns-rushing touchdowns-passing touchdowns) as 'NOTD'@ team and season) as 'tS(NOTD)'"})
    shortcuts.update({"tpS(NOTD)": "(Sum((touchdowns-rushing touchdowns-passing touchdowns) as 'NOTD'@ team and season)[ team and season-1]) as 'tpS(NOTD)'"})
    shortcuts.update({"oS(NOTD)": "Sum((o:touchdowns-o:rushing touchdowns-o:passing touchdowns) as 'o:NOTD'@ o:team and o:season) as 'oS(NOTD)'"})
    shortcuts.update({"oA(NOTD)": "average((o:touchdowns-o:rushing touchdowns-o:passing touchdowns) as 'o:NOTD'@ o:team and o:season) as 'oS(NOTD)'"})
    shortcuts.update({"opS(NOTD)": "(Sum((o:touchdowns-o:rushing touchdowns-o:passing touchdowns) as 'o:NOTD'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(NOTD)'"})
    shortcuts.update({"tp:NOTD": "(tp:touchdowns-tp:rushing touchdowns-tp:passing touchdowns) as 'tp:NOTD'"})
    shortcuts.update({"to:NOTD": "(to:touchdowns-to:rushing touchdowns-to:passing touchdowns) as 'to:NOTD'"})
    shortcuts.update({"op:NOTD": "(op:touchdowns-op:rushing touchdowns-op:passing touchdowns) as 'op:NOTD'"})
    shortcuts.update({"t:NOTD": "(t:touchdowns-t:rushing touchdowns-t:passing touchdowns) as 't:NOTD'"})
    shortcuts.update({"p:NOTD": "(p:touchdowns-p:rushing touchdowns-p:passing touchdowns) as 'p:NOTD'"})
    shortcuts.update({"o:NOTD": "(o:touchdowns-o:rushing touchdowns-o:passing touchdowns) as 'o:NOTD'"})
    shortcuts.update({"NOTD": "(touchdowns-rushing touchdowns-passing touchdowns) as 'NOTD'"})
    shortcuts.update({"tS(OFPL)": "Sum((passes+rushes+tp:sacks) as 'OFPL'@ team and season) as 'tS(OFPL)'"})
    shortcuts.update({"tA(OFPL)": "average((passes+rushes+tp:sacks) as 'OFPL'@ team and season) as 'tS(OFPL)'"})
    shortcuts.update({"tpS(OFPL)": "(Sum((passes+rushes+tp:sacks) as 'OFPL'@ team and season)[ team and season-1]) as 'tpS(OFPL)'"})
    shortcuts.update({"oS(OFPL)": "Sum((o:passes+o:rushes+oo:sacks) as 'o:OFPL'@ o:team and o:season) as 'oS(OFPL)'"})
    shortcuts.update({"oA(OFPL)": "average((o:passes+o:rushes+oo:sacks) as 'o:OFPL'@ o:team and o:season) as 'oS(OFPL)'"})
    shortcuts.update({"opS(OFPL)": "(Sum((o:passes+o:rushes+oo:sacks) as 'o:OFPL'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(OFPL)'"})
    shortcuts.update({"tp:OFPL": "(tp:passes+tp:rushes+too:sacks) as 'tp:OFPL'"})
    shortcuts.update({"to:OFPL": "(to:passes+to:rushes+poo:sacks) as 'to:OFPL'"})
    shortcuts.update({"op:OFPL": "(op:passes+op:rushes+oto:sacks) as 'op:OFPL'"})
    shortcuts.update({"t:OFPL": "(t:passes+t:rushes+tp:sacks) as 't:OFPL'"})
    shortcuts.update({"p:OFPL": "(p:passes+p:rushes+to:sacks) as 'p:OFPL'"})
    shortcuts.update({"o:OFPL": "(o:passes+o:rushes+oo:sacks) as 'o:OFPL'"})
    shortcuts.update({"OFPL": "(passes+rushes+tp:sacks) as 'OFPL'"})
    shortcuts.update({"tS(OT)": "Sum((1*rushing touchdowns) as 'OT'@ team and season) as 'tS(OT)'"})
    shortcuts.update({"tA(OT)": "average((1*rushing touchdowns) as 'OT'@ team and season) as 'tS(OT)'"})
    shortcuts.update({"tpS(OT)": "(Sum((1*rushing touchdowns) as 'OT'@ team and season)[ team and season-1]) as 'tpS(OT)'"})
    shortcuts.update({"oS(OT)": "Sum((1*o:rushing touchdowns) as 'o:OT'@ o:team and o:season) as 'oS(OT)'"})
    shortcuts.update({"oA(OT)": "average((1*o:rushing touchdowns) as 'o:OT'@ o:team and o:season) as 'oS(OT)'"})
    shortcuts.update({"opS(OT)": "(Sum((1*rushing touchdowns) as 'OT'@ team and season)[ team and season-1]) as 'tpS(OT)'"})
    shortcuts.update({"tp:OT": "(1*tp:rushing touchdowns) as 'tp:OT'"})
    shortcuts.update({"to:OT": "(1*to:rushing touchdowns) as 'to:OT'"})
    shortcuts.update({"op:OT": "(1*op:rushing touchdowns) as 'op:OT'"})
    shortcuts.update({"t:OT": "(1*t:rushing touchdowns) as 't:OT'"})
    shortcuts.update({"p:OT": "(1*p:rushing touchdowns) as 'p:OT'"})
    shortcuts.update({"o:OT": "(1*o:rushing touchdowns) as 'o:OT'"})
    shortcuts.update({"OT": "(1*rushing touchdowns) as 'OT'"})
    shortcuts.update({"tS(P1)": "Sum((quarter scores[0]) as 'P1'@ team and season) as 'tS(P1)'"})
    shortcuts.update({"tA(P1)": "average((quarter scores[0]) as 'P1'@ team and season) as 'tS(P1)'"})
    shortcuts.update({"tpS(P1)": "(Sum((quarter scores[0]) as 'P1'@ team and season)[ team and season-1]) as 'tpS(P1)'"})
    shortcuts.update({"oS(P1)": "Sum((o:quarter scores[0]) as 'o:P1'@ o:team and o:season) as 'oS(P1)'"})
    shortcuts.update({"oA(P1)": "average((o:quarter scores[0]) as 'o:P1'@ o:team and o:season) as 'oS(P1)'"})
    shortcuts.update({"opS(P1)": "(Sum((o:quarter scores[0]) as 'o:P1'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(P1)'"})
    shortcuts.update({"tp:P1": "(tp:quarter scores[0]) as 'tp:P1'"})
    shortcuts.update({"to:P1": "(to:quarter scores[0]) as 'to:P1'"})
    shortcuts.update({"op:P1": "(op:quarter scores[0]) as 'op:P1'"})
    shortcuts.update({"t:P1": "(t:quarter scores[0]) as 't:P1'"})
    shortcuts.update({"p:P1": "(p:quarter scores[0]) as 'p:P1'"})
    shortcuts.update({"o:P1": "(o:quarter scores[0]) as 'o:P1'"})
    shortcuts.update({"P1": "(quarter scores[0]) as 'P1'"})
    shortcuts.update({"tS(P2)": "Sum((quarter scores[1]) as 'P2'@ team and season) as 'tS(P2)'"})
    shortcuts.update({"tA(P2)": "average((quarter scores[1]) as 'P2'@ team and season) as 'tS(P2)'"})
    shortcuts.update({"tpS(P2)": "(Sum((quarter scores[1]) as 'P2'@ team and season)[ team and season-1]) as 'tpS(P2)'"})
    shortcuts.update({"oS(P2)": "Sum((o:quarter scores[1]) as 'o:P2'@ o:team and o:season) as 'oS(P2)'"})
    shortcuts.update({"oA(P2)": "average((o:quarter scores[1]) as 'o:P2'@ o:team and o:season) as 'oS(P2)'"})
    shortcuts.update({"opS(P2)": "(Sum((o:quarter scores[1]) as 'o:P2'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(P2)'"})
    shortcuts.update({"tp:P2": "(tp:quarter scores[1]) as 'tp:P2'"})
    shortcuts.update({"to:P2": "(to:quarter scores[1]) as 'to:P2'"})
    shortcuts.update({"op:P2": "(op:quarter scores[1]) as 'op:P2'"})
    shortcuts.update({"t:P2": "(t:quarter scores[1]) as 't:P2'"})
    shortcuts.update({"p:P2": "(p:quarter scores[1]) as 'p:P2'"})
    shortcuts.update({"o:P2": "(o:quarter scores[1]) as 'o:P2'"})
    shortcuts.update({"P2": "(quarter scores[1]) as 'P2'"})
    shortcuts.update({"tS(P3)": "Sum((quarter scores[2]) as 'P3'@ team and season) as 'tS(P3)'"})
    shortcuts.update({"tA(P3)": "average((quarter scores[2]) as 'P3'@ team and season) as 'tS(P3)'"})
    shortcuts.update({"tpS(P3)": "(Sum((quarter scores[2]) as 'P3'@ team and season)[ team and season-1]) as 'tpS(P3)'"})
    shortcuts.update({"oS(P3)": "Sum((o:quarter scores[2]) as 'o:P3'@ o:team and o:season) as 'oS(P3)'"})
    shortcuts.update({"oA(P3)": "average((o:quarter scores[2]) as 'o:P3'@ o:team and o:season) as 'oS(P3)'"})
    shortcuts.update({"opS(P3)": "(Sum((o:quarter scores[2]) as 'o:P3'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(P3)'"})
    shortcuts.update({"tp:P3": "(tp:quarter scores[2]) as 'tp:P3'"})
    shortcuts.update({"to:P3": "(to:quarter scores[2]) as 'to:P3'"})
    shortcuts.update({"op:P3": "(op:quarter scores[2]) as 'op:P3'"})
    shortcuts.update({"t:P3": "(t:quarter scores[2]) as 't:P3'"})
    shortcuts.update({"p:P3": "(p:quarter scores[2]) as 'p:P3'"})
    shortcuts.update({"o:P3": "(o:quarter scores[2]) as 'o:P3'"})
    shortcuts.update({"P3": "(quarter scores[2]) as 'P3'"})
    shortcuts.update({"tS(P4)": "Sum((quarter scores[3]) as 'P4'@ team and season) as 'tS(P4)'"})
    shortcuts.update({"tA(P4)": "average((quarter scores[3]) as 'P4'@ team and season) as 'tS(P4)'"})
    shortcuts.update({"tpS(P4)": "(Sum((quarter scores[3]) as 'P4'@ team and season)[ team and season-1]) as 'tpS(P4)'"})
    shortcuts.update({"oS(P4)": "Sum((o:quarter scores[3]) as 'o:P4'@ o:team and o:season) as 'oS(P4)'"})
    shortcuts.update({"oA(P4)": "average((o:quarter scores[3]) as 'o:P4'@ o:team and o:season) as 'oS(P4)'"})
    shortcuts.update({"opS(P4)": "(Sum((o:quarter scores[3]) as 'o:P4'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(P4)'"})
    shortcuts.update({"tp:P4": "(tp:quarter scores[3]) as 'tp:P4'"})
    shortcuts.update({"to:P4": "(to:quarter scores[3]) as 'to:P4'"})
    shortcuts.update({"op:P4": "(op:quarter scores[3]) as 'op:P4'"})
    shortcuts.update({"t:P4": "(t:quarter scores[3]) as 't:P4'"})
    shortcuts.update({"p:P4": "(p:quarter scores[3]) as 'p:P4'"})
    shortcuts.update({"o:P4": "(o:quarter scores[3]) as 'o:P4'"})
    shortcuts.update({"P4": "(quarter scores[3]) as 'P4'"})
    shortcuts.update({"tS(PENY)": "Sum((1*penalty yards) as 'PENY'@ team and season) as 'tS(PENY)'"})
    shortcuts.update({"tA(PENY)": "average((1*penalty yards) as 'PENY'@ team and season) as 'tS(PENY)'"})
    shortcuts.update({"tpS(PENY)": "(Sum((1*penalty yards) as 'PENY'@ team and season)[ team and season-1]) as 'tpS(PENY)'"})
    shortcuts.update({"oS(PENY)": "Sum((1*o:penalty yards) as 'o:PENY'@ o:team and o:season) as 'oS(PENY)'"})
    shortcuts.update({"oA(PENY)": "average((1*o:penalty yards) as 'o:PENY'@ o:team and o:season) as 'oS(PENY)'"})
    shortcuts.update({"opS(PENY)": "(Sum((1*penalty yards) as 'PENY'@ team and season)[ team and season-1]) as 'tpS(PENY)'"})
    shortcuts.update({"tp:PENY": "(1*tp:penalty yards) as 'tp:PENY'"})
    shortcuts.update({"to:PENY": "(1*to:penalty yards) as 'to:PENY'"})
    shortcuts.update({"op:PENY": "(1*op:penalty yards) as 'op:PENY'"})
    shortcuts.update({"t:PENY": "(1*t:penalty yards) as 't:PENY'"})
    shortcuts.update({"p:PENY": "(1*p:penalty yards) as 'p:PENY'"})
    shortcuts.update({"o:PENY": "(1*o:penalty yards) as 'o:PENY'"})
    shortcuts.update({"PENY": "(1*penalty yards) as 'PENY'"})
    shortcuts.update({"tS(PENFD)": "Sum((1*penalty first downs) as 'PENFD'@ team and season) as 'tS(PENFD)'"})
    shortcuts.update({"tA(PENFD)": "average((1*penalty first downs) as 'PENFD'@ team and season) as 'tS(PENFD)'"})
    shortcuts.update({"tpS(PENFD)": "(Sum((1*penalty first downs) as 'PENFD'@ team and season)[ team and season-1]) as 'tpS(PENFD)'"})
    shortcuts.update({"oS(PENFD)": "Sum((1*o:penalty first downs) as 'o:PENFD'@ o:team and o:season) as 'oS(PENFD)'"})
    shortcuts.update({"oA(PENFD)": "average((1*o:penalty first downs) as 'o:PENFD'@ o:team and o:season) as 'oS(PENFD)'"})
    shortcuts.update({"opS(PENFD)": "(Sum((1*penalty first downs) as 'PENFD'@ team and season)[ team and season-1]) as 'tpS(PENFD)'"})
    shortcuts.update({"tp:PENFD": "(1*tp:penalty first downs) as 'tp:PENFD'"})
    shortcuts.update({"to:PENFD": "(1*to:penalty first downs) as 'to:PENFD'"})
    shortcuts.update({"op:PENFD": "(1*op:penalty first downs) as 'op:PENFD'"})
    shortcuts.update({"t:PENFD": "(1*t:penalty first downs) as 't:PENFD'"})
    shortcuts.update({"p:PENFD": "(1*p:penalty first downs) as 'p:PENFD'"})
    shortcuts.update({"o:PENFD": "(1*o:penalty first downs) as 'o:PENFD'"})
    shortcuts.update({"PENFD": "(1*penalty first downs) as 'PENFD'"})
    shortcuts.update({"tS(PEN)": "Sum((1*penalties) as 'PEN'@ team and season) as 'tS(PEN)'"})
    shortcuts.update({"tA(PEN)": "average((1*penalties) as 'PEN'@ team and season) as 'tS(PEN)'"})
    shortcuts.update({"tpS(PEN)": "(Sum((1*penalties) as 'PEN'@ team and season)[ team and season-1]) as 'tpS(PEN)'"})
    shortcuts.update({"oS(PEN)": "Sum((1*o:penalties) as 'o:PEN'@ o:team and o:season) as 'oS(PEN)'"})
    shortcuts.update({"oA(PEN)": "average((1*o:penalties) as 'o:PEN'@ o:team and o:season) as 'oS(PEN)'"})
    shortcuts.update({"opS(PEN)": "(Sum((1*penalties) as 'PEN'@ team and season)[ team and season-1]) as 'tpS(PEN)'"})
    shortcuts.update({"tp:PEN": "(1*tp:penalties) as 'tp:PEN'"})
    shortcuts.update({"to:PEN": "(1*to:penalties) as 'to:PEN'"})
    shortcuts.update({"op:PEN": "(1*op:penalties) as 'op:PEN'"})
    shortcuts.update({"t:PEN": "(1*t:penalties) as 't:PEN'"})
    shortcuts.update({"p:PEN": "(1*p:penalties) as 'p:PEN'"})
    shortcuts.update({"o:PEN": "(1*o:penalties) as 'o:PEN'"})
    shortcuts.update({"PEN": "(1*penalties) as 'PEN'"})
    shortcuts.update({"tS(PENFD)": "Sum((1*passing first downs) as 'PENFD'@ team and season) as 'tS(PENFD)'"})
    shortcuts.update({"tA(PENFD)": "average((1*passing first downs) as 'PENFD'@ team and season) as 'tS(PENFD)'"})
    shortcuts.update({"tpS(PENFD)": "(Sum((1*passing first downs) as 'PENFD'@ team and season)[ team and season-1]) as 'tpS(PENFD)'"})
    shortcuts.update({"oS(PENFD)": "Sum((1*o:passing first downs) as 'o:PENFD'@ o:team and o:season) as 'oS(PENFD)'"})
    shortcuts.update({"oA(PENFD)": "average((1*o:passing first downs) as 'o:PENFD'@ o:team and o:season) as 'oS(PENFD)'"})
    shortcuts.update({"opS(PENFD)": "(Sum((1*passing first downs) as 'PENFD'@ team and season)[ team and season-1]) as 'tpS(PENFD)'"})
    shortcuts.update({"tp:PENFD": "(1*tp:passing first downs) as 'tp:PENFD'"})
    shortcuts.update({"to:PENFD": "(1*to:passing first downs) as 'to:PENFD'"})
    shortcuts.update({"op:PENFD": "(1*op:passing first downs) as 'op:PENFD'"})
    shortcuts.update({"t:PENFD": "(1*t:passing first downs) as 't:PENFD'"})
    shortcuts.update({"p:PENFD": "(1*p:passing first downs) as 'p:PENFD'"})
    shortcuts.update({"o:PENFD": "(1*o:passing first downs) as 'o:PENFD'"})
    shortcuts.update({"PENFD": "(1*passing first downs) as 'PENFD'"})
    shortcuts.update({"tS(PO)": "Sum((playoffs=1) as 'PO'@ team and season) as 'tS(PO)'"})
    shortcuts.update({"tA(PO)": "average((playoffs=1) as 'PO'@ team and season) as 'tS(PO)'"})
    shortcuts.update({"tpS(PO)": "(Sum((playoffs=1) as 'PO'@ team and season)[ team and season-1]) as 'tpS(PO)'"})
    shortcuts.update({"oS(PO)": "Sum((o:playoffs=1) as 'o:PO'@ o:team and o:season) as 'oS(PO)'"})
    shortcuts.update({"oA(PO)": "average((o:playoffs=1) as 'o:PO'@ o:team and o:season) as 'oS(PO)'"})
    shortcuts.update({"opS(PO)": "(Sum((o:playoffs=1) as 'o:PO'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(PO)'"})
    shortcuts.update({"tp:PO": "(tp:playoffs=1) as 'tp:PO'"})
    shortcuts.update({"to:PO": "(to:playoffs=1) as 'to:PO'"})
    shortcuts.update({"op:PO": "(op:playoffs=1) as 'op:PO'"})
    shortcuts.update({"t:PO": "(t:playoffs=1) as 't:PO'"})
    shortcuts.update({"p:PO": "(p:playoffs=1) as 'p:PO'"})
    shortcuts.update({"o:PO": "(o:playoffs=1) as 'o:PO'"})
    shortcuts.update({"PO": "(playoffs=1) as 'PO'"})
    shortcuts.update({"tS(PTD)": "Sum((1*passing touchdowns) as 'PTD'@ team and season) as 'tS(PTD)'"})
    shortcuts.update({"tA(PTD)": "average((1*passing touchdowns) as 'PTD'@ team and season) as 'tS(PTD)'"})
    shortcuts.update({"tpS(PTD)": "(Sum((1*passing touchdowns) as 'PTD'@ team and season)[ team and season-1]) as 'tpS(PTD)'"})
    shortcuts.update({"oS(PTD)": "Sum((1*o:passing touchdowns) as 'o:PTD'@ o:team and o:season) as 'oS(PTD)'"})
    shortcuts.update({"oA(PTD)": "average((1*o:passing touchdowns) as 'o:PTD'@ o:team and o:season) as 'oS(PTD)'"})
    shortcuts.update({"opS(PTD)": "(Sum((1*passing touchdowns) as 'PTD'@ team and season)[ team and season-1]) as 'tpS(PTD)'"})
    shortcuts.update({"tp:PTD": "(1*tp:passing touchdowns) as 'tp:PTD'"})
    shortcuts.update({"to:PTD": "(1*to:passing touchdowns) as 'to:PTD'"})
    shortcuts.update({"op:PTD": "(1*op:passing touchdowns) as 'op:PTD'"})
    shortcuts.update({"t:PTD": "(1*t:passing touchdowns) as 't:PTD'"})
    shortcuts.update({"p:PTD": "(1*p:passing touchdowns) as 'p:PTD'"})
    shortcuts.update({"o:PTD": "(1*o:passing touchdowns) as 'o:PTD'"})
    shortcuts.update({"PTD": "(1*passing touchdowns) as 'PTD'"})
    shortcuts.update({"tS(PY)": "Sum((1*passing yards) as 'PY'@ team and season) as 'tS(PY)'"})
    shortcuts.update({"tA(PY)": "average((1*passing yards) as 'PY'@ team and season) as 'tS(PY)'"})
    shortcuts.update({"tpS(PY)": "(Sum((1*passing yards) as 'PY'@ team and season)[ team and season-1]) as 'tpS(PY)'"})
    shortcuts.update({"oS(PY)": "Sum((1*o:passing yards) as 'o:PY'@ o:team and o:season) as 'oS(PY)'"})
    shortcuts.update({"oA(PY)": "average((1*o:passing yards) as 'o:PY'@ o:team and o:season) as 'oS(PY)'"})
    shortcuts.update({"opS(PY)": "(Sum((1*passing yards) as 'PY'@ team and season)[ team and season-1]) as 'tpS(PY)'"})
    shortcuts.update({"tp:PY": "(1*tp:passing yards) as 'tp:PY'"})
    shortcuts.update({"to:PY": "(1*to:passing yards) as 'to:PY'"})
    shortcuts.update({"op:PY": "(1*op:passing yards) as 'op:PY'"})
    shortcuts.update({"t:PY": "(1*t:passing yards) as 't:PY'"})
    shortcuts.update({"p:PY": "(1*p:passing yards) as 'p:PY'"})
    shortcuts.update({"o:PY": "(1*o:passing yards) as 'o:PY'"})
    shortcuts.update({"PY": "(1*passing yards) as 'PY'"})
    shortcuts.update({"tS(RFD)": "Sum((1*rushing first downs) as 'RFD'@ team and season) as 'tS(RFD)'"})
    shortcuts.update({"tA(RFD)": "average((1*rushing first downs) as 'RFD'@ team and season) as 'tS(RFD)'"})
    shortcuts.update({"tpS(RFD)": "(Sum((1*rushing first downs) as 'RFD'@ team and season)[ team and season-1]) as 'tpS(RFD)'"})
    shortcuts.update({"oS(RFD)": "Sum((1*o:rushing first downs) as 'o:RFD'@ o:team and o:season) as 'oS(RFD)'"})
    shortcuts.update({"oA(RFD)": "average((1*o:rushing first downs) as 'o:RFD'@ o:team and o:season) as 'oS(RFD)'"})
    shortcuts.update({"opS(RFD)": "(Sum((1*rushing first downs) as 'RFD'@ team and season)[ team and season-1]) as 'tpS(RFD)'"})
    shortcuts.update({"tp:RFD": "(1*tp:rushing first downs) as 'tp:RFD'"})
    shortcuts.update({"to:RFD": "(1*to:rushing first downs) as 'to:RFD'"})
    shortcuts.update({"op:RFD": "(1*op:rushing first downs) as 'op:RFD'"})
    shortcuts.update({"t:RFD": "(1*t:rushing first downs) as 't:RFD'"})
    shortcuts.update({"p:RFD": "(1*p:rushing first downs) as 'p:RFD'"})
    shortcuts.update({"o:RFD": "(1*o:rushing first downs) as 'o:RFD'"})
    shortcuts.update({"RFD": "(1*rushing first downs) as 'RFD'"})
    shortcuts.update({"tS(RTD)": "Sum((1*rushing touchdowns) as 'RTD'@ team and season) as 'tS(RTD)'"})
    shortcuts.update({"tA(RTD)": "average((1*rushing touchdowns) as 'RTD'@ team and season) as 'tS(RTD)'"})
    shortcuts.update({"tpS(RTD)": "(Sum((1*rushing touchdowns) as 'RTD'@ team and season)[ team and season-1]) as 'tpS(RTD)'"})
    shortcuts.update({"oS(RTD)": "Sum((1*o:rushing touchdowns) as 'o:RTD'@ o:team and o:season) as 'oS(RTD)'"})
    shortcuts.update({"oA(RTD)": "average((1*o:rushing touchdowns) as 'o:RTD'@ o:team and o:season) as 'oS(RTD)'"})
    shortcuts.update({"opS(RTD)": "(Sum((1*rushing touchdowns) as 'RTD'@ team and season)[ team and season-1]) as 'tpS(RTD)'"})
    shortcuts.update({"tp:RTD": "(1*tp:rushing touchdowns) as 'tp:RTD'"})
    shortcuts.update({"to:RTD": "(1*to:rushing touchdowns) as 'to:RTD'"})
    shortcuts.update({"op:RTD": "(1*op:rushing touchdowns) as 'op:RTD'"})
    shortcuts.update({"t:RTD": "(1*t:rushing touchdowns) as 't:RTD'"})
    shortcuts.update({"p:RTD": "(1*p:rushing touchdowns) as 'p:RTD'"})
    shortcuts.update({"o:RTD": "(1*o:rushing touchdowns) as 'o:RTD'"})
    shortcuts.update({"RTD": "(1*rushing touchdowns) as 'RTD'"})
    shortcuts.update({"tS(REG)": "Sum((playoffs=0) as 'REG'@ team and season) as 'tS(REG)'"})
    shortcuts.update({"tA(REG)": "average((playoffs=0) as 'REG'@ team and season) as 'tS(REG)'"})
    shortcuts.update({"tpS(REG)": "(Sum((playoffs=0) as 'REG'@ team and season)[ team and season-1]) as 'tpS(REG)'"})
    shortcuts.update({"oS(REG)": "Sum((o:playoffs=0) as 'o:REG'@ o:team and o:season) as 'oS(REG)'"})
    shortcuts.update({"oA(REG)": "average((o:playoffs=0) as 'o:REG'@ o:team and o:season) as 'oA(REG)'"})
    shortcuts.update({"opS(REG)": "(Sum((o:playoffs=0) as 'o:REG'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(REG)'"})
    shortcuts.update({"tp:REG": "(tp:playoffs=0) as 'REG'"})
    shortcuts.update({"to:REG": "(to:playoffs=0) as 'to:REG'"})
    shortcuts.update({"op:REG": "(op:playoffs=0) as 'op:REG'"})
    shortcuts.update({"t:REG": "(t:playoffs=0) as 't:REG'"})
    shortcuts.update({"p:REG": "(p:playoffs=0) as 'p:REG'"})
    shortcuts.update({"o:REG": "(o:playoffs=0) as 'o:REG'"})
    shortcuts.update({"REG": "(playoffs=0) as 'REG'"})
    shortcuts.update({"tS(RY)": "Sum((1*rushing yards) as 'RY'@ team and season) as 'tS(RY)'"})
    shortcuts.update({"tA(RY)": "average((1*rushing yards) as 'RY'@ team and season) as 'tS(RY)'"})
    shortcuts.update({"tpS(RY)": "(Sum((1*rushing yards) as 'RY'@ team and season)[ team and season-1]) as 'tpS(RY)'"})
    shortcuts.update({"oS(RY)": "Sum((1*o:rushing yards) as 'o:RY'@ o:team and o:season) as 'oS(RY)'"})
    shortcuts.update({"oA(RY)": "average((1*o:rushing yards) as 'o:RY'@ o:team and o:season) as 'oS(RY)'"})
    shortcuts.update({"opS(RY)": "(Sum((1*rushing yards) as 'RY'@ team and season)[ team and season-1]) as 'tpS(RY)'"})
    shortcuts.update({"tp:RY": "(1*tp:rushing yards) as 'tp:RY'"})
    shortcuts.update({"to:RY": "(1*to:rushing yards) as 'to:RY'"})
    shortcuts.update({"op:RY": "(1*op:rushing yards) as 'op:RY'"})
    shortcuts.update({"t:RY": "(1*t:rushing yards) as 't:RY'"})
    shortcuts.update({"p:RY": "(1*p:rushing yards) as 'p:RY'"})
    shortcuts.update({"o:RY": "(1*o:rushing yards) as 'o:RY'"})
    shortcuts.update({"RY": "(1*rushing yards) as 'RY'"})
    shortcuts.update({"tS(RZA)": "Sum((1*red zones attempted) as 'RZA'@ team and season) as 'tS(RZA)'"})
    shortcuts.update({"tA(RZA)": "average((1*red zones attempted) as 'RZA'@ team and season) as 'tS(RZA)'"})
    shortcuts.update({"tpS(RZA)": "(Sum((1*red zones attempted) as 'RZA'@ team and season)[ team and season-1]) as 'tpS(RZA)'"})
    shortcuts.update({"oS(RZA)": "Sum((1*o:red zones attempted) as 'o:RZA'@ o:team and o:season) as 'oS(RZA)'"})
    shortcuts.update({"oA(RZA)": "average((1*o:red zones attempted) as 'o:RZA'@ o:team and o:season) as 'oS(RZA)'"})
    shortcuts.update({"opS(RZA)": "(Sum((1*red zones attempted) as 'RZA'@ team and season)[ team and season-1]) as 'tpS(RZA)'"})
    shortcuts.update({"tp:RZA": "(1*tp:red zones attempted) as 'tp:RZA'"})
    shortcuts.update({"to:RZA": "(1*to:red zones attempted) as 'to:RZA'"})
    shortcuts.update({"op:RZA": "(1*op:red zones attempted) as 'op:RZA'"})
    shortcuts.update({"t:RZA": "(1*t:red zones attempted) as 't:RZA'"})
    shortcuts.update({"p:RZA": "(1*p:red zones attempted) as 'p:RZA'"})
    shortcuts.update({"o:RZA": "(1*o:red zones attempted) as 'o:RZA'"})
    shortcuts.update({"RZA": "(1*red zones attempted) as 'RZA'"})
    shortcuts.update({"tS(RZM)": "Sum((1*red zones made) as 'RZM'@ team and season) as 'tS(RZM)'"})
    shortcuts.update({"tA(RZM)": "average((1*red zones made) as 'RZM'@ team and season) as 'tS(RZM)'"})
    shortcuts.update({"tpS(RZM)": "(Sum((1*red zones made) as 'RZM'@ team and season)[ team and season-1]) as 'tpS(RZM)'"})
    shortcuts.update({"oS(RZM)": "Sum((1*o:red zones made) as 'o:RZM'@ o:team and o:season) as 'oS(RZM)'"})
    shortcuts.update({"oA(RZM)": "average((1*o:red zones made) as 'o:RZM'@ o:team and o:season) as 'oS(RZM)'"})
    shortcuts.update({"opS(RZM)": "(Sum((1*red zones made) as 'RZM'@ team and season)[ team and season-1]) as 'tpS(RZM)'"})
    shortcuts.update({"tp:RZM": "(1*tp:red zones made) as 'tp:RZM'"})
    shortcuts.update({"to:RZM": "(1*to:red zones made) as 'to:RZM'"})
    shortcuts.update({"op:RZM": "(1*op:red zones made) as 'op:RZM'"})
    shortcuts.update({"t:RZM": "(1*t:red zones made) as 't:RZM'"})
    shortcuts.update({"p:RZM": "(1*p:red zones made) as 'p:RZM'"})
    shortcuts.update({"o:RZM": "(1*o:red zones made) as 'o:RZM'"})
    shortcuts.update({"RZM": "(1*red zones made) as 'RZM'"})
    shortcuts.update({"tS(RZF)": "Sum((red zones attempted-red zones made) as 'RZF'@ team and season) as 'tS(RZF)'"})
    shortcuts.update({"tA(RZF)": "average((red zones attempted-red zones made) as 'RZF'@ team and season) as 'tS(RZF)'"})
    shortcuts.update({"tpS(RZF)": "(Sum((red zones attempted-red zones made) as 'RZF'@ team and season)[ team and season-1]) as 'tpS(RZF)'"})
    shortcuts.update({"oS(RZF)": "Sum((o:red zones attempted-o:red zones made) as 'o:RZF'@ o:team and o:season) as 'oS(RZF)'"})
    shortcuts.update({"oA(RZF)": "average((o:red zones attempted-o:red zones made) as 'o:RZF'@ o:team and o:season) as 'oS(RZF)'"})
    shortcuts.update({"opS(RZF)": "(Sum((o:red zones attempted-o:red zones made) as 'o:RZF'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(RZF)'"})
    shortcuts.update({"tp:RZF": "(tp:red zones attempted-tp:red zones made) as 'tp:RZF'"})
    shortcuts.update({"to:RZF": "(to:red zones attempted-to:red zones made) as 'to:RZF'"})
    shortcuts.update({"op:RZF": "(op:red zones attempted-op:red zones made) as 'op:RZF'"})
    shortcuts.update({"t:RZF": "(t:red zones attempted-t:red zones made) as 't:RZF'"})
    shortcuts.update({"p:RZF": "(p:red zones attempted-p:red zones made) as 'p:RZF'"})
    shortcuts.update({"o:RZF": "(o:red zones attempted-o:red zones made) as 'o:RZF'"})
    shortcuts.update({"RZF": "(red zones attempted-red zones made) as 'RZF'"})
    shortcuts.update({"tS(S1)": "Sum(sum(quarter scores[:1]) as 'S1'@ team and season) as 'tS(S1)'"})
    shortcuts.update({"tA(S1)": "average(sum(quarter scores[:1]) as 'S1'@ team and season) as 'tS(S1)'"})
    shortcuts.update({"tpS(S1)": "(Sum(sum(quarter scores[:1]) as 'S1'@ team and season)[ team and season-1]) as 'tpS(S1)'"})
    shortcuts.update({"oS(S1)": "Sum(sum(o:quarter scores[:1]) as 'o:S1'@ o:team and o:season) as 'oS(S1)'"})
    shortcuts.update({"oA(S1)": "average(sum(o:quarter scores[:1]) as 'o:S1'@ o:team and o:season) as 'oS(S1)'"})
    shortcuts.update({"opS(S1)": "(Sum(sum(o:quarter scores[:1]) as 'o:S1'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(S1)'"})
    shortcuts.update({"tp:S1": "sum(tp:quarter scores[:1]) as 'tp:S1'"})
    shortcuts.update({"to:S1": "sum(to:quarter scores[:1]) as 'to:S1'"})
    shortcuts.update({"op:S1": "sum(op:quarter scores[:1]) as 'op:S1'"})
    shortcuts.update({"t:S1": "sum(t:quarter scores[:1]) as 't:S1'"})
    shortcuts.update({"p:S1": "sum(p:quarter scores[:1]) as 'p:S1'"})
    shortcuts.update({"o:S1": "sum(o:quarter scores[:1]) as 'o:S1'"})
    shortcuts.update({"S1": "sum(quarter scores[:1]) as 'S1'"})
    shortcuts.update({"tS(S2)": "Sum(sum(quarter scores[:2]) as 'S2'@ team and season) as 'tS(S2)'"})
    shortcuts.update({"tA(S2)": "average(sum(quarter scores[:2]) as 'S2'@ team and season) as 'tS(S2)'"})
    shortcuts.update({"tpS(S2)": "(Sum(sum(quarter scores[:2]) as 'S2'@ team and season)[ team and season-1]) as 'tpS(S2)'"})
    shortcuts.update({"oS(S2)": "Sum(sum(o:quarter scores[:2]) as 'o:S2'@ o:team and o:season) as 'oS(S2)'"})
    shortcuts.update({"oA(S2)": "average(sum(o:quarter scores[:2]) as 'o:S2'@ o:team and o:season) as 'oS(S2)'"})
    shortcuts.update({"opS(S2)": "(Sum(sum(o:quarter scores[:2]) as 'o:S2'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(S2)'"})
    shortcuts.update({"tp:S2": "sum(tp:quarter scores[:2]) as 'tp:S2'"})
    shortcuts.update({"to:S2": "sum(to:quarter scores[:2]) as 'to:S2'"})
    shortcuts.update({"op:S2": "sum(op:quarter scores[:2]) as 'op:S2'"})
    shortcuts.update({"t:S2": "sum(t:quarter scores[:2]) as 't:S2'"})
    shortcuts.update({"p:S2": "sum(p:quarter scores[:2]) as 'p:S2'"})
    shortcuts.update({"o:S2": "sum(o:quarter scores[:2]) as 'o:S2'"})
    shortcuts.update({"S2": "sum(quarter scores[:2]) as 'S2'"})
    shortcuts.update({"tS(S3)": "Sum(sum(quarter scores[:3]) as 'S3'@ team and season) as 'tS(S3)'"})
    shortcuts.update({"tA(S3)": "average(sum(quarter scores[:3]) as 'S3'@ team and season) as 'tS(S3)'"})
    shortcuts.update({"tpS(S3)": "(Sum(sum(quarter scores[:3]) as 'S3'@ team and season)[ team and season-1]) as 'tpS(S3)'"})
    shortcuts.update({"oS(S3)": "Sum(sum(o:quarter scores[:3]) as 'o:S3'@ o:team and o:season) as 'oS(S3)'"})
    shortcuts.update({"oA(S3)": "average(sum(o:quarter scores[:3]) as 'o:S3'@ o:team and o:season) as 'oS(S3)'"})
    shortcuts.update({"opS(S3)": "(Sum(sum(o:quarter scores[:3]) as 'o:S3'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(S3)'"})
    shortcuts.update({"tp:S3": "sum(tp:quarter scores[:3]) as 'tp:S3'"})
    shortcuts.update({"to:S3": "sum(to:quarter scores[:3]) as 'to:S3'"})
    shortcuts.update({"op:S3": "sum(op:quarter scores[:3]) as 'op:S3'"})
    shortcuts.update({"t:S3": "sum(t:quarter scores[:3]) as 't:S3'"})
    shortcuts.update({"p:S3": "sum(p:quarter scores[:3]) as 'p:S3'"})
    shortcuts.update({"o:S3": "sum(o:quarter scores[:3]) as 'o:S3'"})
    shortcuts.update({"S3": "sum(quarter scores[:3]) as 'S3'"})
    shortcuts.update({"tS(SIQ)": "Sum((sum(map(lambda p:p>0,quarter scores))) as 'SIQ'@ team and season) as 'tS(SIQ)'"})
    shortcuts.update({"tA(SIQ)": "average((sum(map(lambda p:p>0,quarter scores))) as 'SIQ'@ team and season) as 'tS(SIQ)'"})
    shortcuts.update({"tpS(SIQ)": "(Sum((sum(map(lambda p:p>0,quarter scores))) as 'SIQ'@ team and season)[ team and season-1]) as 'tpS(SIQ)'"})
    shortcuts.update({"oS(SIQ)": "Sum((sum(map(lambda p:p>0,o:quarter scores))) as 'o:SIQ'@ o:team and o:season) as 'oS(SIQ)'"})
    shortcuts.update({"oA(SIQ)": "average((sum(map(lambda p:p>0,o:quarter scores))) as 'o:SIQ'@ o:team and o:season) as 'oS(SIQ)'"})
    shortcuts.update({"opS(SIQ)": "(Sum((sum(map(lambda p:p>0,o:quarter scores))) as 'o:SIQ'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(SIQ)' "})
    shortcuts.update({"tp:SIQ": "(sum(map(lambda p:p>0,tp:quarter scores))) as 'tp:SIQ' and game number=0 returned no resu"})
    shortcuts.update({"to:SIQ": "(sum(map(lambda p:p>0,to:quarter scores))) as 'to:SIQ'"})
    shortcuts.update({"op:SIQ": "(sum(map(lambda p:p>0,op:quarter scores))) as 'op:SIQ'"})
    shortcuts.update({"t:SIQ": "(sum(map(lambda p:p>0,t:quarter scores))) as 't:SIQ'"})
    shortcuts.update({"p:SIQ": "(sum(map(lambda p:p>0,p:quarter scores))) as 'p:SIQ'"})
    shortcuts.update({"o:SIQ": "(sum(map(lambda p:p>0,o:quarter scores))) as 'o:SIQ'"})
    shortcuts.update({"SIQ": "(sum(map(lambda p:p>0,quarter scores))) as 'SIQ'"})
    shortcuts.update({"tS(SY)": "Sum((1*(1*sack yards) as 'SY') as 'SY'@ team and season) as 'tS(SY)'"})
    shortcuts.update({"tA(SY)": "average((1*(1*sack yards) as 'SY') as 'SY'@ team and season) as 'tS(SY)'"})
    shortcuts.update({"tpS(SY)": "(Sum((1*(1*sack yards) as 'SY') as 'SY'@ team and season)[ team and season-1]) as 'tpS(SY)'"})
    shortcuts.update({"oS(SY)": "Sum((1*o:(1*sack yards) as 'SY') as 'o:SY'@ o:team and o:season) as 'oS(SY)'"})
    shortcuts.update({"oA(SY)": "average((1*o:(1*sack yards) as 'SY') as 'o:SY'@ o:team and o:season) as 'oS(SY)'"})
    shortcuts.update({"opS(SY)": "(Sum((1*(1*sack yards) as 'SY') as 'SY'@ team and season)[ team and season-1]) as 'tpS(SY)'"})
    shortcuts.update({"tp:SY": "(1*tp:(1*sack yards) as 'SY') as 'tp:SY'"})
    shortcuts.update({"to:SY": "(1*to:(1*sack yards) as 'SY') as 'to:SY'"})
    shortcuts.update({"op:SY": "(1*op:(1*sack yards) as 'SY') as 'op:SY'"})
    shortcuts.update({"t:SY": "(1*t:(1*sack yards) as 'SY') as 't:SY'"})
    shortcuts.update({"p:SY": "(1*p:(1*sack yards) as 'SY') as 'p:SY'"})
    shortcuts.update({"o:SY": "(1*o:(1*sack yards) as 'SY') as 'o:SY'"})
    shortcuts.update({"SY": "(1*(1*sack yards) as 'SY') as 'SY'"})
    shortcuts.update({"tS(TOM)": "Sum((turnovers-tp:turnovers) as 'TOM'@ team and season) as 'tS(TOM)'"})
    shortcuts.update({"tA(TOM)": "average((turnovers-tp:turnovers) as 'TOM'@ team and season) as 'tS(TOM)'"})
    shortcuts.update({"tpS(TOM)": "(Sum((turnovers-tp:turnovers) as 'TOM'@ team and season)[ team and season-1]) as 'tpS(TOM)'"})
    shortcuts.update({"oS(TOM)": "Sum((o:turnovers-oo:turnovers) as 'o:TOM'@ o:team and o:season) as 'oS(TOM)' "})
    shortcuts.update({"oA(TOM)": "average((o:turnovers-oo:turnovers) as 'o:TOM'@ o:team and o:season) as 'oS(TOM)' "})
    shortcuts.update({"opS(TOM)": "(Sum((o:turnovers-oo:turnovers) as 'o:TOM'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(TOM)'"})
    shortcuts.update({"tp:TOM": "(tp:turnovers-too:turnovers) as 'tp:TOM'"})
    shortcuts.update({"to:TOM": "(to:turnovers-poo:turnovers) as 'to:TOM'"})
    shortcuts.update({"op:TOM": "(op:turnovers-oto:turnovers) as 'op:TOM'"})
    shortcuts.update({"t:TOM": "(t:turnovers-tp:turnovers) as 't:TOM'"})
    shortcuts.update({"p:TOM": "(p:turnovers-to:turnovers) as 'p:TOM'"})
    shortcuts.update({"o:TOM": "(o:turnovers-oo:turnovers) as 'o:TOM'"})
    shortcuts.update({"TOM": "(turnovers-tp:turnovers) as 'TOM' "})
    shortcuts.update({"tS(TOP)": "Sum((1*time of possession) as 'TOP'@ team and season) as 'tS(TOP)'"})
    shortcuts.update({"tA(TOP)": "average((1*time of possession) as 'TOP'@ team and season) as 'tS(TOP)'"})
    shortcuts.update({"tpS(TOP)": "(Sum((1*time of possession) as 'TOP'@ team and season)[ team and season-1]) as 'tpS(TOP)'"})
    shortcuts.update({"oS(TOP)": "Sum((1*o:time of possession) as 'o:TOP'@ o:team and o:season) as 'oS(TOP)'"})
    shortcuts.update({"oA(TOP)": "average((1*o:time of possession) as 'o:TOP'@ o:team and o:season) as 'oS(TOP)'"})
    shortcuts.update({"opS(TOP)": "(Sum((1*time of possession) as 'TOP'@ team and season)[ team and season-1]) as 'tpS(TOP)'"})
    shortcuts.update({"tp:TOP": "(1*tp:time of possession) as 'tp:TOP'"})
    shortcuts.update({"to:TOP": "(1*to:time of possession) as 'to:TOP'"})
    shortcuts.update({"op:TOP": "(1*op:time of possession) as 'op:TOP'"})
    shortcuts.update({"t:TOP": "(1*t:time of possession) as 't:TOP'"})
    shortcuts.update({"p:TOP": "(1*p:time of possession) as 'p:TOP'"})
    shortcuts.update({"o:TOP": "(1*o:time of possession) as 'o:TOP'"})
    shortcuts.update({"TOP": "(1*time of possession) as 'TOP'"})
    shortcuts.update({"tS(TO)": "Sum((1*turnovers) as 'TO'@ team and season) as 'tS(TO)'"})
    shortcuts.update({"tA(TO)": "average((1*turnovers) as 'TO'@ team and season) as 'tS(TO)'"})
    shortcuts.update({"tpS(TO)": "(Sum((1*turnovers) as 'TO'@ team and season)[ team and season-1]) as 'tpS(TO)'"})
    shortcuts.update({"oS(TO)": "Sum((1*o:turnovers) as 'o:TO'@ o:team and o:season) as 'oS(TO)'"})
    shortcuts.update({"oA(TO)": "average((1*o:turnovers) as 'o:TO'@ o:team and o:season) as 'oS(TO)'"})
    shortcuts.update({"opS(TO)": "(Sum((1*turnovers) as 'TO'@ team and season)[ team and season-1]) as 'tpS(TO)'"})
    shortcuts.update({"tp:TO": "(1*tp:turnovers) as 'tp:TO'"})
    shortcuts.update({"to:TO": "(1*to:turnovers) as 'to:TO'"})
    shortcuts.update({"op:TO": "(1*op:turnovers) as 'op:TO'"})
    shortcuts.update({"t:TO": "(1*t:turnovers) as 't:TO'"})
    shortcuts.update({"p:TO": "(1*p:turnovers) as 'p:TO'"})
    shortcuts.update({"o:TO": "(1*o:turnovers) as 'o:TO'"})
    shortcuts.update({"TO": "(1*turnovers) as 'TO'"})
    shortcuts.update({"tS(TY)": "ts((passing yards+rushing yards) as 'TY')"})
    shortcuts.update({"tA(TY)": "average((passing yards+rushing yards) as 'TY')"})
    shortcuts.update({"tpS(TY)": "(Sum((passing yards+rushing yards) as 'TY'@ team and season)[ team and season-1]) as 'tpS(TY)' and game number=0"})
    shortcuts.update({"oS(TY)": "Y Sum((passing yards+rushing yards) as 'TY'@ team and season) as 'tS(TY)'"})
    shortcuts.update({"oA(TY)": "average((passing yards+rushing yards) as 'TY'@ team and season) as 'tS(TY)'"})
    shortcuts.update({"opS(TY)": "(Sum((o:passing yards+o:rushing yards) as 'o:TY'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(TY)'"})
    shortcuts.update({"tp:TY": "(tp:passing yards+tp:rushing yards) as 'tp:TY'"})
    shortcuts.update({"to:TY": "(to:passing yards+to:rushing yards) as 'to:TY'"})
    shortcuts.update({"op:TY": "(op:passing yards+op:rushing yards) as 'op:TY'"})
    shortcuts.update({"t:TY": "(t:passing yards+t:rushing yards) as 't:TY'"})
    shortcuts.update({"p:TY": "(p:passing yards+p:rushing yards) as 'p:TY'"})
    shortcuts.update({"o:TY": "(o:passing yards+o:rushing yards) as 'o:TY'"})
    shortcuts.update({"TY": "(passing yards+rushing yards) as 'TY'"})
    shortcuts.update({"tS(YPC)": "Sum((passing yards/completions) as 'YPC'@ team and season) as 'tS(YPC)'"})
    shortcuts.update({"tA(YPC)": "average((passing yards/completions) as 'YPC'@ team and season) as 'tS(YPC)'"})
    shortcuts.update({"tpS(YPC)": "(Sum((passing yards/completions) as 'YPC'@ team and season)[ team and season-1]) as 'tpS(YPC)'"})
    shortcuts.update({"oS(YPC)": "Sum((o:passing yards/o:completions) as 'o:YPC'@ o:team and o:season) as 'oS(YPC)' "})
    shortcuts.update({"oA(YPC)": "average((o:passing yards/o:completions) as 'o:YPC'@ o:team and o:season) as 'oA(YPC)'"})
    shortcuts.update({"opS(YPC)": "(Sum((o:passing yards/o:completions) as 'o:YPC'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPC)'"})
    shortcuts.update({"tp:YPC": "(tp:passing yards/tp:completions) as 'tp:YPC'"})
    shortcuts.update({"to:YPC": "(to:passing yards/to:completions) as 'to:YPC'"})
    shortcuts.update({"op:YPC": "(op:passing yards/op:completions) as 'op:YPC'"})
    shortcuts.update({"t:YPC": "(t:passing yards/t:completions) as 't:YPC'"})
    shortcuts.update({"p:YPC": "(p:passing yards/p:completions) as 'p:YPC'"})
    shortcuts.update({"o:YPC": "(o:passing yards/o:completions) as 'o:YPC'"})
    shortcuts.update({"YPC": "(passing yards/completions) as 'YPC'"})
    shortcuts.update({"tS(YPPL)": "Sum(((1.*rushing yards+passing yards)/(rushes+passes+tp:sacks)) as 'YPPL'@ team and season) as 'tS(YPPL)'"})
    shortcuts.update({"tA(YPPL)": "average(((1.*rushing yards+passing yards)/(rushes+passes+tp:sacks)) as 'YPPL'@ team and season) as 'tS(YPPL)'"})
    shortcuts.update({"tpS(YPPL)": "(Sum(((1.*rushing yards+passing yards)/(rushes+passes+tp:sacks)) as 'YPPL'@ team and season)[ team and season-1]) as 'tpS(YPPL)'"})
    shortcuts.update({"oS(YPPL)": "Sum(((1.*o:rushing yards+o:passing yards)/(o:rushes+o:passes+oo:sacks)) as 'o:YPPL'@ o:team and o:season) as 'oS(YPPL)'"})
    shortcuts.update({"oA(YPPL)": "average(((1.*o:rushing yards+o:passing yards)/(o:rushes+o:passes+oo:sacks)) as 'o:YPPL'@ o:team and o:season) as 'oS(YPPL)'"})
    shortcuts.update({"opS(YPPL)": "(Sum(((1.*o:rushing yards+o:passing yards)/(o:rushes+o:passes+oo:sacks)) as 'o:YPPL'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPPL)'"})
    shortcuts.update({"tp:YPPL": "((1.*tp:rushing yards+tp:passing yards)/(tp:rushes+tp:passes+too:sacks)) as 'tp:YPPL'"})
    shortcuts.update({"to:YPPL": "((1.*to:rushing yards+to:passing yards)/(to:rushes+to:passes+poo:sacks)) as 'to:YPPL'"})
    shortcuts.update({"op:YPPL": "((1.*op:rushing yards+op:passing yards)/(op:rushes+op:passes+oto:sacks)) as 'op:YPPL'"})
    shortcuts.update({"t:YPPL": "((1.*t:rushing yards+t:passing yards)/(t:rushes+t:passes+tp:sacks)) as 't:YPPL'"})
    shortcuts.update({"p:YPPL": "((1.*p:rushing yards+p:passing yards)/(p:rushes+p:passes+to:sacks)) as 'p:YPPL'"})
    shortcuts.update({"o:YPPL": "((1.*o:rushing yards+o:passing yards)/(o:rushes+o:passes+oo:sacks)) as 'o:YPPL'"})
    shortcuts.update({"YPPL": "Sum(((1.*o:rushing yards+o:passing yards)/(o:rushes+o:passes+oo:sacks)) as 'o:YPPL'@ o:team and o:season) as 'oS(YPPL)'"})
    shortcuts.update({"tS(YPPT)": "Sum(((1.*rushing yards+passing yards)/points) as 'YPPT'@ team and season) as 'tS(YPPT)'"})
    shortcuts.update({"tA(YPPT)": "average(((1.*rushing yards+passing yards)/points) as 'YPPT'@ team and season) as 'tS(YPPT)'"})
    shortcuts.update({"tpS(YPPT)": "(Sum(((1.*rushing yards+passing yards)/points) as 'YPPT'@ team and season)[ team and season-1]) as 'tpS(YPPT)'"})
    shortcuts.update({"oS(YPPT)": "Sum(((1.*o:rushing yards+o:passing yards)/o:points) as 'o:YPPT'@ o:team and o:season) as 'oS(YPPT)'"})
    shortcuts.update({"oA(YPPT)": "average(((1.*o:rushing yards+o:passing yards)/o:points) as 'o:YPPT'@ o:team and o:season) as 'oS(YPPT)'"})
    shortcuts.update({"opS(YPPT)": "(Sum(((1.*o:rushing yards+o:passing yards)/o:points) as 'o:YPPT'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPPT)'"})
    shortcuts.update({"tp:YPPT": "((1.*rushing yards+passing yards)/points) as 'YPPT'"})
    shortcuts.update({"to:YPPT": "((1.*to:rushing yards+to:passing yards)/to:points) as 'to:YPPT'"})
    shortcuts.update({"op:YPPT": "((1.*op:rushing yards+op:passing yards)/op:points) as 'op:YPPT'"})
    shortcuts.update({"t:YPPT": "((1.*t:rushing yards+t:passing yards)/t:points) as 't:YPPT'"})
    shortcuts.update({"p:YPPT": "((1.*p:rushing yards+p:passing yards)/p:points) as 'p:YPPT'"})
    shortcuts.update({"o:YPPT": "((1.*o:rushing yards+o:passing yards)/o:points) as 'o:YPPT'"})
    shortcuts.update({"YPPT": "((1.*rushing yards+passing yards)/points) as 'YPPT'"})
    shortcuts.update({"tS(YPPA)": "Sum((1.*passing yards/passes) as 'YPPA'@ team and season) as 'tS(YPPA)'"})
    shortcuts.update({"tA(YPPA)": "average((1.*passing yards/passes) as 'YPPA'@ team and season) as 'tS(YPPA)'"})
    shortcuts.update({"tpS(YPPA)": "(Sum((1.*passing yards/passes) as 'YPPA'@ team and season)[ team and season-1]) as 'tpS(YPPA)'"})
    shortcuts.update({"oS(YPPA)": "Sum((1.*o:passing yards/o:passes) as 'o:YPPA'@ o:team and o:season) as 'oS(YPPA)'"})
    shortcuts.update({"oA(YPPA)": "average((1.*o:passing yards/o:passes) as 'o:YPPA'@ o:team and o:season) as 'oS(YPPA)'"})
    shortcuts.update({"opS(YPPA)": "(Sum((1.*o:passing yards/o:passes) as 'o:YPPA'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPPA)'"})
    shortcuts.update({"tp:YPPA": "(1.*tp:passing yards/tp:passes) as 'tp:YPPA'"})
    shortcuts.update({"to:YPPA": "(1.*to:passing yards/to:passes) as 'to:YPPA'"})
    shortcuts.update({"op:YPPA": "(1.*op:passing yards/op:passes) as 'op:YPPA'"})
    shortcuts.update({"t:YPPA": "(1.*t:passing yards/t:passes) as 't:YPPA'"})
    shortcuts.update({"p:YPPA": "(1.*p:passing yards/p:passes) as 'p:YPPA'"})
    shortcuts.update({"o:YPPA": "(1.*o:passing yards/o:passes) as 'o:YPPA'"})
    shortcuts.update({"YPPA": "(1.*passing yards/passes) as 'YPPA'"})
    shortcuts.update({"tS(YPPP)": "Sum((1.*passing yards/(passes+tp:sacks)) as 'YPPP'@ team and season) as 'tS(YPPP)'"})
    shortcuts.update({"tA(YPPP)": "average((1.*passing yards/(passes+tp:sacks)) as 'YPPP'@ team and season) as 'tS(YPPP)'"})
    shortcuts.update({"tpS(YPPP)": "(Sum((1.*passing yards/(passes+tp:sacks)) as 'YPPP'@ team and season)[ team and season-1]) as 'tpS(YPPP)'"})
    shortcuts.update({"oS(YPPP)": "Sum((1.*o:passing yards/(o:passes+oo:sacks)) as 'o:YPPP'@ o:team and o:season) as 'oS(YPPP)'"})
    shortcuts.update({"oA(YPPP)": "average((1.*o:passing yards/(o:passes+oo:sacks)) as 'o:YPPP'@ o:team and o:season) as 'oS(YPPP)'"})
    shortcuts.update({"opS(YPPP)": "(Sum((1.*o:passing yards/(o:passes+oo:sacks)) as 'o:YPPP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPPP)'"})
    shortcuts.update({"tp:YPPP": "(1.*tp:passing yards/(tp:passes+too:sacks)) as 'tp:YPPP'"})
    shortcuts.update({"to:YPPP": "(1.*to:passing yards/(to:passes+poo:sacks)) as 'to:YPPP'"})
    shortcuts.update({"op:YPPP": "(1.*op:passing yards/(op:passes+oto:sacks)) as 'op:YPPP'"})
    shortcuts.update({"t:YPPP": "(1.*t:passing yards/(t:passes+tp:sacks)) as 't:YPPP'"})
    shortcuts.update({"p:YPPP": "(1.*p:passing yards/(p:passes+tp:sacks)) as 'p:YPPP'"})
    shortcuts.update({"o:YPPP": "(1.*o:passing yards/(o:passes+oo:sacks)) as 'o:YPPP'"})
    shortcuts.update({"YPPP": "(1.*passing yards/(passes+tp:sacks)) as 'YPPP'"})
    shortcuts.update({"tS(YPRA)": "Sum((1.*rushing yards/rushes) as 'YPRA'@ team and season) as 'tS(YPRA)'"})
    shortcuts.update({"tA(YPRA)": "average((1.*rushing yards/rushes) as 'YPRA'@ team and season) as 'tS(YPRA)'"})
    shortcuts.update({"tpS(YPRA)": "(Sum((1.*rushing yards/rushes) as 'YPRA'@ team and season)[ team and season-1]) as 'tpS(YPRA)'"})
    shortcuts.update({"oS(YPRA)": "Sum((1.*o:rushing yards/o:rushes) as 'o:YPRA'@ o:team and o:season) as 'oS(YPRA)'"})
    shortcuts.update({"oA(YPRA)": "average((1.*o:rushing yards/o:rushes) as 'o:YPRA'@ o:team and o:season) as 'oS(YPRA)'"})
    shortcuts.update({"opS(YPRA)": "(Sum((1.*o:rushing yards/o:rushes) as 'o:YPRA'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(YPRA)'"})
    shortcuts.update({"tp:YPRA": "(1.*tp:rushing yards/tp:rushes) as 'tp:YPRA' and game number=0 returned no re"})
    shortcuts.update({"to:YPRA": "(1.*to:rushing yards/to:rushes) as 'to:YPRA' and game number=0 returned no re"})
    shortcuts.update({"op:YPRA": "(1.*op:rushing yards/op:rushes) as 'op:YPRA' and game number=0 returned no re"})
    shortcuts.update({"t:YPRA": "(1.*t:rushing yards/t:rushes) as 't:YPRA' and game number=0 returned no re"})
    shortcuts.update({"p:YPRA": "(1.*p:rushing yards/p:rushes) as 'p:YPRA' and game number=0 returned no re"})
    shortcuts.update({"o:YPRA": "(1.*o:rushing yards/o:rushes) as 'o:YPRA' and game number=0 returned no re"})
    shortcuts.update({"YPRA": "(1.*rushing yards/rushes) as 'YPRA'"})
    shortcuts.update({"tS(STDRAPG)": "Sum(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season) as 'tS(STDRAPG)'"})
    shortcuts.update({"tA(STDRAPG)": "average(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season) as 'tS(STDRAPG)'"})
    shortcuts.update({"tpS(STDRAPG)": "(Sum(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season)[ team and season-1]) as 'tpS(STDRAPG)'"})
    shortcuts.update({"oS(STDRAPG)": "Sum(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season) as 'oS(STDRAPG)'"})
    shortcuts.update({"oA(STDRAPG)": "average(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season) as 'oS(STDRAPG)'"})
    shortcuts.update({"opS(STDRAPG)": "(Sum(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(STDRAPG)'"})
    shortcuts.update({"tp:STDRAPG": "average(tp:rushes@tp:team and tp:season and tp:season=season) as 'tp:STDRAPG'"})
    shortcuts.update({"to:STDRAPG": "average(to:rushes@to:team and to:season and to:season=season) as 'to:STDRAPG'"})
    shortcuts.update({"op:STDRAPG": "average(op:rushes@op:team and op:season and op:season=season) as 'op:STDRAPG'"})
    shortcuts.update({"t:STDRAPG": "average(t:rushes@t:team and t:season and t:season=season) as 't:STDRAPG'"})
    shortcuts.update({"p:STDRAPG": "average(p:rushes@p:team and p:season and p:season=season) as 'p:STDRAPG'"})
    shortcuts.update({"o:STDRAPG": "average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'"})
    shortcuts.update({"STDRAPG": "average(rushes@team and season and season=season) as 'STDRAPG'"})
    shortcuts.update({"tS(STDoRAPG)": "Sum(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season) as 'tS(STDRAPG)'"})
    shortcuts.update({"tA(STDoRAPG)": "average(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season) as 'tS(STDRAPG)'"})
    shortcuts.update({"tpS(STDoRAPG)": "(Sum(average(rushes@team and season and season=season) as 'STDRAPG'@ team and season)[ team and season-1]) as 'tpS(STDRAPG)'"})
    shortcuts.update({"oS(STDoRAPG)": "Sum(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season) as 'oS(STDRAPG)'"})
    shortcuts.update({"oA(STDoRAPG)": "average(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season) as 'oS(STDRAPG)'"})
    shortcuts.update({"opS(STDoRAPG)": "(Sum(average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(STDRAPG)'"})
    shortcuts.update({"tp:STDoRAPG": "average(tp:rushes@tp:team and tp:season and tp:season=season) as 'tp:STDRAPG'"})
    shortcuts.update({"to:STDoRAPG": "average(to:rushes@to:team and to:season and to:season=season) as 'to:STDRAPG'"})
    shortcuts.update({"op:STDoRAPG": "average(op:rushes@op:team and op:season and op:season=season) as 'op:STDRAPG'"})
    shortcuts.update({"t:STDoRAPG": "average(t:rushes@t:team and t:season and t:season=season) as 't:STDRAPG'"})
    shortcuts.update({"p:STDoRAPG": "average(p:rushes@p:team and p:season and p:season=season) as 'p:STDRAPG'"})
    shortcuts.update({"o:STDoRAPG": "average(o:rushes@o:team and o:season and o:season=season) as 'o:STDRAPG'"})
    shortcuts.update({"STDoRAPG": "average(rushes@team and season and season=season) as 'STDRAPG'"})
    shortcuts.update({"tS(PRSW)": "Sum((Sum(((0<Team:points-Team:o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'@ team and season) as 'tS(PRSW)'"})
    shortcuts.update({"tA(PRSW)": "average((Sum(((0<Team:points-Team:o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'@ team and season) as 'tS(PRSW)'"})
    shortcuts.update({"tpS(PRSW)": "(Sum((Sum(((0<Team:points-Team:o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'@ team and season)[ team and season-1]) as 'tpS(PRSW)' and game number=0"})
    shortcuts.update({"oS(PRSW)": "Sum((Sum(((0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:playoffs=0 and o:season)[o:team and o:playoffs=0 and o:season-1]) as 'o:PRSW'@ o:team and o:season) as 'oS(PRSW)' and game number=0"})
    shortcuts.update({"oA(PRSW)": "average((Sum(((0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:playoffs=0 and o:season)[o:team and o:playoffs=0 and o:season-1]) as 'o:PRSW'@ o:team and o:season) as 'oS(PRSW)' and game number=0"})
    shortcuts.update({"opS(PRSW)": "(Sum((Sum(((0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:playoffs=0 and o:season)[o:team and o:playoffs=0 and o:season-1]) as 'o:PRSW'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(PRSW)'"})
    shortcuts.update({"tp:PRSW": "(Sum(((0<Team:tp:points-Team:too:points) as 'tp:W')@tp:team and tp:playoffs=0 and tp:season)[tp:team and tp:playoffs=0 and tp:season-1]) as 'tp:PRSW'"})
    shortcuts.update({"to:PRSW": "(Sum(((0<Team:to:points-Team:poo:points) as 'to:W')@to:team and to:playoffs=0 and to:season)[to:team and to:playoffs=0 and to:season-1]) as 'to:PRSW'"})
    shortcuts.update({"op:PRSW": "(Sum(((0<Team:op:points-Team:oto:points) as 'op:W')@op:team and op:playoffs=0 and op:season)[op:team and op:playoffs=0 and op:season-1]) as 'op:PRSW'"})
    shortcuts.update({"t:PRSW": "(Sum(((0<Team:t:points-Team:tp:points) as 't:W')@t:team and t:playoffs=0 and t:season)[t:team and t:playoffs=0 and t:season-1]) as 't:PRSW'"})
    shortcuts.update({"p:PRSW": "(Sum(((0<Team:p:points-Team:to:points) as 'p:W')@p:team and p:playoffs=0 and p:season)[p:team and p:playoffs=0 and p:season-1]) as 'p:PRSW'"})
    shortcuts.update({"o:PRSW": "(Sum(((0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:playoffs=0 and o:season)[o:team and o:playoffs=0 and o:season-1]) as 'o:PRSW'"})
    shortcuts.update({"PRSW": "(Sum(((0<Team:points-Team:o:points) as 'W')@team and playoffs=0 and season)[team and playoffs=0 and season-1]) as 'PRSW'"})
    shortcuts.update({"tS(FD)": "Sum((1*first downs) as 'FD'@ team and season) as 'tS(FD)'"})
    shortcuts.update({"tA(FD)": "average((1*first downs) as 'FD'@ team and season) as 'tS(FD)'"})
    shortcuts.update({"tpS(FD)": "(Sum((1*first downs) as 'FD'@ team and season)[ team and season-1]) as 'tpS(FD)'"})
    shortcuts.update({"oS(FD)": "Sum((1*o:first downs) as 'o:FD'@ o:team and o:season) as 'oS(FD)'"})
    shortcuts.update({"oA(FD)": "average((1*o:first downs) as 'o:FD'@ o:team and o:season) as 'oS(FD)'"})
    shortcuts.update({"opS(FD)": "(Sum((1*first downs) as 'FD'@ team and season)[ team and season-1]) as 'tpS(FD)'"})
    shortcuts.update({"tp:FD": "(1*tp:first downs) as 'tp:FD'"})
    shortcuts.update({"to:FD": "(1*to:first downs) as 'to:FD'"})
    shortcuts.update({"op:FD": "(1*op:first downs) as 'op:FD'"})
    shortcuts.update({"t:FD": "(1*t:first downs) as 't:FD'"})
    shortcuts.update({"p:FD": "(1*p:first downs) as 'p:FD'"})
    shortcuts.update({"o:FD": "(1*o:first downs) as 'o:FD'"})
    shortcuts.update({"FD": "(1*first downs) as 'FD'"})
    shortcuts.update({"tS(TD)": "Sum((1*touchdowns) as 'TD'@ team and season) as 'tS(TD)'"})
    shortcuts.update({"tA(TD)": "average((1*touchdowns) as 'TD'@ team and season) as 'tS(TD)'"})
    shortcuts.update({"tpS(TD)": "(Sum((1*touchdowns) as 'TD'@ team and season)[ team and season-1]) as 'tpS(TD)'"})
    shortcuts.update({"oS(TD)": "Sum((1*o:touchdowns) as 'o:TD'@ o:team and o:season) as 'oS(TD)'"})
    shortcuts.update({"oA(TD)": "average((1*o:touchdowns) as 'o:TD'@ o:team and o:season) as 'oS(TD)'"})
    shortcuts.update({"opS(TD)": "(Sum((1*touchdowns) as 'TD'@ team and season)[ team and season-1]) as 'tpS(TD)'"})
    shortcuts.update({"TD": "(1*touchdowns) as 'TD'"})
    shortcuts.update({"tp:TD": "(1*tp:touchdowns) as 'to:TD'"})
    shortcuts.update({"to:TD": "(1*to:touchdowns) as 'to:TD'"})
    shortcuts.update({"op:TD": "(1*op:touchdowns) as 'op:TD'"})
    shortcuts.update({"t:TD": "(1*t:touchdowns) as 't:TD'"})
    shortcuts.update({"p:TD": "(1*p:touchdowns) as 'p:TD'"})
    shortcuts.update({"o:TD": "(1*o:touchdowns) as 'o:TD'"})
    shortcuts.update({"tS(AWP)": "Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='away')) as 'AWP'@ team and season) as 'tS(AWP)' "})
    shortcuts.update({"tA(AWP)": "average((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='away')) as 'AWP'@ team and season) as 'tS(AWP)' "})
    shortcuts.update({"tpS(AWP)": "(Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='away')) as 'AWP'@ team and season)[ team and season-1]) as 'tpS(AWP)'"})
    shortcuts.update({"oS(AWP)": "Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'@ o:team and o:season) as 'oS(AWP)'"})
    shortcuts.update({"oA(AWP)": "average((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'@ o:team and o:season) as 'oS(AWP)'"})
    shortcuts.update({"opS(AWP)": "(Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(AWP)'"})
    shortcuts.update({"tp:AWP": "(average(100*(((0<Team:tp:points-Team:too:points) as 'tp:W' or (0<Team:too:points-Team:tp:points) as 'tp:L' or 1/0) and (0<Team:tp:points-Team:too:points) as 'tp:W')@tp:team and tp:season and tp:site='away' and tp:season=season)) as 'tp:AWP'"})
    shortcuts.update({"to:AWP": "(average(100*(((0<Team:to:points-Team:poo:points) as 'to:W' or (0<Team:poo:points-Team:to:points) as 'to:L' or 1/0) and (0<Team:to:points-Team:poo:points) as 'to:W')@to:team and to:season and to:site='away' and to:season=season)) as 'to:AWP'"})
    shortcuts.update({"op:AWP": "(average(100*(((0<Team:op:points-Team:oto:points) as 'op:W' or (0<Team:oto:points-Team:op:points) as 'op:L' or 1/0) and (0<Team:op:points-Team:oto:points) as 'op:W')@op:team and op:season and op:site='away' and op:season=season)) as 'op:AWP'"})
    shortcuts.update({"t:AWP": "(average(100*(((0<Team:t:points-Team:tp:points) as 't:W' or (0<Team:tp:points-Team:t:points) as 't:L' or 1/0) and (0<Team:t:points-Team:tp:points) as 't:W')@t:team and t:season and t:site='away' and t:season=season)) as 't:AWP'"})
    shortcuts.update({"p:AWP": "(average(100*(((0<Team:p:points-Team:to:points) as 'p:W' or (0<Team:to:points-Team:p:points) as 'p:L' or 1/0) and (0<Team:p:points-Team:to:points) as 'p:W')@p:team and p:season and p:site='away' and p:season=season)) as 'p:AWP'"})
    shortcuts.update({"o:AWP": "(average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='away' and o:season=season)) as 'o:AWP'"})
    shortcuts.update({"AWP": "(average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='away')) as 'AWP'"})
    shortcuts.update({"tS(HWP)": "Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='home')) as 'HWP'@ team and season) as 'tS(HWP)'"})
    shortcuts.update({"tA(HWP)": "average((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='home')) as 'HWP'@ team and season) as 'tS(HWP)'"})
    shortcuts.update({"tpS(HWP)": "(Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='home')) as 'HWP'@ team and season)[ team and season-1]) as 'tpS(HWP)'"})
    shortcuts.update({"oS(HWP)": "Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'@ o:team and o:season) as 'oS(HWP)'"})
    shortcuts.update({"oA(HWP)": "average((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'@ o:team and o:season) as 'oS(HWP)'"})
    shortcuts.update({"opS(HWP)": "(Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(HWP)'"})
    shortcuts.update({"tp:HWP": "(average(100*(((0<Team:tp:points-Team:too:points) as 'tp:W' or (0<Team:too:points-Team:tp:points) as 'tp:L' or 1/0) and (0<Team:tp:points-Team:too:points) as 'tp:W')@tp:team and tp:season and tp:site='home' and tp:season=season)) as 'tp:HWP'"})
    shortcuts.update({"to:HWP": "(average(100*(((0<Team:to:points-Team:poo:points) as 'to:W' or (0<Team:poo:points-Team:to:points) as 'to:L' or 1/0) and (0<Team:to:points-Team:poo:points) as 'to:W')@to:team and to:season and to:site='home' and to:season=season)) as 'to:HWP'"})
    shortcuts.update({"op:HWP": "(average(100*(((0<Team:op:points-Team:oto:points) as 'op:W' or (0<Team:oto:points-Team:op:points) as 'op:L' or 1/0) and (0<Team:op:points-Team:oto:points) as 'op:W')@op:team and op:season and op:site='home' and op:season=season)) as 'op:HWP'"})
    shortcuts.update({"t:HWP": "(average(100*(((0<Team:t:points-Team:tp:points) as 't:W' or (0<Team:tp:points-Team:t:points) as 't:L' or 1/0) and (0<Team:t:points-Team:tp:points) as 't:W')@t:team and t:season and t:site='home' and t:season=season)) as 't:HWP'"})
    shortcuts.update({"p:HWP": "(average(100*(((0<Team:p:points-Team:to:points) as 'p:W' or (0<Team:to:points-Team:p:points) as 'p:L' or 1/0) and (0<Team:p:points-Team:to:points) as 'p:W')@p:team and p:season and p:site='home' and p:season=season)) as 'p:HWP'"})
    shortcuts.update({"o:HWP": "(average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season and o:site='home' and o:season=season)) as 'o:HWP'"})
    shortcuts.update({"HWP": "(average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season and site='home')) as 'HWP'"})
    shortcuts.update({"tS(WP)": "Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season)) as 'WP'@ team and season) as 'tS(WP)'"})
    shortcuts.update({"tA(WP)": "average((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season)) as 'WP'@ team and season) as 'tS(WP)'"})
    shortcuts.update({"tpS(WP)": "(Sum((average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season)) as 'WP'@ team and season)[ team and season-1]) as 'tpS(WP)'"})
    shortcuts.update({"oS(WP)": "Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season)) as 'o:WP'@ o:team and o:season) as 'oS(WP)'"})
    shortcuts.update({"oA(WP)": "average((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season)) as 'o:WP'@ o:team and o:season) as 'oS(WP)'"})
    shortcuts.update({"opS(WP)": "(Sum((average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season)) as 'o:WP'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(WP)'"})
    shortcuts.update({"tp:WP": "(average(100*(((0<Team:tp:points-Team:too:points) as 'tp:W' or (0<Team:too:points-Team:tp:points) as 'tp:L' or 1/0) and (0<Team:tp:points-Team:too:points) as 'tp:W')@tp:team and tp:season)) as 'tp:WP'"})
    shortcuts.update({"to:WP": "(average(100*(((0<Team:to:points-Team:poo:points) as 'to:W' or (0<Team:poo:points-Team:to:points) as 'to:L' or 1/0) and (0<Team:to:points-Team:poo:points) as 'to:W')@to:team and to:season and to:season=season)) as 'to:WP'"})
    shortcuts.update({"op:WP": "(average(100*(((0<Team:op:points-Team:oto:points) as 'op:W' or (0<Team:oto:points-Team:op:points) as 'op:L' or 1/0) and (0<Team:op:points-Team:oto:points) as 'op:W')@op:team and op:season and op:season=season)) as 'op:WP'"})
    shortcuts.update({"t:WP": "(average(100*(((0<Team:t:points-Team:tp:points) as 't:W' or (0<Team:tp:points-Team:t:points) as 't:L' or 1/0) and (0<Team:t:points-Team:tp:points) as 't:W')@t:team and t:season)) as 't:WP'"})
    shortcuts.update({"p:WP": "(average(100*(((0<Team:p:points-Team:to:points) as 'p:W' or (0<Team:to:points-Team:p:points) as 'p:L' or 1/0) and (0<Team:p:points-Team:to:points) as 'p:W')@p:team and p:season and p:season=season)) as 'p:WP'"})
    shortcuts.update({"o:WP": "(average(100*(((0<Team:o:points-Team:oo:points) as 'o:W' or (0<Team:oo:points-Team:o:points) as 'o:L' or 1/0) and (0<Team:o:points-Team:oo:points) as 'o:W')@o:team and o:season)) as 'o:WP'"})
    shortcuts.update({"WP": "(average(100*(((0<Team:points-Team:o:points) as 'W' or (0<Team:o:points-Team:points) as 'L' or 1/0) and (0<Team:points-Team:o:points) as 'W')@team and season)) as 'WP'"})
    shortcuts.update({"tS(A)": "Sum((site=='away') as 'A'@ team and season) as 'tS(A)'"})
    shortcuts.update({"tA(A)": "average((site=='away') as 'A'@ team and season) as 'tS(A)'"})
    shortcuts.update({"tpS(A)": "(Sum((site=='away') as 'A'@ team and season)[ team and season-1]) as 'tpS(A)'"})
    shortcuts.update({"oS(A)": "Sum((o:site=='away') as 'o:A'@ o:team and o:season) as 'oS(A)'"})
    shortcuts.update({"oA(A)": "average((o:site=='away') as 'o:A'@ o:team and o:season) as 'oS(A)'"})
    shortcuts.update({"opS(A)": "(Sum((o:site=='away') as 'o:A'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(A)'"})
    shortcuts.update({"tp:A": "(tp:site=='away') as 'tp:A'"})
    shortcuts.update({"to:A": "(to:site=='away') as 'to:A'"})
    shortcuts.update({"op:A": "(op:site=='away') as 'op:A'"})
    shortcuts.update({"t:A": "(t:site=='away') as 't:A'"})
    shortcuts.update({"p:A": "(p:site=='away') as 'p:A'"})
    shortcuts.update({"o:A": "(o:site=='away') as 'o:A'"})
    shortcuts.update({"tS(H)": "Sum((site=='home') as 'H'@ team and season) as 'tS(H)'"})
    shortcuts.update({"tA(H)": "average((site=='home') as 'H'@ team and season) as 'tS(H)'"})
    shortcuts.update({"tpS(H)": "(Sum((site=='home') as 'H'@ team and season)[ team and season-1]) as 'tpS(H)'"})
    shortcuts.update({"oS(H)": "Sum((o:site=='home') as 'o:H'@ o:team and o:season) as 'oS(H)'"})
    shortcuts.update({"oA(H)": "average((o:site=='home') as 'o:H'@ o:team and o:season) as 'oS(H)'"})
    shortcuts.update({"opS(H)": "(Sum((o:site=='home') as 'o:H'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(H)'"})
    shortcuts.update({"tp:H": "(tp:site=='home') as 'tp:H'"})
    shortcuts.update({"to:H": "(to:site=='home') as 'to:H'"})
    shortcuts.update({"op:H": "(op:site=='home') as 'op:H'"})
    shortcuts.update({"t:H": "(t:site=='home') as 't:H'"})
    shortcuts.update({"p:H": "(p:site=='home') as 'p:H'"})
    shortcuts.update({"o:H": "(o:site=='home') as 'o:H'"})
    shortcuts.update({"H": "(site=='home') as 'H'"})
    shortcuts.update({"tS(F)": "Sum((line+0<0) as 'F'@ team and season) as 'tS(F)'"})
    shortcuts.update({"tA(F)": "average((line+0<0) as 'F'@ team and season) as 'tS(F)'"})
    shortcuts.update({"tpS(F)": "(Sum((line+0<0) as 'F'@ team and season)[ team and season-1]) as 'tpS(F)'"})
    shortcuts.update({"oS(F)": "Sum((o:line+0<0) as 'o:F'@ o:team and o:season) as 'oS(F)'"})
    shortcuts.update({"oA(F)": "average((o:line+0<0) as 'o:F'@ o:team and o:season) as 'oS(F)'"})
    shortcuts.update({"opS(F)": "(Sum((o:line+0<0) as 'o:F'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(F)'"})
    shortcuts.update({"tp:F": "(tp:line+0<0) as 'tp:F'"})
    shortcuts.update({"to:F": "(to:line+0<0) as 'to:F'"})
    shortcuts.update({"op:F": "(op:line+0<0) as 'op:F'"})
    shortcuts.update({"t:F": "(t:line+0<0) as 't:F'"})
    shortcuts.update({"p:F": "(p:line+0<0) as 'p:F'"})
    shortcuts.update({"o:F": "(o:line+0<0) as 'o:F'"})
    shortcuts.update({"F": "(line+0<0) as 'F'"})
    shortcuts.update({"tS(D)": "Sum((line+0>0) as 'D'@ team and season) as 'tS(D)'"})
    shortcuts.update({"tA(D)": "average((line+0>0) as 'D'@ team and season) as 'tS(D)'"})
    shortcuts.update({"tpS(D)": "(Sum((line+0>0) as 'D'@ team and season)[ team and season-1]) as 'tpS(D)'"})
    shortcuts.update({"oS(D)": "Sum((o:line+0>0) as 'o:D'@ o:team and o:season) as 'oS(D)'"})
    shortcuts.update({"oA(D)": "average((o:line+0>0) as 'o:D'@ o:team and o:season) as 'oS(D)'"})
    shortcuts.update({"opS(D)": "(Sum((o:line+0>0) as 'o:D'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(D)'"})
    shortcuts.update({"tp:D": "(tp:line+0>0) as 'tp:D'"})
    shortcuts.update({"to:D": "(to:line+0>0) as 'to:D'"})
    shortcuts.update({"op:D": "(op:line+0>0) as 'op:D'"})
    shortcuts.update({"t:D": "(t:line+0>0) as 't:D'"})
    shortcuts.update({"p:D": "(p:line+0>0) as 'p:D'"})
    shortcuts.update({"o:D": "(o:line+0>0) as 'o:D'"})
    shortcuts.update({"D": "(line+0>0) as 'D'"})
    shortcuts.update({"tS(W)": "Sum((0<Team:points-Team:o:points) as 'W'@ team and season) as 'tS(W)'"})
    shortcuts.update({"tA(W)": "average((0<Team:points-Team:o:points) as 'W'@ team and season) as 'tS(W)'"})
    shortcuts.update({"tpS(W)": "(Sum((0<Team:points-Team:o:points) as 'W'@ team and season)[ team and season-1]) as 'tpS(W)'"})
    shortcuts.update({"oS(W)": "Sum((0<Team:o:points-Team:oo:points) as 'o:W'@ o:team and o:season) as 'oS(W)'"})
    shortcuts.update({"oA(W)": "average((0<Team:o:points-Team:oo:points) as 'o:W'@ o:team and o:season) as 'oS(W)'"})
    shortcuts.update({"opS(W)": "(Sum((0<Team:o:points-Team:oo:points) as 'o:W'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(W)'"})
    shortcuts.update({"tp:W": "(0<Team:tp:points-Team:too:points) as 'tp:W'"})
    shortcuts.update({"to:W": "(0<Team:to:points-Team:poo:points) as 'to:W'"})
    shortcuts.update({"op:W": "(0<Team:op:points-Team:oto:points) as 'op:W'"})
    shortcuts.update({"t:W": "(0<Team:t:points-Team:tp:points) as 't:W'"})
    shortcuts.update({"p:W": "(0<Team:p:points-Team:po:points) as 'p:W'"})
    shortcuts.update({"o:W": "(0<Team:o:points-Team:oo:points) as 'o:W'"})
    shortcuts.update({"W": "(0<Team:points-Team:o:points) as 'W'"})
    shortcuts.update({"tS(L)": "Sum((0<Team:o:points-Team:points) as 'L'@ team and season) as 'tS(L)'"})
    shortcuts.update({"tA(L)": "average((0<Team:o:points-Team:points) as 'L'@ team and season) as 'tS(L)'"})
    shortcuts.update({"tpS(L)": "(Sum((0<Team:o:points-Team:points) as 'L'@ team and season)[ team and season-1]) as 'tpS(L)'"})
    shortcuts.update({"oS(L)": "Sum((0<Team:oo:points-Team:o:points) as 'o:L'@ o:team and o:season) as 'oS(L)'"})
    shortcuts.update({"oA(L)": "average((0<Team:oo:points-Team:o:points) as 'o:L'@ o:team and o:season) as 'oS(L)'"})
    shortcuts.update({"opS(L)": "(Sum((0<Team:oo:points-Team:o:points) as 'o:L'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(L)'"})
    shortcuts.update({"tp:L": "(0<Team:too:points-Team:tp:points) as 'tp:L'"})
    shortcuts.update({"to:L": "(0<Team:poo:points-Team:to:points) as 'to:L'"})
    shortcuts.update({"op:L": "(0<Team:oto:points-Team:op:points) as 'op:L'"})
    shortcuts.update({"t:L": "(0<Team:tp:points-Team:t:points) as 't:L'"})
    shortcuts.update({"p:L": "(0<Team:po:points-Team:p:points) as 'p:L'"})
    shortcuts.update({"o:L": "(0<Team:oo:points-Team:o:points) as 'o:L'"})
    shortcuts.update({"L": "(0<Team:o:points-Team:points) as 'L'"})
    shortcuts.update({"tS(O)": "Sum((total+0<points+o:points) as 'O'@ team and season) as 'tS(O)'"})
    shortcuts.update({"tA(O)": "average((total+0<points+o:points) as 'O'@ team and season) as 'tS(O)'"})
    shortcuts.update({"tpS(O)": "(Sum((total+0<points+o:points) as 'O'@ team and season)[ team and season-1]) as 'tpS(O)'"})
    shortcuts.update({"oS(O)": "Sum((o:total+0<o:points+oo:points) as 'o:O'@ o:team and o:season) as 'oS(O)'"})
    shortcuts.update({"oA(O)": "average((o:total+0<o:points+oo:points) as 'o:O'@ o:team and o:season) as 'oS(O)'"})
    shortcuts.update({"opS(O)": "(Sum((o:total+0<o:points+oo:points) as 'o:O'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(O)'"})
    shortcuts.update({"tp:O": "(tp:total+0<tp:points+too:points) as 'tp:O'"})
    shortcuts.update({"to:O": "(tp:total+0<tp:points+too:points) as 'tp:O'"})
    shortcuts.update({"op:O": "(to:total+0<to:points+poo:points) as 'to:O'"})
    shortcuts.update({"t:O": "(t:total+0<t:points+tp:points) as 't:O'"})
    shortcuts.update({"p:O": "(p:total+0<p:points+to:points) as 'p:O'"})
    shortcuts.update({"o:O": "(o:total+0<o:points+oo:points) as 'o:O'"})
    shortcuts.update({"O": "o((total+0<points+o:points) as 'O')"})
    shortcuts.update({"tS(U)": "((points+o:points< total) as 'U'@ team and season) as 'tS(U)'"})
    shortcuts.update({"tA(U)": "average((points+o:points< total) as 'U'@ team and season) as 'tS(U)'"})
    shortcuts.update({"tpS(U)": "(Sum((points+o:points< total) as 'U'@ team and season)[ team and season-1]) as 'tpS(U)'"})
    shortcuts.update({"oS(U)": "((o:points+oo:points< o:total) as 'o:U'@ o:team and o:season) as 'oS(U)'"})
    shortcuts.update({"oA(U)": "average((o:points+oo:points< o:total) as 'o:U'@ o:team and o:season) as 'oS(U)'"})
    shortcuts.update({"opS(U)": "(Sum((o:points+oo:points< o:total) as 'o:U'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(U)'"})
    shortcuts.update({"tp:U": "(tp:points+too:points< tp:total) as 'tp:U'"})
    shortcuts.update({"to:U": "(to:points+poo:points< to:total) as 'to:U'"})
    shortcuts.update({"op:U": "(op:points+oto:points< op:total) as 'op:U'"})
    shortcuts.update({"t:U": "(t:points+tp:points< t:total) as 't:U'"})
    shortcuts.update({"p:U": "(p:points+to:points< p:total) as 'p:U'"})
    shortcuts.update({"o:U": "(o:points+oo:points< o:total) as 'o:U'"})
    shortcuts.update({"U": "(points+o:points< total) as 'U'"})
    shortcuts.update({"tS(C)": "Sum((conference=tp:conference) as 'C'@ team and season) as 'tS(C)'"})
    shortcuts.update({"tA(C)": "average((conference=tp:conference) as 'C'@ team and season) as 'tS(C)'"})
    shortcuts.update({"tpS(C)": "(Sum((conference=tp:conference) as 'C'@ team and season)[ team and season-1]) as 'tpS(C)'"})
    shortcuts.update({"oS(C)": "Sum((o:conference=oo:conference) as 'o:C'@ o:team and o:season) as 'oS(C)'"})
    shortcuts.update({"oA(C)": "average((o:conference=oo:conference) as 'o:C'@ o:team and o:season) as 'oS(C)'"})
    shortcuts.update({"opS(C)": "(Sum((o:conference=oo:conference) as 'o:C'@ o:team and o:season)[ o:team and o:season-1]) as 'opS(C)'"})
    shortcuts.update({"tp:C": "(tp:conference=too:conference) as 'tp:C' "})
    shortcuts.update({"to:C": "(to:conference=poo:conference) as 'to:C' "})
    shortcuts.update({"op:C": "(op:conference=oto:conference) as 'op:C'  "})
    shortcuts.update({"t:C": "(t:conference=tp:conference) as 't:C' "})
    shortcuts.update({"p:C": "(p:conference=to:conference) as 'p:C' "})
    shortcuts.update({"o:C": "(o:conference=oo:conference) as 'p:C' "})
    shortcuts.update({"C": "(conference=tp:conference) as 'C'"})
    #shortcuts.update({"A(": "average("})
    #shortcuts.update({"S(": "Sum("})
    shortcuts.update({"A": "(site=='away') as 'A'"})
    #STDRYPG
    #STDPYPG

    return shortcuts


def fn_ok_to_add_quotes(string):
    ######### NOT USED
    equal_pos=string.find('=')
    add_quote=0
    if equal_pos>0:
        before_equal==string[:equal_pos]
        after_equal=string[equal_pos:]
        if (find.before_equal('division')>0 and find.after_equal('division')>0) or (find.before_equal('conference')>0 and find.after_equal('conference')>0):
            add_quote=0
        else:
            add_quote=1
    return add_quote


# In[ ]:


def add_paddings(c):
    max_list = 0
    for lst in c:
        if len(lst) > max_list:
            max_list = len(lst)
    for lst in c:
        if len(lst) < max_list:
            lst += ['-'] * (max_list - len(lst))


# In[ ]:


def fncount_summatives(q):

    #q="/ (tS(plays)+tS(o:plays))"
    summatives=list(['tS','tA','oA'])
    _c=0
    for s in summatives:
        c=q.find(s)
        if c>=0:
            _c+=1
            c=q.find(s,c+1)
            if c>=0:
                _c+=1
        if _c>1: 
            break

    #print(_c)
    return _c


# In[ ]:


def fnstrip_alias(q):

    as_pos=q.find(' as ')
    newq=''
    #newq=q[:as_pos]
    lnquote=0
    while as_pos>=0:

        squote=q.find("'",as_pos)
        dquote=q.find('"',as_pos)
        if squote>0:
            quote=squote
            dquote=-1
        else:
            quote=dquote
            squote=-1
        if squote>0:
            nquote=q.find("'",quote+1)
        else:
            nquote=q.find('"',quote+1)
        #print(newq)
        #print(quote)
        newq=newq+q[lnquote:as_pos]
        lnquote=nquote+1
        as_pos=q.find(' as ',nquote+1)
        #print(newq)

    
    return


# In[ ]:


def fnchop_sdql(q):
    # used to determine grouping
    #q=sdql
    #q=sdql
    q=q+" "
    qlen=len(q)
    leftp=rightp=0

    sdql_parts=list()
    spos=0
    for j in range(0,qlen):
        #print(q[j:j+1],j)
        
        if q[j:j+1]=="(":
            leftp+=1
        if q[j:j+1]==")":
            rightp+=1
        if leftp>0 and leftp==rightp and q[j:j+1]==")":
            sdql_parts.append(q[spos:j+1])
            spos=j+1

        else:    
            if leftp==rightp:
                if q[j:j+1]=='@':
                    sdql_parts.append(q[spos:j-1])
                    sdql_parts.append(q[j:j+1])
                    spos=j+1
                else: 
                    if q[j:j+1] in break_on:
                        sdql_parts.append(q[spos:j+1])
                        spos=j+1
                    
                    else:
                        if q[j:j+5]==" and ":
                            sdql_parts.append(q[spos:j])
                            #print(q[spos:j])
                            sdql_parts.append(q[spos+j+1:j+5])
                            #print(q[spos+j+1:j+5])
                            #print('spos',spos,'j',j)
                            j+=5
                            spos=j

        j+=1
    sdql_parts.append(q[spos:])
    #print(sdql_parts)
    
    return sdql_parts


# In[ ]:


def fngrouping_format_check(groupby,check_data):
    
    grouper=''
    #check_data=sdql_parts
    grouping=0
    at_pos=-1
    new_check_data=list()
    for c in check_data:
        c=c.strip()
        new_check_data.append(c)
    try:
        at_pos=new_check_data.index('@')
    except:
        y=''
    if at_pos<0:
    
        for g in groupby:
            if g in new_check_data and not '@' in new_check_data:
                grouper=g
                grouping=1


        if grouping==0:
            for item in new_check_data:
                if '@' in item:
                    break

                if ',' in item and '(' not in item and not '@' in item and item!=",":
                    #print(item)
                    grouping=1
                    break
    #print(grouping)
    
    return grouping,grouper


# In[ ]:


def fncolumn_format_check_orig(check_data):
        
    column_format=0
    #check_data=sdql_data
    for s in check_data:
        #print(s)
        lat_pos=0
        at_pos=s.find("@")
        while at_pos>0:
            #print(' at pos',at_pos)
            if at_pos>0:
                
                if "(" in s[lat_pos:at_pos] and ")" in s[at_pos+1:]:
                    column_format=0
                else:
                    column_format=1
            lat_pos=at_pos
            at_pos=s.find("@",at_pos+1)
        if s=="@":
            column_format=1
            break
    #print(column_format)

    return column_format    


# In[ ]:


def fncolumn_format_check(q):
    q=q+" "
    qlen=len(q)
    leftp=rightp=0
    column_format=0
    for j in range(0,qlen):
        #print('Character',j,q[j:j+1])
        if q[j:j+1]=="(":
            leftp+=1
        if q[j:j+1]==")":
            rightp+=1
        if q[j:j+1]=="@":    
            if leftp==rightp:
                column_format=1
                break
    return column_format


# In[ ]:


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
    strings.append('time_zone')
    return strings


# In[ ]:


def fncolumn_format(data,headers,columns):
    headers = data['headers']
    headers.append('sdql as terms')
    columns = [d['columns'] for d in data['groups']]
    sdqls = ["".join(d['sdql as terms']) for d in data['groups']]
    
    for col, sdql in zip(columns, sdqls):
        col.append([sdql])
    
    tables = []
    for c in columns:
        pt = PrettyTable()
        add_paddings(c)
        for header, column in zip(headers, c):
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
    big_table.field_names = headers
    for row in all_data:
        values = []
        for header in headers:
            values.append(row[header])
        big_table.add_row(values)
        html=big_table.get_html_string()
    return(html)


# In[ ]:


def fncrawler(q,spos,epos,break_on):
    q=q+" "
    qlen=len(q)
    leftp=rightp=0
    for j in range(spos,qlen):
        #print('Character',j,q[j:j+1])
        if q[j:j+1]=="(":
            leftp+=1
        if q[j:j+1]==")":
            rightp+=1
        if leftp>0 and leftp==rightp:
            epos=rightp
            break
        if leftp==0:
            if q[j:j+1] in break_on:
                break
            #print(j,q[j:j+5])
            if q[j:j+5]==" and ":
                break

    j+=1

    #print('j',j,q[spos:j],qlen)
    return j,q[spos:j]
        


# In[ ]:


def fnget_single_parts(sdql_data):
    ##replace singlecusts

    #sdql_data=querylist
    #print(sdql_data)
    
    single_parts=list()

    for s in sdql_data:
        s=s.strip()
        try:
            is_num=float(s.replace(')','').replace('(',''))
            single_parts.append(s)
        except:
            
            if s!='and' and fnhas_operator(s,operators)==0 and ',' not in s:
                prefix=s[:s.find(':')+1]
                scut=s[s.find(':')+1:]
                
                if scut==scut.upper():
                    singles=list(scut)
                    no_expand=0
                    for single in singles:
                        if single not in single_shortcuts:
                            no_expand=1

                    if no_expand==1:
                        single_parts.append(s)
                    else:
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
                    op_pos=fnhas_operator(s,['+','-','/','*'])
                    while op_pos>0 and len(s)>0:
                        single_parts.append(s[:op_pos])
                        single_parts.append(s[op_pos:op_pos+1])
                        s=s[op_pos+1:]
                        op_pos=fnhas_operator(s,['+','-','/','*'])
                    
                    single_parts.append(s)
                                        
            else:
                if s[len(s)-1:len(s)]=='@':
                    single_parts.append(s[:len(s)-1])
                    single_parts.append('@')
                else:
                    op_pos=fnhas_operator(s,['+','-','/','*'])   #['+','-','/','*','>','<'])
                    while op_pos>0 and len(s)>0:
                        single_parts.append(s[:op_pos])
                        single_parts.append(s[op_pos:op_pos+1])
                        s=s[op_pos+1:]
                        op_pos=fnhas_operator(s,['+','-','/','*'])  #['+','-','/','*','>','<'])
                        
                    
                    single_parts.append(s)
                    #print('last',s)
            #print(s)

    #print(single_parts)  


    return single_parts


# In[ ]:


def fnhas_operator(checkme,operators):
    #print(checkme)
    foundit=0
    for c in checkme:
        #print(c)
        if c in operators:
            foundit=checkme.find(c)
            #print(foundit,c,checkme.find(c))
            break
    return foundit


# In[ ]:


def fnget_inside_parts(inside):
    inside_parts=list()
    last_break=-1
    for j in range(0,len(inside)-1):
        #print(j,inside[j:j+1])
        if inside[j:j+1] in splits:
            #print(inside[j:j+1],j)
            inside_parts.append(inside[last_break+1:j])
            inside_parts.append(inside[j:j+1])
            last_break=j

    inside_parts.append(inside[last_break+1:])
    return inside_parts


# In[ ]:


def fnget_summative_start_end(string):
    #string=query
    query_length_counter=0
    match=0
    string_counter=0
    not_started=1
    s_pos=e_pos=0
    first_one=-1
    for s in summatives:
        sum_pos=string.find(s)
        if sum_pos>=0:
            if sum_pos<=first_one or first_one==-1:
                first_one=sum_pos
    if first_one>=0:
        s_pos=first_one
    while (match!=0 or not_started==1) and (query_length_counter+e_pos+1)<len(string):
        query_length_counter+=1

        char=(string[s_pos+e_pos+string_counter:s_pos+e_pos+string_counter+1])
        #print('s_pos',s_pos,e_pos,char)
        if char=='(':
            match=match-1
            not_started=0 # found 1st (
        if char==')':
            match=match+1

        #print('match',match)
        string_counter+=1
        #print('char',char,string[:s_pos+e_pos+string_counter],match)

        #print('string_counter',string_counter)
        #if match==1: 
            #3/0
    #print("MATCH")

    #string[s_pos:s_pos+e_pos+string_counter]
    e_pos=s_pos+e_pos+string_counter    
    string[s_pos:e_pos]
    
    return s_pos,e_pos


# In[ ]:


def fnget_num_past_season(sumdata):

    num_past_season=0
    sum_pos=sumdata.find('tp')
    if sum_pos<0:
        sum_pos=sumdata.find('op')
    if sum_pos>=0:
        if sumdata[sum_pos+2:sum_pos+3]!=":" and sumdata[sum_pos+2:sum_pos+3]!="o" and sumdata[sum_pos+2:sum_pos+3]!="(":    

            try:
                num_past_season=int(sumdata[2:4])
                sumdata=sumdata[:1]+sumdata[4:]
            except ValueError:
                try:
                    num_past_season=int(sumdata[2:3])
                    sumdata=sumdata[:1]+sumdata[3:]

                except ValueError:
                    t1=sumdata[:2]
                    t2=sumdata[2:sumdata.find('(')-1]
                    t3=sumdata[sumdata.find('(')-1:]
                    num_past_season=len(t2)
                    sumdata=sumdata[:1]+sumdata[2+num_past_season:]                

    return sumdata,num_past_season


# In[ ]:


##### tS(...) tA(...) tp

def fnexpand_t(query,num_past_season):
    
    #query="/ (tS(plays)+tS(o:plays))" #needs -1 in inside_parts
    #query=nq
    #query="tS(rushes@(site=='home') as 'H')"
    #query="tS((0<Team:points-Team:o:points) as 'W'@(site=='home') as 'H')"
    #query="tS(rushes@(site=='home') as 'H')"
    #query="tS((points+line>tp:points) as 'ATSW')"
    #above fails with below
    #if num_past_season==0:
        #new_inside_parts.append(ip[:condition_pos]+'@team and season'+ip[condition_pos:])
    #else:
        #new_inside_parts.append(ip[:condition_pos]+'@team and season-'+str(num_past_season)+ip[condition_pos:])

    temp=fnstrip_alias(query)
    if fncount_summatives(query)>1:
        has_inside_parts=1
    else:
        has_inside_parts=0
    
    if has_inside_parts==1:
        inside_parts=list()
        new_inside_parts=list()
        inside_parts=fnget_inside_parts(query)
        for ip in inside_parts:
            as_words=' as '+"'"+ip+"'"
            if 'tS' in ip or 'tA' in ip:
                ip=ip.replace('tS(','Sum(').replace('tA(','Average(')
                condition_pos=ip.find(',')
                if condition_pos<0:
                    condition_pos=ip.find(')')
                if condition_pos<0:
                    condition_pos=len(ip)
                at_pos=ip.find('@')
                if at_pos<0 or at_pos>condition_pos:
                    condition='@team and season'
                else:
                    condition="and team and season"

                if num_past_season==0:
                    new_inside_parts.append(ip[:condition_pos]+condition+ip[condition_pos:])
                else:
                    new_inside_parts.append(ip[:condition_pos]+condition+'-'+str(num_past_season)+ip[condition_pos:])
            else:
                new_inside_parts.append(ip)
        new_query=''.join(new_inside_parts)

    else:

        if 'tS' in query or 'tA' in query:
            query=query.replace('tS(','Sum(').replace('tA(','Average(')

        at_pos=query.find('@')
        if at_pos>0:
            as_pos=query[at_pos+1:].find(' as ')
            if as_pos>0:
                new_query=query[:at_pos]+query[at_pos:].replace(' as ',' and team and season as ',1)
            else:
                new_query=query[:at_pos]+query[at_pos:].replace(' as ',' and team and season as ',1)
        else:
            comma_pos=query.find(',')
            if comma_pos>0:

                new_query=query[:comma_pos]+' @team and season '+query[comma_pos:]
            else:
                new_query=query[:len(query)-1]+' @team and season '+query[len(query)-1:]
        
        if num_past_season!=0:
            new_query=new_query.replace('team and season','team and season'+str(-num_past_season))
    
    #print(new_query)
    
    return new_query


# In[ ]:


def fnexpand_o(query,num_past_season):
    
    #query="/ (tS(plays)+tS(o:plays))" #needs -1 in inside_parts
    
    #query="tS(rushes@(site=='home') as 'H')"
    #query="tS((0<Team:points-Team:o:points) as 'W'@(site=='home') as 'H')"
    #query="tS(rushes@(site=='home') as 'H')"
    #query="tS((points+line>tp:points) as 'ATSW')"
    #above fails with below
    #if num_past_season==0:
        #new_inside_parts.append(ip[:condition_pos]+'@team and season'+ip[condition_pos:])
    #else:
        #new_inside_parts.append(ip[:condition_pos]+'@team and season-'+str(num_past_season)+ip[condition_pos:])

    temp=fnstrip_alias(query)
    if fncount_summatives(query)>1:
        has_inside_parts=1
    else:
        has_inside_parts=0
    
    if has_inside_parts==1:
        inside_parts=list()
        new_inside_parts=list()
        inside_parts=fnget_inside_parts(query)
        for ip in inside_parts:
            as_words=' as '+"'"+ip+"'"
            if 'oS' in ip or 'oA' in ip:
                ip=ip.replace('oS(','Sum(').replace('oA(','Average(')
                condition_pos=ip.find(',')
                if condition_pos<0:
                    condition_pos=ip.find(')')
                if condition_pos<0:
                    condition_pos=len(ip)
                at_pos=ip.find('@')
                if at_pos<0 or at_pos>condition_pos:
                    condition='@o:team and o:season'
                else:
                    condition="and o:team and o:season"

                if num_past_season==0:
                    new_inside_parts.append(ip[:condition_pos]+condition+ip[condition_pos:])
                else:
                    new_inside_parts.append(ip[:condition_pos]+condition+'-'+str(num_past_season)+ip[condition_pos:])
            else:
                new_inside_parts.append(ip)
        new_query=''.join(new_inside_parts)

    else:

        if 'oS' in query or 'oA' in query:
            query=query.replace('oS(','Sum(').replace('oA(','Average(')
        
        at_pos=query.find('@')
        if at_pos>0:
            as_pos=query[at_pos+1:].find(' as ')
            if as_pos>0:
                new_query=query[:at_pos]+query[at_pos:].replace(' as ',' and o:team and o:season as ',1)
            else:
                new_query=query[:at_pos]+query[at_pos:].replace(' as ',' and o:team and o:season as ',1)
        else:
            new_query=query[:len(query)-1]+' and o:team and o:season '+query[len(query)-1:]
        
        if num_past_season!=0:
            new_query=new_query.replace('and o:team and o:season','and o:team and o:season'+str(-num_past_season))
    
    #print(new_query)
    
    return new_query


# In[ ]:


def fnget_expanded_querylist(query):
    spos=0
    epos=0
    querylist=list()
    while spos<len(query):
        spos,spart=fncrawler(query,spos,epos,break_on)

        querylist.append(spart)
        if query[spos:spos+5]==" and ":
            querylist.append(query[spos:spos+5])
            spos+=5
            #5/0
        if query[spos:spos+4]=="and ":
            querylist.append(query[spos:spos+4])
            spos+=4
            #4/0
        #print('next',query[spos:])
        epos=spos
    #querylist
    expanded_querylist=fnget_single_parts(querylist)
    return expanded_querylist


# In[ ]:


def fnget_replace_dict(expanded_querylist):
    replace_dict=dict()
    c1=0
    for string in expanded_querylist:
        string=string.replace('Average(','average(').replace('A(','average(')
        #print('string',string)
        c1+=1
        if string!='':
            c=0
            for key,value in shortcuts.items():
                c+=1
                as_pos=string.find(' as ')
                if as_pos<0:
                    as_pos=len(string)

                if key in string[:as_pos] and string[:3]!='as ':
                    string=string.replace(key,value)
                    replace_dict.update({key:value})
    return replace_dict


# In[ ]:


# def fnget_parameters_conditions(q):
#     ########### NOT used, being developed
#     parameters=''
#     conditions=''
#     if query.find('@')<0:
#         parameters=query
#     else:
#         q=query+" "
#         qlen=len(q)
#         leftp=rightp=0
#         spos=0
#         for j in range(spos,qlen):
#             #print('Character',j,q[j:j+1])
#             if q[j:j+1]=="(":
#                 leftp+=1
#             if q[j:j+1]==")":
#                 rightp+=1
#             if q[j:j+1]=='@':
#                 if leftp==rightp:
                    
#                     parameters=q[:j]
#                     conditions=q[J+2:]
#                     j=qlen+5
#                     break
#     if parameters=='':
#         parameters=q
#     return parameters,conditions


# In[ ]:


def fnget_newquery_list(expanded_querylist,ordered_replace_dict):
    c=0
    new_querylist=list()

    for part in expanded_querylist:
        c+=1
        #print(part,c)
        if len(ordered_replace_dict)>0:
            for key,value in ordered_replace_dict.items():
                if part.find(key)>=0:
                    as_part=0
                    as_pos=part.find(' as ')
                    as_part=''
                    part1=part

                    if as_pos>=0:
                        as_part=part[as_pos:]
                        part=part[:as_pos].replace(key,value)+as_part
                    else:
                        part=part.replace(key,value)
                    #print('newpart',part)

            new_querylist.append(part)
            #print('Added',part)
        else:    
            new_querylist.append(part)
    return new_querylist


# In[ ]:


def fnget_sdql_data(new_querylist):
    c=0
    sdql_data=list()

    for nq in new_querylist:
        #print('nq start',nq)
        if nq.find('tp')>=0 or nq.find('op')>=0:
            nq,num_past_season=fnget_num_past_season(nq)

        else:
            num_past_season=0
        if (nq.find('tS(')>=0 or nq.find('tA(')>=0) and nq.find('Sum(')<0 and nq.find('Average(')<0:
            nq=fnexpand_t(nq,num_past_season)
        if (nq.find('oS(')>=0 or nq.find('oA(')>=0) and nq.find('Sum(')<0 and nq.find('Average(')<0:
            nq=fnexpand_o(nq,num_past_season)

        sdql_data.append(nq)
    return sdql_data


# In[ ]:


def fnfix_strings(sdql_parts):
    
    tsdql_parts=list()
    c=0
    for sp in sdql_parts:
        sp=sp.replace('time zone','time_zone')
        for string in strings:
            if string in sp:
                c=c+1
                #print(sp,c)    
                sp=sp.replace('  ',' ')

                if sp.replace(' ','').find(string+'=')>=0:
                    string_list=list()
                    bailout=0
                    string_list=sp.split("=")

                    if len(string_list)==2:
                        if string in string_list[0] and string in string_list[1]:
                            bailout=1
                    if not bailout:
                        if '==' in sp:
                            y='' # don't do anything                    
                        else:
                            equal_pos=sp.find(string+' =')
                            if equal_pos>=0:
                                equal_pos=equal_pos+len(string)+2
                            if equal_pos<0:
                                equal_pos=sp.find(string+'=')
                                if equal_pos>=0:
                                    equal_pos=equal_pos+len(string)+1
                            if equal_pos>=0:
                                pos_list=list()
                                pos_list.append(sp[equal_pos:].find(")"))
                                pos_list.append(sp[equal_pos:].find("@"))
                                pos_list.append(sp[equal_pos:].find(","))
                                pos_list.append(sp[equal_pos:].find(" and"))
                                pos_list.append(sp[equal_pos:].find('"'))
                                pos_list.append(sp[equal_pos:].find("'"))
                                newpos_list=list()
                                for pos in pos_list:
                                    if pos>=0:
                                        newpos_list.append(pos+equal_pos)
                                if len(newpos_list)>0:
                                    close_quote_pos=min(newpos_list)
                                else:
                                    close_quote_pos=len(sp)
                                sp=sp.replace('time_zone','time zone')
                                if sp[close_quote_pos:close_quote_pos+1]!="'" and sp[close_quote_pos:close_quote_pos+1]!='"':
                                    sp=sp[:equal_pos]+"'"+sp[equal_pos:close_quote_pos]+"'"+sp[close_quote_pos:]
        tsdql_parts.append(sp)    
    
    return (tsdql_parts)


# In[ ]:


def fnget_ordered_dict(replace_dict):
    ordered_replace_dict=dict()
    for sc_key,sc_value in shortcuts.items():
        if sc_key in replace_dict.keys():
            #print(sc_key,sc_value)
            ordered_replace_dict.update({sc_key: sc_value})
    return ordered_replace_dict


# In[ ]:


def fncheck_lines(sdql_data,lines,money_lines,totals):
    new_sdql_data=list()
    for s in sdql_data:
        if 'line ' in s:
            for l in lines:
                if l in s and l+'[' not in s:
                    s=s.replace(l,l+'[-1]')
        if 'money line ' in s:
            for ml in money_lines:
                if ml in s and ml+'[' not in s:
                    s=s.replace(ml,ml+'[-1]')
        if 'total ' in s:
            for t in totals:
                if t in s and t+'[' not in s:
                    s=s.replace(t,t+'[-1]')
        new_sdql_data.append(s)
        
    return new_sdql_data


def fnapi(sdql, groupby):
    column_format = group_format = 0
    converted_query = ''
    format_no = 1
    sdql_parts=fnchop_sdql(sdql)
    group_format,grouper=fngrouping_format_check(groupby,sdql_parts)
    if group_format == 1:
        converted_query = "t:team,t:points,o:points,t:line,total@" + sdql
    else:
        column_format = fncolumn_format_check(sdql)
        if column_format == 1:
            converted_query = sdql
            format_no = 3
        else:
            converted_query = "date,season,day,site,week,line,total,overtime,t:team,t:points,t:rushes,t:rushing yards,t:passes,t:passing yards,t:completions,t:quarter scores,t:turnovers,o:team,o:points,o:rushes,o:rushing yards,o:passes,o:passing yards,o:completions,o:quarter scores,o:turnovers@" + sdql
            format_no = 2
    return converted_query, format_no, grouper

def get_converted_query(query):
    expanded_querylist=fnget_expanded_querylist(query)
    replace_dict=fnget_replace_dict(expanded_querylist)
    ordered_replace_dict=fnget_ordered_dict(replace_dict)
    new_querylist=fnget_newquery_list(expanded_querylist,ordered_replace_dict)
    sdql_data=fnget_sdql_data(new_querylist)
    sdql_data=fnfix_strings(sdql_data)
    sdql=' '.join(sdql_data).replace('Team:','').replace('> =','>=').replace('< =','<=').replace('average','Average')
    converted_query, format_no, grouper = fnapi(sdql, groupby)
    return converted_query, format_no, grouper

groupby=list()
groupby=['RSWL','ats margin','ats streak','average punt yards','biggest lead','blocked extra points','blocked field goals','blocked punts','close line','close total','coach','completions','conference','date','day','division','dpa','dps','drives','field goals','field goals attempted','first downs','fourth downs attempted','fourth downs made','fumble return touchdowns','fumble return yards','fumbles','fumbles lost','game number','goal to go attempted','goal to go made','interception return yards','interception returns','interception touchdowns','interceptions','kicking extra points','kicking extra points attempted','kickoff return touchdowns','kickoff return yards','kickoff returns','kickoffs','kickoffs for touchback','kickoffs in end zone','lead changes','line','line sdb','losses','margin','margin after the first','margin after the third','margin at the half','matchup losses','matchup wins','money line','month','open line','open total','opponents','ou margin','ou streak','overtime','passes','passing first downs','passing touchdowns','passing yards','penalties','penalty first downs','penalty yards','playoffs','plays','points','punt return touchdowns','punt return yards','punt returns','punts','quarter scores','red zones attempted','red zones made','regular season wins line','rest','return yards','rushes','rushes for a loss','rushing first downs','rushing touchdowns','rushing yards','rushing yards lost','sack yards','sacks','safeties','scored first','season','site','site streak','snf','start time','streak','surface','team','temperature','third downs attempted','third downs made','time of possession','time zone','times tied','total','touchdowns','turnover margin','turnovers','two point conversion attempts','two point conversions','two point conversions attempted','week','wins']

lines=list()
money_lines=list()
total=list()
lines=['line ave',' line ave odds','line ce','line ce odds','line ci','line ci odds','line date','line dk','line dk odds','line fd','line fd odds','line lv','line lv odds','line mgm','line mgm odds','line mir','line mir odds','line pb','line pb odds','line sb','line sb odds','line sdb','line sh','line sh odds','line sp','line sp odds','line time','line ub','line ub odds','line wh','line wh odds']
money_lines=['money line ave','money line ce','money line ci','money line dk','money line fd','money line lv','money line mgm','money line mir','money line pb','money line sb','money line sh','money line sp','money line ub','money line wh']
totals=['total ave','total ave odds','total ci','total ci odds','total dk','total dk odds','total fd','total fd odds','total lv','total lv odds','total mgm','total mgm odds','total mir','total mir odds','total pb','total pb odds','total sb','total sb odds','total sh','total sh odds','total sp','total sp odds','total ub','total ub odds','total wh','total wh odds']


linesB=list()
money_linesB=list()
totalB=list()
for xline in lines:
    linesB.append(xline+"[")
for xmoney_line in money_lines:
    money_linesB.append(xmoney_line+"[")
for xtotal in totals:
    totalB.append(xtotal+"[")

splits=['+','-','/','*','@']
parameters=list()
parameters=['RSWL', '_t', 'ats margin', 'ats streak', 'attendance', 'average net punt yards', 'average punt yards', 'biggest lead', 'blocked extra points', 'blocked field goals', 'blocked punts', 'close line', 'close total', 'coach', 'completions', 'conference', 'dataset', 'date', 'day', 'division', 'dpa', 'dps', 'drives', 'field goals', 'field goals attempted', 'first downs', 'fourth downs attempted', 'fourth downs made', 'fumble return touchdowns', 'fumble return yards', 'fumbles', 'fumbles lost', 'game number', 'goal to go attempted', 'goal to go made', 'head coach', 'interception return yards', 'interception returns', 'interception touchdowns', 'interceptions', 'kicking extra points', 'kicking extra points attempted', 'kickoff return touchdowns', 'kickoff return yards', 'kickoff returns', 'kickoffs', 'kickoffs for touchback', 'kickoffs in end zone', 'lead changes', 'line', 'line sdb', 'losses', 'margin', 'margin after the first', 'margin after the third', 'margin at the half', 'matchup losses', 'matchup wins', 'money line', 'month', 'open line', 'open total', 'opponents', 'ou margin', 'ou streak', 'overtime', 'passes', 'passing first downs', 'passing touchdowns', 'passing yards', 'penalties', 'penalty first downs', 'penalty yards', 'playoffs', 'plays', 'points', 'punt return touchdowns', 'punt return yards', 'punt returns', 'punts', 'quarter scores', 'red zones attempted', 'red zones made', 'regular season wins line', 'rest', 'return yards', 'rot', 'rushes', 'rushes for a loss', 'rushing first downs', 'rushing touchdowns', 'rushing yards', 'rushing yards lost', 'sack yards', 'sacks', 'safeties', 'scored first', 'season', 'site', 'site streak', 'snf', 'start time', 'streak', 'surface', 'team', 'temperature', 'third downs attempted', 'third downs made', 'time of possession', 'time zone', 'times tied', 'total', 'touchdowns', 'turnover margin', 'turnovers', 'two point conversion attempts', 'two point conversions', 'two point conversions attempted', 'week', 'wins']

shortcuts=fnget_shortcuts()
strings=fnget_strings()
operators=['!','=','>','<','+','/','-','*',')','(','@']
break_on=[",","@"]
#parameters=['t','o','p','P','n','N','s','S']
summatives=list(['tS','tA','oA','oS','tp','op'])
#pseason=list(['tp','op'])
single_shortcuts=['H','A','W','L','F','D','O','U','C']

newshortcuts=dict()
for sc_key,sc_value in shortcuts.items():
    newshortcuts.update({sc_key: sc_value})
    if sc_key[:2]=='t:':
        newshortcuts.update({sc_key.replace('t:','n:'): sc_value.replace('t:','n:')})
shortcuts=newshortcuts