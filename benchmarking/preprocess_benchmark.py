import subprocess
import tqdm


def main():
    for i in tqdm.tqdm(range(30)):
        subprocess.call(
            [
                "python3",
                "-W",
                "ignore",
                "./preprocessing/save_dino_embed_video.py",
                "--config",
                "./config/preprocessing.yaml",
                "--data-path",
                f"./dataset/tapvid-davis/{i}",
            ]
        )


if __name__ == "__main__":
    main()
