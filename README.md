# NJSZKI Python I/O feladatok - 2023/10.b.

## 1. feladat
Megkértem a ChatGPT-t, hogy adjon a 10.b. osztály minden tagjának egy nick nevet. Az eredményt
a 10b_nicks.txt fájlban találod.

Írj egy python programot, ami rögtön az elindítása után kiírja az alábbi szöveget:
```Adj meg egy nicket:```
Ezután olvasson is be egy sort, majd nézze meg, hogy van-e olyan tanuló, akinek a bekért név a nick-je.

### Részletek
- A program a feladat01.py fileban legyen
- Ha a program talál olyan tanulót, akinek a nickje megegyezik a beírt nickkel, akkor a program írja ki azt a szót, hogy: ```van```, ha nem talál, akkor azt, hogy: ```nincs```

### Extra feladatok
- Ha a program talál valakit, akkor annak a nevét is írja ki (sorszám nélkül)
- Hibakezelés: ha valaki számot tartalmazó, vagy több szavas nick-et ad meg, akkor a program írja ki, hogy: ```hibás nick```

### Példa futtatások
```
Adj meg egy nicket:
Sunbringer
van
Major Barnabás
```
```
Adj meg egy nicket:
Asdf
nincs
```
```
Adj meg egy nicket:
143 sanyi
hibás nick
```