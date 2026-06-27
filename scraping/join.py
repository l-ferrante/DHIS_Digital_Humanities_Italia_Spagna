import pandas as pd

def join():
    tutti_join_df = []

    for n in range(1,8):
        f = f"output/{n}/fin{n}.csv"
        c = f"output/{n}/cup{n}.csv"

        fin = pd.read_csv(f)
        cup = pd.read_csv(c)

        cup["codice"] = cup["codice"].str.upper() #NORMALIZZAZIONE del codice con uppercase
        fin["codice"] = fin["codice"].str.upper()

        #print(f"join {n}")
        #print(cup.info())
        #print(fin.info())

        join_df = cup.merge(fin, on="codice", how="left")

        media_finanziamento = join_df["finanziamento"].mean()
        join_df["finanziamento"] = join_df["finanziamento"].fillna(media_finanziamento)

        tutti_join_df.append(join_df)

        print(f"JOIN {n} fatto")

        join_final = pd.concat(tutti_join_df, ignore_index=True)

    return join_final


join_final = join()

join_final.to_csv("output/join_final.csv", index = False)
print("esportazione in csv completata")
