# Three IoT temperature sensors learning to predict a typical temperature
# Create the clients

client_data = {
    "Client 1":[20, 21, 19],
    "Client 2":[25, 26, 24],
    "Client 3":[29, 30, 31] 
}

def local_training(data, global_w, lr=0.1, epochs=5):
    w = global_w

    for epoch in range(epochs):
        for temperature in data:
            gradient = 2 * (w - temperature)
            w = w - lr * gradient

    return w

global_w = 20.0

for round_num in range(3):
    client_models = []

    for client_name, data in client_data.items():
        updated_w = local_training(data, global_w)
        client_models.append(updated_w)

        #Server aggregates the client models
        global_w = sum(client_models) / len(client_models)

        print("Server Model:", round(global_w, 2))
        print()