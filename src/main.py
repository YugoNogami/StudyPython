import excel
import os
import glob
import pandas as pd

dirname = os.path.dirname(os.path.abspath(__file__)) + '/data'
filelist = glob.glob(dirname + '/*.xlsx')
outputfilename = os.path.dirname(os.path.abspath(__file__)) + '/output.csv'

# df = pd.DataFrame({'区町村': '練馬区','値': '100'},index = ['0'])
df = pd.DataFrame(columns=['区町村', '総数'])
s = pd.Series({'区町村': '練馬区', '総数': '100'}, name=0)
df = df.append(s)

print(df)

index_count = 1
for filename in filelist:
    excel1 = excel.Excel(filename)
    print(filename)
    s = (pd.Series({
        '区町村': excel1.get_value(10, 0),
        '総数': excel1.get_value(10, 1)},
        name=index_count)
        )
    df = df.append(s)
    index_count += 1
print(df)
df.to_csv(outputfilename, index=False)
