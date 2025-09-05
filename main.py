from datetime import date
import pandas as pd
from send_emails import send_email

SHEET_ID = "1vTau2orm7oc9NEayPg5PU6AlYLfy3h4NplYmLPvlPdU"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["due_date", "remainder_date"]
    # dayfirst=False because your dates are MM/DD/YYYY format (e.g., 8/11/2022)
    df = pd.read_csv(url, parse_dates=parse_dates, dayfirst=False)
    print("Loaded DataFrame dates preview:")
    print(df[["due_date", "remainder_date"]])
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        print(f"Checking {row['email']} - remainder_date: {row['remainder_date'].date()}, has_paid: {row['has_paid']}")
        if (present >= row["remainder_date"].date()) and (row["has_paid"].lower() == "no"):
            print(f"Sending email to: {row['email']}")
            send_email(
                subject=f'[Coding Is Fun] Invoice: {row["invoice_no"]}',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"),
                invoice_no=row["invoice_no"],
                amount=row["amount"],
            )
            email_counter += 1

    return f"Total Emails Sent: {email_counter}"

if __name__ == "__main__":
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)
