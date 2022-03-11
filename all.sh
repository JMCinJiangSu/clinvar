
NM_variant_summary=$(grep NM_ variant_summary.txt)
GRCh37=$(grep GRCh37 $NM_variant_summary)
GRCh38=$(grep GRCh38 $NM_variant_summary)

$GRCh37 | col -b > GRCh37_new.txt
$GRCh38 | col -b > GRCh38_new.txt

var=$(cat germ.txt)
for i in ${var}
do
	grep ${i} GRCh37_new.txt | col -b >> sel_37.txt
	grep ${i} GRCh38_new.txt | ol -b >> sel_38.txt
done