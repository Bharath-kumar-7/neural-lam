# GIF Animation Generation

This script generates GIF animations from PNG prediction images as a post-processing step.

## Usage

After running model evaluation/testing that generates PNG prediction images, you can create GIF animations:

```bash
python -m neural_lam.create_gif_animations <plot_directory> [--fps FPS]
```

### Arguments

- `plot_directory`: Path to the directory containing PNG prediction images
- `--fps`: Frames per second for the GIF animation (default: 1)

### Example

```bash
# Generate GIFs with default 1 FPS
python -m neural_lam.create_gif_animations ./outputs/predictions/

# Generate GIFs with 2 FPS
python -m neural_lam.create_gif_animations ./outputs/predictions/ --fps 2
```

## Expected Input Format

The script expects PNG files with the naming convention:
```
{variable_name}_prediction_lvl_{level:02}_t_{timestep}.png
```

For example:
- `temperature_prediction_lvl_00_t_001.png`
- `temperature_prediction_lvl_00_t_002.png`
- `pressure_prediction_lvl_01_t_001.png`

## Output

The script generates one GIF file for each unique variable/level combination:
```
{variable_name}_prediction_lvl_{level:02}.gif
```

For example:
- `temperature_prediction_lvl_00.gif`
- `pressure_prediction_lvl_01.gif`

## Dependencies

Requires `imageio` library. Install with:
```bash
pip install imageio
```
