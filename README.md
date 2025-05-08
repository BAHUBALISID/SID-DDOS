# SID DDOS - Powerful DDoS Testing Tool



🚀 About



SID DDOS is a high-performance Distributed Denial of Service (DDoS) testing tool for security professionals and ethical hackers. It is designed to test network resilience by simulating various DDoS attack techniques.



⚠️ Disclaimer: This tool is intended for educational and security testing purposes only. Unauthorized use against third-party networks is illegal and strictly prohibited. Use it responsibly.



📦 Installation



Linux (Kali, Ubuntu, Debian)



sudo apt update && sudo apt install python3 python3-pip -y

git clone https://github.com/BAHUBALISID/SID-DDOS.git

cd SID-DDOS

pip install -r requirements.txt



Windows



Install Python 3 from python.org.



Clone the repository:



git clone https://github.com/BAHUBALISID/SID-DDOS.git

cd sid-ddos



Install dependencies:



pip install -r requirements.txt



🚀 Usage



python3 sid.py \<target\_ip> \<port> \<attack\_method> \<time>



Example:



python3 sid.py 192.168.1.1 80 UDP 60



📌 Attack Methods:



UDP - UDP Flood Attack



TCP - TCP SYN Flood



HTTP - HTTP GET Flood



🔧 Features



✅ Multiple Attack Vectors (UDP, TCP, HTTP)

✅ Customizable Attack Duration

✅ Multi-threaded for High Performance

✅ Simple and Easy-to-Use CLI



⚠️ Legal Disclaimer



This tool is intended ONLY for network security testing and educational purposes. Using this tool without authorization is illegal. The developer is not responsible for any misuse or damage caused.



🔹 Use it responsibly!

