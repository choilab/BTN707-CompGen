# Antisense oligonucleotide (ASO) off-target finder

ASO-off-finder is a program that finds target and potential off-target sites in the FASTA sequence for input antisense oligonucleotide (ASO) sequences.

# Table of Content

* [Students](#student)
* [Program overview](#overview)
* [Thinkabouts](#intro)
* [Algorithm outline](#outline)

<a name="student"></a>
# Students

* 김보근
* 박연수

<a name="overview"></a>
# Program overview

* Input: target genome sequence and oligonucleotide sequence (FASTA format)
* Output: target and off-target site coordinate
* Options: # of allowed mismatches/indels

<a name="intro"></a>
# Thinkabouts

* What is the problem to solve?
    1. What is Antisense oligonucleotide (ASO)?
    2. Different types of ASO
* Why is it important? (biological meaning)
    1. How ASO is used in therapeutics?
    2. Why is finding ASO off-target site important?
    3. How to find ASO off-target site?
* How should we solve the problem?
    1. Pre-existing methods to detect ASO off-targets
    2. New methods to try?

<a name="outline"></a>
# Algorithm outline

Problem | Query | Reference
---- | ---- | ----
Read alignment problem | Sequenced reads | Reference genome
ASO off-target finder | ASO sequence | Target RNA sequence database

* Finding ASO off-target sites is similar to the read alignment problem.
* Apply dynamic programming for approxiamte alignment for matching ASO sequence to target sequences
