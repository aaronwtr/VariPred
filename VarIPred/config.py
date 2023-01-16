import torch

SEED = 2022

# ==================== Device ====================================
print()
print()
print()
# GPU = 1
# device = torch.device("cuda:{}".format(GPU) if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")
    torch.manual_seed(SEED)
    torch.cuda.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)
    print(f'There are {torch.cuda.device_count()} GPU(s) available.')
    print('Device name:', torch.cuda.get_device_name(0))
# elif torch.has_mps: # if run the model on MAC
#     torch.cuda.manual_seed(2020)
#     device = torch.device('mps')
#     print('Device name: MPS')
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")


# ==================== Embeds path ====================================


esm_storage_path = './example/embeds'