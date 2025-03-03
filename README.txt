Usage: train.py [OPTIONS]

  Train a GAN using the techniques described in the paper "Alias-Free
  Generative Adversarial Networks".

  Examples:

  # Train StyleGAN3-T for AFHQv2 using 8 GPUs.
  python train.py --outdir=~/training-runs --cfg=stylegan3-t --data=~/datasets/afhqv2-512x512.zip \
      --gpus=8 --batch=32 --gamma=8.2 --mirror=1

  # Fine-tune StyleGAN3-R for MetFaces-U using 1 GPU, starting from the pre-trained FFHQ-U pickle.
  python train.py --outdir=~/training-runs --cfg=stylegan3-r --data=~/datasets/metfacesu-1024x1024.zip \
      --gpus=8 --batch=32 --gamma=6.6 --mirror=1 --kimg=5000 --snap=5 \
      --resume=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhqu-1024x1024.pkl

  # Train StyleGAN2 for FFHQ at 1024x1024 resolution using 8 GPUs.
  python train.py --outdir=~/training-runs --cfg=stylegan2 --data=~/datasets/ffhq-1024x1024.zip \
      --gpus=8 --batch=32 --gamma=10 --mirror=1 --aug=noaug

Options:
  --outdir DIR                    Where to save the results  [required]
  --cfg [stylegan3-t|stylegan3-r|stylegan2]
                                  Base configuration  [required]
  --data [ZIP|DIR]                Training data  [required]
  --gpus INT                      Number of GPUs to use  [x>=1; required]
  --batch INT                     Total batch size  [x>=1; required]
  --gamma FLOAT                   R1 regularization weight  [x>=0; required]
  --cond BOOL                     Train conditional model  [default: False]
  --mirror BOOL                   Enable dataset x-flips  [default: False]
  --aug [noaug|ada|fixed]         Augmentation mode  [default: ada]
  --resume [PATH|URL]             Resume from given network pickle
  --freezed INT                   Freeze first layers of D  [default: 0; x>=0]
  --p FLOAT                       Probability for --aug=fixed  [default: 0.2;
                                  0<=x<=1]
  --target FLOAT                  Target value for --aug=ada  [default: 0.6;
                                  0<=x<=1]
  --batch-gpu INT                 Limit batch size per GPU  [x>=1]
  --cbase INT                     Capacity multiplier  [default: 32768; x>=1]
  --cmax INT                      Max. feature maps  [default: 512; x>=1]
  --glr FLOAT                     G learning rate  [default: varies]  [x>=0]
  --dlr FLOAT                     D learning rate  [default: 0.002; x>=0]
  --map-depth INT                 Mapping network depth  [default: varies]
                                  [x>=1]
  --mbstd-group INT               Minibatch std group size  [default: 4; x>=1]
  --desc STR                      String to include in result dir name
  --metrics [NAME|A,B,C|none]     Quality metrics  [default: fid50k_full]
  --kimg KIMG                     Total training duration  [default: 25000;
                                  x>=1]
  --tick KIMG                     How often to print progress  [default: 4;
                                  x>=1]
  --snap TICKS                    How often to save snapshots  [default: 50;
                                  x>=1]
  --seed INT                      Random seed  [default: 0; x>=0]
  --fp32 BOOL                     Disable mixed-precision  [default: False]
  --nobench BOOL                  Disable cuDNN benchmarking  [default: False]
  --workers INT                   DataLoader worker processes  [default: 3;
                                  x>=1]
  -n, --dry-run                   Print training options and exit
  --help                          Show this message and exit.