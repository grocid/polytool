# Polytool
Polytool is a python program designed to find weight-4 polynomial multiples of LFSR feedback polynomials. It is based on Algorithm 11 given here [here][http://lup.lub.lu.se/luur/download?func=downloadFile&recordOId=4934002&fileOId=4934007]. Preferably, this program should be run with `pypy`.

### Usage

1. Convert the polynomial to decimal notation, i.e. compute `P(2)` and set the variable poly accordingly.
2. The mask can be manually set, but the automatic setting should give the best performance.
3. Run `pypy polytool.py`.
4. Once finished, the program will output the lowest-degree multiple.

NOTE: If second stage fails (or has very few entries compared to first stage), you are using a too small initial table size.


#References
[1] http://lup.lub.lu.se/luur/download?func=downloadFile&recordOId=4934002&fileOId=4934007
