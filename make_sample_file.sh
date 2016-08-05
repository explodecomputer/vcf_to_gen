#!/bin/bash

zcat ../chr1.vcf.gz | head -n 4 | tail -n 1 | cut -f 10- | tr '\t' '\n' > ids.txt
echo "ID_1 ID_2 missing" > samplehead
echo "0 0 0" >> samplehead
awk '{ print $1, $1, "0" }' ids.txt > sampletail
cat samplehead sampletail > data.sample
rm samplehead sampletail ids.txt
