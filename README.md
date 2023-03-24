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

## 2. feladat - játék pontszámok

A 10.b. osztály egyik tanulója összegyűjtötte az osztálytársai által elért legjobb pontszámokat egy népszerű online játékban. A pontszámokat a ```10b_game_scores.txt``` fájlban találod. Írj egy Python programot, ami az alábbi feladatokat végzi:

1. Olvasd be a ```10b_game_scores.txt``` fájl tartalmát és tárold el egy listában.
2. Számítsd ki a pontszámok összegét.
3. Mentsd el az összeget egy új fájlba, ```sum_of_scores.txt``` néven.
4. Írasd ki az alábbi szöveget a konzolra: "Az összes pontszám: X" - ahol X az összeg értéke.


### Részletek
- A program a ```feladat02.py``` fileban legyen.

### Extra feladatok
- Ha a ```10b_game_scores.txt``` fájl nem létezik, akkor a program próbálja meg beolvasni a ```game_scores.txt``` fájlt.
- Ha a ```game_scores.txt``` fájl sem létezik, akkor a program hozza létre azt, a megfelelő formátumban, a ```10b_nicks.txt``` fájlban található nick nevekkel úgy, hogy mindenkinek 1 pontja van, és utána végezze el az összegzést.

### Példa kimenet:
```
Az összes pontszám: 28800
```

## 3. feladat - Legjobb játékosok kiválasztása
Szeretnénk megtudni, hogy kik azok a játékosok, akiknek a pontszáma meghaladja egy adott küszöbértéket az előző listában. Írj egy Python programot, ami az alábbi feladatokat végzi:
- Olvasd be a ```10b_game_scores.txt``` fájl tartalmát.
- Kérj be a felhasználótól egy küszöbértéket: "Adj meg egy küszöbértéket:"
- Válogasd ki azokat a játékosokat, akiknek a pontszáma meghaladja a megadott küszöbértéket.
- Írasd ki a ```top_players.txt``` fájlba a kiválasztott játékosok nevét és pontszámát a következő formátumban: "Név: Pontszám"

### Részletek:

- A program a ```feladat03.py``` fileban legyen.
- Példa futtatás:

```
Adj meg egy küszöbértéket:
15
```
top_players.txt tartalma:
```
Nightblade: 18
Shadowcaster: 17
Ironclad: 16
```

## 4. feladat - Statisztikák

Írasd ki egy fájlba az alábbi statisztikát:
- A legmagasabb pontszám és annak tulajdonosa.
- A legalacsonyabb pontszám és annak tulajdonosa.

### Részletek
- A program a ```feladat04.py``` fileban legyen.
- A kimeneti fájl neve ```stats.txt``` legyen.
- A kimenet formátuma a példában megadottal legyen megegyező:

### Példa kimeneti fájl:
```
Legmagasabb pontszám: Thunderbird - 20
Legalacsonyabb pontszám: Shadowhunter - 16
```

### Extra feladat:
Írasd ki az átlagos pontszámot (két tizedesjegy pontossággal), és annak tulajdonosát is:
```
Átlagos pontszám: 17.89
```
