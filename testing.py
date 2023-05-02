from run_nerf_helpers import NeRFSmall, NeRF
import torch

x = NeRFSmall(num_layers=2,
                        hidden_dim=64,
                        geo_feat_dim=15,
                        num_layers_color=3,
                        hidden_dim_color=64,
                        input_ch=32, input_ch_views=16)
print("hi")
print(x)


# (n, 48) - > (n, 4)
# class NeRFSmallConv(nn.Module):
#     def __init__(self,
#                  num_layers=3,
#                  hidden_dim=64,
#                  geo_feat_dim=15,
#                  num_layers_color=4,
#                  hidden_dim_color=64,
#                  input_ch=3, input_ch_views=3,
#                  ):
#         super(NeRFSmall, self).__init__()