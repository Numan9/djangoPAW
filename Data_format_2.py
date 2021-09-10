import datetime
class Data_format_2:
    def __init__(self,date,season,day,site,week,closeline,closetotal,overtime,tteam,tpoints,trushes,trushingyards,tpasses,tpassingyards,
                 tcompletions,tquarters,tturnovers,oteam,opoints,orushes,orushingyards,opasses,opassingyards,ocompletions,oquarters,oturnovers):

        self.date = date
        self.season = season
        self.site = site
        self.tturnovers = tturnovers
        self.oturnovers = oturnovers
        self.team = tteam
        self.points = tpoints
        self.trushes = trushes
        self.trushingyards = trushingyards
        self.tpasses = tpasses
        self.tpassingyards = tpassingyards
        self.tcompletions = tcompletions
        self.tquarters = tquarters
        self.oteam = oteam
        self.opoints = opoints
        self.orushes = orushes
        self.orushingyards = orushingyards
        self.opasses = opasses
        self.opassingyards = opassingyards
        self.ocompletions = ocompletions
        self.oquarters = oquarters
        self.day = day
        self.closeline = closeline
        self.closetotal = closetotal
        self.week = week
        self.overtime = overtime

    # tr d3,d4

    def trd3(self):
        #Count of(points + line + 6 > o: points)
        #Countof(points + line + 6 < o: points)
        #Countof(points + line + 6 = o:points)
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,line,date) in zip(self.points, self.opoints,self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if (p + line + 6) > op:
                    x = x + 1
                if (p + line + 6) < op:
                    y = y + 1
                if (p + line + 6) == op:
                    z = z + 1
                sum = sum + p + line + 6 - op
        w = (x/len(self.points) - z)*100
        res = "+6: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    def trd4(self):
        #Countof(points + o: points + 6 > total)
        #Countof(points + o: points + 6 < total)
        #Countof(points + o: points + 6 = total
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,total,date) in zip(self.points, self.opoints,self.closetotal,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + op > (total +6):
                    x = x + 1
                if p + op < (total+6):
                    y = y + 1
                if p + op == (total+6):
                    z = z + 1
                sum = sum + p + 6 - op
        w = 0
        try:
            w = (x / len(self.points) - z)*100
        except:
            pass
        res = "+6: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    # tr e3,e4

    def tre3(self):
        #Countof(points + line - 6 > o: points)
        #Countof(points + line - 6 < o: points)
        #Countof(points + line - 6 = o:points)
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,line,date) in zip(self.points, self.opoints,self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + line - 6 > op:
                    x = x + 1
                if p + line - 6 < op:
                    y = y + 1
                if p + line - 6 == op:
                    z = z + 1
                sum = sum + p -6- op
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "-6: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    def tre4(self):
        #Countof(points + o: points - 6 > total)
        #Countof(points + o: points - 6 < total)
        #Countof(points + o: points - 6 = total)
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,total,date) in zip(self.points, self.opoints,self.closetotal,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + op > (total-6):
                    x = x + 1
                if p + op < (total-6):
                    y = y + 1
                if p + op == (total-6):
                    z = z + 1
                sum = sum + p - op - 6
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "-6: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    # tr f3,f4

    def trf3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,line,date) in zip(self.points, self.opoints,self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + line + 10 > op:
                    x = x + 1
                if p + line + 10 < op:
                    y = y + 1
                if p + line + 10 == op:
                    z = z + 1
                sum = sum + p - 10 - op
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "+10: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    def trf4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,total,date) in zip(self.points, self.opoints,self.closetotal,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p +  op > (total+10):
                    x = x + 1
                if p + op  < (total+10):
                    y = y + 1
                if p + op == (total+10):
                    z = z + 1
                sum = sum + p - op + 10
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "+10: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    # tr g3,g4
    def trg3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,line,date) in zip(self.points, self.opoints,self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + line -10 > op:
                    x = x + 1
                if p + line - 10 < op:
                    y = y + 1
                if p + line - 10 == op:
                    z = z + 1
                sum = sum + p - 10 - op
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "-10: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    def trg4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,total,date) in zip(self.points, self.opoints,self.closetotal,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + op > (total-10):
                    x = x + 1
                if p + op < (total-10):
                    y = y + 1
                if p + op == (total-10):
                    z = z + 1
                sum = sum + p - op - 10
        w = 0
        try:
            w = (x / (len(self.points) - z))*100
        except:
            pass
        res = "-10: {x}-{y}-{z} ({w:.1f}%)".format(x=x, y=y, z=z, w=w)
        return res

    def closelineavg(self):
        clsum = 0
        total = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (cl,date) in zip(self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                clsum = clsum + cl
                total = total + 1
        avg = 0
        try:
            avg = clsum/total
            avg = round(avg, 2)
        except:
            pass
        return avg
        #return round(sum(self.closeline)/len(self.closeline),2)

    def closetotalavg(self):
        clsum = 0
        total = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (cl, date) in zip(self.closetotal, self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                clsum = clsum + cl
                total = total + 1

        avg = 0
        try:
            avg = clsum / total
            avg = round(avg, 2)
        except:
            pass
        return avg
        #return round(sum(self.closetotal)/len(self.closetotal),2)

    def q1(self):
        q = []
        for t,o in zip(self.tquarters,self.oquarters):
            #t = ast.literal_eval(t)
            #o = ast.literal_eval(o)
            q.append(str(t[0])+"-"+str(o[0]))
        return q

    def q2(self):
        q = []
        for t, o in zip(self.tquarters, self.oquarters):
            #t = ast.literal_eval(t)
            #o = ast.literal_eval(o)
            q.append(str(t[1]) + "-" + str(o[1]))
        return q

    def q3(self):
        q = []
        for t, o in zip(self.tquarters, self.oquarters):
            #t = ast.literal_eval(t)
            #o = ast.literal_eval(o)
            q.append(str(t[2]) + "-" + str(o[2]))
        return q

    def q4(self):
        q = []
        for t, o in zip(self.tquarters, self.oquarters):
            #t = ast.literal_eval(t)
            #o = ast.literal_eval(o)
            q.append(str(t[3]) + "-" + str(o[3]))
        return q

    def sump13(self):
        sum = []
        for (p, op) in zip(self.points, self.opoints):
            sum.append(p - op)
        return sum

    #m13
    def finalpoints(self):
        ps = []
        for t, o in zip(self.points, self.opoints):
            ps.append(str(t) + "-" + str(o))
        return ps

    def tq1(self):
        sum = 0
        size = 0
        for q in self.tquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[0]
            size = size + 1
        return round(sum / size, 1)

    def tq2(self):
        sum = 0
        size = 0
        for q in self.tquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[1]
            size = size + 1
        return round(sum / size, 1)

    def tq3(self):
        sum = 0
        size = 0
        for q in self.tquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[2]
            size = size + 1
        return round(sum / size, 1)

    def tq4(self):
        sum = 0
        size = 0
        for q in self.tquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[3]
            size = size + 1
        return round(sum / size, 1)

    def oq1(self):
        sum = 0
        size = 0
        for q in self.oquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[0]
            size = size + 1
        return round(sum / size, 1)

    def oq2(self):
        sum = 0
        size = 0
        for q in self.oquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[1]
            size = size + 1
        return round(sum / size, 1)

    def oq3(self):
        sum = 0
        size = 0
        for q in self.oquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[2]
            size = size + 1
        return round(sum / size, 1)

    def oq4(self):
        sum = 0
        size = 0
        for q in self.oquarters:
            #q = ast.literal_eval(q)
            sum = sum + q[3]
            size = size + 1
        return round(sum / size, 1)

    #b7,8
    def trushesb7(self):
        return round(sum(self.trushes) / len(self.trushes), 1)
    def orushesb8(self):
        return round(sum(self.orushes) / len(self.orushes), 1)

    # c7,8
    def trushesyardsc7(self):
        return round(sum(self.trushingyards) / len(self.trushingyards), 1)
    def orushesyardsc8(self):
        return round(sum(self.orushingyards) / len(self.orushingyards), 1)

    # d7,8
    def tpassesd7(self):
        return round(sum(self.tpasses) / len(self.tpasses), 1)
    def opassesd8(self):
        return round(sum(self.opasses) / len(self.opasses), 1)

    # e7,8
    def tpassingyardse7(self):
        return round(sum(self.tpassingyards) / len(self.tpassingyards), 1)
    def opassingyardse8(self):
        return round(sum(self.opassingyards) / len(self.opassingyards), 1)

    # f7,8
    def tcompletionsf7(self):
        return round(sum(self.tcompletions) / len(self.tcompletions), 1)
    def ocompletionsf8(self):
        return round(sum(self.ocompletions) / len(self.ocompletions), 1)

    # g7,8
    def ttosg7(self):
        return round(sum(self.tturnovers) / len(self.tturnovers), 1)
    def otosg8(self):
        return round(sum(self.oturnovers) / len(self.oturnovers), 1)

    # l7,8
    def tfinall7(self):
        return round(sum(self.points) / len(self.points), 1)
    def ofinall8(self):
        return round(sum(self.opoints) / len(self.opoints), 1)

    def suml13season(self, thisseason):
        sum = []
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, season,date) in zip(self.points, self.opoints, self.season,self.date):
            if str(season) == str(thisseason):
                date = datetime.datetime.strptime(str(date), '%Y%m%d')
                if date < today:
                    sum.append(p - op)
        return sum

    def oumn13(self):
        sum = []
        for (p, op, ct) in zip(self.points, self.opoints, self.closetotal):
            sum.append(ct-(p+op))
        return sum

    def dpso13(self):
        sum = []
        for (cl, ct, p) in zip(self.closeline, self.closetotal, self.points):
            val = (ct / 2) - (cl / 2) - p
            sum.append(val)
        return sum

    def dpap13(self):
        sum = []
        for (cl, ct, op) in zip(self.closeline, self.closetotal, self.opoints):
            val = (ct / 2) + (cl / 2) - op
            sum.append(val)
        return sum

    def surq13(self):
        values = []
        for (p, op) in zip(self.points, self.opoints):
            if p > op:
                values.append("W")
            else:
                values.append("L")
        return values

    def ours13(self):
        values = []
        for (p, op, ct) in zip(self.points, self.opoints, self.closetotal):
            if p + op > ct:
                values.append("O")
            elif p + op < ct:
                values.append("U")
            elif p + op == ct:
                values.append("P")
        return values

    def atsr13(self):
        values = []
        for (p, op, cl) in zip(self.points, self.opoints, self.closeline):
            if p + cl > op:
                values.append("W")
            else:
                values.append("L")
        return values

    def atsmm13season(self, thisseason):
        sum = []
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, cl, season,date) in zip(self.points, self.opoints, self.closeline, self.season,self.date):
            if str(season) == str(thisseason):
                date = datetime.datetime.strptime(str(date), '%Y%m%d')
                if date < today:
                    sum.append(p + cl - op)
        return sum

    def atsmm13(self):
        sum = []
        for (p, op, cl) in zip(self.points, self.opoints, self.closeline):
            sum.append(p + cl - op)
        return sum

    def suml13(self):
        sum = []
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,date) in zip(self.points, self.opoints,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                sum.append(p-op)
        return sum
    # B3
    def ATS(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, cl,date) in zip(self.points, self.opoints, self.closeline,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + cl > op:
                    x = x + 1
                if p + cl < op:
                    y = y + 1
                if p == op:
                    z = z + 1
                sum = sum + (p + cl - op)
        w,v = 0,0
        try:
            v = (x / (x + y - z)) * 100
            w = (sum) / (len(self.points))
        except:
            pass
        tie = 0
        m13 = self.atsmm13()
        for s in m13:
            if s == 0:
                tie = tie + 1
        if tie == 0:
            res = "{x}-{y} ({w:.1f},{v:.1f}%)".format(x=x, y=y, w=w, v=v)
        else:
            res = "{x}-{y}-{tie} ({w:.1f},{v:.1f}%)".format(x=x, y=y, tie=tie, w=w, v=v)
        return res

    # B4
    def OU(self):
        x = 0
        y = 0
        z = 0
        opsum = 0
        ctsum = 0
        psum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, ct,date) in zip(self.points, self.opoints, self.closetotal,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                if p + op > ct:
                    x = x + 1
                if p + op < ct:
                    y = y + 1
                if p + op == ct:
                    z = z + 1
                opsum = opsum + op
                psum = psum + p
                ctsum = ctsum + ct
        w,v = 0,0
        try:
            v = (x / (x + y - z)) * 100
            w = (ctsum-opsum-psum)/len(self.points)
        except:
            pass
        res = "{x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # B2
    def SU(self):
        #points = sum(self.points)
        #opoints = sum(self.opoints)
        points = 0
        opoints = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op,date) in zip(self.points, self.opoints,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if date < today:
                points = points + p
                opoints = opoints + op

        x = 0
        y = 0
        z = 0
        for (p, op) in zip(self.points, self.opoints):
            if p > op:
                x = x + 1
            if p < op:
                y = y + 1
            if p == op:
                z = z + 1
        w,v = 0,0
        try:
            v = (x / (x + y - z)) * 100
            w = (points - opoints) / len(self.points)
        except:
            pass
        suml13 = self.suml13()
        tie = 0
        for s in suml13:
            if s == 0:
                tie = tie + 1
        if tie == 0:
            res = "{x}-{y} ({w:.1f},{v:.1f}%)".format(x=x, y=y, w=w, v=v)
        else:
            res = "{x}-{y}-{tie} ({w:.1f},{v:.1f}%)".format(x=x, y=y, tie=tie, w=w, v=v)
        return res

    # this season
    # B3
    def ATSseason(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, cl, season,date) in zip(self.points, self.opoints, self.closeline, self.season,self.date):
            if str(season) == str(thisseason):
                date = datetime.datetime.strptime(str(date), '%Y%m%d')
                if date < today:
                    if p + cl > op:
                        x = x + 1
                    if p + cl < op:
                        y = y + 1
                    if p == op:
                        z = z + 1
                    sum = sum + (p + cl - op)
                    total = total + 1
        #if total == 0:
         #   return self.ATS()

        tie = 0
        m13 = self.atsmm13season(thisseason)
        for s in m13:
            if s == 0:
                tie = tie + 1
        w,v = 0,0
        try:
            v = (x / (x + y - z)) * 100 # in ats the x+y-z becomes 0 which throws error so should i consider v=0 here?
            w = (sum) / (total)
        except:
            pass
        if tie == 0:
            res = "{x}-{y} ({w:.1f},{v:.1f}%)".format(x=x, y=y, w=w, v=v)
        else:
            res = "{x}-{y}-{tie} ({w:.1f},{v:.1f}%)".format(x=x, y=y, tie=tie, w=w, v=v)
        return res

    # B4
    def OUseason(self, thisseason):
        x = 0
        y = 0
        z = 0
        total = 0
        ctsum = 0
        opsum = 0
        psum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, ct, season,date) in zip(self.points, self.opoints, self.closetotal, self.season,self.date):
            if str(season) == str(thisseason):
                date = datetime.datetime.strptime(str(date), '%Y%m%d')
                if date < today:
                    if p + op > ct:
                        x = x + 1
                    if p + op < ct:
                        y = y + 1
                    if p + op == ct:
                        z = z + 1
                    opsum = opsum + op
                    psum = psum + p
                    ctsum = ctsum + ct
                    total = total + 1
        #if total == 0:
         #   return self.OU()
        w,v = 0,0
        try:
            v = (x / (x + y - z)) * 100
            w = (ctsum-opsum-psum) / total
        except:
            pass
        res = "{x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # B2
    def SUseason(self, thisseason):
        x = 0
        y = 0
        z = 0
        total = 0
        psum = 0
        opsum = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (p, op, season,date) in zip(self.points, self.opoints, self.season,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if str(season) == str(thisseason) and date < today:
                if p > op:
                    x = x + 1
                if p < op:
                    y = y + 1
                if p == op:
                    z = z + 1
                total = total + 1
                psum = psum + p
                opsum = opsum + op
        #if total == 0:
         #   return self.SU()
        w = 0
        v = 0
        try:
            w = (psum - opsum) / total
            v = (x / (x + y - z)) * 100
        except:
            pass
        suml13 = self.suml13season(thisseason)
        tie = 0
        for s in suml13:
            if s == 0:
                tie = tie + 1

        if tie == 0:
            res = "{x}-{y} ({w:.1f},{v:.1f}%)".format(x=x, y=y, w=w, v=v)
        else:
            res = "{x}-{y}-{tie} ({w:.1f},{v:.1f}%)".format(x=x, y=y, tie=tie, w=w, v=v)
        return res

        # c3

    def closelineavgseason(self, thisseason):
        sum = 0
        total = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (cl, season,date) in zip(self.closeline, self.season,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if str(season) == str(thisseason) and date < today:
                sum = sum + cl
                total = total + 1
        #if total == 0:
         #   return self.closelineavg()
        res = 0
        try:
            res = round(sum / total, 2)
        except:
            pass
        return res

    # c4
    def closetotalavgseason(self, thisseason):
        sum = 0
        total = 0
        dt = datetime.datetime.today()
        today = datetime.datetime(dt.year, dt.month, dt.day)
        for (cl, season,date) in zip(self.closetotal, self.season,self.date):
            date = datetime.datetime.strptime(str(date), '%Y%m%d')
            if str(season) == str(thisseason) and date < today:
                sum = sum + cl
                total = total + 1
        #if total == 0:
         #   return self.closetotalavg()
        res = 0
        try:
            res = round(sum / total, 2)
        except:
            pass
        return res