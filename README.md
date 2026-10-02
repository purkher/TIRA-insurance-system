# TIRA Insurance Management System - Tanzania

A complete insurance management system compliant with the Tanzania Insurance Regulatory Authority (TIRA) for small insurance operations. Built with Flask to automate policy issuance, claims handling, reporting, and compliance tracking.

## Features Implemented

- Role-Based Access Control: Admin (full access), Agent (policies & claims), Customer (view & claim)
- Policy Holder Management: Full Name, NIDA 20-digit validation, Phone (255), Email, Address
- Policy Management: Auto Policy Number `POL-YYYY-XXX`, Premium auto-calc 5% of sum insured, Types: Motor, Life, Health, Property
- Claims Management: Submit, Approve, Reject workflow, Auto Claim Number `CLM-YYYY-XXX`
- Dashboard Analytics: Total Policies, Holders, Premiums, Claims with Chart.js visualization
- TIRA Reports: Compliance report, Premium collection, Claims ratio, Export-ready tables
- KYC Compliance: Document upload (NIDA Card, Driving License, Passport)
- Security: Password hashing (Werkzeug), Flask-Login, Input validation

## Tech Stack

- Backend: Python 3 + Flask
- Database: SQLAlchemy + SQLite (`insurance.db`)
- Authentication: Flask-Login + Werkzeug Security
- Frontend: Bootstrap 5 + Chart.js + Jinja2 Templates

## Project Structure

```text
TIRA-insurance-system/
├── app.py                     # Main Flask application
├── insurance.db               # SQLite database (auto-created on first run)
├── README.md                  # Project documentation
├── templates/
│   ├── base.html              # Main layout, navbar, sidebar, flash messages
│   ├── login.html             # Login form
│   ├── register.html          # User registration form
│   ├── dashboard.html         # Dashboard with stats and Chart.js
│   ├── holders.html           # Policy holders list
│   ├── add_holder.html        # Add new holder with NIDA validation
│   ├── policies.html          # Policies list
│   ├── add_policy.html        # Add policy with auto calculation
│   ├── claims.html            # Claims list and approval flow
│   ├── add_claim.html         # Submit new claim form
│   ├── reports.html           # TIRA compliance reports
│   └── kyc_upload.html        # KYC upload page
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   └── chart.js           # Dashboard chart logic
│   └── uploads/               # Uploaded KYC documents
├── venv/                      # Optional virtual environment
├── .gitignore                 # Git ignore rules
└── requirements.txt           # Python dependencies (if used)
```

## Installation & Run

### 1. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-login
```

### 2. Run the app

```bash
python app.py
```

### 3. Open in browser

```text
http://127.0.0.1:5000
```

## Default Accounts

The database is auto-created on first run:

| Username | Password | Role | Access |
| --- | --- | --- | --- |
| admin | admin123 | Admin | Full system |
| agent1 | agent123 | Agent | Policies & Claims |
| customer1 | customer123 | Customer | View & Submit Claims |

## Workflow Test (Demo Steps)

1. Login as `admin / admin123`
2. Add a policy holder: `Imani Milinga`, NIDA: `19980101234567890123`
3. Add a policy: select holder, set sum insured to `20,000,000`, then confirm premium auto-calculates to `1,000,000`
4. Log out, register as a new customer, and log in
5. Submit a claim: select policy, enter amount and reason
6. Log out, log in as admin, manage claims, and approve the claim
7. Check the dashboard and reports

## Compliance Notes (TIRA)

- NIDA validation: 20-digit regex `^\d{20}$`
- Premium: 5% of sum insured (TIRA minimum rate)
- Phone: Tanzania format `+255` or `0xxx`
- Policy Number: `POL-YYYY-XXX` unique
- Dates stored in UTC and displayed as `YYYY-MM-DD`

## Future Improvements

- M-Pesa / Tigo Pesa payment integration
- PDF policy certificate generation
- SMS notifications via Beem Africa
- TIRA API integration for real compliance

## Author

Imani Milinga - Insurance Management System  
Ruvuma, Tanzania - 2026

## License

Academic Use - TIRA Compliant Demo System
