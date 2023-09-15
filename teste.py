import paramiko

hostname = 'localhost'
port = 22
username = 'desktop-jvpg9gv/caio'
private_key_path = 'C:/Users/Caio/PycharmProjects/cromai/keys/id_rsa.rsa'

# Criar uma conexão SSH com chave
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Carregar a chave privada
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Conectar usando a chave privada
ssh_client.connect(hostname, port, username, pkey=private_key)

# Executar um comando para obter o uso da CPU (por exemplo, 'top')
stdin, stdout, stderr = ssh_client.exec_command('top -n 1')

# Ler a saída do comando
output = stdout.read().decode('utf-8')

# Fechar a conexão SSH
ssh_client.close()

print(output)

