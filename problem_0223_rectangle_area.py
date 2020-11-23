class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        l1, b1 = C-A, D-B
        l2, b2 = G-E, H-F
        if E>=C or H<=B or G<=A or F>=D:
            return l1*b1+l2*b2
        i_I, i_J = min(C,G), min(D,H)
        i_K, i_L = max(A,E), max(B,F)
        return l1*b1 + l2*b2 - abs(i_I-i_K)*abs(i_J-i_L)
