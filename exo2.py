import socket

# Create a socket connection
ConnexionAUnServeur = socket.socket()

# Connect to a server
host = raw_input("Entrez l'adresse IP du serveur FTP depuis le clavier : ")
port = 21
ConnexionAUnServeur.connect((host, port))  # Establish connection with the server

while True:
    recu = ""
    while True:
        recu += ConnexionAUnServeur.recv(2028)
        m = re.findall("\d\d\d ", recu)
        if len(m) != 0:
            break
    print(recu)
    commande = raw_input()
    ConnexionAUnServeur.send(commande + "\r\n")

ConnexionAUnServeur.close()
