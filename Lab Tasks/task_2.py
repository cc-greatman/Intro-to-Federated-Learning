def aggregate_models(client_models):
    return sum(client_models) / len(client_models)


# Models returned by 3 clients after local training
client_models = [2.0, 4.0, 6.0]

# Server aggregates their models
global_model = aggregate_models(client_models)

print(f"New Global Model: {global_model:.0f}")