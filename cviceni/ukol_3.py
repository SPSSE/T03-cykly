def faktorial(n):
    """
    Vrať faktoriál čísla n (n! = 1 * 2 * 3 * ... * n) pomocí cyklu.
    Faktoriál 0 je podle definice 1.

    Příklad:
        faktorial(5) -> 120  (1*2*3*4*5)
        faktorial(0) -> 1
    """
    vysledek = 1
    for cislo in range(1, n + 1):
        vysledek *= cislo
    return vysledek
