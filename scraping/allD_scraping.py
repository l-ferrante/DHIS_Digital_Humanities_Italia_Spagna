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
            if (re.match(r"^20\d\d", text)): #Regex per trovare codici progetti e titoli
                progetto = re.sub(r"\[", "", str(text)) #Pulizia della stringa con regex
                progetto = re.sub(r"\]", "", progetto)
                progetto = re.sub(r"\"*", "", progetto)
                progetto = re.sub(r"\'*", "", progetto)
                progetto = re.sub(r"^20\d\d\w* - ", "", progetto)

                match = re.match(r"^(20\d\d\w*)", str(text))
                codice = match.group(0)

            if (re.match(r"Università|Scuola", text, re.IGNORECASE)): #Regex per trovare istituzione capofila
                istituzione = re.sub(r"\bdi", "di ", str(text))
                istituzione = re.sub(r"\bdella", "della ", istituzione)
                istituzione = re.sub(r"\bCommerciale", "Commerciale ", istituzione)
                istituzione = re.sub(r"\"", "", istituzione)

                proj_dict = {
                    "codice" : codice,
                    "progetto" : progetto,
                    "istituzione": istituzione,
                }

                D.append(proj_dict)

    
    import pandas as pd



    import pandas as pd
    df = pd.DataFrame(D)
    df = df.groupby("codice").agg({
        "progetto":"first",
        "istituzione":"first"
    })

    df.to_csv("output/7/cup7.csv", index=True)


    browser.close()    


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright, "http://localhost:8000/html/cup7.md")