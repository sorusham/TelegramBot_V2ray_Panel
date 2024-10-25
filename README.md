<h1 align="center">Telegram Bot for v2ray Panel</h1>

<h2>Overview</h2>
<p>This is a Python-based <strong>Telegram bot</strong> designed to connect to <strong>v2ray panels</strong>. It allows users to load and retrieve their information easily. By entering an email in Telegram, users can access specific details about their systems, streamlining user management.</p>

<h2>Features</h2>
<ul>
    <li>🔍 <strong>Search by Email</strong>: Retrieve system information using the user's email address.</li>
    <li>🔗 <strong>v2ray Integration</strong>: Seamlessly connects to v2ray panels for effective user management.</li>
    <li>🐍 <strong>Python-Based</strong>: Built using Python for easy customization and scalability.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
    <li>✅ <strong>Python 3.7+</strong> installed on your machine.</li>
    <li>🔑 <strong>Telegram Bot API Token</strong> (get one from <a href="https://core.telegram.org/bots#botfather">BotFather</a>).</li>
</ul>

<h3>Configuration</h3>
<p>Before running the bot, you need to configure it with your v2ray panel credentials and Telegram bot token:</p>

<h4>Step 1: Set v2ray Panel Credentials</h4>
<p>Open the <code>Login.py</code> file and enter your v2ray panel credentials:</p>
<pre>
<code>
<h2>Multi-Panel Support</h2>
<p>This bot supports multiple v2ray panels. You can add panel information in the form of a dictionary. Each panel's credentials can be stored in a list for easy management.</p>

<h3>Example Structure</h3>
<p>The panels can be organized like this:</p>
<pre>
<code>
panels = [
    {
        "url": "http://panel1.example.com"
        "username": "user1",
        "password": "pass1",
    },
    {
        "url": "http://panel2.example.com"
        "username": "user2",
        "password": "pass2",   
    }
]
</code>
</pre>
<p>This structure allows easy access to multiple panels and supports dynamic querying based on user input.</p>


<h4>Step 2: Add Telegram Bot Token</h4>
<p>In the <code>TelegramBot.py</code> file, insert your Telegram bot token:</p>
<pre>
<code>
# Example
TOKEN = "your_telegram_bot_token"
</code>
</pre>

<h3>Installation</h3>
<p>Follow these steps to set up the project locally:</p>
<pre>
<code>
# Clone the repository
git clone https://github.com/SorushPro/TelegramBot_V2ray_Panel.git
cd TelegramBot_V2ray_Panel

# Install required packages
pip install -r requirements.txt
</code>
</pre>

<h2>Usage</h2>
<p>To run the bot, execute the following command:</p>
<pre>
<code>
python TelegramBot.py
</code>
</pre>
<p>In Telegram, you can search for users by entering their email addresses to get the corresponding system details.</p>

<h3>Example Query</h3>
<pre>
<code>
user@example.com
</code>
</pre>


