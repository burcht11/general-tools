# TMVA outputs a lot in .eps, so quick script to change all files in a directory to another filetype
DIRECTORY=$1
OUTPUT_FILETYPE=png

for f in $DIRECTORY*
do
	EXTENSION=${f##*.}

	if [ $EXTENSION != $OUTPUT_FILETYPE ]; # skip files already in this filetype
	then
		NEW_FILE=${f%%.*}.$OUTPUT_FILETYPE

		# If eps, we should turn into a pdf first
		if [ $EXTENSION == "eps" ];
		then
			echo $f | xargs -n1 pstopdf
			f=${f%.*}.pdf
		fi

		# convert
	    echo sips -s format $OUTPUT_FILETYPE $f --out $NEW_FILE

		# TODO: clean up excess PDFs
	fi

done
