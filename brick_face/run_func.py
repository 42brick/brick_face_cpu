import numpy as np
import dnnlib
import torch
import legacy
import os

from style_mixing import generate_style_mix
from projector import run_projection


async def run_model(col_start, col_end, r=5, test_mode=False, num_steps=1000, seed=2022, network_pkl='../model/network-snapshot-005000.pkl'):
    output_dir = './output/result'

    np.random.seed(seed)
    torch.manual_seed(seed)

    # Load networks.
    print('Loading networks from "%s"...' % network_pkl)
    device = torch.device('cuda')

    with dnnlib.util.open_url(network_pkl) as fp:
        G = legacy.load_network_pkl(fp)['G_ema'].requires_grad_(
            False).to(device)  # type: ignore

    # Image1, 2에 대한 latent vector를 생성
    w_dict = {}
    testfile_length = len(os.listdir('./test_images'))
    for i in range(1, testfile_length+1):
        print(f"이미지를 생성합니다. ===> Input : {i}")  # P
        projected_w = run_projection(
            G=G,
            target_fname=f'./test_images/test{i}.jpg',
            outdir=output_dir,
            save_video=False,  # if Test Mode, Do not Save Video
            seed=seed,  # P
            num_steps=num_steps,
            device=device
        )
        w_dict[f"Image{i}"] = projected_w

    # Style Mixing
    if col_start < r:
        r = col_start-1
        print("RANGE가 자동으로 조정됩니다.")
    test_num = 3

    if test_mode == True:
        for i in range(col_start, col_end):
            generate_style_mix(
                G=G,
                w_dict=w_dict,
                col_start=i-r,
                col_end=i,
                test_num=test_num,
                noise_mode='const',
                outdir=output_dir
            )
            test_num += 1
    else:
        # 파라미터 4~8이 적당해보임.(7~8섞으면 피부색 합성)
        generate_style_mix(
            G=G,
            w_dict=w_dict,
            col_start=col_start,
            col_end=col_end,
            test_num=test_num,
            noise_mode='const',
            outdir=output_dir
        )
