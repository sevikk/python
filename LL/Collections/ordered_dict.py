from collections import OrderedDict

def main():

    sportTeams = [("Royals", (18,12)), ("Rockets", (24,6)), ("Cardinals", (20, 10)), ("Warriors", (25, 5))]

    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    teams = OrderedDict(sortedTeams)

    print(teams)

    tm, vl = teams.popitem(False)
    print("Top team: ", tm, vl)

    for i, team in enumerate(teams, start=1):
        print(i, team)

        if i == 3:
            break


    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    # b = OrderedDict({"a": 1, "b": 2, "c": 3})
    # b = OrderedDict({"b": 2, "a": 1, "c": 3})
    b = {"b": 2, "a": 1, "c": 3}

    print(a== b)


    pass


if __name__ == "__main__":
    main()