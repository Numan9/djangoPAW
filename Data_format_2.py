import ast
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
    def trd3season(self,thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if (p + 6) > op:
                    x = x + 1
                if (p + 6) < op:
                    y = y + 1
                if (p + 6) == op:
                    z = z + 1
                sum = sum + p + 6 - op
                total = total + 1
        if total == 0:
            return self.trd3()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "+6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trd3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if (p + 6) > op:
                x = x + 1
            if (p + 6) < op:
                y = y + 1
            if (p + 6) == op:
                z = z + 1
            sum = sum + p + 6 - op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "+6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trd4season(self,thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p > op + 6:
                    x = x + 1
                if p < op + 6:
                    y = y + 1
                if p == op + 6:
                    z = z + 1
                sum = sum + p - op + 6
                total = total + 1
        if total == 0:
            return self.trd4()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "+6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trd4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if (p + 6) > op:
                x = x + 1
            if (p + 6) < op:
                y = y + 1
            if (p + 6) == op:
                z = z + 1
            sum = sum + p + 6 - op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "+6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # tr e3,e4
    def tre3season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op,season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p - 6 > op:
                    x = x + 1
                if p - 6 < op:
                    y = y + 1
                if p - 6 == op:
                    z = z + 1
                sum = sum + p -6 - op
                total = total + 1
        if total == 0:
            return self.tre3()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "-6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def tre3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if p > op - 6:
                x = x + 1
            if p < op - 6:
                y = y + 1
            if p == op - 6:
                z = z + 1
            sum = sum + p -6- op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "-6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def tre4season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p > op-6:
                    x = x + 1
                if p < op-6:
                    y = y + 1
                if p == op-6:
                    z = z + 1
                sum = sum + p - op - 6
                total = total + 1
        if total == 0:
            return self.tre4()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "-6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def tre4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if p > op -6:
                x = x + 1
            if p < op - 6:
                y = y + 1
            if p == op - 6:
                z = z + 1
            sum = sum + p - op - 6
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "-6: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # tr f3,f4
    def trf3season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if (p + 10) > op:
                    x = x + 1
                if (p + 10) < op:
                    y = y + 1
                if (p + 10) == op:
                    z = z + 1
                sum = sum + p + 10 - op
                total = total + 1
        if total == 0:
            return self.trf3()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "+10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trf3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if (p - 6) > op:
                x = x + 1
            if (p - 6) < op:
                y = y + 1
            if (p - 6) == op:
                z = z + 1
            sum = sum + p - 6 - op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "+10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trf4season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p > op + 10:
                    x = x + 1
                if p < op + 10:
                    y = y + 1
                if p == op + 10:
                    z = z + 1
                sum = sum + p - op + 10
                total = total + 1
        if total == 0:
            return self.trf4()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "+10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trf4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if p > op+10:
                x = x + 1
            if p < op+10:
                y = y + 1
            if p  == op+10:
                z = z + 1
            sum = sum + p - op + 10
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "+10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # tr g3,g4
    def trg3season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if (p - 10) > op:
                    x = x + 1
                if (p - 10) < op:
                    y = y + 1
                if (p - 10) == op:
                    z = z + 1
                sum = sum + p - 10 - op
                total = total + 1
        if total == 0:
            return self.trg3()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "-10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trg3(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if (p - 10) > op:
                x = x + 1
            if (p - 10) < op:
                y = y + 1
            if (p - 10) == op:
                z = z + 1
            sum = sum + p - 10 - op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "-10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trg4season(self, thisseason):
        x = 0
        y = 0
        z = 0
        sum = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p > op - 10:
                    x = x + 1
                if p < op - 10:
                    y = y + 1
                if p == op - 10:
                    z = z + 1
                sum = sum + p - op - 10
                total = total + 1
        if total == 0:
            return self.trg4()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "-10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def trg4(self):
        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op) in zip(self.points, self.opoints):
            if p > op - 10:
                x = x + 1
            if p < op - 10:
                y = y + 1
            if p == op - 10:
                z = z + 1
            sum = sum + p - op - 10
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "-10: {x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    def closelineavg(self):
        return round(sum(self.closeline)/len(self.closeline),2)

    def closetotalavg(self):
        return round(sum(self.closetotal)/len(self.closetotal),2)

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
            sum = sum + q[1]
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
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
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
        for (p, op, cl, season) in zip(self.points, self.opoints, self.closeline, self.season):
            if str(season) == str(thisseason):
                sum.append(p + cl - op)
        return sum

    def atsmm13(self):
        sum = []
        for (p, op, cl) in zip(self.points, self.opoints, self.closeline):
            sum.append(p + cl - op)
        return sum

    def suml13(self):
        sum = []
        for (p, op) in zip(self.points, self.opoints):
            sum.append(p-op)
        return sum
    # B3
    def ATS(self):

        x = 0
        y = 0
        z = 0
        sum = 0
        for (p, op, cl) in zip(self.points, self.opoints, self.closeline):
            if p + cl > op:
                x = x + 1
            if p + cl < op:
                y = y + 1
            if p == op:
                z = z + 1
            sum = sum + (p + cl - op)
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
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
        sum = 0
        for (p, op, ct) in zip(self.points, self.opoints, self.closetotal):
            if p + op > ct:
                x = x + 1
            if p + op < ct:
                y = y + 1
            if p + op == ct:
                z = z + 1
            sum = sum + p + ct - op
        v = (x / (x + y - z)) * 100
        w = (sum) / (len(self.points))
        res = "{x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # B2
    def SU(self):
        points = sum(self.points)
        opoints = sum(self.opoints)
        w = (points - opoints) / len(self.points)
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
        v = (x / (x + y - z)) * 100
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
        for (p, op, cl, season) in zip(self.points, self.opoints, self.closeline, self.season):
            if str(season) == str(thisseason):
                if p + cl > op:
                    x = x + 1
                if p + cl < op:
                    y = y + 1
                if p == op:
                    z = z + 1
                sum = sum + (p + cl - op)
                total = total + 1
        if total == 0:
            return self.ATS()

        tie = 0
        m13 = self.atsmm13season(thisseason)
        for s in m13:
            if s == 0:
                tie = tie + 1
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
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
        sum = 0
        total = 0
        for (p, op, ct, season) in zip(self.points, self.opoints, self.closetotal, self.season):
            if str(season) == str(thisseason):
                if p + op > ct:
                    x = x + 1
                if p + op < ct:
                    y = y + 1
                if p + op == ct:
                    z = z + 1
                sum = sum + p + ct - op
                total = total + 1
        if total == 0:
            return self.OU()
        v = (x / (x + y - z)) * 100
        w = (sum) / (total)
        res = "{x}-{y}-{z} ({w:.1f},{v:.1f}%)".format(x=x, y=y, z=z, w=w, v=v)
        return res

    # B2
    def SUseason(self, thisseason):
        points = sum(self.points)
        opoints = sum(self.opoints)
        w = (points - opoints) / len(self.points)
        x = 0
        y = 0
        z = 0
        total = 0
        for (p, op, season) in zip(self.points, self.opoints, self.season):
            if str(season) == str(thisseason):
                if p > op:
                    x = x + 1
                if p < op:
                    y = y + 1
                if p == op:
                    z = z + 1
                total = total + 1
        if total == 0:
            return self.SU()
        suml13 = self.suml13season(thisseason)
        tie = 0
        for s in suml13:
            if s == 0:
                tie = tie + 1
        v = (x / (x + y - z)) * 100
        if tie == 0:
            res = "{x}-{y} ({w:.1f},{v:.1f}%)".format(x=x, y=y, w=w, v=v)
        else:
            res = "{x}-{y}-{tie} ({w:.1f},{v:.1f}%)".format(x=x, y=y, tie=tie, w=w, v=v)
        return res

        # c3

    def closelineavgseason(self, thisseason):
        sum = 0
        total = 0
        for (cl, season) in zip(self.closeline, self.season):
            if str(season) == str(thisseason):
                sum = sum + cl
                total = total + 1
        if total == 0:
            return self.closelineavg()
        return round(sum / total, 2)

    # c4
    def closetotalavgseason(self, thisseason):
        sum = 0
        total = 0
        for (cl, season) in zip(self.closetotal, self.season):
            if str(season) == str(thisseason):
                sum = sum + cl
                total = total + 1
        if total == 0:
            return self.closetotalavg()
        return round(sum / total, 2)





