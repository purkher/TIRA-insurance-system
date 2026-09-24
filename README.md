TIRA Insurance Management System - Tanzania


A complete Insurance Management System compliant with Tanzania Insurance Regulatory Authority (TIRA) for small insurance operations. Built with Flask to automate policy issuance, claims handling, and regulatory reporting.


Features Implemented
- **Role-Based Access Control:** Admin (full access), Agent (policies & claims), Customer (view & claim)
- **Policy Holder Management:** Full Name, NIDA 20-digit validation, Phone (255), Email, Address
- **Policy Management:** Auto Policy Number POL-YYYY-XXX, Premium auto-calc 5% of sum insured, Types: Motor, Life, Health, Property
- **Claims Management:** Submit, Approve, Reject workflow, Auto Claim Number CLM-YYYY-XXX
- **Dashboard Analytics:** Total Policies, Holders, Premiums, Claims with Chart.js visualization
- **TIRA Reports:** Compliance report, Premium collection, Claims ratio, Export-ready tables
- **KYC Compliance:** Document upload (NIDA Card, Driving License, Passport)
- **Security:** Password hashing (Werkzeug), Flask-Login, Input validation


Tech Stack
- Backend: Python 3 + Flask
- Database: SQLAlchemy + SQLite (insurance.db)
- Authentication: Flask-Login + Werkzeug Security
- Frontend: Bootstrap 5 + Chart.js + Jinja2 Templates


Project Structure
insurance_system/
│
├── http://app.py                  # Main Flask application (all routes & models)
├── http://insurance.db            # SQLite Database (auto-created on first run)
├── http://README.md               # Project documentation
│
├── templates/
│   ├── http://base.html           # Main layout, Navbar, Sidebar, Flash messages
│   ├── http://login.html          # Login form
│   ├── http://register.html       # User registration (role selection)
│   ├── http://dashboard.html      # Dashboard with stats & http://Chart.js
│   ├── http://holders.html        # List of Policy Holders
│   ├── add_holder.html     # Add new Holder with NIDA validation
│   ├── http://policies.html       # List of Policies
│   ├── add_policy.html     # Add Policy with auto calculation
│   ├── http://claims.html         # List, Approve/Reject Claims
│   ├── add_claim.html      # Submit new Claim form
│   ├── http://reports.html        # TIRA Compliance Reports
│   └── kyc_upload.html     # KYC document upload
│
├── static/
│   ├── css/
│   │   └── http://style.css       # Custom styles (optional)
│   ├── js/
│   │   └── http://chart.js        # Dashboard charts logic
│   └── uploads/            # Folder for uploaded KYC documents
│
└── venv/                   # Virtual environment (optional)


Installation & Run


1. Install dependencies:
```bash
pip install flask flask-sqlalchemy flask-login
2. Run the app:
python app.py
3. Open in browser:
http://127.0.0.1:5000
Default Accounts
Database auto-creates on first run:
Username        Password        Role        Access
admin        admin123        Admin        Full system
agent1        agent123        Agent        Policies & Claims
customer1        customer123        Customer        View & Submit Claims
Workflow Test (Demo Steps)
1. Login as `admin / admin123`
2. Add Policy Holder: Imani Milinga, NIDA: 19980101234567890123
3. Add Policy: Select holder, Sum 20,000,000 -> Premium auto 1,000,000
4. Logout -> Register as new Customer -> Login
5. Submit Claim: Select policy, Amount, Reason
6. Logout -> Login as Admin -> Manage Claims -> Approve
7. Check Reports & Dashboard


Compliance Notes (TIRA)
- NIDA validation: 20 digits regex `^\d{20}$`
- Premium: 5% of sum insured (TIRA minimum rate)
- Phone: Tanzania format +255 or 0xxx
- Policy Number: POL-YYYY-XXX unique
- Dates stored UTC, displayed YYYY-MM-DD


Future Improvements
- M-Pesa / Tigo Pesa payment integration
- PDF Policy Certificate generation
- SMS notification via Beem Africa
- TIRA API integration for real compliance


Author
imani milinga - Insurance Management System
Ruvuma, Tanzania - 2026


License
Academic Use - TIRA Compliant Demo System