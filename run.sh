#!/bin/bash

i=$1
vcf_lik_to_gen.py ../chr${i}.vcf.gz data_chr${i}.gen.gz

