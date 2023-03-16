import njit_corrector as nc


with nc.exam():

    with nc.task("1.FELADAT"):

        with nc.subtask("Helyes fájlnév", 1):
            nc.assertFileName("feladat01.py")

        with nc.subtask("Helyes kimenet ha létező nicket adunk meg", 1):
            nc.runFile("feladat01.py", "Frostborn")
            output = nc.readOut()
            correct = output == "Adj meg egy nicket:\nvan\nHorváth Márk\n"
            nc.runFile("feladat01.py", "Darkseeker")
            output = nc.readOut()
            correct = correct and output == "Adj meg egy nicket:\nvan\nKovács Zolta\n"
            nc.runFile("feladat01.py", "Firestarter")
            output = nc.readOut()
            correct = correct and output == "Adj meg egy nicket:\nvan\nSinka Dávid\n"
            nc.assertValues(correct, True)

        with nc.subtask("Helyes kimenet ha nem létező nicket adunk meg", 1):
            nc.runFile("feladat01.py", "ASDF")
            output = nc.readOut()
            correct = output == "Adj meg egy nicket:\nnincs\n"
            nc.assertValues(correct, True)

        with nc.subtask("Helyes kimenet ha hibás nicket adunk meg", 1):
            code = nc.readFile("feladat01.py")
            code = nc.addExitToCode(code)
            nc.runCode(code, "ASDF123")
            output = nc.readOut()
            correct = output == "Adj meg egy nicket:\nhibás nick\n"
            nc.runCode(code, "ASDF ASDF")
            output = nc.readOut()
            correct = correct and output == "Adj meg egy nicket:\nhibás nick\n"
            nc.assertValues(correct, True)