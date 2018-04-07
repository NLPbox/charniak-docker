#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import os
import pytest
import sh


EXPECTED_OUTPUT = """(S1 (S (NP (DT This)) (VP (AUX is) (NP (DT some) (NN text) (SBAR (IN that) (S (NP (PRP we)) (VP (MD should) (, ,) (ADVP (RB presumably)) (, ,) (NP (NN parse))))))) (. !)))
(S1 (S (NP (NP (DT A) (JJ second) (NN sentence)) (PRN (-LRB- -LRB-) (PP (ADVP (RB much)) (IN like) (NP (DT the) (JJ first))) (-RRB- -RRB-))) (VP (MD will) (ADVP (RB also)) (VP (VB help))) (. .)))
(S1 (S (NP (DT This) (NN sentence)) (VP (VBZ contains) (NP (NP (NP (DT some) (ADJP (RB very) (JJ funny)) (NNS tokens)) (, ,) (PP (JJ such) (IN as) (NP (NP (NNS \/)) (UCP (CC and) (ADJP (# #) (CC and) (NN %) (NN %)) (CC and) (ADJP (JJ *) (CC &) (JJ *)) (CC and) (. !) (. !) (FRAG (CC and) (NP (NN ~) (CC and) (NN +=) (NNS <)) (. .)) (. .)))) (. ?)) (: ;) (NP (NNS _)) (: -) (CC &) (NP (NNS >))))))
"""


def test_charniak():
    """The Charniak parser produces the expected output."""
    parser = sh.Command('./parse.sh')
    input_filepath = os.path.abspath('sample-text/sample-data.txt')
    result = parser(input_filepath)
    assert result.stdout == EXPECTED_OUTPUT, result.stderr.encode('utf-8')

