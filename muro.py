import os
import sys
import time
import random
import requests
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f'''{Fore.CYAN}
███╗   ███╗██╗   ██╗██████╗  ██████╗ 
████╗ ████║██║   ██║██╔══██╗██╔═══██╗
██╔████╔██║██║   ██║██████╔╝██║   ██║
██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║
██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
{Fore.RED}╔═════════════════════════════════════════╗
║  {Fore.YELLOW}[Developer]{Fore.CYAN} Your Name                   {Fore.RED}║
║  {Fore.YELLOW}[Version]{Fore.CYAN}   2.0.0                      {Fore.RED}║
║  {Fore.YELLOW}[GitHub]{Fore.CYAN}    github.com/your-username   {Fore.RED}║
╚═════════════════════════════════════════╝
{Fore.GREEN}[+] Advanced Social Media Username Checker Tool
{Fore.YELLOW}[+] Last Updated: {datetime.now().strftime('%Y-%m-%d')}{Style.RESET_ALL}
'''
    print(banner)

def print_menu():
    menu = f'''
{Fore.CYAN}┌──────────────── SOCIAL PLATFORMS ────────────────┐
{Fore.CYAN}│                                                  │
{Fore.CYAN}│  [{Fore.WHITE}01{Fore.CYAN}] Instagram     [{Fore.WHITE}02{Fore.CYAN}] TikTok         │
{Fore.CYAN}│  [{Fore.WHITE}03{Fore.CYAN}] Twitter       [{Fore.WHITE}04{Fore.CYAN}] Facebook       │
{Fore.CYAN}│  [{Fore.WHITE}05{Fore.CYAN}] Snapchat      [{Fore.WHITE}06{Fore.CYAN}] LinkedIn       │
{Fore.CYAN}│  [{Fore.WHITE}07{Fore.CYAN}] Pinterest     [{Fore.WHITE}08{Fore.CYAN}] Reddit         │
{Fore.CYAN}│  [{Fore.WHITE}09{Fore.CYAN}] YouTube       [{Fore.WHITE}10{Fore.CYAN}] Twitch         │
{Fore.CYAN}│  [{Fore.WHITE}11{Fore.CYAN}] Discord       [{Fore.WHITE}12{Fore.CYAN}] Telegram       │
{Fore.CYAN}│                                                  │
{Fore.CYAN}└──────────────── TOOL OPTIONS ──────────────────┘
{Fore.CYAN}│                                                  │
{Fore.CYAN}│  [{Fore.WHITE}13{Fore.CYAN}] Search Available Usernames                │
{Fore.CYAN}│  [{Fore.WHITE}14{Fore.CYAN}] Find Similar Usernames                   │
{Fore.CYAN}│  [{Fore.WHITE}15{Fore.CYAN}] Export Results                           │
{Fore.CYAN}│  [{Fore.WHITE}00{Fore.CYAN}] Exit Tool                                │
{Fore.CYAN}│                                                  │
{Fore.CYAN}└──────────────────────────────────────────────────┘

{Fore.YELLOW}[*] Select an option: {Style.RESET_ALL}'''
    print(menu)

def fancy_loading():
    loading_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    loading_colors = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]
    
    for i in range(20):
        color = random.choice(loading_colors)
        char = loading_chars[i % len(loading_chars)]
        sys.stdout.write(f'\r{color}Processing {char} ')
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def check_username(platform, username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    platform_urls = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Telegram": f"https://t.me/{username}"
    }

    try:
        url = platform_urls.get(platform)
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        if platform == "Instagram":
            url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
            response = requests.get(url, headers=headers)
            return response.status_code != 200
        else:
            return response.status_code == 404

    except requests.exceptions.RequestException:
        return None

def generate_usernames(length=3):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    usernames = set()
    
    while len(usernames) < 5:
        username = ''.join(random.choice(chars) for _ in range(length))
        usernames.add(username)
    
    return list(usernames)

