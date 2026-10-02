# TIRA Insurance Management System

A complete insurance management system built for Tanzania, aligned with the requirements of the Tanzania Insurance Regulatory Authority (TIRA). This project helps small insurance businesses manage policy issuance, claims processing, KYC verification, and compliance reporting through a web-based dashboard.

## Overview

The system is designed to support the core operations of a small insurance business with simple, secure, and role-based management features. It includes:

- policy holder registration and validation
- policy creation and premium calculation
- claims submission and approval workflow
- dashboard analytics and compliance reporting
- user role management for admin, agent, and customer access
- KYC document uploads for identity verification

## Key Features

- Role-Based Access Control
  - Admin: full access to the system
  - Agent: manage policies and claims
  - Customer: view records and submit claims

- Policy Holder Management
  - Full name
  - NIDA validation (20 digits)
  - Phone number validation for Tanzania
  - Email and address capture

- Policy Management
  - Auto-generated policy numbers in the format `POL-YYYY-XXX`
  - Premium calculated automatically at 5% of the insured value
  - Covered policy types: Motor, Life, Health, and Property

- Claims Management
  - Submit claims
  - Approve or reject claims
  - Auto-generated claim numbers in the format `CLM-YYYY-XXX`

- Dashboard Analytics
  - Total policies
  - Total holders
  - Premium totals
  - Claims overview
  - Chart.js-based visual reports

- TIRA Reporting
  - Compliance summaries
  - Premium collection reports
  - Claims ratio reporting
  - Export-ready report tables

- KYC Compliance
  - Upload supporting documents such as NIDA card, passport, and driving license

- Security
  - Password hashing with Werkzeug
  - Flask-Login session management
  - Input validation and user access restrictions

## Tech Stack

- Python 3
- Flask
- SQLAlchemy
- SQLite
- Flask-Login
- Bootstrap 5
- Chart.js
- Jinja2 Templates

## Project Structure

```text
TIRA-insurance-system/
├── app.py                     # Main Flask application
├── insurance.db               # SQLite database (created automatically)
├── README.md                  # Project documentation
├── templates/
│   ├── base.html              # Shared layout and navigation
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── dashboard.html         # Dashboard and analytics
│   ├── holders.html           # Policy holder list
│   ├── add_holder.html        # Add a new holder
│   ├── policies.html          # Policy list
│   ├── add_policy.html        # Add a new policy
│   ├── claims.html            # Claims overview and management
│   ├── add_claim.html         # Submit a claim
│   ├── reports.html           # TIRA report panel
│   └── kyc_upload.html        # KYC document upload page
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling
│   ├── js/
│   │   └── chart.js           # Chart.js logic for analytics
│   └── uploads/               # Uploaded KYC files
├── venv/                      # Optional virtual environment
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies (if used)
└── LICENSE                    # Project license (if added)
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/purkher/TIRA-insurance-system.git
cd TIRA-insurance-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-login
```

### 4. Run the app

```bash
python app.py
```

### 5. Open the app

```text
http://127.0.0.1:5000
```

## Default Accounts

When the database is created for the first time, the following default users are generated:

| Username | Password | Role | Access |
| --- | --- | --- | --- |
| admin | admin123 | Admin | Full system access |
| agent1 | agent123 | Agent | Policies and claims management |
| customer1 | customer123 | Customer | View and claim access |

## Demo Workflow

1. Log in as `admin / admin123`
2. Add a policy holder, for example:
   - Name: `Imani Milinga`
   - NIDA: `19980101234567890123`
3. Create a policy for the holder
4. Set the sum insured to `20,000,000`
5. Confirm that the premium is automatically calculated as `1,000,000`
6. Log out and register a new customer account
7. Log in as the customer and submit a claim
8. Log out and log back in as admin
9. Approve the claim from the claims management section
10. Review the dashboard and compliance reports

## Compliance Notes

This system is designed as a TIRA-aligned demo for educational and operational planning purposes.

- NIDA validation uses a 20-digit format: `^\d{20}$`
- Premium calculation follows a 5% rate of the sum insured
- Phone validation supports Tanzanian number formats such as `+255` and `0xxx`
- Policy numbers follow the format `POL-YYYY-XXX`
- Claim numbers follow the format `CLM-YYYY-XXX`
- Dates are stored in UTC and displayed in `YYYY-MM-DD`

## Future Enhancements

- M-Pesa and Tigo Pesa payment integration
- PDF policy certificate generation
- SMS notifications with Beem Africa
- TIRA API integration for live compliance validation
- Better report export options and audit history
- Enhanced dashboard filters and chart customization

## Author

Imani Milinga  
Insurance Management System  
Ruvuma, Tanzania  
2026

## License

Academic Use - TIRA Compliant Demo System

## Conclusion

This project is a practical demonstration of a small-scale insurance management platform tailored to the Tanzanian regulatory environment. It can be used as a foundation for a more complete commercial system, with further expansion into billing, notifications, document signing, and integration with external insurance infrastructure.
