
rm -rf src-all/*
cp -r src/* src-all
cp -r ../typefacet/python/src-main/* src-all
find . | grep "\.pyc" | xargs rm
python code_cleanup.py

echo 'complete.'
