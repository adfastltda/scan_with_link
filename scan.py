import socket 
import ipaddress 
import concurrent.futures 
import os 
import requests

def scan_port(ip, port): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port)) 
    sock.close() 
    if result == 0: 
        return ip 
 
def parse_ip_range(ip_range): 
    ip_list = [] 
    if "-" in ip_range: 
        start, end = ip_range.split("-") 
        start_ip = ipaddress.IPv4Address(start.strip()) 
        end_ip = ipaddress.IPv4Address(end.strip()) 
        ip_list = [str(ipaddress.IPv4Address(ip)) for ip in range(int(start_ip), int(end_ip) + 1)] 
    else: 
        try: 
            ip_net = ipaddress.IPv4Network(ip_range) 
            ip_list.extend(str(ip) for ip in ip_net) 
        except ipaddress.AddressValueError: 
            print(f"Formato inválido: {ip_range}") 
    return ip_list 
 
def main(): 

    # Menu
    while True:
        print("Menu:")
        print("1. Cloudflare Scan Lento")
        print("2. Cloudfront Scan Lento")
        print("3. Cloudflare Scan Rapido")
        print("4. Cloudfront Scan Rapido")
        try:
            option = int(input("Enter your option (1-4): "))
            if option not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Get IP ranges and CIDR from the link
    if option == 1:
        url = "https://bitbin.it/ADRgwo4o/raw/"
    elif option == 2:
        url = "https://bitbin.it/ZG86YD7p/raw/" # Change this URL
    elif option == 3:
        url = "https://bitbin.it/ADRgwo4o/raw/" # Change this URL
    else:
        url = "https://bitbin.it/7P5WoQbn/raw/" # Change this URL

    response = requests.get(url)
    if response.status_code == 200:
        ip_ranges = response.text.splitlines()
    else:
        print("Error getting IP ranges and CIDR from the link")
        return

    try: 
        print(f"\nDESLIGUE O WI-FI\n") 
        num_threads = int(input("Digite o número de threads (padrão: 100): ") or 100) 
    except ValueError: 
        print("Entrada inválida. Usando 100 threads por padrão.") 
        num_threads = 100 
 
    for ip_range in ip_ranges: 
        ip_list = parse_ip_range(ip_range) 
 
        print(f"\nTestando IPs no ranger: {ip_range}...\n") 
        open_ips = [] 
 
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor: 
            futures = [executor.submit(scan_port, ip, 443) for ip in ip_list] 
 
            for future in concurrent.futures.as_completed(futures): 
                result = future.result() 
                if result: 
                    open_ips.append(result) 

        if open_ips: 
            print("Sucesso:") 
            for ip in open_ips: 
                print(ip) 
 
        confirm = input("\nDeseja continuar? (s/n): ") 
        if confirm.lower() != 's': 
            break 

        os.system('clear' if os.name == 'posix' else 'cls')  # Limpar a tela 

if __name__ == "__main__": 
    main()
