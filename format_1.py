def calculate_ATS(records):
    wCount = 0
    lCount = 0
    pCount = 0
    totalPointsBoth = 0
    totalPointsCloseTotal = 0
    for i in range(len(records[0])):
        if (records[1][i] + records[3][i]) > records[2][i]:
            wCount += 1
        elif (records[1][i] + records[3][i]) < records[2][i]:
            lCount += 1
        else:
            pCount += 1
        totalPointsCloseTotal += records[2][i]
        totalPointsBoth += (records[1][i] + records[3][i])
    return f"{wCount}-{lCount}-{pCount} ({round((totalPointsBoth / len(records[0])) - (totalPointsCloseTotal / len(records[0])), 2)}, {round((wCount / len(records[0])) * 100, 1)}%)"


def calculate_average_close_line(records):
    closeLine = 0
    for i in range(len(records[0])):
        closeLine += records[3][i]
    return round(closeLine / len(records[0]), 1)


def calculate_OU(records):
    wCount = 0
    lCount = 0
    pCount = 0
    totalPointsCloseTotal = 0
    totalPointsBoth = 0
    for i in range(len(records[0])):
        if (records[1][i] + records[2][i]) > records[4][i]:
            wCount += 1
        elif (records[1][i] + records[2][i]) < records[4][i]:
            lCount += 1
        else:
            pCount += 1
        totalPointsCloseTotal += records[4][i]
        totalPointsBoth += (records[1][i] + records[2][i])
    return f"{wCount}-{lCount}-{pCount} ({round((totalPointsBoth / len(records[0])) - (totalPointsCloseTotal / len(records[0])), 2)}, {round((wCount / len(records[0])) * 100, 1)}%)"


def calculate_average_close_total(records):
    closeTotal = 0
    for i in range(len(records[0])):
        closeTotal += records[4][i]
    return round(closeTotal / len(records[0]), 1)


def calculate_SU(records):
    wCount = 0
    lCount = 0
    pCount = 0
    totalPoints = 0
    totalPointsOpponent = 0
    for i in range(len(records[0])):
        if records[1][i] > records[2][i]:
            wCount += 1
        elif records[1][i] < records[2][i]:
            lCount += 1
        else:
            pCount += 1
        totalPoints += records[1][i]
        totalPointsOpponent += records[2][i]
    return f"{wCount}-{lCount}-{pCount} ({round((totalPoints / len(records[0])) - (totalPointsOpponent / len(records[0])), 2)}, {round((wCount / len(records[0])) * 100, 1)}%)"

def get_output_format(json_data):
    htmlData = """
    <table class="table">
    <thead>
        <tr>
        <th scope="col" style="color:#0800ff;">games</th>
        <th scope="col" style="color:#0800ff;"><div style="padding-left:70px;">ATS</div><div>W - L- P (marg, %win)</div></th>
        <th scope="col" style="color:#0800ff;">Avg Line</th>
        <th scope="col" style="color:#0800ff;"><div style="padding-left:70px;">OU</div><div>W - L- P (marg, %win)</div></th>
        <th scope="col" style="color:#0800ff;">Avg Total</th>
        <th scope="col" style="color:#0800ff;"><div style="padding-left:70px;">SU</div><div>W - L- P (marg, %win)</div></th>
        <th scope="col" style="color:#0800ff;">SDQL</th>
        </tr>
    </thead>
    <tbody>"""

    for data in json_data["groups"]:
        ats = calculate_ATS(data["columns"])
        avg_line = calculate_average_close_line(data["columns"])
        ou = calculate_OU(data["columns"])
        avg_total = calculate_average_close_total(data["columns"])
        su = calculate_SU(data["columns"])
        htmlData += f"""<tr>
        <td>{len(data["columns"][0])}</td>
        <td>{ats}</td>
        <td>{avg_line}</td>
        <td>{ou}</td>
        <td>{avg_total}</td>
        <td>{su}</td>
        <td>{data["sdql as terms"][-3].split('=')[1]}</td>
        </tr>"""

    htmlData += """</tbody>
    </table>
    """

    return htmlData