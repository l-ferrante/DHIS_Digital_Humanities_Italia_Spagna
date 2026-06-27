from playwright.sync_api import sync_playwright
import re

agent = "CorsoDataJournalismBot/1.0 (ricerca didattica; contatto: email@example.com)"       

def run(playwright, url = None):
    # Avvia il browser in modalità non headless per poter osservare l'azione.
    browser = playwright.chromium.launch(headless=True)
    # Imposta un user agent
    context = browser.new_context(user_agent=agent)
    # Apre una nuova pagina
    page = context.new_page()
    page.goto(url)

    table = page.locator("table")

    rows = table.locator("tr").all()

    D = []

    for row in rows:
        cells = row.locator("td, th").all()
        row_data = [cell.inner_text() for cell in cells]

        for text in row_data:
            if (re.match(r"\d+\.*2022\w{6}", text)):
            #if (re.match(r"\d+\.*\w*\w*\b.*2022\w{6}", text)): #Solo per allegato6
                codice = str(text)
                codice = re.sub(r"\d+\.( )?", "", codice)
                #codice = re.sub(r"\w* (\w*)+( )?(-)?( )?", "", codice) #Solo per allegato6
            
            if (re.match(r"\d{1,3}\.\d{3}\b", text)):
                finanziamento = str(text)

                fin_dict = {
                    "codice" : codice,
                    "finanziamento": finanziamento,
                }
                
                D.append(fin_dict)

    import pandas as pd




    import pandas as pd
    df = pd.DataFrame(D)
    df = df.astype({"finanziamento":"float64"})
    df = df.groupby("codice").sum()

    df.to_csv("output/6/fin6.csv", index=True)


    browser.close()    


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright, "http://localhost:8000/html/allegatoC6.md")