def faktorial(n):
    """
    Vrať faktoriál čísla n (n! = 1 * 2 * 3 * ... * n) pomocí cyklu.
    Faktoriál 0 je podle definice 1.
    Pokud je n záporné, vyhoď ValueError s výstižnou zprávou.

    Příklad:
        faktorial(5) -> 120  (1*2*3*4*5)
        faktorial(0) -> 1
    """
    if n < 0:
        raise ValueError("n nesmí být záporné, faktoriál záporného čísla není definován")

    vysledek = 1
    for cislo in range(1, n + 1):
        vysledek *= cislo
    return vysledek
