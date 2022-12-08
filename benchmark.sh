time for i in {1..100}; do 
    python3 $1_read_files.py ./data > /dev/null;
    echo -ne "Run: $i\r"
done