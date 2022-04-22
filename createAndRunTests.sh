for f in Tests*.ipynb;
do
    ipythToPython.sh  $f
done

coverage run Tests.py $f
for f in Tests_*.py
do
   coverage run -a $f
done
coverage report
