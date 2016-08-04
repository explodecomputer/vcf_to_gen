# Convert vcf to gen format

Used on GOYA imputed data where the genotype probabilities were converted to log10(p) genotype likelihoods.

To run a single chromosome

```
python vcf_lik_to_gen.py input.vcf.gz output.gen.gz
```

To run using GNU parallele:

```
parallel run.sh ::: {1..23}
```

