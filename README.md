# Týden 03 – Cykly

## Cíl lekce
- Naučit se opakovat kód pomocí cyklu `while`.
- Naučit se opakovat kód pomocí cyklu `for` a funkce `range()`.
- Umět použít `break` a `continue` pro řízení průběhu cyklu.

## Výklad

### Cyklus while
Opakuje blok kódu, dokud platí podmínka:
```python
pocitadlo = 0
while pocitadlo < 5:
    print(pocitadlo)
    pocitadlo += 1  # nezapomeň měnit hodnotu, jinak vznikne nekonečný cyklus!
```

### Cyklus for a range()
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (krok 2)
    print(i)
```

### break a continue
- `break` okamžitě ukončí celý cyklus.
- `continue` přeskočí zbytek aktuální iterace a pokračuje další.

Podrobné okomentované ukázky najdeš v souborech `priklady/priklad_1.py` (while) a `priklady/priklad_2.py` (for, range).

## Cvičení

Doplň funkce v souborech ve složce `cviceni/`:

- **`ukol_1.py` - `soucet_do_n(n)`**: Vrať součet všech celých čísel od 1 do `n` (včetně). Pro `n < 1` vrať `0`.
  - Příklad: `soucet_do_n(5)` -> `15`
- **`ukol_2.py` - `pocet_sudych(n)`**: Vrať počet sudých čísel v rozsahu od 1 do `n` (včetně).
  - Příklad: `pocet_sudych(10)` -> `5`
- **`ukol_3.py` - `faktorial(n)`**: Vrať faktoriál čísla `n` pomocí cyklu (`faktorial(0)` je `1`).
  - Příklad: `faktorial(5)` -> `120`

## Jak si to sám zkontrolovat
```bash
pip install -r requirements.txt
pytest cviceni -v
```
Po nahrání na GitHub navíc automaticky poběží testy přes GitHub Actions – uvidíš zelenou/červenou fajfku u commitu.

## Odevzdání
Vyplň soubory v `cviceni/`, commitni a pushni do svého repozitáře do stanoveného termínu. Řešení (branch `reseni`) zveřejní vyučující až po deadline.
