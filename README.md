# ☁️ DigitalOcean Droplet IP Finder

A Python automation tool that creates multiple cloud droplets and searches for a specific IP range.

The script repeatedly creates **DigitalOcean droplets**, checks their assigned public IP addresses, and determines if they fall within a desired CIDR range. When a matching IP is found, it is saved and the process stops.

This can be useful for **cloud infrastructure experiments, networking research, and automated IP allocation testing**.

---

# ✨ Features

* ☁️ Automatically creates multiple **DigitalOcean droplets**
* 🔍 Checks whether droplet IPs fall within a **target CIDR range**
* ⚡ Fully automated droplet creation and deletion loop
* 🧵 Handles multiple droplets simultaneously
* 💾 Saves matching IPs to `live.txt`
* 🗑 Includes a script to **delete droplets automatically**

---

# 📂 Files

```
digitalocean-ip-finder/
│
├── create.py
├── delete.py
├── live.txt
└── README.md
```

---

# 🧰 Requirements

* Python **3.7+**

Python packages:

```
python-digitalocean
requests
```

Install dependencies:

```
pip install python-digitalocean requests
```

---

# 🔑 Setup

Create a **DigitalOcean API token** from your account dashboard.

Set it as an environment variable:

```
export DO_TOKEN=your_api_token
```

Update the script to use the token:

```python
token = os.getenv("DO_TOKEN")
```

---

# 🚀 Usage

### 1️⃣ Create droplets and search for IPs

```
python create.py
```

The script will:

1. Create multiple droplets
2. Wait for them to become active
3. Check their public IP addresses
4. Compare them against the target CIDR range
5. Save a matching IP to `live.txt`

Example output:

```
Droplet: droplet-1, IP: 137.184.137.22
Droplet: droplet-2, IP: 137.184.138.10
Found valid IP: 137.184.138.10
```

---

### 2️⃣ Delete droplets

To remove droplets created by the script:

```
python delete.py
```

Example output:

```
Successfully deleted droplet id: 123456789
Successfully deleted droplet id: 123456790
```

---

# 📊 How It Works

1. Create droplets using the **DigitalOcean API**
2. Wait until each droplet becomes active
3. Retrieve the public IP address
4. Check if the IP belongs to a target CIDR range
5. Save valid IPs
6. Delete droplets and repeat if no match is found

---

# ⚠️ Disclaimer

This tool is intended for:

* Cloud automation experiments
* Networking research
* Educational purposes

Always ensure you understand **cloud provider pricing and API limits** before running automated infrastructure scripts.

---

# 🤝 Contributions

Contributions are welcome.

Possible improvements:

* Support for multiple regions
* Faster droplet provisioning
* Automatic droplet tagging
* Multi-threaded droplet management
* Improved error handling
* Proxy / API rate-limit handling

---

# 🚀 Future Updates

Planned improvements:

* 🌍 Multi-region droplet creation
* ⚡ Parallel droplet creation
* 📊 Real-time droplet status dashboard
* 🔐 Secure environment variable token handling
* 📁 JSON export of results
* 🧠 Automatic CIDR range configuration
* 🧵 Improved concurrency

---

# 👨‍💻 Author

Krainium
GitHub: https://github.com/krainium

---

# 📜 License

MIT License
