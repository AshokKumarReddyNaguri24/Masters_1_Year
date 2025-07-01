import socket

def run_client():
    #setting up client TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #server details. localhost
    server_ip = '127.0.0.1'
    server_port = 8888

    #connecting client to server using server IP and port
    client.connect((server_ip, server_port))

    #receiving and printing 'Hello there!' from server
    print(client.recv(1024).decode('utf-8'))

    #sending 'HELLO [name]\n' to server
    client.send(f"HELLO vedulapurapu.t\n".encode('utf-8'))

    #running an infinite loop to receive and answer random number of MATH questions
    
    while True:
        #getting each MATH question details and displaying it on the screen
        question = client.recv(1024).decode('utf-8')

        #break the infinite loop if 'MATH' not found in the question
        if (question[0:4] != 'MATH'):
            print(question)
            break
        else:
            #if it 'MATH' is found in quetion, then using eval() to calculate rest of the question
            answer = int(eval(question[5:]))
            #sending the answer in 'ANSWER [answer]\n' format
            client.send(f'ANSWER {answer}\n'.encode('utf-8'))

    client.close()

run_client()


