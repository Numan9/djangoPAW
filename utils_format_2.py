# from Data_format_2 import Data_format_2
# import datetime

# def checkseason(list1, list2):
#     result = False
#     # traverse in the 1st list
#     for x in list1:
#         # traverse in the 2nd list
#         for y in list2:
#             # if one common
#             if str(x) in str(y):
#                 result = True
#                 return result
#     return False

# def f(msg):
#     return "<td>"+str(msg)+"</td>"

# def tohtml(data,thisseason):
#     # page = "<!DOCTYPE html> <html>"
#     # header = "<head>"
#     # header = header + '<meta charset = "utf-8">'
#     # header = header + '<meta name = "viewport" content = "width=device-width, initial-scale=1">'
#     # header = header + '<link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
#     # header = header + '<script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"> </script >'
#     # header = header + '<script src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"> </script>'
#     # header = header + '<script src = "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"> </script>'
#     # header = header+"<style>"
#     # header = header +"body"
#     # header = header +"{"
#     # header = header +"font-family: sans-serif";
#     # header = header +"}"
#     # header = header +"</style>"
#     # header = header + "</head>"

#     # page = page + header

#     page = ""

#     page = page + "<div class='container-fluid  mt-4'>"

#     row1 = '<div class="row ml-4">'

#     top = "<table class='table table-bordered w-auto text-xsmall'><thead>"
#     strRW = ""
#     strRW = strRW + "<tr><td style='color:blue;text-align: center;' colspan='7'>History of Database</td><td style='color:blue;text-align: center;' colspan='3'>This Season</td></tr>"
#     strRW = strRW + "<tr><td style='color:blue' colspan='10'></td></tr>"
#     strRW = strRW + "<tr>" + "<td>SU</td><td colspan='2'>" + data.SU() + "</td><td colspan='4' style='text-align: center;' >Teaser Records</td>" + "<td>SU</td><td colspan='2'>" + data.SUseason(thisseason) + "</td>" +  "</tr>"
#     strRW = strRW + "<tr>" + "<td>ATS</td><td>" + data.ATS() + "</td><td>" + str(data.closelineavg()) + "</td>" + f(data.trd3()) + f(data.tre3()) + f(data.trf3()) + f(data.trg3())+ "<td>ATS</td><td>" + data.ATSseason(thisseason) + "</td><td>" + str(data.closelineavgseason(thisseason)) + "</td>" + "</tr>"
#     strRW = strRW + "<tr>" + "<td>OU</td><td>" + data.OU() + "</td><td>" + str(data.closetotalavg()) + "</td>" + f(data.trd4()) + f(data.tre4()) + f(data.trf4()) + f(data.trg4()) + "<td>OU</td><td>" + data.OUseason(thisseason) + "</td><td>" + str(data.closetotalavgseason(thisseason)) + "</td>" +  "</tr></thead>"
#     top = top +  strRW
#     top = top + "</table>"

#     row1 = row1 +  top
#     row1 = row1 + "</div>"


#     #table 2
#     table2 ="<table class='table table-bordered w-auto text-xsmall'><thead><tr>" \
#                "<th></th>" \
#                "<th>Rushes</th><th>Rush Yds</th><th>Passes</th><th>Pass Yds</th><th>Comp</th><th>TOs</th><th>Q1</th>" \
#                "<th>Q2</th><th>Q3</th><th>Q4</th><th>Final</th></tr></thead><tbody>"

#     strRW = ""
#     strRW = strRW+"<tr>"
#     strRW = strRW + f("Team")+f(data.trushesb7()) +f(data.trushesyardsc7())+f(data.tpassesd7())+f(data.tpassingyardse7())+f(data.tcompletionsf7())+f(data.ttosg7())+f(data.tq1())+f(data.tq2())
#     strRW = strRW + f(data.tq3())+f(data.tq4())+f(data.tfinall7())
#     strRW = strRW + "</tr>"

