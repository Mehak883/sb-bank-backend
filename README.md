# CEDAV - Banking App

Banking application powered by NextJS and FastAPI. Connect in real time with your bank via Plaid APIs.

## Application
Functionalities:
- Directly connected to your bank account to fetch bank data
- Automatically categorizes transactions
- Budgeting tools
- Expense tracking by category
- Multiple accounts connected

Technologies:
- NextJS
- Chakra UI
- TypeScript
- Vercel
- Plaid API
- Python
- Supabase
- Prisma ORM

Frontend Repository:
https://github.com/davidmonnom/banking-frontend

---

Please note that this application is not yet in production. If you try to connect to it, you'll get an access error.
However, you can download it and add your own API identifier via Google & Plaid.

Here are the necessary environment variables to place in the .env file
```
DATABASE_URL="postgres database"

PLAID_REDIRECT_URI=https://cedav.be
PLAID_CLIENT_ID=
PLAID_SECRET=
PLAID_SANDBOX_SECRET=
PLAID_ENV=development
PLAID_PRODUCTS=transactions,auth

GOOGLE_CLIENT_ID=
GOOGLE_SECRET=
ALLOWED_USER="email addresses of allowed users"
```

## Screenshots
#### Dashboard
<p float="left">
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/dashboard_light.png" width="300" />
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/dashboard_dark.png" width="300" />
</p>

#### Transaction
<p float="left">
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/transaction_light.png" width="300" />
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/transaction_dark.png" width="300" />
</p>

#### Category
<p float="left">
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/category_light.png" width="300" />
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/category_dark.png" width="300" />
</p>

#### Saving
<p float="left">
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/saving_light.png" width="300" />
  <img alt="Dashboard in dark and light mode" src="https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/saving_dark.png" width="300" />
</p>

## Video
[![Watch the video](https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/dashboard_dark.png)](https://github.com/davidmonnom/banking-frontend/blob/main/screenshots/cedav.mp4)
