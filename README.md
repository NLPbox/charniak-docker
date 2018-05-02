# charniak-docker

[![Travis Build Status](https://travis-ci.org/NLPbox/charniak-docker.svg?branch=master)](https://travis-ci.org/NLPbox/charniak-docker)
[![Docker Build Status](https://img.shields.io/docker/build/nlpbox/charniak.svg)](https://hub.docker.com/r/nlpbox/charniak/builds/)

This docker container allows you to build, install and run the most recent version of the
[Charniak parser](https://github.com/BLLIP/bllip-parser)
(aka Charniak-Johnson reranking parser, BLLIP parser) in a docker container.


## Building / Installing the Charniak parser

```
git clone https://github.com/NLPbox/charniak-docker
cd charniak-docker
docker build -t charniak-docker .
```

## Running the Charniak parser

To test if parser works, just run ``docker run charniak``.
To run the parser on the file ``/tmp/input.txt`` on your
local machine with the standard parser model, run:

```
docker run -v /tmp:/tmp -ti charniak /tmp/input.txt
```

Input files must be sentence segmented, with sentences enclosed in an
`<s>` element and surrounded by spaces:

```
<s> Sentence 1 </s>
<s> Sentence 2 </s>
```

## Example Input

```
<s> Henryk Szeryng (22 September 1918 - 8 March 1988) was a violin 
virtuoso of Polish and Jewish heritage. </s>

<s> He was born in Zelazowa Wola, Poland. </s>
<s> Henryk started piano and harmony training with his mother when he 
was 5, and at age 7 turned to the violin, receiving instruction from 
Maurice Frenkel. </s>

<s> After studies with Carl Flesch in Berlin (1929-32), he went to 
Paris to continue his training with Jacques Thibaud at the 
Conservatory, graduating with a premier prix in 1937. </s>

<s> He made his solo debut in 1933 playing the Brahms Violin Concerto. 
</s><s> From 1933 to 1939 he studied composition in Paris with Nadia 
Boulanger, and during World War II he worked as an interpreter for the 
Polish government in exile (Szeryng was fluent in seven languages) and 
gave concerts for Allied troops all over the world. </s><s> During one 
of these concerts in Mexico City he received an offer to take over the 
string department of the university there. </s>

<s> In 1946, he became a naturalized citizen of Mexico. </s>

<s> Szeryng subsequently focused on teaching before resuming his 
concert career in 1954. </s><s> His debut in New York City brought him 
great acclaim, and he toured widely for the rest of his life. </s>
<s> He died in Kassel. </s>

<s> Szeryng made a number of recordings, including two of the complete 
sonatas and partitas for violin by Johann Sebastian Bach, and several 
of sonatas of Beethoven and Brahms with the pianist Arthur 
Rubinstein. </s><s> He also composed; his works include a number of violin 
concertos and pieces of chamber music. </s>

<s> He owned the Del Gesu "Le Duc", the Stradivarius "King David" as 
well as the Messiah Strad copy by Jean-Baptiste Vuillaume which he gave 
to Prince Rainier III of Monaco. </s><s> The "Le Duc" was the instrument on 
which he performed and recorded mostly, while the latter ("King David" 
Strad) was donated to the State of Israel. </s>
```

## Example Output

```
(S1 (S (NP (NP (NNP Henryk) (NNP Szeryng)) (PRN (-LRB- -LRB-) (NP (NP (CD 22) (NNP September) (NN 1918)) (: -) (NP (CD 8) (NNP March) (CD 1988))) (-RRB- -RRB-))) (VP (AUX was) (NP (NP (DT a) (NN violin) (NN virtuoso)) (PP (IN of) (NP (JJ Polish) (CC and) (JJ Jewish) (NN heritage))))) (. .)))
(S1 (S (NP (PRP He)) (VP (AUX was) (VP (VBN born) (PP (IN in) (NP (NP (NNP Zelazowa) (NNP Wola)) (, ,) (NP (NNP Poland)))))) (. .)))
(S1 (S (NP (NNP Henryk)) (VP (VP (VBD started) (NP (NP (NN piano)) (CC and) (NP (NN harmony) (NN training))) (PP (IN with) (NP (PRP$ his) (NN mother))) (SBAR (WHADVP (WRB when)) (S (NP (PRP he)) (VP (AUX was) (NP (CD 5)))))) (, ,) (CC and) (VP (PP (IN at) (NP (NN age) (CD 7))) (VBD turned) (PP (TO to) (NP (DT the) (NN violin))) (, ,) (S (VP (VBG receiving) (NP (NN instruction)) (PP (IN from) (NP (NNP Maurice) (NNP Frenkel))))))) (. .)))
(S1 (S (PP (IN After) (NP (NP (NNS studies)) (PP (IN with) (NP (NP (NNP Carl) (NNP Flesch)) (PP (IN in) (NP (NNP Berlin))))) (PRN (-LRB- -LRB-) (NP (CD 1929-32)) (-RRB- -RRB-)))) (, ,) (NP (PRP he)) (VP (VBD went) (PP (TO to) (NP (NNP Paris))) (S (VP (TO to) (VP (VB continue) (NP (NP (PRP$ his) (NN training)) (PP (IN with) (NP (NNP Jacques) (NNP Thibaud)))) (PP (IN at) (NP (DT the) (NNP Conservatory))) (, ,) (S (VP (VBG graduating) (PP (IN with) (NP (DT a) (JJ premier) (NNP prix))) (PP (IN in) (NP (CD 1937))))))))) (. .)))
(S1 (S (NP (PRP He)) (VP (VBD made) (NP (PRP$ his) (JJ solo) (NN debut)) (PP (IN in) (NP (CD 1933))) (S (VP (VBG playing) (NP (NP (DT the) (NNP Brahms) (NNP Violin) (NNP Concerto.) (NN </s><s>)) (PP (IN From) (NP (CD 1933)))) (PP (TO to) (NP (NP (CD 1939)) (SBAR (S (NP (PRP he)) (VP (VP (VBD studied) (NP (NN composition)) (PP (IN in) (NP (NNP Paris))) (PP (IN with) (NP (NNP Nadia) (NNP Boulanger)))) (, ,) (CC and) (VP (PP (IN during) (NP (NNP World) (NNP War) (NNP II))) (SBAR (S (NP (PRP he)) (VP (VP (VBD worked) (PP (IN as) (NP (NP (DT an) (NN interpreter)) (PP (IN for) (NP (DT the) (NNP Polish) (NN government))))) (PP (IN in) (NP (NN exile))) (PRN (-LRB- -LRB-) (S (NP (NNP Szeryng)) (VP (AUX was) (ADJP (JJ fluent)) (PP (IN in) (NP (CD seven) (NNS languages))))) (-RRB- -RRB-))) (CC and) (VP (VBD gave) (NP (NP (NNS concerts)) (PP (IN for) (NP (NNP Allied) (NNS troops)))) (PP (DT all) (IN over) (NP (DT the) (VBN world.) (NN </s><s>))) (PP (IN During) (NP (NP (CD one)) (PP (IN of) (NP (NP (DT these) (NNS concerts)) (PP (IN in) (NP (NNP Mexico) (NNP City))) (SBAR (S (NP (PRP he)) (VP (VBD received) (NP (DT an) (NN offer) (S (VP (TO to) (VP (VB take) (PRT (RP over)) (NP (NP (DT the) (NN string) (NN department)) (PP (IN of) (NP (NP (DT the) (NN university)) (ADVP (RB there))))))))))))))))))))))))))))) (. .)))
(S1 (S (PP (IN In) (NP (CD 1946))) (, ,) (NP (PRP he)) (VP (VBD became) (NP (NP (DT a) (JJ naturalized) (NN citizen)) (PP (IN of) (NP (NNP Mexico))))) (. .)))
(S1 (S (NP (NNP Szeryng)) (ADVP (RB subsequently)) (VP (VBD focused) (PP (IN on) (NP (NN teaching))) (PP (IN before) (S (VP (VBG resuming) (NP (PRP$ his) (NN concert) (NN career)) (PP (IN in) (NP (NP (JJ 1954.) (NNS </s><s>)) (SBAR (S (S (NP (NP (PRP$ His) (NN debut)) (PP (IN in) (NP (NNP New) (NNP York) (NNP City)))) (VP (VBD brought) (NP (PRP him)) (NP (JJ great) (NN acclaim)))) (, ,) (CC and) (S (NP (PRP he)) (VP (VBD toured) (ADVP (RB widely)) (PP (IN for) (NP (NP (DT the) (NN rest)) (PP (IN of) (NP (PRP$ his) (NN life))))))))))))))) (. .)))
(S1 (S (NP (PRP He)) (VP (VBD died) (PP (IN in) (NP (NNP Kassel)))) (. .)))
(S1 (S (S (NP (NNP Szeryng)) (VP (VBD made) (NP (NP (DT a) (NN number)) (PP (IN of) (NP (NNS recordings))) (, ,) (PP (VBG including) (NP (NP (NP (CD two)) (PP (IN of) (NP (NP (DT the) (JJ complete) (NNS sonatas) (CC and) (NNS partitas)) (PP (IN for) (NP (NP (NN violin)) (PP (IN by) (NP (NNP Johann) (NNP Sebastian) (NNP Bach)))))))) (, ,) (CC and) (NP (NP (JJ several)) (PP (IN of) (NP (NP (NNS sonatas)) (PP (IN of) (NP (NNP Beethoven) (CC and) (NNP Brahms))) (PP (IN with) (NP (NP (DT the) (NN pianist)) (SBAR (S (NP (NNP Arthur) (NNP Rubinstein.)) (VP (VBD </s><s>) (SBAR (S (NP (PRP He)) (ADVP (RB also)) (VP (VBN composed))))))))))))))))) (: ;) (S (NP (PRP$ his) (NNS works)) (VP (VBP include) (NP (NP (DT a) (NN number)) (PP (IN of) (NP (NP (NN violin) (NNS concertos)) (CC and) (NP (NP (NNS pieces)) (PP (IN of) (NP (NN chamber) (NN music))))))))) (. .)))
(S1 (S (NP (PRP He)) (VP (VBD owned) (NP (NP (DT the) (NNP Del) (NNP Gesu) (`` ``) (NNP Le) (NNP Duc) ('' '')) (, ,) (NP (DT the) (NNP Stradivarius) (`` ``) (NNP King) (NNP David) ('' ''))) (PP (IN as) (ADVP (RB well) (PP (IN as) (NP (NP (DT the) (NNP Messiah) (NNP Strad) (NN copy)) (PP (IN by) (NP (NNP Jean-Baptiste) (NNP Vuillaume))) (SBAR (WHNP (WDT which)) (S (NP (PRP he)) (VP (VBD gave) (PP (TO to) (NP (NP (NNP Prince) (NNP Rainier) (NNP III)) (PP (IN of) (NP (NP (NNP Monaco.) (CD </s><s>)) (SBAR (S (NP (DT The) (`` ``) (NNP Le) (NNP Duc) ('' '')) (VP (AUX was) (NP (NP (DT the) (NN instrument)) (SBAR (WHPP (IN on) (WHNP (WDT which))) (S (NP (PRP he)) (VP (VP (VBD performed)) (CC and) (VP (VBD recorded) (ADVP (RB mostly)) (, ,) (SBAR (IN while) (S (NP (DT the) (JJ latter) (PRN (-LRB- -LRB-) (NP (`` ``) (NNP King) (NNP David) ('' '') (NNP Strad)) (-RRB- -RRB-))) (VP (AUX was) (VP (VBN donated) (PP (TO to) (NP (NP (DT the) (NNP State)) (PP (IN of) (NP (NNP Israel))))))))))))))))))))))))))))) (. .)))
```

# Citation

Eugene Charniak and Mark Johnson (2005). [Coarse-to-fine n-best parsing and MaxEnt discriminative reranking.](http://aclweb.org/anthology/P/P05/P05-1022.pdf)  
Proceedings of the 43rd Annual Meeting on Association for Computational Linguistics.

Eugene Charniak (2000). [A maximum-entropy-inspired parser.](http://aclweb.org/anthology/A/A00/A00-2018.pdf)  
Proceedings of the 1st North American chapter of the Association for Computational Linguistics conference.