def find_similar_usernames(username):
    similar = []
    # Add numbers
    similar.extend([f"{username}{i}" for i in range(5)])
    # Add underscores
    similar.extend([f"_{username}", f"{username}_"])
    # Replace letters
    replacements = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5'}
    for old, new in replacements.items():
        if old in username:
            similar.append(username.replace(old, new))
    
    return similar

def check_available_usernames(platform):
    print(f"\n{Fore.YELLOW}[*] Searching for available usernames...{Style.RESET_ALL}")
    available = []
    usernames = generate_usernames()
    
    for username in usernames:
        print(f"\r{Fore.CYAN}[*] Checking: {username}", end='')
        result = check_username(platform, username)
        
        if result:
            available.append(username)
            print(f"\n{Fore.GREEN}[+] Found available: {username}{Style.RESET_ALL}")
        
        time.sleep(1)  # Avoid rate limiting
    
    return available

def export_results(results, filename="results.txt"):
    try:
        with open(filename, 'w') as f:
            f.write(f"MURO Tool Results - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for result in results:
                f.write(f"{result}\n")
        return True
    except:
        return False

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        choice = input().strip()
        
        if choice == "00":
            print(f"\n{Fore.RED}[!] Exiting MURO Tool...{Style.RESET_ALL}")
            sys.exit(0)
            
        elif choice in [str(i).zfill(2) for i in range(1, 13)]:
            platforms = {
                "01": "Instagram", "02": "TikTok", "03": "Twitter",
                "04": "Facebook", "05": "Snapchat", "06": "LinkedIn",
                "07": "Pinterest", "08": "Reddit", "09": "YouTube",
                "10": "Twitch", "11": "Discord", "12": "Telegram"
            }
            
            username = input(f"\n{Fore.YELLOW}[*] Enter username to check: {Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}[*] Checking {username} on {platforms[choice]}...")
            fancy_loading()
            
            result = check_username(platforms[choice], username)
            if result is not None:
                status = f"{Fore.GREEN}Available" if result else f"{Fore.RED}Taken"
                print(f"\n{Fore.CYAN}[Result] {status} on {platforms[choice]}{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}[!] Error checking username{Style.RESET_ALL}")
            
        elif choice == "13":
            platform = input(f"\n{Fore.YELLOW}[*] Enter platform to search (e.g., Instagram): {Style.RESET_ALL}")
            available = check_available_usernames(platform)
            
            if available:
                print(f"\n{Fore.GREEN}[+] Available usernames:{Style.RESET_ALL}")
                for username in available:
                    print(f"{Fore.CYAN}[*] {username}{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}[!] No available usernames found{Style.RESET_ALL}")
                
        elif choice == "14":
            username = input(f"\n{Fore.YELLOW}[*] Enter username to find similar: {Style.RESET_ALL}")
            platform = input(f"{Fore.YELLOW}[*] Enter platform to check: {Style.RESET_ALL}")
            
            similar = find_similar_usernames(username)
            print(f"\n{Fore.CYAN}[*] Checking similar usernames...{Style.RESET_ALL}")
            
            for similar_username in similar:
                result = check_username(platform, similar_username)
                if result:
                    print(f"{Fore.GREEN}[+] Available: {similar_username}{Style.RESET_ALL}")
                time.sleep(1)
                
        elif choice == "15":
            username = input(f"\n{Fore.YELLOW}[*] Enter username to check all platforms: {Style.RESET_ALL}")
            results = []
            
            for platform in ["Instagram", "TikTok", "Twitter", "Facebook", "Snapchat"]:
                result = check_username(platform, username)
                status = "Available" if result else "Taken"
                results.append(f"{platform}: {status}")
            
            if export_results(results, f"muro_results_{username}.txt"):
                print(f"\n{Fore.GREEN}[+] Results exported successfully{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}[!] Error exporting results{Style.RESET_ALL}")
            
        else:
            print(f"\n{Fore.RED}[!] Invalid option!{Style.RESET_ALL}")
            
        input(f"\n{Fore.GREEN}[*] Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Tool terminated by user{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)
