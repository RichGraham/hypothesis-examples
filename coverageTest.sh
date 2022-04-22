coverage run Tests.py $f
for f in Tests_*.py
do
   coverage run -a $f
done
coverage report
coverage html
open htmlcov/index.html

