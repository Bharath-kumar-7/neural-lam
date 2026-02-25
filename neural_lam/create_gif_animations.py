#!/usr/bin/env python3
"""Generate GIF animations from PNG prediction images."""
import argparse
import glob
from pathlib import Path

import imageio.v2 as imageio


def create_gifs(plot_dir, fps=1):
    """
    Create GIF animations from PNG images for each variable and level.

    Parameters
    ----------
    plot_dir : str or Path
        Directory containing the PNG prediction images
    fps : int
        Frames per second for the GIF animation (default: 1)
    """
    plot_dir = Path(plot_dir)

    # Find all unique variable/level combinations
    png_files = sorted(plot_dir.glob("*_prediction_lvl_*_t_*.png"))

    if not png_files:
        print(f"No prediction PNG files found in {plot_dir}")
        return

    # Extract unique variable/level combinations
    var_lvl_combos = set()
    for png_file in png_files:
        # Parse filename: {var_name}_prediction_lvl_{lvl:02}_t_{time}.png
        parts = png_file.stem.split("_prediction_lvl_")
        if len(parts) == 2:
            var_name = parts[0]
            lvl_part = parts[1].split("_t_")[0]
            var_lvl_combos.add((var_name, lvl_part))

    # Generate GIF for each combination
    for var_name, lvl in sorted(var_lvl_combos):
        pattern = f"{var_name}_prediction_lvl_{lvl}_t_*.png"
        images = sorted(plot_dir.glob(pattern))

        if images:
            gif_path = plot_dir / f"{var_name}_prediction_lvl_{lvl}.gif"
            with imageio.get_writer(gif_path, mode="I", fps=fps) as writer:
                for img_path in images:
                    image = imageio.imread(img_path)
                    writer.append_data(image)
            print(f"Created: {gif_path.name}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate GIF animations from prediction PNG images"
    )
    parser.add_argument(
        "plot_dir", type=str, help="Directory containing PNG prediction images"
    )
    parser.add_argument(
        "--fps", type=int, default=1, help="Frames per second (default: 1)"
    )

    args = parser.parse_args()
    create_gifs(args.plot_dir, args.fps)


if __name__ == "__main__":
    main()
