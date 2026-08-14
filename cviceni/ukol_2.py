def pocet_sudych(n):
    """
    Vrať počet sudých čísel v rozsahu od 1 do n (včetně n).
    Pokud n není celé číslo (int), vyhoď TypeError s výstižnou zprávou.

    Příklad:
        pocet_sudych(10) -> 5  (2, 4, 6, 8, 10)
        pocet_sudych(1) -> 0
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n musí být celé číslo (int)")

    pocet = 0
    for cislo in range(1, n + 1):
        if cislo % 2 == 0:
            pocet += 1
    return pocet
