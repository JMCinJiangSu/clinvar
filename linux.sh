

grep NM_ variant_summary.txt |col -b > NM_variant_summary.txt
grep GRCh37 NM_variant_summary.txt | col -b > GRCh37.txt
grep GRCh38 NM_variant_summary.txt | col -b > GRCh38.txt

sed -n '1p' GRCh37.txt

cat GRCh37.txt | cut -f 3,5,7 | col -b > GRCh37_new.txt
cat GRCh38.txt | cut -f 3,5,7 | col -b > GRCh38_new.txt

cat germgene.txt | tr "\r" "\t" > germ.txt


var=$(cat germ.txt)
for i in ${var}
do
	grep ${i} GRCh37_new.txt | col -b > sel37.txt
	grep ${i} GRCh38_new.txt | col -b > sel38.txt
done