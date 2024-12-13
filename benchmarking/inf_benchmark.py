import subprocess
import tqdm


def main():
    for i in tqdm.tqdm(range(30)):
        subprocess.call(
            [
                "python3",
                "-W",
                "ignore",
                "./inference_benchmark.py",
                "--config",
                "./config/train.yaml",
                "--data-path",
                f"./dataset/tapvid-davis/{i}",
                "--benchmark-pickle-path",
                "./tapvid/tapvid_davis_data_strided.pkl",
                "--video-id",
                f"{i}",
                "--batch-size",
                "20",
            ]
        )


if __name__ == "__main__":
    main()
