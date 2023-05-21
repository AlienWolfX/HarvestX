import socket
import subprocess


def check_ip(ip):
    try:
        socket.setdefaulttimeout(1)  # Set a timeout of 1 second
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, 80))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    except socket.error:
        return False


def main():
    alive_ips = []
    dead_ips = []

    for i in range(13):  # IP RANGE
        for j in range(256):  # IP RANGE
            ip = "172.18." + str(i) + "." + str(j + 1)
            if check_ip(ip):
                alive_ips.append(ip)
                print(f"IP {ip} is alive")
            else:
                dead_ips.append(ip)
                print(f"IP {ip} is dead")

    with open("mini_alive.txt", "w") as alive_file:
        alive_file.write("\n".join(alive_ips))

    with open("dead.txt", "w") as dead_file:
        dead_file.write("\n".join(dead_ips))

    print("Results saved in mini_alive.txt and dead.txt.")


if __name__ == "__main__":
    #main()

    #Execute Vulnerabilities
    #subprocess.run(["python3", "mini_htppd_vulnerability.py"])
    subprocess.run(["python3", "boa_httpd_vulnerability.py"])

