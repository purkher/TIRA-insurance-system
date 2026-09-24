from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tira-secret-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insurance.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- MODELS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='Customer')

class PolicyHolder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    nida = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(50), unique=True)
    holder_id = db.Column(db.Integer, db.ForeignKey('policy_holder.id'), nullable=False)
    holder = db.relationship('PolicyHolder', backref='policies')
    type = db.Column(db.String(50))
    premium_amount = db.Column(db.Float)
    coverage_amount = db.Column(db.Float, default=10000000)
    start_date = db.Column(db.Date, default=lambda: datetime.utcnow().date())
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='Active')

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_number = db.Column(db.String(50), unique=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)
    policy = db.relationship('Policy', backref='claims')
    amount_claimed = db.Column(db.Float)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    submitted_date = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def gen_policy_number(p_type):
    count = Policy.query.count() + 1
    return f"TIRA/{p_type[:3].upper()}/{datetime.now().year}/{count:04d}"

def gen_claim_number():
    count = Claim.query.count() + 1
    return f"CLM/{datetime.now().year}/{count:05d}"

# --- ROUTES ---
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash('Username exists!')
            return redirect(url_for('register'))
        user = User(username=request.form['username'], email=request.form['email'],
                    password_hash=generate_password_hash(request.form['password']),
                    role=request.form.get('role', 'Customer'))
        db.session.add(user)
        db.session.commit()
        flash('Registered! Login now')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    for p in Policy.query.all():
        if p.end_date and datetime.utcnow().date() > p.end_date:
            p.status = 'Expired'
    db.session.commit()
    return render_template('dashboard.html',
        total_policies=Policy.query.count(),
        total_claims=Claim.query.count(),
        pending_claims=Claim.query.filter_by(status='Pending').count(),
        total_premium=db.session.query(db.func.sum(Policy.premium_amount)).scalar() or 0)

@app.route('/holders/add', methods=['GET','POST'])
@login_required
def add_holder():
    if current_user.role == 'Customer':
        flash('Access Denied: Customers cannot add holders')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        # NIDA Validation
        nida = request.form['nida'].replace('-','').strip()
        if len(nida) != 20 or not nida.isdigit():
            flash('Invalid NIDA: Must be 20 digits!')
            return redirect(url_for('add_holder'))
        if PolicyHolder.query.filter_by(nida=request.form['nida']).first():
            flash('NIDA already exists!')
            return redirect(url_for('add_holder'))
        holder = PolicyHolder(full_name=request.form['full_name'], phone=request.form['phone'],
                              nida=request.form['nida'], email=request.form['email'], address=request.form.get('address',''))
        db.session.add(holder)
        db.session.commit()
        flash('Holder added successfully!')
        return redirect(url_for('dashboard'))
    return render_template('add_holder.html')

@app.route('/policies/add', methods=['GET','POST'])
@login_required
def add_policy():
    if current_user.role == 'Customer':
        flash('Access Denied')
        return redirect(url_for('dashboard'))
    holders = PolicyHolder.query.all()
    if not holders:
        flash('Add a Holder first!')
        return redirect(url_for('add_holder'))
    if request.method == 'POST':
        policy = Policy(policy_number=request.form['policy_number'] or gen_policy_number(request.form['type']),
                        holder_id=request.form['holder_id'], type=request.form['type'],
                        premium_amount=float(request.form['premium']),
                        coverage_amount=float(request.form.get('coverage', 10000000)),
                        start_date=datetime.utcnow().date(),
                        end_date=datetime.utcnow().date() + timedelta(days=365))
        db.session.add(policy)
        db.session.commit()
        flash('Policy created!')
        return redirect(url_for('policies_list'))
    return render_template('add_policy.html', holders=holders)

@app.route('/policies')
@login_required
def policies_list():
    return render_template('policies.html', policies=Policy.query.all())

@app.route('/claims/add', methods=['GET','POST'])
@login_required
def add_claim():
    policies = Policy.query.all()
    if request.method == 'POST':
        claim = Claim(claim_number=gen_claim_number(), policy_id=request.form['policy_id'],
                      amount_claimed=float(request.form['amount']),
                      description=request.form['description'])
        db.session.add(claim)
        db.session.commit()
        flash('Claim submitted! Waiting for approval.')
        return redirect(url_for('claims_list'))
    return render_template('add_claim.html', policies=policies)

@app.route('/claims')
@login_required
def claims_list():
    if current_user.role == 'Customer':
        # Customer sees only claims for policies? For demo, show all for now
        claims = Claim.query.order_by(Claim.submitted_date.desc()).all()
    else:
        claims = Claim.query.order_by(Claim.submitted_date.desc()).all()
    return render_template('claims.html', claims=claims)

@app.route('/claims/<int:id>/approve')
@login_required
def approve_claim(id):
    if current_user.role == 'Customer':
        flash('Access Denied')
        return redirect(url_for('dashboard'))
    c = Claim.query.get_or_404(id)
    c.status = 'Approved'
    db.session.commit()
    flash(f'Claim {c.claim_number} Approved!')
    return redirect(url_for('claims_list'))

@app.route('/claims/<int:id>/reject')
@login_required
def reject_claim(id):
    if current_user.role == 'Customer':
        flash('Access Denied')
        return redirect(url_for('dashboard'))
    c = Claim.query.get_or_404(id)
    c.status = 'Rejected'
    db.session.commit()
    flash(f'Claim {c.claim_number} Rejected!')
    return redirect(url_for('claims_list'))

@app.route('/reports')
@login_required
def reports():
    if current_user.role == 'Customer':
        flash('Access Denied: Reports for Admin only')
        return redirect(url_for('dashboard'))
    total_policies = Policy.query.count()
    total_claims = Claim.query.count()
    pending = Claim.query.filter_by(status='Pending').count()
    approved = Claim.query.filter_by(status='Approved').count()
    rejected = Claim.query.filter_by(status='Rejected').count()
    total_premium = db.session.query(db.func.sum(Policy.premium_amount)).scalar() or 0
    total_claim_amount = db.session.query(db.func.sum(Claim.amount_claimed)).scalar() or 0
    return render_template('reports.html', total_policies=total_policies, total_claims=total_claims,
                           pending=pending, approved=approved, rejected=rejected,
                           total_premium=total_premium, total_claim_amount=total_claim_amount,
                           motor=Policy.query.filter_by(type='Motor').count(),
                           health=Policy.query.filter_by(type='Health').count(),
                           life=Policy.query.filter_by(type='Life').count())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@tira.go.tz',
                         password_hash=generate_password_hash('admin123'), role='Admin')
            db.session.add(admin)
            db.session.commit()
            print("Default admin: admin / admin123")
    app.run(debug=True)