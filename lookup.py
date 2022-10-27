import socket
import pandas as pd

df=pd.read_csv(r'C:\Users\Dan\Documents\arp_lookup.csv')
df.dropna(inplace=True)
print(df)
for i, row in df.iterrows():
    y=df.at[i,'IP']
    try:
        x=socket.gethostbyaddr(y)
        df.at[i,'host name']=x
    except:
        x="nan"
        df.at[i,'host name']=x
    print(i)

print(df)
df.to_excel(r'C:\Users\Dan\Documents\output.xlsx')  
    
