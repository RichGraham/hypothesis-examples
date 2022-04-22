for f in Tests*.py
do
   python $f
done

for f in Property_Tests*.py
do
   pytest -s $f
done
