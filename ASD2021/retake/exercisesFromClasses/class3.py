"""
Zadanie 4. Proszę zaproponować algorytm scalający k posortowanych list.
Solution: Using min heap we store first values from lists. After taking the lowest value from the heap we add
another one from the list that previous was taken from. Than we use heapify to restore proper heap.
when all lists are without numbers we end our algorithm.
"""

