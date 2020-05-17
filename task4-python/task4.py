import pandas as pd
import sys

if __name__ == "__main__":
    #check that user input 1 csv file
    try:
        if len(sys.argv) !=1:
            raise ValueError("Please include 1 csv file")
        else:
            filename = sys.argv[1]

            data = pd.read_csv(filename)
            #data = pd.read_csv(r'C:\Users\weetong\Desktop\DE\dataeng_test-master\04-17-2020_Dataset.csv')
            dataExtracted = pd.DataFrame(data, columns= ['price','firstName']) #extrac 3rd and 1st column
            jsonFormat = dataExtracted.to_json(orient ='records') #change to json format

            #print(jsonFormat)
            #print(dataExtracted.head())


            ###function to output xml###

            def func(row):
                xml = ['<item>']
                for field in row.index:
                    xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
                xml.append('</item>')
                
                return '\n'.join(xml)

            #print('\n'.join(dataExtracted.apply(func, axis=1)))

            print("Uncomment to see output")
    except:
        print("Invalid argument.Please` Include 1 csv file")
