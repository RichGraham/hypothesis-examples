for f in Tests*.ipynb;
do
    ipythToPython.sh  $f
done

for f in Property_Tests*.py
do
   pytest -s $f
done


coverage run Tests.py $f
for f in Tests_*.py
do
   coverage run -a $f
done
coverage report
