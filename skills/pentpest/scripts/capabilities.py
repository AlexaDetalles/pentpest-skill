"""List installed CLI capabilities; do not install or start anything."""
import shutil,json
names=['python3','node','uv','nmap','httpx','subfinder','nuclei','ffuf','katana','dig','whois','wafw00f','testssl.sh','nikto','wpscan','arjun','gau','waybackurls','subjack','feroxbuster','amass','masscan','rustscan','gowitness','semgrep','cppcheck','php','composer','jq','git','gh','sqlmap','curl']
print(json.dumps({'executables':{n:shutil.which(n) for n in names},'note':'Presence on PATH is not version verification; httpx may be the Python HTTP client rather than ProjectDiscovery. MCP connections require separate discovery.'},indent=2))