#     strRW = strRW + "<tr>"
#     strRW = strRW + f("Opp") + f(data.orushesb8()) + f(data.orushesyardsc8()) + f(data.opassesd8()) + f(data.opassingyardse8()) + f(data.ocompletionsf8()) + f(data.otosg8()) + f(data.oq1()) + f(data.oq2())
#     strRW = strRW + f(data.oq3()) + f(data.oq4()) + f(data.ofinall8())
#     strRW = strRW + "</tr>"

#     table2 = table2 + strRW
#     table2 = table2 + "</tbody></table>"

#     row2 = '<div class="row ml-4"><div class=col-md-8>'+table2+'</div></div>'


#     table3 = "<table id=\"myTable2\" class='table table-bordered w-auto text-xsmall'><thead><tr>" \
#                "<th style='color:blue'>Date</th>" \
#              "<th style='color:blue'>Link</th>" \
#              "<th style='color:blue'>Day</th><th style='color:blue'>Week</th><th style='color:blue'>Season</th><th  style='color:blue'>Team</th><th style='color:blue'>Opp</th><th style='color:blue'>Site</th>" \
#              "<th style='color:blue'>Q1</th><th style='color:blue'>Q2</th><th style='color:blue'>Q3</th><th style='color:blue'>Q4</th><th style='color:blue'>Final</th>" \
#                "<th style='color:blue'>Line</th><th style='color:blue'>Total</th><th style='color:blue'>SUm</th><th style='color:blue'>ATSm</th style='color:blue'>" \
#               "<th style='color:blue'>OUm</th><th style='color:blue'>DPS</th>" \
#                "<th style='color:blue'>DPA</th style='color:blue'><th style='color:blue'>SUr</th><th style='color:blue'>ATSr</th><th style='color:blue'>OUr</th><th style='color:blue'>ot</th></tr></thead><tbody>"

#     for (date,day,week,season,team,opp,site,q1,q2,q3,q4,fp,cl,ct,sump13,m13,oumn13,dpso13,dpa13,surq13,astr13,ours13,ot) in zip(data.date,data.day,data.week,data.season,data.team,data.oteam,data.site,
#                                                     data.q1(),data.q2(),data.q3(),data.q4(),data.finalpoints(),data.closeline,data.closetotal,
#                                                                          data.suml13(), data.atsmm13(), data.oumn13(),
#                                                                          data.dpso13(),
#                                                                          data.dpap13(), data.surq13(), data.atsr13(),
#                                                                          data.ours13(),data.overtime
#                                                                          ):
#         strRW = "<tr>"
#         date = datetime.datetime.strptime(str(date), '%Y%m%d').strftime('%b %d, %Y')

#         strRW = strRW + "<td>" + str(date) + "</td>"+"<td style='color:blue'>view</td>"+"<td>" + str(day[:3]) + "</td><td>"+str(week)+"</td><td>" + str(season) + "</td>"
#         strRW = strRW + "<td>" + str(team) + "</td><td>" + str(opp) + "</td><td>" + str(site) + "</td>"
#         strRW = strRW + "<td>" + str(q1) + "</td><td>" + str(q2) + "</td><td>" + str(q3) + "</td><td>"+ str(q4) + "</td>"
#         strRW = strRW + "<td>" + str(fp) + "</td><td>" + str(cl) + "</td><td>" + str(ct) + "</td>"
#         strRW = strRW + "<td>" + str(sump13) + "</td><td>" + str(m13) + "</td>"
#         strRW = strRW + "<td>" + str(oumn13) + "</td><td>" + str(dpso13) + "</td><td>" + str(dpa13) + "</td>"
#         strRW = strRW + "<td>" + str(surq13) + "</td><td>" + str(astr13) + "</td><td>" + str(ours13) + "</td>"
#         if ot > 0:
#             strRW = strRW + "<td> 1 </td>"
#         else:
#             strRW = strRW + "<td> 0 </td>"
#         strRW = strRW + "</tr>"
#         table3 = table3 + strRW

#     table3 = table3 + "</tbody></table>"

