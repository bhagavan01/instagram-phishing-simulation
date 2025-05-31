# Instagram Phishing Simulation (Educational Use Only)

> ⚠️ **Disclaimer:** This project is for educational purposes only to demonstrate phishing concepts and security awareness. **Do NOT use it for malicious activities.**

---

## Overview

This is a simple Flask web application simulating an Instagram login page.  
It captures entered credentials (username and password) and saves them securely in a file for educational and testing purposes.  
After submission, it redirects users to the official Instagram login page.

---

## Features

- Clean, Instagram-like login page UI
- Saves username and password with timestamp and client IP in a log file
- Redirects user to the real Instagram login after form submission
- Logging for all captured credentials with timestamps

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/instagram-phishing-simulation.git
   cd instagram-phishing-simulation
2.Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.Run the app:
```bash
python app.py
```
Usage
Enter any username and password on the login page.

Credentials will be saved to data/user_credentials.txt along with timestamp and IP address.

You will be redirected to the official Instagram login page.

Important Notes
This project is meant for learning and awareness only.

Use responsibly and ethically.

Do not deploy this app publicly without explicit consent from users.

This app is NOT secure for production use.

The saved credentials file contains sensitive data; handle it carefully.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Bhagavan -https://github.com/bhagavan01
