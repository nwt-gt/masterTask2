# Disclaimer

Link for the csv wasn't given so I used my own csv input and replaced ID with price

**Task 4B**

For more [info](https://stackoverflow.com/questions/29091138/regex-replace-on-specific-column-with-sed-awk)

 * -F to specify delimiter 

 * NR to count row number

 * gsub to replace alphanumeric with xxxxx for the third column.

```
awk -F "," 'NR>=2{gsub(/^([a-z0-9])/, "xxxxx", $3)} 1' testset.csv > output.csv
```