#     row3 = '<div class="row ml-4"><div class=col-md-10>'+table3+'</div></div>'

#     page = page + row1 +row2 + row3+"</div>"

#     return page






from Data_format_2 import Data_format_2
import datetime

def checkseason(list1, list2):
    result = False
    # traverse in the 1st list
    for x in list1:
        # traverse in the 2nd list
        for y in list2:
            # if one common
            if str(x) in str(y):
                result = True
                return result
    return False

def f(msg):
    return "<td>"+str(msg)+"</td>"

def tohtml(data,thisseason):
    # page = "<!DOCTYPE html> <html>"
    # header = "<head>"
    # header = header + '<meta charset = "utf-8">'
    # header = header + '<meta name = "viewport" content = "width=device-width, initial-scale=1">'
    # header = header + '<link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
    # header = header + '<script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"> </script >'
    # header = header + '<script src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"> </script>'
    # header = header + '<script src = "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"> </script>'
    # header = header+"<style>"
    # header = header +"body"
    # header = header +"{"
    # header = header +"font-family: sans-serif";
    # header = header +"}"
    # header = header +"</style>"
    # header = header + "</head>"

    # page = page + header

    page = ""

    page = page + "<body><div class='container-fluid  mt-4'>"

    row1 = '<div class="row ml-4">'

    top = "<table class='table table-bordered w-auto text-xsmall'><thead>"
    strRW = ""
    strRW = strRW + "<tr><td style='color:blue;text-align: center;' colspan='7'>History of Database</td><td style='color:blue;text-align: center;' colspan='3'>This Season</td></tr>"
    strRW = strRW + "<tr><td style='color:blue' colspan='10'></td></tr>"
    strRW = strRW + "<tr>" + "<td>SU</td><td colspan='2'>" + data.SU() + "</td><td colspan='4' style='text-align: center;' >Teaser Records</td>" + "<td>SU</td><td colspan='2'>" + data.SUseason(thisseason) + "</td>" +  "</tr>"
    strRW = strRW + "<tr>" + "<td>ATS</td><td>" + data.ATS() + "</td><td>" + str(data.closelineavg()) + "</td>" + f(data.trd3()) + f(data.tre3()) + f(data.trf3()) + f(data.trg3())+ "<td>ATS</td><td>" + data.ATSseason(thisseason) + "</td><td>" + str(data.closelineavgseason(thisseason)) + "</td>" + "</tr>"
    strRW = strRW + "<tr>" + "<td>OU</td><td>" + data.OU() + "</td><td>" + str(data.closetotalavg()) + "</td>" + f(data.trd4()) + f(data.tre4()) + f(data.trf4()) + f(data.trg4()) + "<td>OU</td><td>" + data.OUseason(thisseason) + "</td><td>" + str(data.closetotalavgseason(thisseason)) + "</td>" +  "</tr></thead>"
    top = top +  strRW
    top = top + "</table>"

    row1 = row1 +  top
    row1 = row1 + "</div>"


    #table 2
    table2 ="<table class='table table-bordered w-auto text-xsmall'><thead><tr>" \
               "<th></th>" \
               "<th>Rushes</th><th>Rush Yds</th><th>Passes</th><th>Pass Yds</th><th>Comp</th><th>TOs</th><th>Q1</th>" \
               "<th>Q2</th><th>Q3</th><th>Q4</th><th>Final</th></tr></thead><tbody>"

    strRW = ""
    strRW = strRW+"<tr>"
    strRW = strRW + f("Team")+f(data.trushesb7()) +f(data.trushesyardsc7())+f(data.tpassesd7())+f(data.tpassingyardse7())+f(data.tcompletionsf7())+f(data.ttosg7())+f(data.tq1())+f(data.tq2())
    strRW = strRW + f(data.tq3())+f(data.tq4())+f(data.tfinall7())
    strRW = strRW + "</tr>"

    strRW = strRW + "<tr>"
    strRW = strRW + f("Opp") + f(data.orushesb8()) + f(data.orushesyardsc8()) + f(data.opassesd8()) + f(data.opassingyardse8()) + f(data.ocompletionsf8()) + f(data.otosg8()) + f(data.oq1()) + f(data.oq2())
    strRW = strRW + f(data.oq3()) + f(data.oq4()) + f(data.ofinall8())
    strRW = strRW + "</tr>"

    table2 = table2 + strRW
    table2 = table2 + "</tbody></table>"

    row2 = '<div class="row ml-4"><div class=col-md-8>'+table2+'</div></div>'


    table3 = "<table id=\"myTable2\" class='table table-bordered w-auto text-xsmall'><thead><tr>" \
               "<th style='color:blue'>Date</th>" \
             "<th style='color:blue'>Link</th>" \
             "<th style='color:blue'>Day</th><th style='color:blue'>Week</th><th style='color:blue'>Season</th><th  style='color:blue'>Team</th><th style='color:blue'>Opp</th><th style='color:blue'>Site</th>" \
             "<th style='color:blue'>Q1</th><th style='color:blue'>Q2</th><th style='color:blue'>Q3</th><th style='color:blue'>Q4</th><th style='color:blue'>Final</th>" \
               "<th style='color:blue'>Line</th><th style='color:blue'>Total</th><th style='color:blue'>SUm</th><th style='color:blue'>ATSm</th style='color:blue'>" \
              "<th style='color:blue'>OUm</th><th style='color:blue'>DPS</th>" \
               "<th style='color:blue'>DPA</th style='color:blue'><th style='color:blue'>SUr</th><th style='color:blue'>ATSr</th><th style='color:blue'>OUr</th><th style='color:blue'>ot</th></tr></thead><tbody>"


    for (date,day,week,season,team,opp,site,q1,q2,q3,q4,fp,cl,ct,sump13,m13,oumn13,dpso13,dpa13,surq13,astr13,ours13,ot) in zip(data.date,data.day,data.week,data.season,data.team,data.oteam,data.site,
                                                    data.q1(),data.q2(),data.q3(),data.q4(),data.finalpoints(),data.closeline,data.closetotal,
                                                                         data.suml13(True), data.atsmm13(), data.oumn13(),
                                                                         data.dpso13(),
                                                                         data.dpap13(), data.surq13(), data.atsr13(),
                                                                         data.ours13(),data.overtime
                                                                         ):
        strRW = "<tr>"
        date = datetime.datetime.strptime(str(date), '%Y%m%d').strftime('%b %d, %Y')

        strRW = strRW + "<td>" + str(date) + "</td>"+"<td style='color:blue'>view</td>"+"<td>" + str(day[:3]) + "</td><td>"+str(week)+"</td><td>" + str(season) + "</td>"
        strRW = strRW + "<td>" + str(team) + "</td><td>" + str(opp) + "</td><td>" + str(site) + "</td>"
        strRW = strRW + "<td>" + str(q1) + "</td><td>" + str(q2) + "</td><td>" + str(q3) + "</td><td>"+ str(q4) + "</td>"
        strRW = strRW + "<td>" + str(fp) + "</td><td>" + str(cl) + "</td><td>" + str(ct) + "</td>"
        strRW = strRW + "<td>" + str(sump13) + "</td><td>" + str(m13) + "</td>"
        strRW = strRW + "<td>" + str(oumn13) + "</td><td>" + str(dpso13) + "</td><td>" + str(dpa13) + "</td>"
        strRW = strRW + "<td>" + str(surq13) + "</td><td>" + str(astr13) + "</td><td>" + str(ours13) + "</td>"
        if ot > 0:
            strRW = strRW + "<td> 1 </td>"
        else:
            strRW = strRW + "<td> 0 </td>"
        strRW = strRW + "</tr>"
        table3 = table3 + strRW

    table3 = table3 + "</tbody></table>"

    row3 = '<div class="row ml-4"><div class=col-md-10>'+table3+'</div></div>'

    page = page + row1 +row2 + row3+"</div>"

    return page