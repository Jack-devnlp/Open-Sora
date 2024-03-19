num_frames = 64
frame_interval = 2 # should be 3
image_size = (256, 256)

# Define dataset
root = None
data_path = "CSV_PATH"
use_image_transform = False
num_workers = 4

# Define acceleration
dtype = "bf16"
grad_checkpoint = True
plugin = "zero2"
sp_size = 1

# Define model
model = dict(
    type="STDiT2-XL/2", # new model
    space_scale=0.5, # 256/512, base = 512
    time_scale=1.0, # base = 64 * 2
    from_pretrained="PixArt-XL-2-1024-MS.pth",
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=128,
)
text_encoder = dict(
    type="t5",
    from_pretrained="./pretrained_models/t5_ckpts",
    model_max_length=120,
    shardformer=True,
)
scheduler = dict(
    type="iddpm",
    timestep_respacing="",
)

# Others
seed = 42
outputs = "outputs"
wandb = False

epochs = 1000
log_every = 10
ckpt_every = 250
load = None

batch_size = 16
lr = 2e-5
grad_clip = 1.0
