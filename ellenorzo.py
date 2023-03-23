import njit_corrector as nc
import os
import re
import random

with nc.exam():

    with nc.task("1.FELADAT"):

        with nc.subtask("Helyes fájlnév", 1):
            nc.assertFileName("feladat01.py")

        with nc.subtask("Helyes kimenet ha létező nicket adunk meg", 1):
            nc.runFile("feladat01.py", "Frostborn")
            output = nc.readOut()
            correct = output.startswith("Adj meg egy nicket:\nvan")
            nc.runFile("feladat01.py", "Darkseeker")
            output = nc.readOut()
            correct = correct and output.startswith("Adj meg egy nicket:\nvan")
            nc.runFile("feladat01.py", "Firestarter")
            output = nc.readOut()
            correct = correct and output.startswith("Adj meg egy nicket:\nvan")
            nc.assertValues(correct, True)

        with nc.subtask("Helyes kimenet ha nem létező nicket adunk meg", 1):
            nc.runFile("feladat01.py", "ASDF")
            output = nc.readOut()
            correct = output == "Adj meg egy nicket:\nnincs\n"
            nc.assertValues(correct, True)

        with nc.subtask("Extra: Helyes kimenet + név kiíratása, ha létező nicket adunk meg", 1):
            nc.runFile("feladat01.py", "Frostborn")
            output = nc.readOut()
            nc.assertValues(output == "Adj meg egy nicket:\nvan\nHorváth Márk\n", True)

        with nc.subtask("Extra: Helyes kimenet ha hibás nicket adunk meg", 1):
            code = nc.readFile("feladat01.py")
            code = nc.addExitToCode(code)
            nc.runCode(code, "ASDF123")
            output = nc.readOut()
            correct = output == "Adj meg egy nicket:\nhibás nick\n"
            nc.runCode(code, "ASDF ASDF")
            output = nc.readOut()
            correct = correct and output == "Adj meg egy nicket:\nhibás nick\n"
            nc.assertValues(correct, True)


    with nc.task("2.FELADAT"):

        with nc.subtask("Helyes fájlnév", 1):
            nc.assertFileName("feladat02.py")

        with nc.subtask("Helyes kiíratás a prompt-ra", 2):
            nc.runFile("feladat02.py")
            nc.assertLastLine("Az összes pontszám: 340")

        with nc.subtask("Helyesen létrehozott fájl", 2):
            nc.runFile("feladat02.py")
            output = nc.readOut()
            with open("sum_of_scores.txt", "r") as f:
                sum_value = int(f.read().strip())
                nc.assertValues(sum_value, 340)

        with nc.subtask("Helyes eredmény tetszőleges tartalmú 10b_game_scores.txt esetén is", 2):
            os.rename("10b_game_scores.txt", "10b_game_scores.txt_ARCHIVE")
            with open("10b_game_scores.txt", "w") as f:
                f.write("Flamebearer:14\n")
                f.write("Dreamweaver:18\n")
                f.write("Starwatcher:18\n")
                f.write("Thunderbolt:4\n")
            nc.runFile("feladat02.py")
            nc.assertLastLine("Az összes pontszám: 54")
            nc.remove_file_if_exists("10b_game_scores.txt")
            os.rename("10b_game_scores.txt_ARCHIVE", "10b_game_scores.txt")

        with nc.subtask("Extra: Helyes fájlgenerálás ha nincs 10b_game_scores.txt, de van game_scores.txt", 2):
            nc.rename_file_if_exists("10b_game_scores.txt", "game_scores.txt")
            nc.runFile("feladat02.py")
            nc.assertLastLine("Az összes pontszám: 340")
            nc.rename_file_if_exists("game_scores.txt", "10b_game_scores.txt")

        with nc.subtask("Extra: Helyes fájlgenerálás ha nincs 10b_game_scores.txt és nincs game_scores.txt se", 1):
            nc.rename_file_if_exists("10b_game_scores.txt", "10b_game_scores.txt_ARCHIVE")
            nc.rename_file_if_exists("game_scores.txt", "game_scores.txt_ARCHIVE")
            nc.runFile("feladat02.py")

            with open("game_scores.txt", "r") as f:
                line = f.readline()
                match = re.match(r"^[A-Za-z]+:1$", line.strip())
                nc.assertValues(bool(match), True)  

            nc.rename_file_if_exists("10b_game_scores.txt_ARCHIVE", "10b_game_scores.txt")
            nc.remove_file_if_exists("10b_game_scores.txt_ARCHIVE")

            if os.path.exists("game_scores.txt_ARCHIVE"):
                os.remove("game_scores.txt")
                os.rename("game_scores.txt_ARCHIVE", "game_scores.txt")
            else:
                nc.remove_file_if_exists("game_scores.txt_ARCHIVE")
                nc.remove_file_if_exists("game_scores.txt")


        with nc.subtask("Extra: Helyes eredmény ha nincs 10b_game_scores.txt és nincs game_scores.txt se", 1):
            nc.rename_file_if_exists("10b_game_scores.txt", "10b_game_scores.txt_ARCHIVE")
            nc.rename_file_if_exists("game_scores.txt", "game_scores.txt_ARCHIVE")
            nc.runFile("feladat02.py")

            nc.assertLastLine(value="Az összes pontszám: 31")
            
            nc.rename_file_if_exists("10b_game_scores.txt_ARCHIVE", "10b_game_scores.txt")
            nc.remove_file_if_exists("10b_game_scores.txt_ARCHIVE")

            if os.path.exists("game_scores.txt_ARCHIVE"):
                os.remove("game_scores.txt")
                os.rename("game_scores.txt_ARCHIVE", "game_scores.txt")
            else:
                nc.remove_file_if_exists("game_scores.txt_ARCHIVE")
                nc.remove_file_if_exists("game_scores.txt")


    with nc.task("3.FELADAT"):

        with nc.subtask("Helyes fájlnév", 1):
            nc.assertFileName("feladat03.py")

        with nc.subtask("Helyesen megoldás", 2):
            nc.runFile("feladat03.py", "19")
            with open("top_players.txt", "r") as f:
                line = f.readline()
                correct = line.strip() == "Thunderbird: 20"
            nc.runFile("feladat03.py", "15")
            linecount = 0
            with open("top_players.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip() == "":
                        continue
                    match = re.match(r"^[A-Za-z]+: [0-9]+$", line.strip())
                    correct = correct and bool(match)
                    linecount += 1
                
                if correct and linecount == 9:
                    correct = True
                else:
                    correct = False

            nc.assertValues(correct, True)

    with nc.task("4.FELADAT"):

        with nc.subtask("Helyes fájlnév", 1):
            nc.assertFileName("feladat04.py")
        
        with nc.subtask("Helyesen generált statisztikák", 2):
            nc.runFile("feladat04.py")
            with open("stats.txt", "r", encoding="utf-8") as f:
                content = f.read().strip().split("\n")
                highest = "Legmagasabb pontszám: " in content[0]
                lowest = "Legalacsonyabb pontszám: " in content[1]
                correct = highest and lowest
                nc.assertValues(correct, True)
        
        with nc.subtask("Extra: helyesen generált átlag", 2):
            nc.runFile("feladat04.py")
            with open("stats.txt", "r", encoding="utf-8") as f:
                content = f.read().strip().split("\n")
                average = "Átlagos pontszám: " in content[2]
                nc.assertValues(average, True)

